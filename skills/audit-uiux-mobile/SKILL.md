---
name: audit-uiux-mobile
description: Audit native mobile UI/UX on iOS and Android with quick, deep, or release review modes. Use research-first evidence and mobile UX principles to evaluate journeys, explicitness, progressive disclosure, states, accessibility, localization, interaction, motion, trust, and screenshot-based visual QA. Do not implement fixes unless requested.
---

# Audit UI/UX Mobile

Produce an evidence-backed mobile UI/UX audit before recommending changes.

Use [Mobile UX principles](references/mobile-ux-principles.md) as the review
standard. Do not treat it as a box-ticking exercise: apply the principles to
the user's actual goal, context, route, and state, and attach evidence to every
important conclusion.

## 0. Select an audit mode

Choose the smallest mode that matches the request. If no mode is specified,
use **Deep** for a new or high-risk journey and **Quick** for a narrow review.

- **Quick:** one journey or screen; context brief, core principles, highest-risk
  states, and prioritized findings. Do not pretend to have release evidence.
- **Deep:** primary journey plus representative secondary routes; full principle
  scorecard, content/decision review, state matrix, and visual evidence review.
- **Release:** Deep plus a device/accessibility matrix, automated checks, real
  runtime screenshots, interruption/offline checks, and explicit open gates.

## 1. Establish context and evidence

Write a short context brief before inspecting details:

- target user and situation;
- user goal and successful end state;
- primary route and affected secondary routes;
- risk level: ordinary, financial, privacy, safety, or irreversible;
- supported platforms and form factors;
- product/design constraints and explicit scope boundary;
- available runtime, screenshot, test, and provider evidence.

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

For **Deep** and **Release**, record coverage for every route/state rather than
reviewing only the default loaded screenshot.

## 3. Inspect mobile quality

Review findings under these headings:

- **UX principles:** explicitness, progressive disclosure, visibility of system
  status, mental-model fit, recognition over recall, user control and freedom,
  error prevention/recovery, consistency, flexibility, and minimalist signal-
  to-noise. Read the reference for the mobile-specific questions.

- **Hierarchy:** one-second focal point, primary action, scan order, and useful
  negative space.
- **Composition:** product-specific visual language, meaningful card use, token
  fidelity, icon consistency, and reference parity.
- **Interaction:** platform-sized targets or compensating hit area (commonly
  44pt on iOS and 48dp on Android), pressed/focused/disabled feedback, keyboard
  avoidance, safe areas, sheets, gestures, and back behavior.
- **States:** stable loading footprint, actionable empty state, specific
  recoverable error, offline response, and crowded content.
- **Accessibility:** role, label, state, uniqueness, Dynamic Type/large text,
  reduced motion, and decorative content hidden from assistive technology.
- **Localization:** translated copy, long strings, diacritics, right-to-left
  behavior when supported, and no clipped or fixed-width text.
- **Motion/native surfaces:** causal animation, cancellation/recovery, reduced
  motion, and blur/mask/glass behavior under transforms.
- **Content and decisions:** terminology, information scent, consequence
  clarity, optional versus required actions, permission timing, and whether the
  copy helps users decide before they commit.
- **Trust and dark patterns:** cancellation, consent, destructive actions,
  urgency, defaults, hidden costs, and whether the interface pressures or
  misleads the user.

For each relevant principle, mark **Strong**, **Concern**, **Critical**,
**Unknown**, or **Not applicable**. Explain the user impact and cite the route,
state, screenshot, source, or test that supports the rating.

When principles conflict, state the trade-off explicitly. Common conflicts are
minimalism versus discoverability, progressive disclosure versus transparency,
gesture efficiency versus accessibility, platform convention versus brand
differentiation, and personalization versus consistency.

Reject token-only polish when hierarchy, composition, interaction, or state
coverage remains weak. A visually attractive screen can still fail because it
hides the next action, overloads the first view, breaks the user's mental model,
or makes recovery difficult.

## 4. Verify mobile conditions

Use the mode-appropriate matrix:

| Condition | Quick | Deep | Release |
| --- | --- | --- | --- |
| Narrow and large phone viewport | Target state | Required | Required |
| Large text / Dynamic Type | If text-heavy | Required when relevant | Required |
| Keyboard and focus | If input exists | Required when relevant | Required |
| VoiceOver/TalkBack or equivalent | Risk-based | Required for a11y findings | Required |
| Offline/interruption/resume | Risk-based | Required when relevant | Required |
| Portrait/landscape/tablet/foldable | N/A unless supported | When supported | Required when supported |
| iOS/Android platform difference | Target platform | All supported platforms | All release platforms |

Record the exact device or simulator, OS/build, viewport, data state, and
screenshots. If a condition was not observed, mark it **Unknown**.

## 5. Prioritize

Classify each finding:

- **P0:** blocks use, causes serious accessibility failure, or risks harm.
- **P1:** breaks a core journey or makes the primary task unreliable.
- **P2:** materially harms clarity, access, consistency, or polish.
- **P3:** minor refinement with limited user impact.

For every finding include route/component, reproduction or screenshot evidence,
user impact, recommendation, confidence, and verification method. Do not claim a
fix from source inspection alone.

## 6. Report

Return:

1. **Context brief** — user, goal, risk, platforms, scope, and mode.
2. **Executive summary** — top risks and the most important journey outcome.
3. **Coverage matrix** — routes, states, devices, evidence, and unknowns.
4. **Principle scorecard** — status and evidence for each relevant principle.
5. **Findings table** — priority, principle, route/state, evidence, impact,
   recommendation, confidence, and verification method.
6. **Recommendation sequence** — scope boundaries and principle trade-offs.
7. **Checks and observations** — exact commands, runtime states, devices, and
   screenshots actually observed.
8. **Open gates** — native-device, provider, production, store, or review work.

Use this finding shape:

| Priority | Principle | Route/state | Evidence | Impact | Recommendation | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 |  |  |  |  |  | High/Medium/Low |

If rendering is unavailable, say visual QA is not observed and keep confidence
lower rather than treating tests or source code as visual proof.
