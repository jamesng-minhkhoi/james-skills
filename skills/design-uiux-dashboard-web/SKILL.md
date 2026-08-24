---
name: design-uiux-dashboard-web
description: Design clear, data-driven responsive dashboard UI/UX for SaaS, admin, analytics, operations, finance, and internal tools. Use when creating dashboard information architecture, scan order, tables, charts, filters, search, bulk-action flows, drill-downs, alerts, settings, dense states, responsive rules, prototypes, or design handoffs. Do not implement product code, data plumbing, or release checks.
---

# Craft Dashboard Web

Design a dashboard as an instrument for scanning, comparing, deciding, and
acting. Let the data, user decisions, and workflow drive the shape of the UI;
do not decorate a grid of cards and call it a dashboard. This skill produces a
data-aware UI/UX design and handoff, not chart code, queries, permissions, or
runtime verification.
Use [audit-uiux-web](../audit-uiux-web/SKILL.md) for independent diagnosis and
`frontend-web-engineering` for implementation.

Load [the dashboard craft process](references/dashboard-craft-process.md) for
a new dashboard or major redesign. Load [data and information
architecture](references/dashboard-data-and-information-architecture.md) when
choosing tables, lists, timelines, charts, cards, navigation, filters, or
density. Load [dashboard interaction and states](references/dashboard-interaction-and-states.md)
for progressive disclosure, tooltips, onboarding, permissions, bulk actions,
and recovery. Load [dashboard critique and proof](references/dashboard-critique-and-proof.md)
before handoff or declaring the dashboard complete.

## Non-negotiable order

Decision → Evidence/Data Contract → Navigation/IA → Data Shape → Scan Order →
Explicitness → Structure → System → Interaction/States → Responsive →
Accessibility/Performance → Proof

Do not begin with KPI cards, chart colors, gradients, or a sidebar mockup
before knowing what users need to monitor, compare, decide, and do.

## 1. Frame the decision

Write:

- persona, role, permissions, situation, frequency, and urgency;
- primary decision or action;
- data needed to make that decision;
- current status, trend, exception, and next step the user must understand;
- acceptable staleness and consequences of wrong or missing data;
- primary, secondary, bulk, destructive, and escalation actions;
- success, failure, and recovery evidence.

Separate evidence, hypothesis, and decision. Preserve data, permissions,
analytics, URLs, exports, audit history, and provider contracts.

## 2. Inspect the data contract before the layout

Inventory real records, schema fields, units, time zones, currencies,
categories, statuses, nulls, outliers, permissions, freshness, pagination,
sorting, filtering, and error conditions. Test typical, empty, one-item,
many-item, long, missing, partial, stale, conflicting, and failed data.

Let the data drive the form:

- align numeric values for comparison;
- use chips or labels for bounded categorical states;
- truncate only with a way to inspect the full value;
- choose a timeline for time-delineated events when a table hides sequence;
- use a chart only when it answers a defined comparison question;
- show inactive, unavailable, or stale records without making them look active.

## 3. Design navigation as the product spine

Organize global navigation by relevance and user frequency. Make the current
location, active state, role, workspace, search, and account context clear.
Place low-frequency settings and help where they do not compete with the core
workflow. A collapsible sidebar still needs labels, tooltips, keyboard support,
and a discoverable expanded state.

Use routes, breadcrumbs, tabs, split views, or drawers according to whether the
user needs durable context, comparison, or a contextual action. Preserve
browser back, refresh, direct URL, query state, and return-from-detail behavior.

## 4. Compose the dashboard around scan order

The first viewport should answer:

1. Where am I and what scope am I viewing?
2. What matters now?
3. What changed or needs attention?
4. What can I do next?

Use a strict grid as a tool, not a prison. Prioritize the main decision,
exceptions, trends, and next actions. A dashboard may use KPI cards, but every
card needs a decision job and meaningful relationship to the data.

Avoid:

- generic card soup;
- decorative charts without units, range, or action;
- equal visual weight for unrelated metrics;
- huge empty hero areas in an operational surface;
- every route using the same four-card template;
- icons or color with no semantic purpose.

## 5. Apply explicitness and progressive disclosure

Keep primary status, search, scope, urgent exceptions, and high-frequency
actions visible. Reveal lower-frequency actions through popovers, menus,
tooltips, hover, selection mode, drawers, or contextual panels only when the
trigger is discoverable and accessible.

Model the explicitness spectrum:

Visible → Directly revealed → Contextual → Deferred → Advanced/hidden

Do not hide a core decision, destructive consequence, permission effect, or
recovery path. Do not dump every feature into a first-login modal. Sequence
onboarding with contextual tooltips, a checklist, or progressive feature
exposure that teaches the next useful action.

Treat invisible UI as part of the product: cell copy actions, row menus,
comments, drawers, tooltips, overlays, keyboard shortcuts, bulk actions,
empty-state actions, and failure recovery must be designed and tested.

## 6. Design data visualization and semantics

For every chart define the user question, metric, unit, time range, aggregation,
comparison, source, freshness, and accessible text summary. Use the simplest
chart that answers the question. Labels, gridlines, legends, range selectors,
tooltips, and data tables should reduce interpretation cost.

Use color from data meaning: status, urgency, category, selection, or emphasis.
Do not use a rainbow palette merely to make a chart look rich. Build semantic
ramps for neutral surfaces, functional accents, statuses, and chart categories;
do not enforce a fixed 60-30-10 ratio. If practical, use a perceptually
consistent system such as OKLCH, then check contrast, color blindness, dark
mode, print/export behavior, and a non-color explanation.

## 7. Design the full interaction surface

Cover:

- search, filters, sort, pagination, grouping, saved views, date ranges, and
  URL persistence;
- row selection, bulk actions, confirmation, progress, partial success,
  rollback, retry, and result summary;
- drill-down, detail, side panel, modal, popover, and return context;
- loading skeleton or stable footprint, empty, no-results, stale, offline,
  permission-denied, provider failure, and interrupted states;
- hover/focus/pressed/selected/disabled states and accessible alternatives;
- copy/export, toast/banner/inline feedback, undo, and audit history;
- onboarding, help, tooltips, keyboard shortcuts, and role-specific actions.

Do not make a core action hover-only or icon-only. Use tooltips for ambiguous
icons and low-frequency actions, not as the only source of essential meaning.

Maintain an interaction matrix for every high-value dashboard control and
workflow:

| Element/flow | Intent | Trigger | Feedback/timing | Outcome | Recovery/accessible alternative |
| --- | --- | --- | --- | --- | --- |
|  |  | pointer/keyboard/touch/route/delay | focus/pending/status | success/error/partial | undo/retry/cancel/keyboard/screen reader |

Include focus-visible, hover and no-hover behavior, tooltip delay, pressed,
selected, disabled, loading, success, error, empty, stale, permission,
interruption, resume, and reduced-motion behavior where relevant. A polished
default dashboard or Figma hover prototype does not prove the interaction.

If the dashboard genuinely contains AI work, add only job-relevant patterns
such as input/attachment context, history or memory controls, inline editing,
progress transparency, and uncertainty cues. Do not import AI-startup UI as a
generic dashboard style.

## 8. Design responsive dashboard behavior

Check narrow mobile, large mobile, tablet/intermediate, desktop, zoom, large
text, and keyboard where supported. Recompose the dashboard:

- move from sidebar to appropriate navigation;
- stack or prioritize metrics instead of shrinking them;
- convert tables to focused rows, horizontal comparison, or detail views only
  when the comparison task remains honest;
- preserve filters, scope, selected records, and scroll context;
- keep primary action and urgent status reachable;
- avoid clipped columns, hidden overflow, and fixed-height data traps.

## 9. Prepare the design handoff

Use real or clearly labelled data fixtures and document query, pagination,
permission, mutation, audit, analytics, export, freshness, and provider
assumptions as design constraints. Never create fake chart values, fake
success, or impossible state combinations to make the dashboard look finished.

Do not implement queries, charts, mutations, permissions, exports, analytics,
or provider behavior. Hand those responsibilities to engineering and product
owners; this skill defines the UI/UX requirements and unresolved questions.

## 10. Prove the design

Follow:

Plan → Model → Wireframe → Compose → Prototype → Critique → Handoff

Walk the primary decision journey plus typical, dense, empty, no-results,
loading, stale, permission, error, rollback, and interrupted states in the
prototype or design artifact. Review search/filter/sort, selection, bulk
action, chart interpretation, drill-down, browser-history expectations,
keyboard/screen-reader intent, reduced motion, responsive widths, semantic
light/dark color, contrast, tooltip timing, and no-hover equivalents. Review
the interaction matrix, not only the default cards.

Report the design artifact, routes/roles/query states covered, data fixtures,
viewport/input matrix, screenshots/recordings, design decisions, data/provider
questions, engineering gates, and unknowns. Do not call a dashboard complete
because the default cards look polished.
