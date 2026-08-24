# Mobile UIUX principles

Use this reference to make design decisions, not to impose a visual style.
The principles are ordered by the questions that should be answered before
polish.

## Contents

- [Evidence and intent](#evidence-and-intent)
- [Content and data shape](#content-and-data-shape)
- [The explicitness spectrum](#the-explicitness-spectrum)
- [Hierarchy and subtraction](#hierarchy-and-subtraction)
- [State and feedback architecture](#state-and-feedback-architecture)
- [Visual language](#visual-language)
- [Motion and personality](#motion-and-personality)
- [Trust, interruption, and recovery](#trust-interruption-and-recovery)

## Evidence and intent

Begin with the user's situation, not the desired component. Write:

> When [situation], [user] needs to [job] so they can [outcome].

Then separate three things:

1. **Evidence:** shipped behavior, user research, analytics, tickets, product
   rules, platform conventions, or an existing visual system.
2. **Hypothesis:** an unverified assumption about user intent, hierarchy, or
   interaction.
3. **Decision:** the chosen behavior and why it best serves the job.

Inspect comparable products as flows. Record the task, information density,
navigation, disclosure, feedback, and recovery pattern. Borrow the reasoning,
not the brand's surface treatment or a desktop pattern that depends on hover.

## Content and data shape

Content is a structural input. Inventory realistic titles, labels, counts,
dates, statuses, media, nulls, errors, and longest supported translations
before choosing containers.

Choose a structure by user task:

- **List:** scan, compare lightly, and act on individual records.
- **Grouped sections:** scan categories or priority clusters.
- **Timeline:** understand change over time or event order.
- **Chart:** answer a defined comparison question with honest axes, labels,
  range, units, and an accessible fallback.
- **Detail surface:** understand one object before acting.
- **Table:** compare many consistent fields; add search, filter, sort, and
  truncation rules instead of shrinking everything until it is unreadable.
- **Cards:** represent distinct objects or decisions, not merely decorate a
  list.

For any dense surface, name the user's comparison task and decide how they
search, filter, sort, select, edit, and recover from no data or stale data.

## The explicitness spectrum

Every action and explanation belongs somewhere on this spectrum:

`Visible → Directly revealed → Contextual → Deferred → Advanced/hidden`

Choose the level using:

- **Frequency:** frequent actions should require less discovery.
- **Consequence:** destructive, irreversible, or safety-critical actions need
  stronger explicitness and confirmation.
- **Discoverability:** hidden controls need a visible affordance, familiar
  placement, or contextual explanation.
- **Space and cognitive load:** secondary detail can be deferred when the user
  can still understand the current decision.
- **Timing:** teach a feature at the moment it becomes useful, not in a large
  onboarding wall.

For mobile, translate hidden or hover-dependent behavior into a visible button,
labelled menu, bottom sheet, press/focus state, inline expansion, or accessible
gesture with an alternative. Never hide the only path to a core job.

## Hierarchy and subtraction

The first viewport should answer three questions quickly: where am I, what
matters, and what can I do? Establish one focal point and one dominant primary
action. Use size, position, contrast, grouping, whitespace, and language before
adding decoration.

Run two passes:

1. **Removal pass:** delete redundant arrows, borders, labels, cards, shadows,
   gradients, and repeated explanations.
2. **Affordance pass:** verify that every remaining control looks actionable,
   has an adequate target, responds to touch, and communicates its result.

Cards are justified when they distinguish an object or actionable group. A
stack of identical cards is usually a sign that grouping, spacing, or content
hierarchy needs work.

## State and feedback architecture

Model important components as state machines rather than styling only the
default state. At minimum, consider:

`idle → pressed/focused → pending → success | recoverable error`

Add selected, disabled, empty, no-results, offline, permission-denied,
interrupted, resumed, and stale states when they can occur.

For each transition, document:

- what changed and why the user should care;
- where feedback appears and how long it remains;
- whether the user can continue, undo, retry, or cancel;
- what happens if the app backgrounds, the network fails, or the data changes;
- whether the UI updates optimistically and how rollback is communicated.

Preserve the semantic identity of an object between states. A saved row should
become the same saved row, not an unrelated replacement, so motion and focus
can explain continuity.

## Visual language

- Use semantic color roles: content, surface, border, action, success,
  warning, danger, and information. Confirm contrast in every supported theme.
- Treat dark mode as a re-composition: adjust contrast, saturation, elevation,
  and shadow behavior rather than inverting hex values.
- Use one icon family with consistent optical size, stroke, and weight. Add a
  label or supporting text when an icon is unfamiliar or consequential.
- Keep typography simple and purposeful: distinguish hierarchy, support
  scanning, and protect readable line lengths.
- Use borders and shadows to communicate grouping or depth. If an effect does
  not improve comprehension, affordance, trust, or personality, remove it.
- Treat platform conventions as part of the system: safe areas, keyboard,
  large text, focus, haptics, back behavior, and native sheet semantics.

## Motion and personality

Motion is optional and should clarify cause, continuity, hierarchy, progress,
or result. Classify meaningful motion as within-page navigation, between-page
navigation, or direct manipulation. For each one, name its subject, user
benefit, progress source, commit/cancel behavior, duration/easing family, and
reduced-motion fallback. A gesture must have a discoverable alternative for a
core action and must not conflict silently with scrolling or system gestures.
Avoid effects that delay a consequential action or make a loading state look
like success. See the [motion and gesture system](mobile-motion-gesture-system.md)
for the contract and proof matrix.

Personality can enter through natural language, contextual illustration,
meaningful empty states, and small moments of delight. Keep the tone playful
only where it supports the product; never use delight to soften a failure,
hide risk, or compete with a health, financial, security, or destructive
decision.

## Trust, interruption, and recovery

Users should understand whether their action was received, is still pending,
completed, or failed. Preserve entered data and progress across keyboard
changes, navigation, backgrounding, permission prompts, and recoverable errors.

Do not use a timeout, disappearing toast, or animation as the only evidence of
a consequential result. Provide a durable state, a retry path, and an undo or
recovery path when the product contract allows it.
