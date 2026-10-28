---
description: Critique UI animations, easing curves, and frame budgets with review-animations
---

Load the `review-animations` and `animation-performance` skills to review motion in:
$ARGUMENTS

Critique:
1. Intent: Is this animation purposeful, or is it decorative clutter?
2. Curves & Timing: Does it use appropriate easing (spring physics for gestures, fast timing curves 150-300ms for UI)?
3. Interruptibility: Can the user interrupt or reverse the interaction mid-flight?
4. Performance budget: Are properties restricted to composite-only (`transform`, `opacity`) without layout thrash?
5. Reduced motion: Does it gracefully degrade under `prefers-reduced-motion`?
