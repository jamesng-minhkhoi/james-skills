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
- assign design issues to `design-uiux` and Expo implementation issues
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
- use the shared vocabulary: name the highest proof rung, mark unobserved gates
  `NOT_RUN`/`UNKNOWN`, and give each finding a stable `F-mobile-<n>` ID.

## Case 4: Tap-first edit sheet, project asks for touch-first

Prompt/artifact: The project's design docs say mobile users prefer drag and
swipe. A pet-care edit sheet sets a dose with − and + buttons, a frequency
with a segmented control, and deletes with a red button beside Save. Its
weight screen never shows which of the user's pets it belongs to, its list
has a divider above the first row, and the source places a photo badge at the
corner of a number display (no render was taken).

Expected audit behavior:

- run the forensic overlay and report NATIVE (steppers, segmented control),
  STRUCTURE (standing Delete), CONTENT (missing entity identity), and SYSTEM
  (divider) findings with stable `F-mobile-<n>` IDs, naming the drag, wheel,
  and overflow-menu replacements;
- report the badge overlap as `UNKNOWN`: source declares placement, nothing
  observed it;
- add a FLOW finding if the sheet is the only place to manage the records;
- name the highest proof rung reached (`declared` for source or a design
  board), not `rendered`.

## Case 5: Native controls the project endorses

Prompt/artifact: An app uses the iOS segmented control, a native stepper, and
native grey/red swipe actions, and its design docs endorse them.

Expected audit behavior:

- report no defect for these controls, or P3 at most with the stated reason;
- still check for a visible and an assistive path for each swipe action.

## Case 6: Design boards for a document viewer

Prompt/artifact: Design boards (no build) for a pet document viewer. The
document is a full-width multi-page PDF that scrolls vertically. A swipe up
on the page opens details "like Photos". A bottom toolbar has the pet's
avatar, Details, Share, and More; the avatar, Details, and a summary line
above the toolbar all open details. Delete appears under More and in the
details view. The press-and-hold
menu says "Change kind" where the app ships "Change type". The current screen
shows "Peti is reading" and "Peti couldn't read this"; the boards show only
the read state, and mark the assistant's summary with a ✦ sparkle although the
app has a mascot.

Expected audit behavior:

- report the swipe-up collision with vertical scroll, naming the borrowed
  Photos gesture as the source and a handle or end-of-document trigger as the
  fix;
- report STRUCTURE for three controls opening details and two homes for
  Delete; STATE for the dropped reading and failed states; CONTENT for the
  label drift and the generic sparkle;
- give every finding a stable `F-mobile-<n>` ID and the `declared` rung; feel,
  thresholds, and the real PDF render stay `UNKNOWN`.

## Case 7: One visible home, one swipe

Prompt/artifact: Boards where Delete lives under More and also as a row
swipe, with accessibility actions on the swipe.

Expected audit behavior:

- no duplicate-Delete finding: the swipe is not a visible home, so Delete has
  one.

## Case 8: Expo total snaps after a stepper change

Prompt/artifact: Expo cart; tapping the quantity stepper changes the order
total with no motion. A simulator recording is available. A second build has
a digit pop-in with no blur.

Expected audit behavior:

- report the first build under the "Silent or noisy value change" row at P2,
  because the total is the main result of the action, at the `interactive`
  rung at most (simulator);
- not mark the second build down for the missing blur, which is the named
  native substitution.

Must not have: a `device` claim from a simulator recording; a finding for
missing blur.

## Case 9: Custom motion craft versus platform motion

Prompt/artifact: A device recording of an Expo app: a custom bottom sheet
eases behind the finger while dragged and stops dead at its top edge, a custom
favourite toggle's knob slides rigidly, cards jump to the detail screen with
no shared element, and the native tab bar and system Switch use platform
motion.

Expected audit behavior:

- load the motion audit reference and the [motion craft
  checklist](../../_shared/motion-craft.md); report M14 (tween while held),
  M19 (no rubber band), M5 (rigid knob), and M20 (no shared identity), each
  citing its rule ID with the recording as evidence;
- leave the native tab bar and system Switch out of the findings, because
  platform motion is exempt;
- keep findings at P3 unless the drag lag blocks the task.

## Case 10: Grouping and controls that read as text

Prompt/artifact: A simulator screenshot of a Home screen: a question with
three pale answer pills, then a row of round shortcut buttons, every block
20 pt apart; a tile icon drawn with a gradient that fades to transparent on
a pale disc; a "Journal" label inside a 60 pt circle touching its edge.

Expected audit behavior:

- measure the gaps and report that the shortcut row reads as more answers
  (Proximity), with the measured values and the fix order (spacing, then a
  hairline between groups with different jobs);
- report the pills as not reading as buttons, the icon under 3:1 against its
  disc, and the label's clearance, each with a crop as evidence;
- report the measured contrast and gaps at the `rendered` rung, and mark
  device and screen-reader checks `NOT_RUN`.

## Must not have

A report fails if it contains any of these:

- a `device` or store claim inferred from a simulator;
- `PASS` or `READY` for a gate that was not observed;
- a proof label or verdict outside the shared ontology;
- a finding without a stable `F-mobile-<n>` ID;
- an accessibility or interruption claim made without a device or runtime
  observation (a contrast or geometry value measured on rendered pixels is
  an observation at the `rendered` rung, not such a claim);
- a gesture called fine on boards without checking what the content already
  does with that motion (6);
- grouping or control contrast passed from a text-only contrast check, or a
  uniform stack left unflagged (10).
