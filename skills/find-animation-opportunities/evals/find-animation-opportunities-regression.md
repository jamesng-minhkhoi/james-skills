# Find animation opportunities regression cases

Use these forward-test fixtures when changing the
`find-animation-opportunities` skill. They are review prompts with expected
gates, not executable tests.

## Case 1: propose motion, reject over-animation

Prompt: "What could be animated here? Make this dashboard feel more alive."
(code provided)

Expected behavior:

- pass every candidate through the gate: frequency of encounter, purpose,
  and whether the user benefits — reject decoration on high-frequency
  interactions (keyboard actions, hover on dense lists);
- for accepted opportunities, give exact values (property, curve, duration)
  in the required output format;
- stay read-only: it proposes, it does not implement — builds route to
  `animate`;
- say plainly where the right answer is "don't animate".

## Must not have

A completion claim fails if it contains any of these:

- source code edited;
- an accepted proposal without exact curve and duration values;
- motion proposed for keyboard-initiated or 100+/day actions;
- "more alive" answered by animating everything.
