# Dashboard critique and proof

Use after rendering and exercising the real dashboard with representative
roles, data, widths, and query states.

## Review order

1. **Decision:** Does the user know what to monitor, compare, or do?
2. **Data:** Does the representation match the data and decision?
3. **Navigation:** Is scope, role, current location, and return context clear?
4. **Scan order:** Are exceptions, changes, and next actions prioritized?
5. **Explicitness:** Are primary controls visible and secondary controls
   discoverable without hiding core meaning?
6. **Interaction:** Do filters, search, sort, selection, bulk actions, drill-down,
   tooltips, dialogs, and keyboard paths work?
7. **States:** Are loading, empty, stale, permission, error, rollback, and
   interruption states real and actionable?
8. **Visualization:** Do charts have a question, units, labels, range, source,
   accessible summary, and meaningful color?
9. **Responsive:** Does the dashboard recompose without destroying comparison?
10. **Accessibility/performance:** Are semantics, focus, contrast, large text,
    reduced motion, loading, layout shift, and input response acceptable?
11. **Polish:** Do effects improve comprehension, trust, or personality?
12. **Proof:** Were the important roles, states, widths, and outcomes observed?

## Rendered-state matrix

| Dimension | Evidence |
| --- | --- |
| Navigation | Sidebar/top nav, active state, role/workspace, search, collapse, back |
| Data | Typical, one, dense, empty, no-results, long, null, stale, conflicting |
| Query | Search, filter, sort, date range, pagination, saved view, URL refresh |
| Interaction | Row menu, tooltip, selection, bulk action, chart hover/focus, drawer/dialog |
| Visualization | Labels, units, range, comparison, legend, table/text alternative |
| Permissions | Visible, disabled, hidden, denied, role change, unauthorized route |
| Responsive | Narrow mobile, tablet/intermediate, desktop, zoom, large text |
| Recovery | Provider failure, retry, rollback, partial success, interruption/resume |
| Runtime | Browser back, refresh, direct link, performance, layout shift, reduced motion |
| Color/theme | Semantic ramps, light/dark adaptation, contrast, non-color meaning, export |

## Interaction-state proof

For each primary action, hidden surface, and important data interaction, record
and observe:

| Check | Evidence to capture |
| --- | --- |
| Intent | Decision or task supported and why the control is visible/disclosed |
| Trigger | Pointer, keyboard, touch, route, delay, or system event |
| Feedback | Focus, hover, pressed, pending, tooltip, progress, toast, or status |
| Outcome | Success, partial success, error, empty, stale, or permission result |
| Recovery | Cancel, escape, close, undo, retry, resume, or alternate path |
| Accessibility | Name, role, state, focus order/return, announcement, non-color cue |
| Motion | Timing/easing, interruption, reduced-motion behavior, no-hover fallback |

Mark unobserved states as unknown. Static cards and screenshots cannot prove
keyboard behavior, focus return, delayed tooltips, reduced motion, or recovery.

## Fast questions

- Is the first viewport organized around a real decision rather than a KPI wall?
- Does the data determine the table, list, timeline, chart, or card form?
- Can users tell what changed, what is urgent, what is stale, and what to do?
- Are numbers aligned and categorical states easy to scan?
- Can users find the primary action without discovering hover or hidden UI?
- Does onboarding sequence the next useful action instead of dumping features?
- Do tooltips, row menus, drawers, and bulk actions work beyond the happy path?
- Can users recover from no-results, permission, provider, and bulk-action errors?
- Does responsive reflow preserve the comparison task and selected context?
- Would the dashboard still make sense without its color palette and gradients?

## Finding shape

| Priority | Tag | Route/role/query/state | Evidence + proof level | Impact | Recommendation | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 | DECISION, DATA, NAV, EXPLICITNESS, STATE, CHART, ACCESS, RESPONSIVE, PERFORMANCE, SYSTEM |  |  |  |  |  |

Do not call a dashboard AI slop as a finding. Name the observable generic
pattern, user impact, evidence, confidence, and exact verification.

## Completion report

Report exact route, role, data fixture, freshness, query state, browser/OS,
viewport, screenshots/recordings, checks run, provider boundaries, and unknowns.
Distinguish source-declared, rendered-static, interactive-local,
data-connected, failure-observed, device/browser-observed, and
production-observed evidence.
