# Animation performance regression cases

Use these forward-test fixtures when changing the `animation-performance`
skill. They are review prompts with expected gates, not executable tests.

## Case 1: jank under load

Prompt: "My tab indicator stutters while the next page loads."

Expected behavior:

- match the symptom table first; name the cause before proposing code;
- suspect a `requestAnimationFrame`-based animation (Framer Motion `x`/`y`
  shorthand) fighting the page load on the main thread;
- move the motion to CSS or WAAPI so it runs off the main thread, or use the
  full `transform` string for the hardware-accelerated path;
- refuse to conclude from a fast machine; require a busy-load reproduction
  (throttled CPU or real page-load scenario);
- report in Phase 3 form and mark feel claims that need a device recording as
  unverified.

## Must not have

A completion claim fails if it contains any of these:

- "fixed" without a busy-load reproduction behind it;
- reaching for `will-change` as a blanket fix without naming which layer it
  promotes and why it helps here;
- animating `width`, `height`, `margin`, or `padding` in the fix;
- updating an inherited CSS variable per frame on a container.
