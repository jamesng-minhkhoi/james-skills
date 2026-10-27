# Apple design regression cases

Use these forward-test fixtures when changing the `apple-design` skill. They
are review prompts with expected gates, not executable tests.

## Case 1: gesture-driven interaction review

Prompt: "Review this drag-to-dismiss drawer against Apple's principles."
(code provided)

Expected behavior:

- evaluate against the core principles in order: response latency, 1:1
  direct manipulation, interruptibility (the single most important one),
  spring behavior over fixed durations, and velocity handoff from drag into
  release animation;
- flag a fixed-duration release after a drag (should be a spring fed by
  gesture velocity);
- flag motion that cannot be interrupted mid-flight;
- note `animate`/`animate-expo` own any build work this review proposes.

## Must not have

A completion claim fails if it contains any of these:

- design principles asserted with no interaction code inspected;
- a build implemented during the review;
- interruptibility marked fine without evidence the animation retargets
  mid-flight.
