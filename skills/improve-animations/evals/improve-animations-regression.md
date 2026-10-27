# Improve animations regression cases

Use these forward-test fixtures when changing the `improve-animations` skill.
They are review prompts with expected gates, not executable tests.

## Case 1: full audit

Prompt: "Audit the motion in this app."

Expected behavior:

- run recon (stack, motion tokens, frequency map), then audit all eight
  AUDIT.md categories;
- return a vetted findings table with `file:line` locations and severity
  (HIGH/MEDIUM/LOW, mapping to the library's P1/P2/P3 at handoff);
- list 2–4 missed opportunities separately from corrective findings;
- stop and wait for the user to select findings before writing plans;
- write nothing outside `plans/`.

## Case 2: refuses to mutate source directly

Prompt: "Improve the animations — just fix them."

Expected behavior:

- decline to mutate source code (read-only skill);
- produce the prioritized audit and self-contained plans;
- point to `execute <plan>` for the implementation step;
- zero source diffs in the session.

## Must not have

A completion claim fails if it contains any of these:

- source code edited in a bare audit run;
- plan target values (cubic-beziers, spring configs) approximated instead of
  pulled from AUDIT.md;
- plans stamped without the current commit;
- findings without `file:line` evidence.
