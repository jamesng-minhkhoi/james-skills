#!/usr/bin/env bash
# Check that realistic requests route to the right skill or agent.
#
# Runs each case in evals/routing.txt through headless Claude Code from an
# empty directory, so only the installed global setup is in play (run
# ./install.sh first), and checks which skill or agent it names first. Hooks
# are off: memory plugins would otherwise inject recent sessions, including
# edits to these very cases.
#
#   scripts/eval-routing.sh                 run every case
#   scripts/eval-routing.sh petio-seo ...   run only the named cases
#   EVAL_MODEL=sonnet scripts/eval-routing.sh

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
CASES="$REPO/evals/routing.txt"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
mkdir "$WORK/cwd"

# Every name a routing answer can mention: skills plus agents.
NAMES=()
for dir in "$REPO"/skills/*/; do NAMES+=("$(basename "$dir")"); done
for file in "$REPO"/agents/*.md; do NAMES+=("$(basename "$file" .md)"); done

PROMPT_HEAD="Routing check — do NOT perform the task or call any tools. Given the \
skills and subagents available to you, reply with ONE line: the skill name(s) \
and/or subagent you would use first, then ' — ' and a reason under 15 words."

# The first known name to appear in the answer is what it routed to.
first_named() {
  local answer="$1" best="" best_pos=999999 name pos rest
  for name in "${NAMES[@]}"; do
    rest="${answer%%"$name"*}"
    [ "$rest" = "$answer" ] && continue
    pos=${#rest}
    if [ "$pos" -lt "$best_pos" ]; then best="$name"; best_pos=$pos; fi
  done
  echo "$best"
}

ids=()
while IFS='|' read -r id expected prompt; do
  case "$id" in ''|\#*) continue ;; esac
  if [ $# -gt 0 ] && [[ " $* " != *" $id "* ]]; then continue; fi
  ids+=("$id")
  printf '%s\n' "$expected" > "$WORK/$id.expected"
  (
    cd "$WORK/cwd"
    claude -p "$PROMPT_HEAD

Task: $prompt" --max-turns 1 --settings '{"disableAllHooks": true}' ${EVAL_MODEL:+--model "$EVAL_MODEL"} \
      > "$WORK/$id.out" 2>&1 || true
  ) &
done < "$CASES"
wait

if [ ${#ids[@]} -eq 0 ]; then
  echo "no matching cases"
  exit 1
fi

failed=0
for id in "${ids[@]}"; do
  expected="$(cat "$WORK/$id.expected")"
  answer="$(tail -1 "$WORK/$id.out")"
  got="$(first_named "$answer")"
  if [ -n "$got" ] && [[ "/$expected/" == *"/$got/"* ]]; then
    echo "pass  $id → $got"
  else
    echo "FAIL  $id → ${got:-nothing} (expected $expected)"
    echo "      $answer"
    failed=$((failed + 1))
  fi
done

echo
echo "$(( ${#ids[@]} - failed ))/${#ids[@]} routed correctly"
[ "$failed" -eq 0 ]
