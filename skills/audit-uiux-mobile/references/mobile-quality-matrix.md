# Mobile quality matrix

Use this reference in Deep and Release audits and whenever the product contains
dense data, overlays, complex state changes, or web-derived patterns.

## Contents

- [Structure and data](#structure-and-data)
- [Feedback selection](#feedback-selection)
- [State transitions](#state-transitions)
- [Web-to-mobile translation](#web-to-mobile-translation)
- [Visual semantics](#visual-semantics)

## Structure and data

| User need | Expected structure | Audit failures |
| --- | --- | --- |
| Scan and act on records | List or grouped list | Card soup, missing status, unclear ordering, gesture-only action |
| Understand event order | Timeline | Lost date context, wrong ordering, missing events, no pagination/loading |
| Compare a metric | Chart with units, labels, range, and summary | Decorative data, misleading scale, unlabeled axes, inaccessible meaning |
| Compare many fields | Table or structured rows | Tiny text, uncontrolled overflow, no search/filter/sort, arbitrary truncation |
| Understand one object | Detail route or contextual sheet | Missing back/cancel, context loss, unrelated actions competing for attention |
| Choose or edit options | Inline control, menu, sheet, or route based on complexity | Full modal for a trivial choice, ambiguous current value, accidental commit |

Check typical, long, localized, null, empty, dense, partial, stale, error, and
unexpected values. Ask what comparison or decision the structure supports. Do
not accept cards or charts merely because they look polished.

## Feedback selection

| Situation | Expected surface | Flag when |
| --- | --- | --- |
| Local validation | Inline message | Error is detached, premature, vague, or input is lost |
| Brief non-blocking confirmation | Toast or inline status | It is the only proof of a consequential result or hides a next step |
| Persistent system/network status | Banner or durable row | It auto-dismisses before resolution or offers no recovery |
| Contextual editing/filtering | Sheet | Keyboard, safe area, cancel/apply, or context restoration fails |
| Complex consequential decision | Modal or full-screen route | Interruption is unnecessary, actions are ambiguous, or back commits work |
| Long-running operation | Progress surface | Pending work appears complete, cannot be resumed/cancelled, or silently fails |

Match feedback prominence and persistence to consequence. More interruption is
not automatically more clarity.

## State transitions

For each important action trace:

`entry → affordance → press/focus → pending → success | error → retry/undo/next`

Record:

- the triggering action and data input;
- whether feedback appears where attention is directed;
- whether the component keeps semantic and focus identity;
- optimistic assumption, pending treatment, rollback, retry, and stale-data
  behavior;
- cancellation, back, background/resume, and duplicate-submission behavior;
- whether the state was naturally observed, manually forced, or inferred.

Flag impossible combinations such as editable controls during an irreversible
submission, success while data remains unchanged, or loading that replaces the
whole layout and causes destructive movement.

## Web-to-mobile translation

| Web pattern | Expected mobile treatment | Flag |
| --- | --- | --- |
| Sidebar | Bottom tabs for primary destinations; route or sheet for secondary navigation | Narrow desktop sidebar or unreachable controls |
| Hover tooltip | Visible label, info action, press/focus state, or contextual help | Meaning exists only on hover |
| Hover action | Visible action, menu, selection mode, or swipe with visible alternative | Core action is undiscoverable on touch |
| Popover | Anchored menu for short choices or bottom sheet for contextual work | Tiny desktop popover or needless blocking modal |
| Modal | Native sheet or full-screen flow according to complexity and permanence | Ambiguous back/cancel or lost context |
| Infinite canvas | Prioritized vertical sections and progressive disclosure | Desktop density scaled down without restructuring |
| Desktop table | Structured rows, focused detail, or intentional horizontal comparison | Unreadable columns converted into arbitrary cards |

## Visual semantics

- Color should use stable roles for content, surface, action, success, warning,
  danger, and information. Flag decorative color that contradicts meaning.
- Dark mode should rebalance contrast, saturation, elevation, and shadow rather
  than mechanically invert colors.
- Typography should support hierarchy and scanning. Flag excessive type roles,
  weak contrast, tiny metadata, and lines that become unreadable with large
  text.
- Icons should share a family, optical size, and weight. Unfamiliar or
  consequential icons need labels or supporting text.
- Borders, elevation, gradients, glow, and glass should communicate grouping,
  affordance, depth, state, or brand. Flag effects with no functional role.
- Component consistency should preserve meaning, not force every task into the
  same shape. Flag variants that differ without purpose and uniform components
  that erase meaningful hierarchy.
