# Dashboard interaction and states

Use this reference for progressive disclosure, hidden UI, onboarding, filters,
tables, charts, bulk actions, permissions, and recovery.

## Contents

- [State architecture](#state-architecture)
- [Progressive disclosure](#progressive-disclosure)
- [Onboarding](#onboarding)
- [Filters, selection, and bulk actions](#filters-selection-and-bulk-actions)
- [Tooltips and invisible UI](#tooltips-and-invisible-ui)
- [Feedback choice](#feedback-choice)
- [Accessibility and keyboard](#accessibility-and-keyboard)

## State architecture

For every important action, trace:

entry → scope/filter → affordance → focus/press → pending → success | error
→ retry/undo/next

Add empty, no-results, stale, partial, offline, permission-denied,
session-expired, interrupted, resumed, duplicate-submit, and rollback when
applicable. Preserve row/object identity and selected context between states.

For each high-value control, keep a compact state contract:

| Element/flow | Intent | Trigger | Feedback/timing | Outcome | Recovery/alternative |
| --- | --- | --- | --- | --- | --- |
|  |  | pointer/keyboard/touch/route/delay | focus/pending/status | success/error/partial | undo/retry/cancel/accessible path |

Test hover and no-hover behavior, tooltip delay, focus-visible, pressed,
selected, disabled, loading, success, error, interruption, resume, and
reduced-motion behavior where relevant. A Figma prototype or default screenshot
does not prove the state contract.

## Progressive disclosure

Use visible controls for primary actions and current status. Reveal secondary
actions through:

- row menus and popovers;
- hover plus an equivalent keyboard/screen-reader path;
- selection toolbar;
- contextual drawer or detail panel;
- tooltip for ambiguous icon meaning;
- onboarding tooltip or checklist at the moment of need.

Do not use a one-time modal to explain the entire product. Do not hide a core
action, destructive consequence, permission effect, or recovery path.

## Onboarding

Sequence:

1. orient the user's role, scope, and first useful outcome;
2. point to the primary action;
3. confirm the result;
4. introduce the next useful capability;
5. leave a durable help or checklist path.

Allow skip, pause, revisit, and recovery. Do not block the dashboard with
unrelated education before the user sees its value.

## Filters, selection, and bulk actions

Define:

- active filter and scope summary;
- clear-all and no-results recovery;
- selection count, select-all semantics, partial selection, and exit;
- bulk action confirmation, pending progress, partial success, failure, retry,
  and audit/result summary;
- permission differences between visible and actionable records.

Use URL state when a view should be shareable or survive refresh. Never silently
discard a user's filters or selected records during navigation.

## Tooltips and invisible UI

Tooltips should clarify unfamiliar icons, values, or truncated content. They
must be available to keyboard and touch users and should not contain the only
path to a core action. Check delay, placement, collision, focus, dismissal,
screen-reader announcement, and reduced-motion behavior.

Prefer semantic color roles and ramps for neutral surfaces, functional accents,
statuses, selection, and chart categories. Do not force a 60-30-10 ratio or
make color the only explanation. Verify light/dark values, contrast, color
vision differences, print/export, and non-color text or icon equivalents.

Also test copy-cell actions, comment indicators, row menus, drawers, popovers,
keyboard shortcuts, empty-state actions, and error recovery. Dense UI is
finished only when these hidden or conditional surfaces work.

## Feedback choice

| Situation | Prefer | Avoid |
| --- | --- | --- |
| Local validation | Inline field or row message | Detached or premature red alert |
| Brief safe confirmation | Toast or inline status | Toast as only proof of a consequential write |
| Persistent network/data state | Banner or durable status | Disappearing warning |
| Contextual edit/filter | Drawer, sheet, or popover | Losing dashboard context |
| Complex/destructive decision | Dialog or route | Accidental commit or ambiguous cancel |
| Long-running bulk action | Progress with cancel/result summary | Frozen page or fake completion |

## Accessibility and keyboard

Support semantic table structure, row/column relationships, labels, sort state,
filter state, chart summaries, focus-visible, keyboard navigation, escape,
focus return, and screen-reader announcements for results. Do not rely on color,
hover, motion, or a tooltip alone.
