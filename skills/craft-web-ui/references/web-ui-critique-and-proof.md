# Web UI critique and proof

Use after rendering the real route in a supported browser. Source inspection
and tests support a review but do not replace rendered and interactive proof.

## Review order

1. **Outcome:** Can the user complete the intended job?
2. **Flow:** Are entry, navigation, back, refresh, cancel, save, and recovery
   coherent?
3. **Content:** Do real data, labels, nulls, errors, and translations fit?
4. **Explicitness:** Are actions visible or discoverably revealed?
5. **Hierarchy:** Is location, focal content, scan order, and primary action clear?
6. **Structure:** Does the chosen route, list, table, detail, dialog, or sheet
   fit the information task?
7. **Interaction:** Do pointer, keyboard, focus, hover, forms, menus, overlays,
   and feedback work?
8. **Responsive:** Does the composition adapt across widths and input methods?
9. **Accessibility:** Do semantics, labels, roles, focus, contrast, zoom, and
   reduced motion preserve the task?
10. **Performance:** Are loading, layout shift, images, fonts, animation, and
    input response acceptable?
11. **Polish:** Do visual details add comprehension, trust, or personality?
12. **Proof:** Were important states, widths, and outcomes actually observed?

## Rendered-state matrix

| Dimension | Evidence |
| --- | --- |
| Journey | Entry, primary action, result, next step, back, refresh, cancel |
| Content | Typical, longest, translated, empty, no-results, dense, error |
| Interaction | Hover, focus-visible, pressed, disabled, menu, dialog, form states |
| Responsive | Narrow mobile, large mobile, tablet/intermediate, desktop, zoom |
| Accessibility | Keyboard traversal, focus return, screen reader names/roles/states, contrast |
| Network | Loading, slow, partial, success, failure, retry, offline if supported |
| Browser | Direct URL, refresh, browser back, new tab, session expiry |
| Performance | Image/font loading, layout shift, long task, input latency, motion |
| Color/theme | Semantic roles, light/dark ramps, contrast, non-color meaning, chart states |

## Interaction-state proof

For every primary action and important interactive component, record and test:

| Check | Evidence to capture |
| --- | --- |
| Intent | What user goal the control supports and why it is visible or disclosed |
| Trigger | Pointer, keyboard, touch, route, delay, or system event |
| Feedback | Focus, hover, pressed, pending, tooltip, toast, progress, or status |
| Outcome | Success, partial success, error, empty, stale, or permission result |
| Recovery | Cancel, close, escape, undo, retry, resume, or alternate path |
| Accessibility | Name, role, state, focus order/return, screen-reader announcement |
| Motion | Timing/easing, interruption, reduced-motion behavior, no-hover fallback |

If a state is not observed, mark it unknown. A static screenshot cannot prove
timing, focus return, keyboard behavior, delayed tooltips, reduced motion, or
recovery.

## Finding shape

| Priority | Tag | Route/viewport/state | Evidence + proof level | Impact | Recommendation | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 | FLOW, CONTENT, STRUCTURE, EXPLICITNESS, STATE, NATIVE, ACCESS, SYSTEM, PERFORMANCE |  |  |  |  |  |

Do not call a page AI-generated as a finding. Name the observable generic
pattern, user impact, evidence, confidence, and exact verification.

## Completion report

Report the exact route, data fixture, browser/OS, viewport, theme, input
method, screenshots or recording, automated checks, and unobserved
provider/production/analytics gates. Do not call visual work complete because
lint, typecheck, or tests pass.
