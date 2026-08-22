# Release artifact inspection

Use the exact uploaded or intended artifact. Record the command, tool version,
path, hash, and output location. If a tool is unavailable, mark the result
Unknown; do not infer it from source config.

## Common identity checks

```sh
shasum -a 256 path/to/artifact
file path/to/artifact
```

Record bundle/package ID, display name, version, build/version code, signing,
architectures, target SDK, permissions, entitlements, and supported devices.

Use the bundled read-only helper when available:

```sh
./scripts/inspect-release-artifact.sh ipa path/to/app.ipa
./scripts/inspect-release-artifact.sh apk path/to/app.apk
./scripts/inspect-release-artifact.sh aab path/to/app.aab
./scripts/inspect-release-artifact.sh app-dir path/to/App.app
```

The helper prints `status=unknown` when a platform decoder is unavailable so
the audit can preserve the evidence gap without treating the tool installation
itself as an app failure.

## iOS IPA or app bundle

```sh
audit_dir="$(mktemp -d "${TMPDIR:-/tmp}/store-audit-ipa.XXXXXX")"
trap 'rm -rf "$audit_dir"' EXIT
unzip -q path/to/app.ipa -d "$audit_dir"
find "$audit_dir/Payload" -maxdepth 1 -name '*.app' -print
plutil -p "$audit_dir"/Payload/*.app/Info.plist
codesign -dv --verbose=4 "$audit_dir"/Payload/*.app 2>&1
codesign -d --entitlements :- "$audit_dir"/Payload/*.app 2>&1
```

Inspect `CFBundleIdentifier`, `CFBundleDisplayName`, `CFBundleName`, version,
build, URL schemes, usage descriptions, supported orientations, extensions,
associated domains, entitlements, and privacy manifests. Keep the temporary
directory scoped to this artifact and delete it after evidence capture.

## Android APK

Use the first available tool and record which one was used:

```sh
apkanalyzer manifest application-id path/to/app.apk
apkanalyzer manifest version-code path/to/app.apk
apkanalyzer manifest version-name path/to/app.apk
apkanalyzer manifest permissions path/to/app.apk
apkanalyzer manifest print path/to/app.apk
```

If `apkanalyzer` is unavailable, use `aapt2 dump badging` or `aapt dump badging`
and mark fields that cannot be decoded. Inspect package name, application label,
version, target SDK, permissions, exported components, deep links, supported
ABIs, and native libraries.

## Android App Bundle

```sh
bundletool dump manifest --bundle=path/to/app.aab
bundletool dump resources --bundle=path/to/app.aab
```

Inspect the base module and relevant split/device configuration. A local AAB
existing on disk does not prove Play processed the uploaded artifact.

## Expo/EAS and generated native files

```sh
npx expo config --type public --json
```

Use the exact build profile and generated native output used for the artifact.
Do not treat an Expo config export as proof of native signing, processing,
installability, reviewer access, or store approval.

## Evidence rule

Capture the relevant output in the evidence ledger. A source/configuration
finding is **Source**; a decoded IPA/APK/AAB is **Build**; a successful clean
install and observed route is **Runtime**; a portal upload/processing state is
**Portal**. Never promote one level to another without observing it.
