# Prototype regression cases

Use these forward-test fixtures when changing the `prototype` skill. They are
review prompts with expected gates, not executable tests. The skill is
user-invoked only (`disable-model-invocation: true`).

## Case 1: build variants

Prompt: (user-invoked) "prototype: three versions of a hero card for the
launch page."

Expected behavior:

- build genuinely different versions — different structure or emphasis, not
  the same layout with a swapped color;
- render them behind the PICKER.md switcher so James can flip through them
  live;
- promote exactly the version James picks and discard the rest without
  merging traits unless asked;
- state what each variant optimizes for.

## Must not have

A completion claim fails if it contains any of these:

- variants that differ only in color or copy;
- a single variant presented as options;
- promotion of a variant without the user's pick.
