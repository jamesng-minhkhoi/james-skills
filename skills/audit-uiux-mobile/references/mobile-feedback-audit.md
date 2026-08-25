# Mobile feedback audit

Use this reference for every Deep, Release, or Forensic audit. The purpose is
to prevent a polished default state from hiding missing feedback during the
states users actually experience.

## Required matrix

Create one row per important route/action. Use **Implemented**, **Partial**,
**Missing**, **Unknown**, or **Not applicable**; attach proof level and the
next verification action.

| State | Required question | Preferred evidence |
| --- | --- | --- |
| Initial load | Is the shell stable? Does a list use final-shape skeleton rows when no usable content exists? | Runtime slow-load capture or source plus explicit Unknown |
| Background refresh | Does existing content remain usable while refresh runs? | Runtime pull/focus refresh |
| Empty/no-results | Does the message explain why and provide the next useful action? | Rendered state with representative data |
| Press/focus | Is the interaction acknowledged immediately? | Device or interactive local observation |
| Mutation pending | Is only the affected control/row disabled or busy? Is duplicate submit prevented? | Interaction trace and source/state evidence |
| Success | Does the user know what changed and what to do next? Is a toast/banner/inline status appropriate? | Runtime success after a real action |
| Recoverable error | Is the affected object/field named and is retry/recovery local and actionable? | Forced failure or data-connected observation |
| Offline/stale | Is freshness/status honest and is retry/queue behavior explicit? | Network interruption/resume observation |
| Permission denied | Does the user get a useful explanation and retry/settings path without a dead button? | First-request and previously-denied device pass |
| Cancellation/back | Can users cancel safely and keep or discard work intentionally? | Back, cancel, destructive-action trace |
| Interrupted/resumed | Does backgrounding, notification entry, or process restart preserve context and progress? | Device background/resume/process test |
| Accessibility | Are state changes announced with role, label, value, busy/disabled/selected state? | VoiceOver/TalkBack or equivalent observation |

## Surface selection rules

Use the least interruptive surface that preserves comprehension:

- **Skeleton:** initial content fetch with no safe content. Match the eventual
  row geometry; do not use shimmer merely as decoration.
- **Spinner:** a compact control-level or short local operation. A spinner is
  not a substitute for a list skeleton when the user is waiting for records.
- **Inline message:** validation or an error attached to the field/control that
  can be corrected locally.
- **Toast:** brief, non-blocking confirmation where the user can continue. Do
  not make a toast the only durable proof of a consequential save, payment,
  deletion, or status transition.
- **Banner/durable row:** persistent network, account, permission, or system
  condition. Include a clear action when recovery exists.
- **Progress:** upload, import, processing, or other long operation. State what
  is complete, what remains, and whether retry/cancel/resume is possible.
- **Modal/Alert:** destructive confirmation, imminent data loss, or a decision
  that genuinely blocks the current task. Do not use Alerts for ordinary success
  or every recoverable error.

## Static inventory pass

Before rating feedback coverage, search the repository for the implementation
signals and compare them with the route/state matrix:

```text
ActivityIndicator | Skeleton | shimmer | RefreshControl | Alert.alert
Toast | Snackbar | Banner | notice | inline error | accessibilityLiveRegion
loading | pending | submitting | refreshing | retry | undo | cancel
permission | Linking.openSettings | offline | stale | error boundary
```

For each result, determine whether it is:

1. attached to the correct user action;
2. scoped to the affected screen/row/control;
3. visually and semantically distinct from success, disabled, and empty;
4. recoverable without losing input or context; and
5. actually reachable from the route and data state.

Absence of a matching primitive is a finding only when the state is applicable;
presence of a primitive is not proof that the state is reachable.

## Runtime checkpoints

For the highest-risk journey, observe at least:

1. cold start with slow or delayed data;
2. list refresh with existing content;
3. one successful mutation and its next state;
4. one forced mutation failure and retry;
5. permission denial and settings recovery when relevant;
6. background/resume or notification entry during pending work.

Record device/build, viewport, data fixture, network/permission condition, and
whether the state was naturally observed, manually forced, or inferred. Source,
tests, and screenshots may establish intent or rendered appearance, but not
native reachability or production delivery.

## Finding prompts

Ask these questions explicitly in the report:

- Where does the user's attention go while the action is pending?
- Does the feedback preserve the object identity and layout, or cause a
  destructive jump that can lead to a second tap?
- Does success state what changed and expose the next useful action?
- If the operation failed, can the user retry only the failed unit?
- Does the user receive feedback where they acted, including assistive
  technology?
- Is a toast too ephemeral for the consequence, or is an Alert too disruptive?
- Does a missing skeleton make the first viewport feel blank or broken?
