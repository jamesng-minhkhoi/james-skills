# Ask sonner regression cases

Use these forward-test fixtures when changing the `ask-sonner` skill. They
are review prompts with expected gates, not executable tests.

## Case 1: troubleshooting a broken toast

Prompt: "My Sonner toasts appear behind the modal and ignore my Tailwind
classes."

Expected behavior:

- use the troubleshooting section: z-index/stacking-context fix for toasts
  behind modals, and the styled-components/Tailwind class pass-through fix;
- give the minimal config change, not a library swap;
- verify the fix against the documented escalation ladder rather than
  guessing CSS.

## Case 2: picking the right call

Prompt: "Show the toast for a save that can fail, with retry."

Expected behavior:

- use the promise toast recipe (`toast.promise`) rather than hand-wiring
  `loading` → manual `dismiss`;
- match the documented API exactly; do not invent props.

## Must not have

A completion claim fails if it contains any of these:

- a recommended migration to another toast library without trying the
  documented fixes first;
- invented Sonner API props;
- styling changes that skip the escalation ladder.
