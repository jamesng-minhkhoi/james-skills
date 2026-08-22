---
name: craft-ui-mobile
description: Design and implement polished native mobile UI for iOS and Android by starting from user intent, flow, content, and states before visual polish. Use when building or redesigning mobile screens, components, navigation, sheets, forms, micro-interactions, loading/empty/error states, or responsive mobile layouts. Preserve business logic and data contracts when the request is UI/UX-only.
---

# Craft UI Mobile

Build the product journey first and the pixels second. Use
[the mobile craft process](references/mobile-craft-process.md) for any screen
that needs more than a small local edit. Load
[mobile craft principles](references/mobile-craft-principles.md) when making
hierarchy, disclosure, content, motion, or visual-language decisions. Load
[the mobile pattern matrix](references/mobile-pattern-matrix.md) for data-heavy
surfaces, overlays, feedback, navigation, or translating a web reference to
mobile. Load [the motion and gesture system](references/mobile-motion-gesture-system.md)
when designing navigation transitions, swipes, drags, sheets, card browsing, or
other meaningful motion. Load [the critique checklist](references/mobile-critique-checklist.md)
when reviewing rendered work or writing the handoff. When changing this skill,
use the [regression evaluation](evals/craft-ui-mobile-regression.md) to compare
the candidate against the previous version.

## Non-negotiable order

`Intent → Evidence → Flow → Content → Explicitness → Structure → System → Interaction → Gesture/Transition → Motion → Proof`

Do not start with gradients, shadows, colors, or isolated component polish when
the user's path, information hierarchy, or state coverage is unclear.

## 1. Frame the job

- State the target user, situation, user intent, entry point, and successful
  outcome in plain language.
- Write the moment of value: what the user should understand, decide, or do
  after this surface. Separate that from the underlying database operation.
- Inspect the closest shipped mobile surface, product/design docs, analytics or
  issue evidence when available, tokens, primitives, route composition, and
  visual references before inventing UI. Record what is evidence and what is a
  design hypothesis.
- Identify the primary action, secondary actions, irreversible actions, and
  what the user must understand before committing.
- Mark the scope boundary. For UI/UX-only work, preserve queries, schemas,
  writes, permissions, analytics, navigation destinations, localization
  meaning, and feature contracts. Surface required contract changes separately.

## 2. Sketch the flow before the screen

Map the smallest complete journey with boxes and arrows before detailed styling:

- entry, first decision, primary action, result, and next step;
- back, cancel, skip, save, retry, no-results, and permission paths;
- loading, empty, error, offline, interrupted, and resumed states;
- long content, many records, missing media, and first-time versus repeat use.

If search, filtering, skip, save, back, or recovery is implied by the user's
intent, account for it before polishing the happy path. Keep one decision per
step where a wizard is necessary; avoid steps that only move content around.

## 3. Let content and data shape the UI

Inventory real content before choosing a composition:

- labels, titles, descriptions, counts, statuses, dates, media, and nulls;
- longest realistic strings and supported locales;
- data density, ordering, grouping, and the user's comparison task.

Choose a representation that fits the data. Use a timeline for time-based
events, a list for scan-and-act work, a chart only when its axes and comparison
answer are clear, and a detail surface when context matters. Do not force every
dataset into cards, tables, or decorative charts.

For data-heavy surfaces, also decide how users search, filter, sort, compare,
select, edit, and recover from stale or empty data. See the pattern matrix.

## 4. Choose the right degree of explicitness

Place every action, explanation, and piece of context on an explicitness
spectrum: always visible, visible after a direct interaction, contextual,
deferred until needed, or hidden behind an advanced surface. Choose based on
frequency, consequence, discoverability, and available space—not personal
preference.

- Keep primary jobs and safety-critical information visible.
- Reveal secondary detail progressively, but provide a clear affordance and
  preserve the user's context.
- Never make a core action depend only on hover, long press, edge swipe, or an
  unlabeled icon.
- Sequence onboarding and feature education at the moment of relevance; do
  not front-load a wall of explanation.

Use the mobile pattern matrix when selecting a bottom sheet, menu, popover,
modal, toast, banner, or full-screen route.

## 5. Build the visual system before exceptions

- Reuse the project's tokens and shipped primitives for type, spacing, color,
  radius, icons, shadows, buttons, inputs, lists, sheets, and feedback.
- Establish a small, coherent scale and reuse it. Do not introduce arbitrary
  radius, font, icon, or shadow values to fix one screenshot.
- Use one icon family and optical weight within a functional area. Label an
  unfamiliar icon; never use an icon merely to fill empty space.
- Use grids and auto-layout principles to align groups, but let content and
  platform constraints justify a deliberate break.
- Treat dark mode, large text, contrast, safe areas, and keyboard behavior as
  system requirements when the app supports them.
- Use semantic roles for color and typography. A ratio such as 60-30-10 may
  help balance a composition, but it is not a substitute for meaning,
  contrast, hierarchy, or platform conventions.
- Keep visual materials restrained. Borders, shadows, gradients, glow, and
  glass need a grouping, depth, emphasis, or brand job; otherwise subtract
  them.

## 6. Compose with hierarchy and subtraction

- Give each screen one focal point and one visually dominant primary action.
- Make the first viewport answer: where am I, what matters, and what can I do?
- Use whitespace to group related content and create rhythm; mobile usually
  needs more breathing room than a compressed desktop layout.
- Remove redundant arrows, borders, labels, cards, effects, and decoration
  before adding more. Every element must improve comprehension, affordance,
  trust, or product personality.
- Use cards only for distinct objects or actionable groups. Avoid card soup and
  the generic “icon + title + subtitle” template.
- Use progressive disclosure for secondary actions, but keep the reveal
  discoverable. On mobile, replace hover-only behavior with visible buttons,
  menus, sheets, or an accessible press/gesture alternative.
- Let context and personality support comprehension: natural language,
  meaningful empty states, illustrations, and small moments of delight are
  welcome when they do not compete with the task or critical information.

## 7. Design the full interaction surface

Implement the states a user can actually experience:

- pressed, focused, selected, disabled, loading, submitting, success, and
  error;
- empty, no-results, offline, permission-denied, and retry;
- keyboard open, sheet open/closed, back/cancel, gesture progress, and resume.
- For each important component, define a state map and the transition that
  caused it. For a gesture, model at least `idle → tracking → committed |
  cancelled → settled`. Preserve semantic identity between states so motion
  explains continuity instead of decorating a replacement.
- Define gesture ownership and conflicts with scrolling, system-edge back,
  sheets, sliders, maps, tap, long press, and selection. Every core action
  needs a visible or accessible alternative to a gesture.
- Choose feedback deliberately: inline feedback for local correction, a toast
  for brief non-blocking confirmation, a banner for persistent status, a sheet
  for contextual work, and a blocking modal only when the decision truly
  requires interruption. See the pattern matrix.
- For optimistic changes, define the success assumption, pending treatment,
  rollback, retry, and stale-data behavior before implementation.

Keep loading in the final footprint. Make feedback visible quickly and match
its intensity to the consequence. Keep destructive actions explicit and
recoverable where possible. A visually perfect default state is unfinished if
the system is silent during a save or failure.

## 8. Add purposeful motion and personality

- First choose whether motion is needed. If it is, classify it as within-page
  navigation, between-page navigation, or direct manipulation. Use the motion
  and gesture system reference to write a motion contract before coding.
- Animate the subject of a change: press, transition, reveal, save, progress,
  success, error, or navigation. For direct manipulation, the motion should
  follow the user's input and define commit, cancellation, reversal, and
  recovery behavior.
- Use motion to clarify continuity, hierarchy, and cause/effect; add delight
  only when it does not compete with the task.
- Prefer subtle depth and restrained effects. A gradient, glow, glass layer, or
  shadow needs a compositional job and must survive the native runtime.
- Use project motion tokens, respect reduced motion, and provide non-motion
  feedback for important changes.
- Check blur, mask, glass, zero-frame, clipping, transform-ancestor, frame-rate,
  safe-area, and platform-gesture issues on the actual platform.

## 9. Implement without breaking the product

Prefer the existing component contract. Split a large screen by meaningful
visual regions, not arbitrary line count. Keep route files thin when the app's
architecture expects screen components elsewhere. Preserve business behavior
and keep UI-only changes reviewable.

When a new mental model is consequential, present two or three concrete
directions with trade-offs before coding and honor the selected direction.

## 10. Prove the result

Follow:

`Plan → Build → Run → Screenshot → Critique → Refine → Verify`

- Run the narrowest relevant lint, typecheck, tests, i18n checks, and build.
- Render the primary journey plus representative non-happy states on the
  simulator/device or closest available mobile harness.
- Review one-second hierarchy, content fit, touch/focus feedback, safe areas,
  keyboard, localization, accessibility, motion, and interruption recovery.
- For gesture or transition work, observe rest, in-progress, threshold,
  completion, cancellation, conflict, reduced-motion, interruption, and
  runtime-performance checkpoints. Record slow drags and quick flicks where
  relevant; screenshots alone cannot prove gesture quality.
- Compare against the approved reference or explain why none exists.
- Report exact checks, routes/states/devices rendered, screenshots observed,
  and native/provider/production gates not observed. Never call visual work
  complete from source inspection or tests alone.
