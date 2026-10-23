# Critique and proof

Use after the proposal is rendered on the Design artifact, and again before
handoff. This is a design critique, not product QA: source inspection and
tests can support a review but cannot replace looking at the rendered work.
Run [slop and consistency](slop-and-consistency.md) first.

## Review order

Fix the earliest failed layer first:

1. **Outcome:** Can the intended user complete the job or make the decision?
2. **Flow:** Are entry, next step, back, cancel, skip, save, and recovery
   clear? On web, also refresh, direct URL, and new tab.
3. **Content:** Do real labels, data, nulls, errors, prices, and translations
   fit?
4. **Explicitness:** Are primary actions visible and secondary actions
   discoverable without hover or hidden gestures?
5. **Hierarchy:** Are location, focal point, scan order, and primary action
   clear in one second?
6. **Structure:** Does the chosen list, table, timeline, chart, detail, sheet,
   dialog, or route fit the information task?
7. **System:** Do type, spacing, icons, color, materials, and components match
   the product's design system and each other?
8. **Interaction:** Are pointer, touch, keyboard, focus, forms, overlays,
   loading, success, error, offline, and interruption behavior designed?
9. **Motion:** Is each motion necessary, classified, and cancellable where a
   gesture drives it?
10. **Responsive and platform:** Does the composition re-compose across widths
    or devices, safe areas, keyboard, large text, and dark mode where
    supported?
11. **Accessibility:** Do names, roles, focus order, contrast, zoom, and
    reduced motion preserve the task?
12. **Proof:** Were the important states actually rendered and looked at?

Surface-specific first questions:

- **Dashboard:** Does the first viewport serve a real decision rather than a
  KPI wall? Can users tell what changed, what is urgent, what is stale, and
  what to do?
- **Landing page:** Can a new visitor explain the offer after the first
  viewport? Does every major claim have nearby, credible proof? Is the CTA
  honest about what happens next?
- **Mobile:** Is the primary action reachable with one hand and named by its
  outcome? After each one-way door, does every back path fail to re-enter the
  old state?

## Rendered-state matrix

Render at least the rows that apply:

| Dimension | Evidence |
| --- | --- |
| Journey | Entry, primary action, result, next step, back/cancel |
| Content | Typical, longest realistic, translated, empty, no-results, dense, error |
| Network | Loading, slow, partial, success, recoverable error, offline if supported |
| Interaction | Pressed, hover, focus-visible, selected, disabled, keyboard, sheet or dialog |
| Platform | Small and large phone, safe areas, dark mode, large text (mobile); narrow, tablet, desktop, zoom (web) |
| Data (dashboard) | One, dense, null, stale, conflicting; search, filter, sort, pagination; permissions |
| Message (landing) | First viewport, headline wrapping, CTA, proof, form pending/success/error |
| Motion | Rest, in progress, threshold, completion, cancellation, reduced motion |
| Recovery | Retry, undo, rollback, permission denial, interruption and resume |

A static artboard cannot prove timing, focus return, keyboard behavior,
gesture feel, or recovery. Mark those as unknown and leave them as gates for
engineering.

## Interaction-state proof

For each primary action and important component, record:

| Check | Evidence |
| --- | --- |
| Intent | The goal it supports and why it is visible or disclosed |
| Trigger | Pointer, touch, keyboard, route, delay, or system event |
| Feedback | Pressed, focus, pending, progress, toast, or status |
| Outcome | Success, partial success, error, empty, stale, or permission result |
| Recovery | Cancel, close, undo, retry, resume, or alternate path |
| Accessibility | Name, role, state, focus order and return, non-color cue |
| Motion | Timing and easing, interruption, reduced-motion behavior |

## Finding shape

| Priority | Tag | Screen/viewport/state | Evidence | User impact | Proposed fix |
| --- | --- | --- | --- | --- | --- |
| P0–P3 | FLOW, CONTENT, STRUCTURE, EXPLICITNESS, STATE, SYSTEM, MOTION, NATIVE, ACCESS, DATA, MESSAGE, PROOF |  |  |  |  |

## Completion report

State the artifact, the screens and states rendered, the content fixtures,
the device or viewport, the decisions made, and the gates left to
engineering. Do not call product behavior complete because a design or
prototype looks right.
