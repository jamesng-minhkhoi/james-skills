#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 <ipa|apk|aab|app-dir> <path>" >&2
  exit 2
}

[[ $# -eq 2 ]] || usage
kind="$1"
path="$2"

[[ -e "$path" ]] || {
  echo "ERROR: artifact does not exist: $path" >&2
  exit 2
}

echo "artifact=$path"
echo "kind=$kind"
if [[ -f "$path" ]] && command -v shasum >/dev/null 2>&1; then
  echo "sha256=$(shasum -a 256 "$path" | awk '{print $1}')"
elif [[ -f "$path" ]] && command -v sha256sum >/dev/null 2>&1; then
  echo "sha256=$(sha256sum "$path" | awk '{print $1}')"
elif [[ -d "$path" ]]; then
  echo "sha256=directory-not-hashed"
fi
if command -v file >/dev/null 2>&1; then
  file "$path"
fi

case "$kind" in
  ipa)
    command -v unzip >/dev/null 2>&1 || {
      echo "ERROR: unzip is required for IPA inspection" >&2
      exit 2
    }
    tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/store-audit-ipa.XXXXXX")"
    trap 'rm -rf "$tmp_dir"' EXIT
    unzip -q "$path" -d "$tmp_dir"
    app_path="$(find "$tmp_dir/Payload" -maxdepth 1 -name '*.app' -print -quit)"
    [[ -n "$app_path" ]] || {
      echo "ERROR: no .app bundle found in IPA" >&2
      exit 2
    }
    echo "app_bundle=$app_path"
    if command -v plutil >/dev/null 2>&1; then
      plutil -p "$app_path/Info.plist"
    else
      echo "status=unknown"
      echo "UNKNOWN: plutil unavailable; Info.plist fields are Unknown" >&2
    fi
    if command -v codesign >/dev/null 2>&1; then
      codesign -dv --verbose=4 "$app_path" 2>&1 || true
      codesign -d --entitlements :- "$app_path" 2>&1 || true
    else
      echo "status=unknown"
      echo "UNKNOWN: codesign unavailable; signing and entitlements are Unknown" >&2
    fi
    ;;
  apk)
    if command -v apkanalyzer >/dev/null 2>&1; then
      apkanalyzer manifest print "$path"
    elif command -v aapt2 >/dev/null 2>&1; then
      aapt2 dump badging "$path"
      aapt2 dump permissions "$path"
    elif command -v aapt >/dev/null 2>&1; then
      aapt dump badging "$path"
      aapt dump permissions "$path"
    else
      echo "status=unknown"
      echo "UNKNOWN: apkanalyzer, aapt2, or aapt is required for APK inspection" >&2
    fi
    ;;
  aab)
    if ! command -v bundletool >/dev/null 2>&1; then
      echo "status=unknown"
      echo "UNKNOWN: bundletool is required for AAB manifest inspection" >&2
      exit 0
    fi
    bundletool dump manifest --bundle="$path"
    ;;
  app-dir)
    plist_path="$path/Info.plist"
    [[ -f "$plist_path" ]] || plist_path="$path/Contents/Info.plist"
    [[ -f "$plist_path" ]] || {
      echo "ERROR: app-dir must contain Info.plist" >&2
      exit 2
    }
    if ! command -v plutil >/dev/null 2>&1; then
      echo "status=unknown"
      echo "UNKNOWN: plutil is required for app directory inspection" >&2
      exit 0
    fi
    plutil -p "$plist_path"
    if command -v codesign >/dev/null 2>&1; then
      codesign -dv --verbose=4 "$path" 2>&1 || true
      codesign -d --entitlements :- "$path" 2>&1 || true
    fi
    ;;
  *)
    usage
    ;;
esac
