# Animate regression cases

Use these forward-test fixtures when changing the `animate` skill. They are
review prompts with expected gates, not executable tests.

## Case 1: make a dropdown feel better

Prompt: "Make this dropdown feel better." (existing React dropdown, code
provided)

Expected behavior:

- run the frequency/purpose gate before writing any code;
- animate `transform` and `opacity` only, with a strong custom ease-out
  (`cubic-bezier(0.23, 1, 0.32, 1)`), 150–250 ms;
- set `transform-origin` at the trigger, not center;
- include reduced-motion handling and gate hover states behind
  `@media (hover: hover) and (pointer: fine)`;
- never `ease-in` on the enter animation, never `scale(0)`;
- do not install a motion library for this.

## Case 2: component request, not animation

Prompt: "Add a toast to my app."

Expected behavior:

- recognize this is a *component* request at step 3 of the build sequence;
- stop the animation path and route the library decision to the
  `pick-ui-library` flow — note it cannot self-invoke, so recommend from its
  list or hand the invocation to the user;
- never hand-roll a `<div>` toast with no focus management or exit behavior.

## Must not have

A completion claim fails if it contains any of these:

- an enter animation on a keyboard-initiated action;
- `transition: all` or a duration over 300 ms on a UI element;
- a keyframes-based animation on a rapidly-triggered element (toasts,
  toggles) where interrupts would restart from zero;
- a feel claim ("feels snappy") with no slow-motion or frame-by-frame check
  planned.
