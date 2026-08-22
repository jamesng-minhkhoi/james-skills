# Web UI craft process

Use for a new product route, workflow, settings area, form, editor, search
surface, detail view, or substantial component redesign. For a tiny local fix,
apply only the relevant sections.

## 1. Frame the job

Write:

> When [situation], [user] needs to [job] so they can [outcome].

Name the moment of value, entry point, primary action, failure cost, and
success state. Record ordinary, privacy, financial, safety, or irreversible
risk. Record what the user is trying to decide or accomplish before choosing
the visual treatment. Keep product intent separate from the underlying
database operation.

## 2. Gather evidence

Inspect the current route, browser entry paths, real content, data shape,
analytics, permissions, design system, closest shipped surface, support
evidence, and comparable products. Record:

- evidence: directly observed behavior or product rule;
- hypothesis: unverified assumption;
- decision: selected behavior and why.

Borrow pattern reasoning—navigation, density, disclosure, feedback, and
recovery—not another product's visual skin.

## 3. Map the journey

Sketch entry, decision, primary action, result, next step, back, refresh,
deep-link, cancel, undo, retry, permission, and interruption paths. Add
loading, partial, empty, no-results, stale, offline, provider-error, and
session-expired states where the product can encounter them.

## 4. Shape content before containers

Test real labels, long copy, localized strings, dates, counts, media, nulls,
permissions, errors, and realistic density. Let the user's information task
choose list, detail, table, editor, split view, sheet, dialog, or inline
reveal. Keep decision-critical information near the decision.

## 5. Wireframe before polish

Use grayscale or low-fidelity structure to test location, content order,
primary action, first viewport, empty space, and state placeholders. If the
flow is unclear without color or effects, fix structure first.

## 6. Build system and states

Define type roles, spacing, content width, color roles, surfaces, borders,
icons, focus, motion, responsive rules, and component variants. Define a
semantic color architecture: neutral surface layers, functional accent ramps,
semantic status ramps, and separate light/dark theme values. A 60-30-10 ratio
may inspire exploration but is not a validation rule for product UI. Verify
contrast and non-color meaning.

Model important controls as transitions:

idle → focused/pressed → pending → success | recoverable error

Add selected, disabled, empty, no-results, permission-denied, stale,
interrupted, resumed, rollback, and unsaved-change states where relevant.
For each high-value control, record intent, trigger, visible feedback, timing,
result, recovery, keyboard/screen-reader path, touch path, and reduced-motion
behavior. Include tooltip, hover, focus, loading, toast, and overlay states;
they are product behavior, not decoration.

## 7. Critique in layers

Review in this order:

1. outcome and task completion;
2. browser flow and user control;
3. content and data fit;
4. explicitness and progressive disclosure;
5. hierarchy, grid, rhythm, and scan order;
6. interaction, feedback, and recovery;
7. responsive behavior;
8. accessibility, performance, and semantics;
9. personality and polish.

Check conventions and content structure before novelty. Use progressive
disclosure to preserve orientation and control, and prefer a user-controlled
"load more" pattern over endless loading when access to the footer, position,
or task completion matters.

Fix the earliest failed layer. Do not add another card or animation to conceal
an unclear task.

## 8. Handoff evidence

Report route, states, content fixtures, browser/viewport matrix, screenshots or
recordings, automated checks, data/provider boundaries, and unobserved gates.
