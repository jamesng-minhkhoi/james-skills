#!/usr/bin/env bash
# Check skills against structure rules and size budgets.
#
# Text that loads in every session (descriptions, ROUTING.md) costs context
# everywhere, so it has the tightest budget. Overages listed in
# scripts/lint-baseline.txt may shrink but never grow.
#
#   scripts/lint-skills.sh              check everything
#   scripts/lint-skills.sh --baseline   print current overages in baseline format

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
BASELINE="$REPO/scripts/lint-baseline.txt"

MAX_DESC_WORDS=80
MAX_SKILL_LINES=300
MAX_ROUTING_LINES=40

PRINT_BASELINE=0
[ "${1:-}" = "--baseline" ] && PRINT_BASELINE=1

errors=0
fail() { echo "  FAIL $*"; errors=$((errors + 1)); }

baseline_value() {
  awk -v s="$1" -v m="$2" '$1==s && $2==m {print $3}' "$BASELINE" 2>/dev/null
}

# A metric over budget fails unless the baseline allows at least that much.
check_budget() {
  local skill="$1" metric="$2" value="$3" limit="$4" allowed
  [ "$value" -le "$limit" ] && return
  if [ "$PRINT_BASELINE" -eq 1 ]; then
    echo "$skill $metric $value"
    return
  fi
  allowed="$(baseline_value "$skill" "$metric")"
  if [ -z "$allowed" ]; then
    fail "$skill: $metric $value > budget $limit"
  elif [ "$value" -gt "$allowed" ]; then
    fail "$skill: $metric grew to $value (baseline $allowed, budget $limit)"
  elif [ "$value" -lt "$allowed" ]; then
    echo "  note $skill: $metric shrank to $value — lower its baseline from $allowed"
  fi
}

for file in "$REPO"/skills/*/SKILL.md; do
  dir="$(dirname "$file")"
  skill="$(basename "$dir")"

  name="$(awk '/^name:/ {print $2; exit}' "$file")"
  desc="$(awk '/^description:/ {sub(/^description: */, ""); print; exit}' "$file")"
  [ "$name" = "$skill" ] || fail "$skill: frontmatter name '$name' does not match folder"
  [ -n "$desc" ] || fail "$skill: missing description"

  check_budget "$skill" desc_words "$(printf '%s' "$desc" | wc -w | tr -d ' ')" "$MAX_DESC_WORDS"
  check_budget "$skill" skill_lines "$(wc -l < "$file" | tr -d ' ')" "$MAX_SKILL_LINES"

  # Every skill shares one vocabulary; a private redefinition is the drift this
  # library exists to prevent.
  grep -q '\.\./_shared/ontology\.md' "$file" || fail "$skill: missing link to ../_shared/ontology.md"
  if grep -q 'mostly complete' "$file"; then
    fail "$skill: banned phrase 'mostly complete' (use a verdict from the ontology)"
  fi

  # A rule without a case is a rule nobody can test.
  compgen -G "$dir/evals/*.md" > /dev/null || fail "$skill: no behavior case in evals/"

  # Every relative Markdown link in the skill must resolve.
  for md in "$file" "$dir"/references/*.md; do
    [ -f "$md" ] || continue
    while read -r link; do
      case "$link" in http*|mailto:*) continue ;; esac
      [ -e "$(dirname "$md")/$link" ] || fail "$skill: broken link $link in ${md#"$REPO"/}"
    done < <(grep -oE '\]\([^)#]+' "$md" | sed 's/^](//')
  done
done

# Shared references must keep their own links resolving.
for md in "$REPO"/skills/_shared/*.md; do
  [ -f "$md" ] || continue
  while read -r link; do
    case "$link" in http*|mailto:*) continue ;; esac
    [ -e "$(dirname "$md")/$link" ] || fail "shared: broken link $link in ${md#"$REPO"/}"
  done < <(grep -oE '\]\([^)#]+' "$md" | sed 's/^](//')
done

[ "$PRINT_BASELINE" -eq 1 ] && exit 0

routing_lines="$(wc -l < "$REPO/ROUTING.md" | tr -d ' ')"
[ "$routing_lines" -le "$MAX_ROUTING_LINES" ] || fail "ROUTING.md: $routing_lines lines > budget $MAX_ROUTING_LINES"

if [ "$errors" -gt 0 ]; then
  echo "lint failed"
  exit 1
fi
echo "lint passed"
