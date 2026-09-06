# Dashboard UIUX process

Use for a new dashboard, admin surface, analytics page, operational console,
or dense internal tool. For a small local component fix, use only relevant
sections.

## 1. Define the decision

Write:

> When [situation], [role] needs to [decision/action] so they can [outcome].

Name frequency, urgency, scope, permissions, acceptable staleness, failure
cost, and the moment of value. A dashboard is not successful because it
contains many metrics; it is successful when the user makes the right next
decision efficiently.

## Visual direction without losing the task

State the audience, decision, intended character, and preserve/overhaul scope.
Inspect the existing surface before changing it. Set density by comparison and
scan needs, variation by hierarchy, and motion by feedback. A polished refresh
does not imply lower density, more animation, or a new component library.

For a supplied reference, record observed grid proportions, type hierarchy,
row spacing, semantic color roles, shape rules, and focus/interaction behavior.
Label values measured, estimated, or proposed; include the source and viewport.
A static screenshot cannot prove sorting, responsive behavior, or transitions.
Turn the relevant observations into design rules with responsive exceptions
and rendered checks using typical and dense data.

Keep useful repetition, tables, familiar navigation, semantic status colors,
and chart categories. Do not apply landing-page image quotas, single-accent
limits, hero spacing, or carousel substitutions to operational data. Express
brand through consistent type, alignment, surfaces, and state treatment.
Evaluate visual novelty by whether the user can still compare and act.

## 2. Inventory the data

Create a data contract inventory:

- records, fields, units, categories, statuses, nulls, and outliers;
- freshness, time zone, currency, pagination, filters, sorting, and grouping;
- source, confidence, permissions, and failure behavior;
- typical, empty, dense, stale, partial, conflicting, and failed fixtures.

Write the comparison or decision each field supports. Let this inventory drive
the representation before choosing a component.

## 3. Map the dashboard flow

Map scope selection, landing state, primary decision, drill-down, edit/action,
result, next step, back, return context, retry, and recovery. Include query
parameters, refresh, direct links, browser back, role changes, and permission
denial.

## 4. Choose the information architecture

Establish navigation spine, current location, workspace/role context, search,
global scope, local tabs, detail relationship, and low-frequency settings/help.
Use breadcrumbs or a clear return path when a user can enter a detail view
without following the expected hierarchy.

## 5. Shape the data surface

Choose the least disruptive representation:

- table for structured field comparison;
- list for scan-and-act records;
- timeline for event order and time;
- chart for a defined trend or comparison;
- card for a distinct KPI, object, alert, or decision;
- detail route/panel for context before action.

Test the shape with real data before visual polish.

## 6. Design explicitness and invisible UI

Show scope, primary status, exceptions, search, and high-frequency actions.
Progressively reveal secondary actions through contextual controls. Design
tooltips, row menus, cell copy, drawers, comments, keyboard shortcuts,
selection mode, onboarding, empty actions, and failure recovery as first-class
states.

For every high-value control, record intent, trigger, visible feedback, timing,
success or failure result, recovery, keyboard/screen-reader path, touch path,
and reduced-motion behavior. Include hover, focus, tooltip, loading, toast,
overlay, and no-hover equivalents; hidden UI is still product behavior.

Use semantic color roles rather than a fixed 60-30-10 distribution: neutral
surface layers, functional accents, status ramps, and light/dark theme values.
Verify contrast and non-color explanations in charts, statuses, selection, and
alerts.

## 7. Compose and critique in passes

1. decision and first viewport;
2. navigation and scope;
3. data shape and scan order;
4. filters, comparisons, and bulk actions;
5. states, permissions, and recovery;
6. accessibility and responsive re-composition;
7. performance, semantics, and visual system;
8. subtraction and polish.

Fix the earliest failed pass. Do not add a chart to compensate for a missing
data question or another card to compensate for weak prioritization.

## 8. Design handoff evidence

Report roles, routes, query states, data fixtures, freshness, viewport/input
matrix, interactions reviewed, screenshots/recordings, design decisions,
provider constraints, implementation questions, and unresolved unknowns.
