# Mobile motion and gesture audit

Use this reference when a route contains navigation transitions, swipe or drag
interactions, card browsing, sheets, reordering, dismissal, scroll-linked
motion, or meaningful animated state changes. Audit the observed product, not
the animation library or the designer's intention.

## Audit stance

Motion is not automatically good or bad. First decide whether motion is
necessary for the task. Then determine whether the observed behavior makes a
useful relationship legible:

- **Continuity:** the same object or context remains identifiable.
- **Hierarchy:** the user can tell what entered, left, expanded, or became
  important.
- **Cause and effect:** the response clearly follows the user's action.
- **Progress:** direct manipulation or meaningful work is visible.
- **Result:** completion, failure, or recovery is understandable.

If none applies, record a possible decorative-motion concern. Do not call an
animation a defect only because it is not personally preferred.

## Classify what is observed

| Category | Examples | Audit focus |
| --- | --- | --- |
| Within-page navigation | Carousel, gallery, card stack, segmented content, local expansion | Does the subject remain connected to its previous context? |
| Between-page navigation | Push/pop route, detail screen, modal, sheet, interactive back | Does motion communicate hierarchy and preserve back/source context? |
| Direct swipe or drag | Dismiss, archive, reorder, reveal, page, confirm, compare | Does the interaction follow input and explain commitment, cancellation, and recovery? |
| No meaningful motion | Static settings, dense data entry, repetitive operations | Does the interface avoid adding delay or decorative animation? |

Do not confuse a timed transition, a scroll gesture, a system-edge gesture, and
a direct-manipulation control. They have different owners, progress models,
thresholds, and accessibility requirements.

## Evidence contract

For each important motion or gesture, record what is known:

| Field | Audit question | Evidence status |
| --- | --- | --- |
| Trigger | What tap, swipe, drag, navigation, or system event starts it? | Observed / source-declared / unknown |
| Subject | What moves, what remains fixed, and what preserves identity? | Observed / inferred / unknown |
| Purpose | What user benefit does the motion provide? | Strong / concern / unknown |
| Progress | Is progress time-based, state-based, scroll-linked, or controlled by the finger? | Observed / source-declared / unknown |
| Commit rule | What distance, velocity, release, or explicit action commits it? | Observed / unknown |
| Cancel rule | Can the user reverse or cancel before a consequential action? | Observed / unknown |
| Completion | What durable result, feedback, and focus follow completion? | Observed / unknown |
| Recovery | Is there undo, rollback, retry, or another safe path? | Observed / unknown |
| Ownership | Does it conflict with scrolling, sheets, sliders, or system back? | Observed / unknown |
| Alternative | Can the same core action be completed without the gesture? | Observed / unknown |
| Accessibility | Does reduced motion preserve meaning? Can assistive technology perform it? | Observed / unknown |
| Runtime | Was it tested on a named device/build, or only in a design/mock? | Proof level |

Never fill an unknown from a screenshot, design file, or source declaration.

## Checkpoint walkthrough

Observe or explicitly mark unknown at each checkpoint:

1. **Rest:** Is the starting affordance discoverable, and is the primary action
   visible without already knowing the gesture?
2. **In progress:** Does the interface respond continuously, preserve context,
   and communicate what will happen?
3. **Threshold:** Can the user tell when commitment is likely? Is the rule
   consistent for slow drags and quick flicks?
4. **Completion:** Is the result durable, correctly focused, and connected to
   the user's action?
5. **Cancellation:** Does reversal return cleanly without accidental commit,
   data loss, or a confusing intermediate state?
6. **Conflict:** What happens when the user scrolls, starts at the screen edge,
   interacts with a sheet, or touches a nested control?
7. **Accessibility:** Does reduced motion preserve status, focus, and cause?
   Is there an equivalent accessible action?
8. **Interruption:** What happens when the app backgrounds, the network fails,
   permissions intervene, or data changes during the interaction?

For a Release audit, capture a recording or device observation for applicable
checkpoints. For Quick and Deep audits, state exactly which checkpoints were
not observed.

## Failure patterns

Use an observable failure rather than a taste judgement:

| Failure | Observable evidence | Typical impact |
| --- | --- | --- |
| Decorative motion | Animation adds delay or spectacle without clarifying a change | Slower task completion, distraction |
| False continuity | Unrelated objects appear to transform into each other | Misleading mental model |
| Undefined transition | Loading, success, or error is animated but the underlying state is unclear | False confidence or uncertainty |
| Hidden gesture | Core action exists only through swipe, long press, or edge gesture | Discoverability and accessibility failure |
| Unclear commitment | Threshold, velocity, or release behavior is unpredictable | Accidental actions or abandonment |
| No cancellation | User cannot reverse before a consequential action commits | Loss of control or data |
| No recovery | Completed gesture has no undo, rollback, retry, or durable status | Irrecoverable mistake or distrust |
| Gesture conflict | Swipe steals scrolling, slider input, sheet dismissal, or system back | Unreliable interaction |
| Motion accessibility failure | Reduced motion removes status, focus, or meaning | Equivalent task becomes unclear or inaccessible |
| Runtime failure | Clipping, dropped frames, delayed response, or native mismatch is observed | Perceived instability and poor control |
| Fake feedback | Animation implies success while data does not change or failure is hidden | Trust and functional integrity failure |

## Severity guidance

- **P0:** Motion or gesture blocks a core task, causes serious accessibility
  failure, hides destructive consequences, or creates material risk.
- **P1:** A core gesture or transition is unreliable, undiscoverable, cannot be
  cancelled, or reports a misleading result.
- **P2:** Motion materially harms hierarchy, orientation, recovery, platform fit,
  or repeat-use efficiency.
- **P3:** Minor timing, easing, consistency, or personality refinement with
  limited user impact.

Adjust severity for frequency, consequence, affected users, and availability of
an equivalent path. A beautiful but optional animation is not P1 merely because
it could be smoother.

## Reporting shape

Add these fields to a motion or gesture finding:

| Field | Required content |
| --- | --- |
| Category | Within-page, between-page, direct manipulation, or no-motion concern |
| Checkpoint | Rest, progress, threshold, completion, cancellation, conflict, accessibility, interruption, or runtime |
| Observation | Specific behavior, not a style preference |
| Evidence | Route, state, input, recording/screenshot, source, device, and build |
| Proof level | Highest directly observed level; keep untested behavior Unknown |
| Impact | What the user cannot understand, complete, control, access, or trust |
| Recommendation | Smallest useful correction, including visible alternative where needed |
| Verification | Exact gesture, state, device, accessibility setting, or data result to recheck |

Example finding:

| Priority | Tag | Route/checkpoint | Observation | Impact | Verification |
| --- | --- | --- | --- | --- | --- |
| P1 | MOTION / ACCESS | /inbox, threshold | Row commits after a short horizontal flick, but no progress or undo appears and the same row also horizontally scrolls | Users can archive the wrong item and cannot recover | Test slow drag, quick flick, scroll conflict, and undo on a named device |
