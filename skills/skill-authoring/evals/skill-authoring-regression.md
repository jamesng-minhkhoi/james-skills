# Skill authoring regression cases

Run these when changing `skill-authoring`, `_shared/authoring.md`, or
`ROUTING.md`. They are review prompts with expected gates, not executable
tests.

## Case 1: new skill from a real failure

Prompt: "Our agents keep writing Supabase migrations that drop a column before
the backfill runs. Add a skill for safe migrations."

Expected behavior:

- states the failure as a prompt and an expected outcome before writing;
- checks `ROUTING.md` and the three nearest descriptions, and names what the
  new skill owns that `frontend-web-engineering` does not;
- description is one to three sentences, ≤ 80 words, with a `Not for X (→ skill)` boundary;
- workflow steps produce a migration plan, a backfill check, and a rollback
  path — not "be careful with data";
- adds a behavior case and a routing case before the body is called done.

Must not have:

- a new skill that restates `supabase-postgres-best-practices` or
  `frontend-web-engineering`;
- a description that lists features instead of a trigger;
- a rule with no eval case.

## Case 2: rewrite instead of append

Prompt: "The audit skill keeps telling agents to fix things. Make it stop."

Expected behavior:

- finds the line that grants permission to edit and rewrites that section so
  the boundary is stated once;
- adds a negative routing case ("fix the findings" → engineering skill);
- keeps the file shorter than or equal to its previous length;
- runs `scripts/lint-skills.sh` and hands the diff to `skill-reviewer`.

Must not have:

- a new "do not edit" paragraph appended below the old permission;
- a contradiction left for the reader to reconcile;
- a rewrite that changes unrelated sections.

## Case 3: split without losing depth

Prompt: "`offensive-rce` is 1,070 lines and eats the context window. Split it."

Expected behavior:

- keeps the trigger, scope gate, and top checks in `SKILL.md`;
- moves payload depth to `references/`, named from the step that needs it;
- preserves every payload and attribution footer verbatim;
- updates `scripts/lint-baseline.txt` downward, never upward;
- re-runs the behavior case and the offensive scope case.

Must not have:

- a summary that silently drops payloads or CVE detail;
- a baseline raised to make lint pass;
- a license footer lost in the move.
