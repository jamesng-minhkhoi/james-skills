# Mobile critique and proof checklist

Use after rendering the design artifact or prototype in a design tool,
simulator, device, or closest available mobile harness. Source inspection and
tests can support the review but cannot replace rendered design evidence.

## Review order

Fix the earliest failed layer first:

1. **Outcome:** Can the intended user complete the job?
2. **Flow:** Are entry, next step, back, cancel, skip, save, and recovery clear?
3. **Content:** Do real labels, data, nulls, errors, and translations fit?
4. **Explicitness:** Are primary actions visible and secondary actions
   discoverable without hover or hidden gestures?
5. **Hierarchy:** Is the focal point and primary action clear in one second?
6. **Structure:** Does the chosen list, timeline, chart, table, sheet, or route
   match the user's information task?
7. **System:** Are type, spacing, icons, color, materials, components, and
   platform conventions coherent?
8. **Interaction:** Are touch, focus, keyboard, selection, back, loading,
   success, error, offline, and interruption behavior understandable?
9. **Gesture/transition:** If motion or gestures exist, are they correctly
   classified, spatially coherent, discoverable, interruptible, cancellable,
   and free of scroll/system-gesture conflicts?
10. **Motion/personality:** Is motion necessary, does it clarify change, and
    does personality support rather than compete with comprehension?
11. **Proof:** Are the important states, gesture checkpoints, and devices
    actually rendered and observed?

## Rendered-state matrix

Capture or inspect at least:

| Dimension | Representative evidence |
| --- | --- |
| Journey | Entry, primary action, success, next step, back/cancel |
| Data | Typical record, longest realistic content, empty, no-results, dense list |
| Network | Loading, slow/pending, success, recoverable error, offline if supported |
| Interaction | Pressed, focused, selected, disabled, keyboard, sheet, gesture ownership and conflict |
| Platform | Small phone, large phone, safe areas, dark mode, large text if supported |
| Recovery | Retry, rollback/undo, permission denial, interruption and resume |
| Motion | Rest, in-progress, threshold, completion, cancellation, reduced motion, and runtime recording |

## Evidence report

Report:

- exact route, state, and data fixture rendered;
- device/simulator, orientation, theme, text-size, and platform;
- screenshots or recording reviewed and the visual issues observed;
- design checks and prototype walkthroughs performed;
- unresolved native, provider, production, analytics, or store dependencies;
- product behaviors and data contracts that engineering must preserve.

Do not call product behavior complete because a prototype or design review
passes. Do not call a native or production gate complete without engineering
observing that gate.

## Fast questions

- Can a first-time user tell where they are and what to do?
- Is the primary action reachable with one hand and named by its outcome?
- Can the user recover without losing entered data or context?
- Does every hidden action have an understandable reveal?
- If a gesture exists, can users discover it, cancel it, recover from it, and
  perform the same core action without the gesture?
- Does a swipe or drag conflict with scrolling, a sheet, or a system-edge
  gesture?
- Does feedback appear where attention is already directed?
- Do color, icon, motion, or density carry meaning that survives accessibility
  settings and reduced motion?
- Would this still work with a long name, missing image, slow network, or
  translated string?
