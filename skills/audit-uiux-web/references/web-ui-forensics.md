# Web UI forensic pass

Use this overlay for AI-generated, vibe-coded, template-heavy, suspiciously
generic, or polished-but-unproven interfaces. Do not judge authorship. Identify
observable patterns, user impact, proof, and verification.

## Forensic categories

### Visual drift

- multiple unrelated accent colors compete in one viewport;
- raw hex values bypass tokens or near-identical colors multiply;
- typography, spacing, border, radius, or elevation changes between routes;
- gradients, blur, shadows, illustrations, or icon treatments add no meaning;
- brand color is used for every status, link, badge, icon, and surface.

### Flat or decorative surfaces

- a large surface is a plain fill with no texture, depth, or grouping cue, and
  the page reads empty in the first viewport (flatness);
- a background texture (grain, dots, grid, halftone, blur, paper, pixels) is
  present but has no stated job, or two textures compete on one surface;
- a background texture sits behind text with contrast that fails 4.5:1 at its
  worst pixel, or a texture is animated where it appears on every screen;
- a texture makes a screen heavy (a large SVG filter, blur, or canvas) with no
  measured cost, so the cost stays `unverified`.

Judge each against [background textures](../../design-uiux/references/background-textures.md)
gates. Report the finding with the surface, the measured worst-pixel contrast,
and the observed render, not a guess from a screenshot.

### Structural drift

- every section becomes a rounded elevated card;
- dashboard/KPI tiles appear without a decision or monitoring job;
- hero-plus-grid layout is repeated for list, detail, form, or settings tasks;
- tables become unreadable cards on mobile or remain horizontally unusable;
- a phone composition reads as a generic web card stack: full-width bordered
  cards wrapping every figure, floating full-width control tracks, navigation
  or controls that follow web conventions instead of native platform patterns;
- selectable option sets read as engineering defaults: arbitrary endpoints,
  missing natural ranges, or options limited to what the data model makes easy;
- decorative whitespace displaces the primary task while secondary actions share
  equal emphasis.

### Borders and dividers without separation jobs

A divider or border is evidence of separation; drawing one where nothing is
separated is a generated-pattern tell. Check:

- **Edge borders on divided lists** — inside a container that already has its
  own border, the first row draws a top border or the last row draws a bottom
  border, producing a double line at the container's edge (the classic
  `border` + row-`border-t` misuse, or a `divide-*` applied to include the
  edges). Rows in a bordered container separate *from each other*, not from
  the container.
- **Divider adjacent to the container's own border** — a hairline running
  parallel to and a few pixels from the card border, separating content from
  padding.
- **Divider under nothing** — a hairline above a lone block (single row,
  single figure) with no sibling above it to separate from.
- **Wrapping cards around plain content** — one figure, one trend, or one
  stat row sealed inside its own bordered card when the surrounding grammar
  leaves stat blocks open and reserves cards for grouped lists. Packaging
  added by pattern, not by need; on a phone this doubles as the generic-web
  card-stack tell above.

### Interaction theater

- hover-only actions, unlabeled icon buttons, fake dropdowns, or static tabs;
- buttons that do not change route, data, or visible state;
- success toast without persistence, rollback, or error path;
- loading animation without stable footprint or actual pending work;
- motion limited to hover bounce or page-load flourish despite a requested
  state-change transition;
- menus, dialogs, sheets, or tooltips without escape, focus return, touch, or
  no-hover behavior.

### Value changes and catalogued component motion

These checks run in every audit mode, not only the forensic overlay. The
Motion lens in SKILL.md points here.

Numbers the user changes, such as a cart total, a price toggle, a balance, or
a filtered stat. Judge them against
[digit pop-in](../../design-uiux/references/library/signature-motion/06-digit-pop-in.md):

| Check | Severity |
| --- | --- |
| The value is the main result of the action (a total after a quantity change, the price on a plan toggle) and it snaps with no transition | P2 |
| Any other user-changed value snaps. Report it whether or not the page animates other things | P3 |
| A count-up runs through made-up in-between values for one discrete change | P2 (it shows numbers that were never true) |
| No reduced-motion path, or a screen reader hears split or doubled digits | P2 |
| A pop-in fires on polling or live ticks, where a quiet subtle change or nothing belongs (a *count-up* on a poll is the P2 row above, not this one) | P3 |
| Every character animates, including the unchanged prefix and the separators; or a ghost old digit appears when the length changes (`$12` to `$120`) | P3 |
| The row width jitters (no `tabular-nums`), or an `overflow: hidden` container clips the exit or the blur | P3 |
| Two different number motions run on values visible at the same time | P3 |

Catalogued components (a dropdown, modal, toast, tooltip, tabs, accordion,
toggle, checkbox, success, error, skeleton, or AI status line). Judge them
against the
[transitions catalogue](../../design-uiux/references/transitions-catalog.md):

- The state change is instant, or uses hand-rolled timing, where a
  catalogued transition fits. Name the slug in the fix direction. This is P3,
  or P2 when the missing motion hides cause and effect (for example, a panel
  appears with no sign of where it came from).
- A loading or AI-status animation keeps running after the work ends, or a
  success animation plays before the write lands. This is P2 (fake feedback).
- `transitions-polish`'s read-only `transitions review` output may support a
  token-drift finding. It is `declared` evidence, not proof of the look.

Evidence: paused frames or a recording, at 0, 100, 250, 450, and 730 ms after
a real change for numbers. A snap seen only in the source is at the
`declared` rung. A single screenshot cannot reach `rendered` for motion, so
say which frames would settle the finding.

### Browser reality gaps

- direct URL, refresh, back/forward, new tab, or query parameters break context;
- route works only after a specific navigation sequence;
- session expiry, permission denial, or provider failure exposes a blank page;
- browser scroll, focus, selection, or unsaved work is unexpectedly lost;
- fixed headers, sticky regions, or overlays trap content at intermediate widths.

### Content and state gaps

- generic copy does not explain the decision or next step;
- fake metrics, placeholder avatars, impossible dates, or fabricated success;
- no long-label, translated, empty, no-results, dense, error, or partial state;
- error text names an internal failure but gives no recovery;
- permission, cost, destructive consequence, or cancellation is hidden.

## Forensic finding rule

Write:

`observable pattern → route/state → user impact → evidence/proof level → fix direction → verification`

“Looks AI-generated” is not a finding. “Five parallel summary cards use five
accent fills with no semantic distinction, competing with the primary action”
is a finding because it is observable and testable.
