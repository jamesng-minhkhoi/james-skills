---
name: audit-uiux-mobile
description: Audit native mobile UI/UX on iOS and Android with research-first evidence, prioritized findings, state coverage, accessibility, localization, interaction, motion, and screenshot-based visual QA. Use when reviewing a mobile journey or screen; do not implement fixes unless requested.
---

# Audit UI/UX Mobile

Produce an evidence-backed mobile UI/UX audit before recommending changes.

## 1. Establish evidence

Read the app instructions and authoritative design docs, then inspect the
target route, screen composition, shared primitives/tokens, state paths, and
closest shipped surface. Check available screenshots, Figma references, tests,
and visual harnesses.

Separate what is proven from what is assumed:

- Source proves intended or implemented behavior, not runtime reachability.
- Tests prove tested behavior, not visual quality.
- A screenshot/device observation proves a rendered state only for its route,
  data, viewport, and build.
- Production schema, provider, native device, store, and dashboard status need
  their own evidence.

## 2. Walk the journey

Map the primary flow and representative secondary routes. For each surface,
record route, state/input, user action, expected response, recovery path, and
evidence.

Check the applicable states:

- first load, slow/partial load, refresh, and retry;
- empty, one item, typical content, and many items;
- long names/descriptions, missing media, unexpected values, and localization;
- keyboard/focus, disabled controls, validation, submission, cancellation,
  back navigation, and destructive actions;
- offline, permission, authentication, and provider failure.

## 3. Inspect mobile quality

Review findings under these headings:

- **Hierarchy:** one-second focal point, primary action, scan order, and useful
  negative space.
- **Composition:** product-specific visual language, meaningful card use, token
  fidelity, icon consistency, and reference parity.
- **Interaction:** 44pt targets or hit area, pressed/focused/disabled feedback,
  keyboard avoidance, safe areas, sheets, gestures, and back behavior.
- **States:** stable loading footprint, actionable empty state, specific
  recoverable error, offline response, and crowded content.
- **Accessibility:** role, label, state, uniqueness, Dynamic Type/large text,
  reduced motion, and decorative content hidden from assistive technology.
- **Localization:** translated copy, long strings, diacritics, right-to-left
  behavior when supported, and no clipped or fixed-width text.
- **Motion/native surfaces:** causal animation, cancellation/recovery, reduced
  motion, and blur/mask/glass behavior under transforms.

Reject token-only polish when hierarchy, composition, interaction, or state
coverage remains weak.

## 4. Prioritize

Classify each finding:

- **P0:** blocks use, causes serious accessibility failure, or risks harm.
- **P1:** breaks a core journey or makes the primary task unreliable.
- **P2:** materially harms clarity, access, consistency, or polish.
- **P3:** minor refinement with limited user impact.

For every finding include route/component, reproduction or screenshot evidence,
user impact, recommendation, confidence, and verification method. Do not claim a
fix from source inspection alone.

## 5. Report

Return:

1. Executive summary and top risks.
2. Route/state coverage and missing evidence.
3. Findings grouped by P0–P3.
4. Recommended sequence with scope boundaries.
5. Automated checks run and exact results.
6. Rendered routes/states, device/viewport, and screenshots actually observed.
7. Open native-device, provider, production, store, or review gates.

If rendering is unavailable, say visual QA is not observed and keep confidence
lower rather than treating tests or source code as visual proof.
