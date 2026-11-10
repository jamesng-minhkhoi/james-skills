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
| Edge-to-edge flat blocks as swipe actions: mid-grey Edit, muddy red Delete | Separate rounded icon buttons: a brand tint for Edit, one vivid hue for Delete, nothing grey or dull |
| A big title, a grey subtitle, and a large number all restating the screen | A hero illustration or data picture; one small label; the number lives inside the picture |
| A static illustration sitting dead straight, as if pasted on | Unless the project's art direction forbids it, one soft tilt (a starting value of 4–8°) shared by the whole set |
| A clip-art icon on every row because the row looked empty | Rows led by the item's name; one drawn visual only where it carries the item's identity |
| A generic AI sparkle (✦) marking what the assistant found, in a product that has its own assistant character | The character in the still form the product already uses at rest (its existing art, without animation), small, in the same place in every state; the state rides on a small badge or the text, not a swapped icon. If no still form exists, mark one as new and ask |
| Text laid straight over a busy gradient or artwork, or a colourful gradient faded with opacity until it goes grey and muddy | Keep the art at full strength and add a scrim that is solid under the text and clears toward the art (for example 95% → 0 across the card). Render it and check every line of text on the darkest and lightest part behind it; texture (grain, pattern) stays faint, about 10–15% |
| A card's copy squeezed into a narrow column, three or four short lines next to empty space | Use the card's width. Secondary copy one step smaller and lighter than body, ideally two lines; let the card grow for a longer locale rather than shrinking the type |
| Small pictures inside a sentence (avatars, thumbnails, icons) drawn as default circles, stacked tight with rings, or taller than the line so the lines spread apart | Each picture keeps its shipped shape (the product's avatar mask, card ratio, document shape). Size it to the text, not above the line height (about 20 px beside 14 px text), overlap shapes only slightly, no rings, and bind each picture to its word so it never wraps alone |
| Shipped headline text swapped for a logo or glyph lockup nobody asked for | Keep the shipped text in the brand colour; a logo at text size breaks the line and loses legibility |
| "Lazy" motion: entry and loop fighting over one element's transform, a separate timer per element so they drift apart, everything starting at once | Entry on a wrapper, the loop on the inner element; one shared loop clock that starts after the entry settles; text lands in a short stagger (60–80 ms), the visual last with a small overshoot. Check rendered frames at several timestamps before showing |

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
| Dividers | Between items only: none above the first row, none below the last, none under a heading |
| Overlaps and padding | A badge, avatar, or sticker never covers data or a display; text inside an illustrated object has equal padding on opposite sides; a sheet's content starts clear of its header (at least 16 pt below the header controls) |
| Destructive actions | Placed per [mobile patterns](mobile-patterns.md#touch-first-input-and-actions) |
| Subject | Shown per [mobile patterns](mobile-patterns.md#glance-sheet-dedicated-screen) |
| Labels for existing actions and statuses | The shipped string, verbatim (the locale file, or the source where it renders); a rename is named as a copy change in the board's note |
| Canvas notes | Every claim in a note matches its board: the items a menu holds, where an action lives, which gesture opens what. Re-read the notes after the last board edit |
| Status and data colors (dashboards) | Status colors never reused as chart series; a series keeps its color across charts |

## The "would an expert ship this" pass

Before showing the work, look at each artboard and ask:

- Does it look like this product, or like any app? Could the logo be swapped
  for a competitor's without anyone noticing?
- Is there one focal point and one primary action per screen?
- Is any element only there to fill space?
- Does it hold up next to the strongest reference gathered, side by side?
- Is it final quality, or does it still read as a wireframe?
