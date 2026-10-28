#!/usr/bin/env bash
# Link every skill in this repo into the agent skill directories, install the
# subagents in each harness's dialect, link custom slash commands, and add
# ROUTING.md to the global instruction files.
#
# Skills, Claude agents, and slash commands are symlinked, not copied. OpenCode,
# Codex, and Gemini agents are generated conversions (marked, pruned when stale).
# Re-run after adding, renaming, or removing one.
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
COMMANDS_SRC="$REPO/commands"
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
  TARGETS=("$HOME/.claude/skills" "$HOME/.codex/skills" "$HOME/.agents/skills" "$HOME/.gemini/skills")
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
MARK="# managed by james-skills install.sh — edit agents/<name>.md in the repo"

# One frontmatter field value from an agent file.
field() { awk -v f="$1:" 'index($0, f)==1 {sub(/^[^:]*: */, ""); print; exit}' "$2"; }

# Write stdin to a target only when it differs (dry-run aware).
gen() {
  local want
  want="$(mktemp)"
  cat > "$want"
  if [ -f "$1" ] && cmp -s "$1" "$want"; then rm -f "$want"; return; fi
  if [ -e "$1" ]; then echo "  replace $(basename "$1")"; else echo "  gen     $(basename "$1")"; fi
  if [ "$DRY_RUN" -eq 0 ]; then mkdir -p "$(dirname "$1")" && mv "$want" "$1"; else rm -f "$want"; fi
}

if [ "$GLOBAL" -eq 1 ]; then
  # agents/*.md is the source of truth, in the Claude Code dialect. Claude
  # links it directly; OpenCode, Codex, and Gemini accept different formats,
  # so they get generated conversions with the tool bans translated.
  AGENT_COUNT=0
  for file in "$AGENTS_SRC"/*.md; do
    [ -f "$file" ] || continue
    AGENT_COUNT=$((AGENT_COUNT + 1))
    name="$(basename "$file" .md)"
    desc="$(field description "$file" | sed 's/\\/\\\\/g; s/"/\\"/g')"
    denied="$(field disallowedTools "$file")"

    # Claude Code: link as-is.
    link="$HOME/.claude/agents/$name.md"
    if [ ! -L "$link" ] || [ "$(readlink "$link")" != "$file" ]; then
      if [ -e "$link" ] || [ -L "$link" ]; then
        echo "  replace $name.md"
        run rm -f "$link"
      else
        echo "  link    $name.md"
      fi
      run ln -s "$file" "$link"
    fi

    body="$(awk 'n==2{print} /^---$/{n++; next}' "$file")"
    preloads="$(awk '/^skills:$/{f=1; next} f && /^  - /{printf "%s ", $2} f && /^---$/{f=0}' "$file")"
    if [ -n "$preloads" ]; then
      body="Follow these skills when the target matches (installed globally): $preloads
$body"
    fi

    # OpenCode: markdown agent; tool bans become permission denials.
    oc_permit="  edit: deny"
    case "$denied" in *Bash*) oc_permit="$oc_permit
  bash: deny" ;; esac
    case "$denied" in *WebFetch*) oc_permit="$oc_permit
  webfetch: deny" ;; esac
    case "$denied" in *WebSearch*) oc_permit="$oc_permit
  websearch: deny" ;; esac
    gen "$HOME/.config/opencode/agents/$name.md" <<EOF
---
$MARK
description: '$(field description "$file" | sed "s/'/''/g")'
mode: subagent
permission:
$oc_permit
---
$body
EOF

    # Codex: TOML agent; tool bans become a read-only sandbox.
    case "$body" in *"'''"*)
      echo "  skip    $name.toml (body would break the TOML literal)" >&2
      continue ;;
    esac
    gen "$HOME/.codex/agents/$name.toml" <<EOF
$MARK
name = "$name"
description = "$desc"
sandbox_mode = "read-only"
developer_instructions = '''
$body
'''
EOF

    # Gemini CLI: an allowlist that leaves out every tool that writes files.
    gemini_tools="  - read_file
  - glob
  - grep_search
  - list_directory
  - run_shell_command"
    case "$denied" in *WebFetch*) ;; *) gemini_tools="$gemini_tools
  - web_fetch" ;; esac
    case "$denied" in *WebSearch*) ;; *) gemini_tools="$gemini_tools
  - google_web_search" ;; esac
    gen "$HOME/.gemini/agents/$name.md" <<EOF
---
$MARK
name: $name
description: '$(field description "$file" | sed "s/'/''/g")'
model: inherit
tools:
$gemini_tools
---
$body
EOF
  done

  # Prune conversions whose source file no longer exists, and dangling
  # Claude links.
  for dir in "$HOME/.claude/agents" "$HOME/.config/opencode/agents" "$HOME/.codex/agents" "$HOME/.gemini/agents"; do
    [ -d "$dir" ] || continue
    for entry in "$dir"/*; do
      [ -e "$entry" ] || [ -L "$entry" ] || continue
      base="$(basename "$entry")"
      if [ -L "$entry" ]; then
        case "$(readlink "$entry")" in
          "$AGENTS_SRC"/*) [ -e "$entry" ] || { echo "  prune   $base (broken)"; run rm "$entry"; } ;;
        esac
      elif grep -q "^$MARK$" "$entry" 2>/dev/null; then
        [ -f "$AGENTS_SRC/${base%%.*}.md" ] || { echo "  prune   $dir/$base (stale)"; run rm -f "$entry"; }
      fi
    done
  done

  # Slash commands: linked directly into ~/.claude/commands and ~/.config/opencode/commands
  COMMAND_COUNT=0
  if [ -d "$COMMANDS_SRC" ]; then
    for target_cmds in "$HOME/.claude/commands" "$HOME/.config/opencode/commands"; do
      [ -d "$target_cmds" ] || run mkdir -p "$target_cmds"
      for file in "$COMMANDS_SRC"/*.md; do
        [ -f "$file" ] || continue
        name="$(basename "$file")"
        link="$target_cmds/$name"
        if [ -L "$link" ] && [ "$(readlink "$link")" = "$file" ]; then
          continue
        fi
        if [ -e "$link" ] || [ -L "$link" ]; then
          echo "  replace $name"
          run rm -rf "$link"
        else
          echo "  link    $name"
        fi
        run ln -s "$file" "$link"
      done

      # Prune broken command links pointing to this repo
      for entry in "$target_cmds"/*; do
        [ -L "$entry" ] || continue
        case "$(readlink "$entry")" in
          "$COMMANDS_SRC"/*) [ -e "$entry" ] || { echo "  prune   $(basename "$entry") (broken)"; run rm "$entry"; } ;;
        esac
      done
    done
    for file in "$COMMANDS_SRC"/*.md; do
      [ -f "$file" ] && COMMAND_COUNT=$((COMMAND_COUNT + 1))
    done
  fi

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
  write_block "$HOME/.config/opencode/AGENTS.md" "$(cat "$ROUTING")"
  write_block "$HOME/.gemini/GEMINI.md" "$(cat "$ROUTING")"
fi

echo
echo "Linked ${#SKILLS[@]} skills."
[ "$GLOBAL" -eq 1 ] && echo "Installed $AGENT_COUNT agents, $COMMAND_COUNT commands (Claude/OpenCode links), and the routing guide."
