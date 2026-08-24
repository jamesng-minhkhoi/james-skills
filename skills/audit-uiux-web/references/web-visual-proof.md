# Web visual proof

Use after rendering the real route in a supported browser. Source inspection,
lint, tests, and static screenshots support a review but do not replace
interactive proof.

## Browser proof sequence

For each primary journey:

1. Open the real entry URL in the supported browser.
2. Record browser/OS, build, viewport, theme, input method, fixture, and auth
   or permission state.
3. Capture the initial route and the primary action before interacting.
4. Trigger the action with pointer and keyboard where applicable.
5. Observe pending, success, failure, recovery, focus, URL/history, and motion.
6. Reload, use browser back/forward, and open the relevant URL in a new tab.
7. Repeat representative states at narrow, intermediate, and desktop widths.
8. Test reduced motion, zoom/large text, and no-hover paths when relevant.

If the supported browser cannot reach a local app, report the browser proof as
unobserved. Do not replace it with source confidence.

## Visual acceptance gates

Rate Strong, Concern, Critical, Unknown, or Not applicable:

| Gate | Pass condition |
| --- | --- |
| Hierarchy | User, location, focal content, primary action, and next step are clear without decorative effects |
| Color restraint | One dominant accent; other saturated colors have semantic or data meaning; raw/duplicate colors are justified or consolidated |
| Container discipline | Cards and elevation group distinct tasks or objects; repeated rows and wrappers are not card soup |
| Typography | Intended font and declared type roles are applied; long content remains usable |
| Responsive composition | Layout re-composes at narrow, intermediate, and desktop widths without overflow or task loss |
| Interaction completeness | Focus, hover/pressed, pending, success, error, empty, disabled, menu/dialog, and recovery states have usable paths |
| Requested motion | Each requested motion moment has a trigger, purpose, timing/easing, reduced-motion behavior, and observed proof |

## Interaction-state proof

For each important control, record:

| Check | Evidence |
| --- | --- |
| Intent | User goal and why the control is visible or disclosed |
| Trigger | Pointer, keyboard, touch, route, delay, or system event |
| Feedback | Focus, hover, pressed, pending, progress, toast, or status |
| Outcome | Success, partial success, error, empty, stale, or permission result |
| Recovery | Cancel, close, escape, undo, retry, resume, or alternate path |
| Browser | URL, history, refresh, new tab, session, and scroll/focus behavior |
| Accessibility | Name, role, state, focus order/return, announcement, contrast |
| Motion | Purpose, timing/easing, interruption, reduced motion, no-hover fallback |

If a state is not observed, mark it Unknown. A static screenshot cannot prove
timing, focus return, keyboard behavior, delayed feedback, recovery, or motion.

## Finding shape

| Priority | Tag/principle | Route/viewport/state | Evidence + proof level | Impact | Recommendation | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 | FLOW, IA, STATE, RESPONSIVE, ACCESS, SYSTEM, MOTION, PERFORMANCE, TRUST |  |  |  |  | High/Medium/Low |

## Completion evidence

Report exact routes, data fixtures, browsers/OS, viewport sizes, theme, input
method, screenshots/recordings, automated checks, and provider/production gates
not observed. Do not call visual work complete because lint, typecheck, or one
desktop screenshot passes.
