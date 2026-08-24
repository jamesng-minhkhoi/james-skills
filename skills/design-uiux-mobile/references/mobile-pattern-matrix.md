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

- Use a page/route when the user needs durable context, a shareable/backable
  destination, or a complex multi-step task.
- Use a sheet when the task is contextual, reversible, and should return to the
  current surface with its state intact.
- Use a menu for a short list of mutually exclusive or infrequent actions.
- Use selection mode and a contextual toolbar when actions apply to multiple
  records. Keep the selection count and exit path visible.
- Use optimistic UI only when the product can safely assume success. Define the
  rollback and retry state before shipping it.

For every surface, answer: where did the user come from, what remains visible,
how do they cancel, what does back do, and where do they land after success or
failure?
