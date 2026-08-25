# AI UIUX mobile audit regression cases

Use these fixtures when changing the mobile audit skill. They protect against
audits that reward polish while missing functional, state, and native gaps.

## Case 1: Polished but incomplete flow

Prompt/artifact: A generated card-based app has attractive default screens,
but primary cards do nothing, no loading/error states are visible, and a core
action is available only through a swipe.

Expected audit behavior:

- run the forensic overlay, inventory routes/controls/data/state transitions,
  and verify reachability and outcome rather than rating screenshots;
- report observable FLOW/FUNCTIONAL/STATE/EXPLICITNESS findings with route,
  proof level, impact, confidence, verification, and P0–P3 priority;
- require a visible/accessibility alternative to the gesture and mark
  unobserved native/runtime behavior Unknown;
- assign design issues to `design-uiux-mobile` and Expo implementation issues
  to `frontend-mobile-engineering`.

## Case 2: Screenshot-only release request

Prompt: “The screenshots look good; approve this app for release.”

Expected audit behavior:

- refuse to infer device, accessibility, offline, interruption, permission,
  notification, data, or production proof from screenshots;
- return a coverage matrix, highest proof level, unknown gates, and exact next
  observations required for Release mode.

## Case 3: Feedback coverage omission

Prompt/artifact: A polished marketplace app uses a full-screen spinner for list
loading, native Alerts for all success and error outcomes, and disables an entire
screen during row mutations. It has no skeleton rows, toast/banner/inline
feedback strategy, or forced failure observations.

Expected audit behavior:

- load the mobile feedback audit reference and produce a dedicated feedback
  coverage matrix for initial load, refresh, mutation pending, success, error,
  retry, offline/stale, permission, interruption, and accessibility;
- flag missing final-shape skeletons, over-broad pending scope, and misuse of
  Alerts as STATE/FUNCTIONAL/EXPLICITNESS findings with proof level and impact;
- distinguish “not implemented” from “not observed” and require a runtime
  slow-load/failure/recovery checkpoint before promoting source claims;
- recommend the least interruptive appropriate surface: inline, toast, banner,
  progress, or modal according to consequence.
