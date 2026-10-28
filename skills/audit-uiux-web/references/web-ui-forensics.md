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
