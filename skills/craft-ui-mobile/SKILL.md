---
name: craft-ui-mobile
description: Design and implement native mobile UI for iOS and Android apps. Use when building or redesigning screens, components, navigation flows, sheets, forms, loading/empty/error states, motion, accessibility, or responsive mobile layouts. Preserve business logic and data contracts when the request is UI/UX-only.
---

# Craft UI Mobile

Build mobile UI as a complete user journey, not as isolated styling.

## Loop

Follow:

`Plan → Build → Run → Screenshot → Critique → Refine → Verify`

## Before coding

- Read the app's instructions, design docs, tokens, route/screen composition,
  shared primitives, and closest existing screen.
- Identify the user's job, entry point, primary action, affected states, and
  the visual source of truth (device screenshot, Figma, or shipped surface).
- For UI/UX-only work, preserve queries, schemas, writes, permissions,
  analytics, navigation destinations, localization meaning, and feature
  contracts. Surface any required contract change separately.
- If the choice changes the user's mental model, offer a few concrete options
  with trade-offs before implementing and honor the selected direction.

## Compose

- Give each screen one focal point and one visually dominant primary action.
- Prefer the existing button, text, input, card, list, sheet, toast, skeleton,
  and empty/error primitives. Do not make a lookalike when the real component
  already exists.
- Use cards only for distinct objects or actionable groups; avoid card-wrapping
  every row and avoid generic “icon + title + subtitle” screens.
- Choose native mobile patterns deliberately: bottom sheets for focused,
  reversible decisions; inline feedback for recoverable errors; full routes for
  deep-linkable or multi-step journeys.
- Account for safe areas, keyboard avoidance, back behavior, gestures, narrow
  widths, large text, long localized copy, and missing media.

## Build the state machine

Cover the applicable states: loading, loaded, empty, error, offline, disabled,
focused, submitting, success, zero items, many items, and long content. Keep
loading in the final footprint, make empty states actionable, and make errors
specific and recoverable. Every control needs a useful accessibility label,
role, and state; target 44pt or compensate with hit area.

Use project motion tokens and animate the subject of a change. Avoid decorative
loops, respect reduced motion, and check blur, masks, glass, and other native
surfaces under animated transforms.

## Verify

- Run the narrowest relevant lint, typecheck, test, i18n, and build checks.
- Render the primary journey and representative non-happy states on a real
  simulator/device or the closest available mobile harness.
- Use the one-second test: name the focal point and primary action. Inspect
  hierarchy, press/focus feedback, keyboard/safe-area behavior, localization,
  accessibility, motion, and edge states.
- Report changed files, exact checks and results, routes/states actually
  rendered, screenshots observed, and native/provider/production gates not
  observed. Tests passing is not visual acceptance.
