# Pick UI library regression cases

Use these forward-test fixtures when changing the `pick-ui-library` skill.
They are review prompts with expected gates, not executable tests. The skill
is user-invoked only (`disable-model-invocation: true`).

## Case 1: library selection

Prompt: (user-invoked) "pick-ui-library: I need a command menu for the new
app."

Expected behavior:

- recommend from the curated list only — vetted libraries, not a search for
  whatever ranks first today;
- name the mismatch traps the skill warns about (hand-rolled toasts,
  abandoned packages, wrong tool for numbers/OTP/virtualization);
- justify the pick by task fit, not popularity.

## Must not have

A completion claim fails if it contains any of these:

- a recommendation outside the curated list without flagging it;
- hand-rolled component advice ("just build a small dropdown") for a task
  the list covers;
- auto-triggering on a plain feature request without the explicit
  invocation.
