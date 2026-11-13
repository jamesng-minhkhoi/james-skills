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
| Chips and tags that clutter a card or message | Fewer, plainer labels, or the information stated in the content itself. One chip is right only where it replaces a whole sentence (the words-only row below) |
| Generic icons pasted over photos and cards | The product's real icon set, only where an icon earns its place |
| Rainbow, confetti, stickers, neo-brutalist cards | Playfulness through the product's own shapes, colors, and motion |
| Stock-looking photography | Real product imagery, or photography art-directed to feel cinematic and specific |
| Invented components, masks, or shapes approximating real ones | The real component, path, or asset from the codebase |
| Edge-to-edge flat blocks as swipe actions: mid-grey Edit, muddy red Delete | Separate rounded icon buttons: a brand tint for Edit, one vivid hue for Delete, nothing grey or dull |
| A big title, a grey subtitle, and a large number all restating the screen | A hero illustration or data picture; one small label; the number lives inside the picture |
| A static illustration sitting dead straight, as if pasted on | Unless the project's art direction forbids it, one soft tilt (a starting value of 4–8°) shared by the whole set |
| Every block on a screen the same distance apart, so nothing reads as a group | The ratio and its fix order in [gate 7](critique-and-proof.md), measured on the render |
| Choices drawn as pale pills with a hairline edge, which read as labels, not buttons | Buttons in the product's own button style with a 3:1 edge, per [gate 11](critique-and-proof.md) |
| A clip-art icon on every row because the row looked empty | Rows led by the item's name; one drawn visual only where it carries the item's identity |
| A generic AI sparkle (✦) marking what the assistant found, in a product that has its own assistant character | The character in the still form the product already uses at rest (its existing art, without animation), small, in the same place in every state; the state rides on a small badge or the text, not a swapped icon. If no still form exists, mark one as new and ask |
| Text laid straight over a busy gradient or artwork, or a colourful gradient faded with opacity until it goes grey and muddy | Keep the art at full strength and add a scrim that is solid under the text and clears toward the art (for example 95% → 0 across the card). Render it and check every line of text on the darkest and lightest part behind it; texture (grain, pattern) stays faint, about 10–15% |
| A card's copy squeezed into a narrow column, three or four short lines next to empty space | Use the card's width. Secondary copy one step smaller and lighter than body, ideally two lines; let the card grow for a longer locale rather than shrinking the type |
| Small pictures inside a sentence (avatars, thumbnails, icons) drawn as default circles, stacked tight with rings, or taller than the line so the lines spread apart | Each picture keeps its shipped shape (the product's avatar mask, card ratio, document shape). Size it to the text, not above the line height (about 20 px beside 14 px text), overlap shapes only slightly, no rings, and bind each picture to its word so it never wraps alone |
| Empty selector chips drawn grey with a solid outline, so they read as disabled; a comma or period wrapping to the start of a line | The project's add-slot style in the accent (dashed + a short noun where the project uses dashed for "put something here"); each phrase bound to its chip and punctuation |
| A menu or popover drawn under the primary button, clipped by the sheet's edge, or dimming the whole sheet | The menu on the top layer, opening toward the room it has, fully on screen; no dim for a pull-down |
| Shipped headline text swapped for a logo or glyph lockup nobody asked for | Keep the shipped text in the brand colour; a logo at text size breaks the line and loses legibility |
| A status, speaker, answer, or source said in a words-only line: a caps label ("Unwell ·", "Assistant asks"), "You said: Not sure · today", "Prepared answer · checked by our doctor" | The picture the product already has. The speaker is its avatar beside a speech bubble. The user's own answer is a reply bubble on the trailing side, with the answer's icon and a visible way to change it. A status label becomes an icon indicator only where the visible line beside it already says the state in words ("Fever since this morning"), so gate 9's glyph + word still holds; a state that blocks the task or needs a decision now (failed, declined, offline) keeps a visible word. A source is one icon chip plus an (i) button that opens the full sentence (popover or sheet). One chip stands in for one sentence; this is not a licence to add chips. Write each accessibility label, with its shipped string, in the board's note |
| An eyebrow or framing line that restates what the content below already shows ("Play idea for today · if you like · 3 min" above the idea) | Remove it, so the screen opens on the content ([gate 8](critique-and-proof.md)). A fact only the line carried (the 3 min) moves into the content or its meta line |
| Progress through a long plan drawn as a row of dots (14 nights, 30 days) | A small progress ring or bar beside the words that give the exact count ("night 4 of 14"). Dots only for five or fewer (a house threshold, not a standard). Page indicators on a pager keep the platform's dots |
| Placeholder text in the same colour and weight as entered or secondary text | Lower contrast than entered and secondary text, one weight step lighter than entered text where the type has one, and never below 4.5:1 on its field (in a dark theme that is a darker grey, not a lighter one). Where lower contrast cannot hold at 4.5:1, keep 4.5:1 and let the lighter weight alone set it apart. Give it its own token, marked new if the system has none, so a later palette remap cannot merge it into secondary text |
| An object with several actions offered as one pill for the action the brief named ("Change cover" on a photo) | For a standalone object (not a row in a list), a ••• button opening a menu with the object's whole action set (view, change, edit, then remove last and apart), per [mobile patterns](mobile-patterns.md#touch-first-input-and-actions) |
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
| Accent colors | One per role (primary action, active, progress), the same on every screen. A tint that appears on one control only (a pink disc on Add alone) fails until it is removed, or named as a role and marked new |
| Neutral families | One temperature, warm or cool |
| Corner radii | Every value from a scale stated by role ("actions pill, cards 16, inputs 8") |
| Icon families | One, at one optical weight per area; the platform symbol set on mobile |
| Labels per intent | One phrasing for each intent everywhere it appears |
| Display type sizes | One per screen |
| Materials (gradient, glow, glass, heavy shadow, sheen) | Each has a stated grouping, depth, emphasis, or brand job, and every control of that role carries it. Apply a material by role class or token, never per element: a control whose fill is a raw value silently misses it |
| Emoji in navigation, buttons, or chrome | None, unless the brand voice calls for it |
| Controls | Platform or design-system controls unless the design states why not |
| Dividers | Between items only: none above the first row, none below the last, none under a heading |
| Overlaps and padding | A badge, avatar, or sticker never covers data or a display; text inside an illustrated object has equal padding on opposite sides; a label inside a circle or pill keeps at least 8 pt/px clear of the edge measured on the label's own line (a circle narrows away from its centre, so a label under an icon inside a circle hits the edge: put the label under the circle, or keep the project's documented control; a reshaped shipped control is marked new); a sheet's content starts clear of its header (at least 16 pt below the header controls) |
| Destructive actions | Placed per [mobile patterns](mobile-patterns.md#touch-first-input-and-actions) |
| Subject | Shown per [mobile patterns](mobile-patterns.md#glance-sheet-dedicated-screen) |
| Labels for existing actions and statuses | The shipped string, verbatim (the locale file, or the source where it renders); a rename is named as a copy change in the board's note |
| Overlays | Every open menu, popover, or picker is on top of every other layer, uncut, and inside the screen in the board's capture |
| Canvas notes | Every claim in a note matches its board: the items a menu holds, where an action lives, which gesture opens what. Re-read the notes after the last board edit |
| Role collapse after a palette remap | Every role keeps a distinct value after a remap (placeholder versus secondary text, pressed versus rest). List the pairs an earlier fix separated, and re-measure each pair after the remap |
| Status and data colors (dashboards) | Status colors never reused as chart series; a series keeps its color across charts |

## The "would an expert ship this" pass

Before showing the work, look at each artboard and ask:

- Does it look like this product, or like any app? Could the logo be swapped
  for a competitor's without anyone noticing?
- Is there one focal point and one primary action per screen?
- Is any element only there to fill space?
- Does it hold up next to the strongest reference gathered, side by side?
- Is it final quality, or does it still read as a wireframe?
