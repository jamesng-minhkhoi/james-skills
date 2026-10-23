# Slop and consistency

"AI slop" is the look a model reaches for when it has no direction: generic
materials, decoration standing in for hierarchy, and screens that disagree
with each other. Run this file before showing any proposal and again before
handoff. In a written finding, name the observable pattern and its cost to
the user instead of using the word "slop".

## Tells James has rejected

Each was called slop in a real review. Treat them as defaults to avoid; use
one only when the project's own design system already does and you can say
what job it does there.

| Tell | Instead |
| --- | --- |
| Drop shadows used for depth by default | Separation through spacing, surface tone, and grouping; a shadow only where the system uses one for elevation |
| Borders, dividers, and outlined wrappers around everything | Whitespace, grouping, and surface contrast; inset grouped lists where the platform uses them |
| Floating, bobbing, or looping idle animation | Entry and state-change motion with a job (see the motion reference) |
| Decorative gradients: gradient text, bars, buttons | The product's own signature surfaces, used where the system uses them |
| Dashed borders and decorative dashes | Solid, purposeful structure or nothing |
| Chips and tags that clutter a card or message | Fewer, plainer labels, or the information stated in the content itself |
| Generic icons pasted over photos and cards | The product's real icon set, only where an icon earns its place |
| Rainbow, confetti, stickers, neo-brutalist cards | Playfulness through the product's own shapes, colors, and motion |
| Stock-looking photography | Real product imagery, or photography art-directed to feel cinematic and specific |
| Invented components, masks, or shapes approximating real ones | The real component, path, or asset from the codebase |

Subtraction alone is not the fix. Stripping a design to flat white reads as
"too basic" and "boring": keep the product's signature (its card surfaces,
avatar shapes, type, and color) and remove the generic layer on top of it.

## Consistency check

Count across every screen in the proposal. It is mechanical: a failed count
is a fix, not a matter of taste. It checks consistency, not style, so a
role-based choice the design system states is a pass. Adapted from Appllama's
anti-slop pre-flight (MIT).

| Count | Pass |
| --- | --- |
| Accent colors | One per role (primary action, active, progress), the same on every screen |
| Neutral families | One temperature, warm or cool |
| Corner radii | Every value from a scale stated by role ("actions pill, cards 16, inputs 8") |
| Icon families | One, at one optical weight per area; the platform symbol set on mobile |
| Labels per intent | One phrasing for each intent everywhere it appears |
| Display type sizes | One per screen |
| Materials (gradient, glow, glass, heavy shadow) | Each has a stated grouping, depth, emphasis, or brand job |
| Emoji in navigation, buttons, or chrome | None, unless the brand voice calls for it |
| Controls | Platform or design-system controls unless the design states why not |
| Status and data colors (dashboards) | Status colors never reused as chart series; a series keeps its color across charts |

## The "would an expert ship this" pass

Before showing the work, look at each artboard and ask:

- Does it look like this product, or like any app? Could the logo be swapped
  for a competitor's without anyone noticing?
- Is there one focal point and one primary action per screen?
- Is any element only there to fill space?
- Does it hold up next to the strongest reference gathered, side by side?
- Is it final quality, or does it still read as a wireframe?
