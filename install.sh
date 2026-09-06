#!/usr/bin/env bash
# Link every skill in this repo into the agent skill directories.
#
# Skills are symlinked, not copied, so editing the repo updates every runtime
# immediately. Re-run after adding, renaming, or removing a skill.
#
#   ./install.sh                 link into the default targets
#   ./install.sh --dry-run       show what would change
#   ./install.sh ~/.claude/skills   link into specific targets only

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO/skills"

DRY_RUN=0
TARGETS=()
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    -h|--help) sed -n '2,9p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) TARGETS+=("$arg") ;;
  esac
done
if [ ${#TARGETS[@]} -eq 0 ]; then
  TARGETS=("$HOME/.claude/skills" "$HOME/.codex/skills" "$HOME/.agents/skills")
fi

# Skill directories in this repo, i.e. those that actually have a SKILL.md.
SKILLS=()
for dir in "$SRC"/*/; do
  [ -f "$dir/SKILL.md" ] || continue
  SKILLS+=("$(basename "$dir")")
done

run() { if [ "$DRY_RUN" -eq 1 ]; then echo "    would: $*"; else "$@"; fi; }

for target in "${TARGETS[@]}"; do
  echo "==> $target"
  [ -d "$target" ] || run mkdir -p "$target"

  # Link every current skill, replacing stale copies and outdated links.
  for name in "${SKILLS[@]}"; do
    link="$target/$name"
    want="$SRC/$name"
    if [ -L "$link" ] && [ "$(readlink "$link")" = "$want" ]; then
      continue
    fi
    if [ -e "$link" ] || [ -L "$link" ]; then
      echo "  replace $name"
      run rm -rf "$link"
    else
      echo "  link    $name"
    fi
    run ln -s "$want" "$link"
  done

  # Drop links that point into this repo but no longer resolve, so a renamed
  # or deleted skill does not linger as a broken entry.
  for entry in "$target"/*; do
    [ -L "$entry" ] || continue
    case "$(readlink "$entry")" in
      "$SRC"/*) [ -e "$entry" ] || { echo "  prune   $(basename "$entry") (broken)"; run rm "$entry"; } ;;
    esac
  done
done

echo
echo "Linked ${#SKILLS[@]} skills."
