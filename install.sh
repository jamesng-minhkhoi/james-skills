#!/usr/bin/env bash
# Link every skill in this repo into the agent skill directories, link the
# subagents into ~/.claude/agents, and add ROUTING.md to the global
# instruction files.
#
# Skills and agents are symlinked, not copied, so editing the repo updates
# every runtime immediately. Re-run after adding, renaming, or removing one.
#
#   ./install.sh                 install into the default targets
#   ./install.sh --dry-run       show what would change
#   ./install.sh ~/.claude/skills   link skills into specific targets only

set -euo pipefail

# pwd -P resolves symlinks and the filesystem's real casing. Plain pwd would
# echo back however the caller spelled the path, and on a case-insensitive
# filesystem that silently produces links the prune step cannot match.
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
SRC="$REPO/skills"
AGENTS_SRC="$REPO/agents"
ROUTING="$REPO/ROUTING.md"

DRY_RUN=0
TARGETS=()
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    -h|--help) sed -n '2,11p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) TARGETS+=("$arg") ;;
  esac
done
GLOBAL=0
if [ ${#TARGETS[@]} -eq 0 ]; then
  TARGETS=("$HOME/.claude/skills" "$HOME/.codex/skills" "$HOME/.agents/skills")
  GLOBAL=1
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

  # Shared references (ontology, tone, loading) are not skills, but skills link
  # to ../_shared, so each target needs the directory linked once.
  if [ -d "$SRC/_shared" ]; then
    link="$target/_shared"
    want="$SRC/_shared"
    if [ ! -L "$link" ] || [ "$(readlink "$link")" != "$want" ]; then
      if [ -e "$link" ] || [ -L "$link" ]; then
        echo "  replace _shared"
        run rm -rf "$link"
      else
        echo "  link    _shared"
      fi
      run ln -s "$want" "$link"
    fi
  fi

  # Drop links that point into this repo but no longer resolve, so a renamed
  # or deleted skill does not linger as a broken entry.
  for entry in "$target"/*; do
    [ -L "$entry" ] || continue
    case "$(readlink "$entry")" in
      "$SRC"/*) [ -e "$entry" ] || { echo "  prune   $(basename "$entry") (broken)"; run rm "$entry"; } ;;
    esac
  done
done

# Subagents and routing are global setup, so only the default run touches them.
if [ "$GLOBAL" -eq 1 ]; then
  target="$HOME/.claude/agents"
  echo "==> $target"
  [ -d "$target" ] || run mkdir -p "$target"
  AGENT_COUNT=0
  for file in "$AGENTS_SRC"/*.md; do
    [ -f "$file" ] || continue
    AGENT_COUNT=$((AGENT_COUNT + 1))
    link="$target/$(basename "$file")"
    if [ -L "$link" ] && [ "$(readlink "$link")" = "$file" ]; then
      continue
    fi
    if [ -e "$link" ] || [ -L "$link" ]; then
      echo "  replace $(basename "$file")"
      run rm -f "$link"
    else
      echo "  link    $(basename "$file")"
    fi
    run ln -s "$file" "$link"
  done
  for entry in "$target"/*; do
    [ -L "$entry" ] || continue
    case "$(readlink "$entry")" in
      "$AGENTS_SRC"/*) [ -e "$entry" ] || { echo "  prune   $(basename "$entry") (broken)"; run rm "$entry"; } ;;
    esac
  done

  # Replace the marked block in an instruction file, keeping everything else.
  # Claude can @import the live file; Codex cannot, so it gets a copy.
  write_block() {
    local file="$1" body="$2" start="<!-- JAMES_SKILLS_START -->" end="<!-- JAMES_SKILLS_END -->"
    local block="$start"$'\n'"$body"$'\n'"$end"
    local current=""
    [ -f "$file" ] && current="$(cat "$file")"
    local stripped
    stripped="$(printf '%s\n' "$current" | awk -v s="$start" -v e="$end" '$0==s{skip=1;next} $0==e{skip=0;next} !skip')"
    local next
    if [ -n "$(printf '%s' "$stripped" | tr -d '[:space:]')" ]; then
      next="$stripped"$'\n\n'"$block"
    else
      next="$block"
    fi
    if [ "$next" = "$current" ]; then
      return
    fi
    echo "==> $file"
    echo "  update  routing block"
    if [ "$DRY_RUN" -eq 0 ]; then
      mkdir -p "$(dirname "$file")"
      printf '%s\n' "$next" > "$file"
    fi
  }
  write_block "$HOME/.claude/CLAUDE.md" "@$ROUTING"
  write_block "$HOME/.codex/AGENTS.md" "$(cat "$ROUTING")"
fi

echo
echo "Linked ${#SKILLS[@]} skills."
[ "$GLOBAL" -eq 1 ] && echo "Linked $AGENT_COUNT agents and installed the routing guide."
