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
- decorative whitespace displaces the primary task while secondary actions share
  equal emphasis.

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
