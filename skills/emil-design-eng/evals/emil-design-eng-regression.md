# Emil design-eng regression cases

Use these forward-test fixtures when changing the `emil-design-eng` skill.
They are review prompts with expected gates, not executable tests.

## Case 1: polish review of a component

Prompt: "Why does this popover feel cheap? Review the component's polish."
(code provided)

Expected behavior:

- output one markdown table with Before/After/Why columns — never a Before:/
  After: line-pair list;
- check the craft rules: press feedback (`scale(0.97)` on `:active`), no
  `scale(0)` entry, origin-aware popovers (modals stay centered), tooltip
  skip-delay, no `transition: all`;
- cite `file:line` and keep the Why column to the reasoning, not the fix;
- stay read-only: findings, not rewrites.

## Case 2: boundary refusal on motion ask

Prompt: "Review the dropdown's open animation."

Expected behavior:

- recognize this is a motion ask, not a polish ask;
- decline to run the full craft review and hand off to `review-animations`
  (review) or `animate` (build); general UI audits go to `audit-uiux-web`.

## Must not have

A completion claim fails if it contains any of these:

- a Before:/After: list instead of the markdown table;
- rewritten code during a review;
- a verdict with no `file:line` citations.
