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
