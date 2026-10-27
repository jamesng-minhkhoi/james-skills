# Review animations regression cases

Use these forward-test fixtures when changing the `review-animations` skill.
They are review prompts with expected gates, not executable tests. The skill
is user-invoked only (`disable-model-invocation: true`); every case assumes an
explicit invocation.

## Case 1: single-diff motion review

Prompt: (user-invoked) "Review my animation diff."

Expected behavior:

- output one markdown table with Before/After/Why columns — never a Before:/
  After: list;
- check the ten non-negotiable standards; pull exact values from
  STANDARDS.md, never approximations;
- cite `file:line` for every finding;
- fire the escalation triggers when present (animation on keyboard action,
  `scale(0)` entry, `ease-in` on enter, `transition: all`);
- render an explicit Block/Approve verdict; approval is earned, not given.

## Case 2: scope refusal

Prompt: (user-invoked) "Also review this API handler while you're here."

Expected behavior:

- decline non-motion review and point to `audit-uiux-web` (UI) or the
  project's general code-review flow;
- produce no findings outside motion code.

## Must not have

A completion claim fails if it contains any of these:

- a Before:/After: line-pair list instead of the markdown table;
- an Approve verdict with any unresolved escalation trigger;
- feature code written or bugs fixed during the review.
