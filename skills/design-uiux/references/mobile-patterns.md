# Mobile pattern matrix

Use this reference when choosing a structure or translating a desktop/web
reference into a touch-first mobile flow. Pick the least disruptive surface
that gives the user enough context to complete the job.

## Content structure

| User need | Prefer | Check before design handoff |
| --- | --- | --- |
| Scan and act on records | List or grouped list | Long labels, status, swipe alternatives, empty and no-results states |
| Understand event order | Timeline | Date grouping, timezone, missing events, pagination or loading |
| Compare a defined metric | Chart with labels | Units, axes, range, loading, accessible text summary, misleading decoration |
| Compare many fields | Table or structured rows | Search, filter, sort, truncation, horizontal overflow, selection and bulk actions |
| Understand one object | Detail route or sheet | Back behavior, edit/save, related records, destructive actions |
| Choose among a few options | Inline choice, menu, or sheet | Current selection, cancel, confirmation, keyboard/focus behavior |

Do not choose cards because they are visually convenient. Choose them only when
each card represents a distinct object, decision, or actionable group.

## Touch-first input and actions

Thumbs drag and swipe more readily than they aim at small taps. Choose the
gesture first, then name the visible alternative; tap is for commit.

| Job | Prefer | Not | Visible alternative |
| --- | --- | --- | --- |
| Set a number (dose, weight, quantity) | Ruler or slider the user drags past a fixed marker | − and + steppers, typed digits | A visible "type a value" field; assistive technology adjusts the value |
| Set a time of day | Draggable knob on a 24-hour ring, or a sliding time ruler | A time-picker row that opens a second sheet | Tapping the ring or ruler |
| Set a date near today | Swipeable strip of days | A calendar-popover row | A "More dates" link to the full calendar |
| Pick one of a few options in a form | Swipeable wheel with the choice centred | Segmented tabs in the middle of a sheet | Tapping a neighbouring option |
| Act on a list row | Swipe for Edit and Delete, press-and-hold for peek and menu | A button on every row | Row opens a detail with the same actions; Edit mode for assistive tech |
| Delete anything | Overflow (•••) menu, swipe, or the detail screen | A standing button beside Save | The same menu item, reachable without a gesture |
| Pick one of a short list in a sheet (language, unit, region) | Snapping wheel with the choice centred in a band, a haptic tick per row, and Done to commit | A tall list of tappable cards with a check disc | Tapping a row rolls it to the centre; the wheel is adjustable for assistive tech |

- When the choice changes how the app reads (language, units), the sheet
  previews it live: the title and commit button relabel into the centred
  option, from the real locale strings, before anything is committed.

- Every adjustable control (ruler, ring, wheel, strip) also exposes an
  assistive path: an adjustable value, or accessibility actions that do what
  the swipe does. State it in the board's note.
- Delete may live in the ••• menu (a deliberate tap, away from the primary
  action), the swipe, or the detail screen. It never lives in a
  press-and-hold quick menu, which holds only safe actions (Edit, Pause).
- A segmented control still fits switching views on a screen, such as a chart
  range. **Never inside a sheet**: no tabs, segmented control, or chip rail,
  whether switching views or entering a value. It is a gate failure
  (critique-and-proof gate 6), not a taste note; do not draw it as an option.
- Show each gesture on the canvas as its own board: the swiped row, the held
  row with its menu, the scrubbed chart.

### Gesture map before gesture boards

When a screen gets any custom gesture, write this table on the canvas before
drawing the boards, then put each row in its board's note. Scrolling, zooming,
and panning content counts: it already owns its motion even though nobody
designed it as a gesture. Example, a photo carousel with a caption:

| Gesture | Does | Visible control | Already claimed by | Resolution |
| --- | --- | --- | --- | --- |
| Swipe left on a photo | Deletes it | Delete in the ••• menu | Paging to the next photo | Dropped; delete stays in the menu |
| Pull down | Closes | Close button | Scrolling a long caption; sheet dismissal | Live only when the caption is at its top |

"Already claimed by" names what the content or platform already does with
that motion: scroll, zoom, pan, page, edge back, sheet dismissal. A gesture
whose motion the content already uses moves to a handle, waits for a boundary
(top, end, normal zoom), or is dropped. A reference app's gesture transfers
only if its content behaves the same: Photos swipes up for info because a
photo does not scroll, so the same swipe on a list or a multi-page document
never fires. Ownership details:
[motion and gesture](motion-and-gesture.md#gesture-ownership-and-conflict-rules).

Next and previous between items (a sideways swipe in a viewer) states its
order for every way the screen opens (the list, search, a link from another
screen), for an item listed in two places, and for a next item not yet
loaded. If any of these has no answer, the gesture is an open question on the
canvas, not a drawn feature.

## Glance sheet, dedicated screen

A sheet that lists records the user manages (medications, visits, weights)
shows a glance and an expand control that opens a dedicated screen with
add, edit, and remove. Do not make the sheet the only place to manage them.
In an app that holds several entities (pets, children, workspaces), every
entity-scoped screen and sheet carries a subject chip in its header, the
entity's photo or initial with its name, so the user never has to infer
whose data it is.

## Web-to-mobile translation

| Web pattern | Mobile translation | Failure to avoid |
| --- | --- | --- |
| Sidebar | Bottom tabs for top-level destinations; sheet or compact route for secondary navigation | Shrinking a desktop sidebar into an unusable narrow column |
| Hover tooltip | Visible label, info button, press/focus feedback, or contextual inline help | Making meaning unavailable to touch or keyboard users |
| Hover action | Visible action, overflow menu, swipe with visible alternative, or selection toolbar | Hiding a core action behind an undiscoverable gesture |
| Popover | Anchored menu for short choices; bottom sheet for contextual work | Blocking the task with a full modal for a simple choice |
| Modal dialog | Native sheet for reversible contextual work; full-screen route for complex or permanent work | Losing context or making back/cancel ambiguous |
| Toast | Brief non-blocking confirmation for non-consequential status | Using a disappearing toast as the only proof of a critical result |
| Infinite canvas | Prioritized vertical sections with progressive disclosure | Presenting a desktop information density that cannot be scanned on a phone |

## Feedback selection

| Situation | Surface | Requirements |
| --- | --- | --- |
| Local validation or correction | Inline message | Beside the field or object; preserve input and explain the fix |
| Brief non-blocking confirmation | Toast or inline status | State what happened; do not hide a required next step |
| Persistent system or network status | Banner or durable status row | Explain impact and recovery; remain available until resolved |
| Contextual editing or filtering | Sheet | Preserve context, support cancel/apply, and handle keyboard and safe area |
| Complex or consequential decision | Modal or full-screen route | Clear title, explicit actions, back/cancel behavior, and no accidental commit |
| Long-running operation | Inline progress or progress surface | Show pending state, continuation, cancellation, and failure recovery |

## Navigation and state decisions

Navigation is what a screenshot cannot show. Every transition answers: what
is this destination, must the user be able to come back, and what does back
(chevron, iOS edge swipe, Android back) do afterwards? Adapted from
Appllama's navigation laws (MIT).

| The step is | Present it as | Back and dismissal |
| --- | --- | --- |
| Deeper into the same context | Push | Pops to the source with its state intact |
| Moving past a state the world has left (signed in, onboarding done, paid, session finished) | Replace — a one-way door | Must never re-enter the old state; Android back from home exits the app |
| A self-contained task with steps | Modal with its own stack and Cancel/Done | Cancel asks first only if work would be lost |
| A short interruption (picker, filters, item options) | Sheet with detents | Drag or tap outside to dismiss; returns to the same place |
| Immersive content | Full-screen modal | Explicit Close |
| Floating over a still-visible screen (confirm card, lightbox, coach mark) | Overlay | Dismiss returns focus to the screen beneath |
| A destructive confirmation | Action sheet or dialog | Cancel is always available |
| Actions on one item | Native context menu | — |
| Share, web, photo picking | The system controller | Never a rebuilt route |

- A sheet that grows a second step was a modal all along. If a link could
  open it, it is a route.
- One-way doors keep the user's place: sign-in demanded by one action (save,
  follow, buy) is a modal that completes that action where it was tapped, and
  a paywall opened from a feature dismisses back onto the feature, unlocked.
- Block back in exactly two cases: an irreversible request in flight (seconds,
  with visible progress) and unsaved work in a modal (ask first). Transient
  in-screen state (selection mode, expanded search) consumes the first back.
  Anything else that traps back — a funnel, a rating prompt — is a defect.
- Tabs are peers: no slide between them, each keeps its own stack, re-tapping
  the active tab returns to its root. Full-attention screens (composer,
  player, checkout) present above the tabs.
- Deep links land with a sensible stack beneath; a cold start lands by
  session state, never flashing sign-in before home.
- Use a menu for a short list of mutually exclusive or infrequent actions.
- Use selection mode and a contextual toolbar when actions apply to multiple
  records. Keep the selection count and exit path visible.
- Use optimistic UI only when the product can safely assume success. Define the
  rollback and retry state before shipping it.

For every surface, answer: where did the user come from, what remains visible,
how do they cancel, what does back do, and where do they land after success or
failure? When studying references, record each step's presentation as well as
its look; consistent presentation is part of what makes a flow feel native.
