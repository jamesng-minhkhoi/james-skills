# Mobile native regression cases

Use these forward-test fixtures when changing the `mobile-native` skill. They
are review prompts with expected gates, not executable tests.

## Case 1: "works in Chrome, feels wrong on my phone"

Prompt: "Works in Chrome but the bottom bar sits under the home indicator and
taps feel laggy on my iPhone."

Expected behavior:

- fix safe areas: `viewport-fit=cover` plus `env(safe-area-inset-*)` padding;
- fix tap feel: `touch-action: manipulation`, visible `:active` or
  pointerdown feedback instead of the 300 ms tap-highlight flash;
- never ship `user-scalable=no` or block zoom to solve input zoom (fix input
  font sizes instead);
- state which fixes need verification on real hardware, not a simulator.

## Case 2: platform-layer vs frame-budget split

Prompt: "The app feels janky on my phone."

Expected behavior:

- check the platform-layer tells first (sticky hover states, tap highlight,
  scroll hijacking, viewport bugs) before treating it as an animation
  problem;
- hand true frame-budget causes (dropped frames from a specific animated
  property) to `animation-performance`;
- say which diagnosis is confirmed versus suspected.

## Must not have

A completion claim fails if it contains any of these:

- a "feels native" claim with no real-device checklist for the fixes;
- hover effects applied without an `@media (hover: hover)` gate;
- `-webkit-tap-highlight-color: transparent` without replacing the feedback
  it removed;
- a 100vh layout fix using `height: 100vh` unmodified.
