---
name: audit-uiux-mobile
description: Audit native mobile UI/UX on iOS and Android with quick, deep, release, and adversarial AI-generated UI review. Use research-first evidence to evaluate journeys, data-to-structure fit, explicitness, progressive disclosure, functional states, accessibility, localization, native interaction, visual systems, motion, trust, and rendered proof. Use for vibe-coded, template-generated, or suspected AI-slop mobile projects as well as conventional product audits. Do not implement fixes unless requested.
---

# Audit UI/UX Mobile

Produce an evidence-backed mobile UI/UX audit before recommending changes.

Use [Mobile UX principles](references/mobile-ux-principles.md) as the review
standard. Do not treat it as a box-ticking exercise: apply the principles to
the user's actual goal, context, route, and state, and attach evidence to every
important conclusion.

For Deep or Release audits, or whenever the surface contains dense data,
overlays, charts, complex states, or web-derived patterns, also use
[the mobile quality matrix](references/mobile-quality-matrix.md). For
AI-generated, vibe-coded, template-heavy, or suspiciously polished projects,
always run [the AI-generated UI forensic pass](references/ai-ui-forensics.md).
Judge the observed product, not the tool that produced it.
For any surface with transitions, swipes, drags, card browsing, sheets, or
meaningful animated state changes, also use [the mobile motion and gesture
audit](references/mobile-motion-gesture-audit.md).
For every Deep, Release, or Forensic audit, also use [the mobile feedback audit](references/mobile-feedback-audit.md).
When changing this audit skill, use the [mobile audit regression cases](evals/ai-uiux-mobile-audit-regression.md).

## 0. Select an audit mode

Choose the smallest mode that matches the request. If no mode is specified,
use **Deep** for a new or high-risk journey and **Quick** for a narrow review.

- **Quick:** one journey or screen; context brief, core principles, highest-risk
  states, and prioritized findings. Do not pretend to have release evidence.
- **Deep:** primary journey plus representative secondary routes; full principle
  scorecard, content/decision review, state matrix, and visual evidence review.
- **Release:** Deep plus a device/accessibility matrix, automated checks, real
  runtime screenshots, interruption/offline checks, and explicit open gates.
- **Forensic overlay:** Add to any mode when the project is AI-generated,
  template-heavy, or requested as an anti-slop review. Inventory routes,
  controls, data provenance, state transitions, and proof levels before rating
  visual polish.

## 1. Establish context and evidence

Write a short context brief before inspecting details:

- target user and situation;
- user goal and successful end state;
- primary route and affected secondary routes;
- risk level: ordinary, financial, privacy, safety, or irreversible;
- supported platforms and form factors;
- product/design constraints and explicit scope boundary;
- available runtime, screenshot, test, and provider evidence.

For Deep, Release, and Forensic work, inventory the relevant routes, entry
points, navigation destinations, actionable controls, data sources or fixtures,
shared primitives, and visible states. Sampling only the prettiest route is not
representative evidence.

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

Label the highest proof level actually reached: **source-declared**,
**rendered-static**, **interactive-local**, **data-connected**,
**failure-observed**, **device-observed**, or **production-observed**. Never
promote one level into another by inference.

## 2. Walk the journey

Map the primary flow and representative secondary routes. For each surface,
record route, state/input, user action, expected response, recovery path, and
evidence.

For important controls, verify reachability and outcome: where the control is
found, whether it responds, what state transition occurs, whether data changes,
and how failure or cancellation behaves. A visible button is not evidence of a
functional action.

Check the applicable states:

- first load, slow/partial load, refresh, and retry;
- empty, one item, typical content, and many items;
- long names/descriptions, missing media, unexpected values, and localization;
- keyboard/focus, disabled controls, validation, submission, cancellation,
  back navigation, and destructive actions;
- offline, permission, authentication, and provider failure;
- stale data, optimistic pending state, rollback, interruption, and resume when
  the product can encounter them.

For **Deep**, **Release**, and **Forensic** work, record coverage for every
in-scope route/state rather than reviewing only the default loaded screenshot.

### Mandatory feedback-state gate

For every primary journey and every important mutation, complete the feedback
audit before scoring visual polish. Do not accept “there is a spinner” or “the
test passes” as feedback coverage. Record the surface, trigger, user-visible
state, proof level, next action, and accessibility announcement for:

`idle → pressed/focused → pending → success | recoverable error → retry/undo/next`

Also check initial loading, background refresh, empty/no-results, offline/stale,
permission-denied, authentication expiry, cancellation, duplicate submission,
background/resume, and interruption when applicable. Choose the feedback
surface by consequence:

- skeleton or final-shape placeholder for an initial list when no usable content
  exists; keep the shell and existing content during refresh;
- local field validation for input correction;
- row/button-level pending treatment for a local mutation;
- toast or inline status for brief, non-blocking confirmation;
- durable banner or row for persistent network/system state, with recovery;
- progress surface for uploads or long operations;
- modal/Alert only for a blocking or destructive decision.

Read `references/mobile-feedback-audit.md` for the required matrix, static
inventory search, and runtime checkpoints. If a feedback state was not observed,
mark it **Unknown** rather than inferring it from source or a happy-path test.

## 3. Inspect mobile quality

Review findings under these headings:

- **UX principles:** explicitness, progressive disclosure, visibility of system
  status, mental-model fit, recognition over recall, user control and freedom,
  error prevention/recovery, consistency, flexibility, and minimalist signal-
  to-noise. Read the reference for the mobile-specific questions.

- **Hierarchy:** one-second focal point, primary action, scan order, and useful
  negative space.
- **Structure and data:** whether list, grouped list, timeline, chart, table,
  card, detail route, or sheet matches the user's information task; search,
  filter, sort, selection, stale data, and density behavior where applicable.
- **Composition:** product-specific visual language, meaningful card use, token
  fidelity, icon consistency, and reference parity.
- **Interaction:** platform-sized targets or compensating hit area (commonly
  44pt on iOS and 48dp on Android), pressed/focused/disabled feedback, keyboard
  avoidance, safe areas, sheets, gestures, and back behavior.
- **States and transitions:** stable loading footprint, actionable empty state,
  specific recoverable error, offline response, crowded content, semantic
  continuity, optimistic rollback, and interruption recovery.
- **Feedback surfaces:** whether inline feedback, toast, banner, sheet, modal,
  route, or progress surface matches the consequence and preserves context.
  Complete the mandatory feedback-state gate; explicitly flag missing skeletons,
  toasts/banners, local pending states, retry/undo paths, and announcements.
- **Accessibility:** role, label, state, uniqueness, Dynamic Type/large text,
  reduced motion, and decorative content hidden from assistive technology.
- **Localization:** translated copy, long strings, diacritics, right-to-left
  behavior when supported, and no clipped or fixed-width text.
- **Motion/native surfaces:** classify within-page, between-page, direct
  manipulation, or no-motion behavior. Audit purpose, subject continuity,
  finger-following progress, commit threshold, cancellation, recovery, gesture
  ownership, visible/accessibility alternatives, reduced motion, interruption,
  and runtime behavior. Use the motion audit reference and keep unobserved
  checkpoints **Unknown**.
- **Visual semantics:** meaningful color roles, dark-mode composition,
  typography hierarchy, icon optics, border/elevation purpose, and whether
  effects clarify grouping, affordance, depth, or brand.
- **Content and decisions:** terminology, information scent, consequence
  clarity, optional versus required actions, permission timing, and whether the
  copy helps users decide before they commit.
- **Trust and dark patterns:** cancellation, consent, destructive actions,
  urgency, defaults, hidden costs, and whether the interface pressures or
  misleads the user.
- **Functional reality:** dead or disconnected controls, static success states,
  hard-coded or fabricated data, placeholder content, duplicate routes,
  impossible state combinations, and polished surfaces unsupported by product
  behavior. Apply the forensic reference when relevant.

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

Do not use “AI slop” as a finding by itself. Translate it into an observable
failure, user impact, evidence, and verification method. Generic aesthetics
without user harm may be P3; a polished but nonfunctional core flow is P1.

## 4. Verify mobile conditions

Use the mode-appropriate matrix:

| Condition | Quick | Deep | Release |
| --- | --- | --- | --- |
| Narrow and large phone viewport | Target state | Required | Required |
| Large text / Dynamic Type | If text-heavy | Required when relevant | Required |
| Keyboard and focus | If input exists | Required when relevant | Required |
| VoiceOver/TalkBack or equivalent | Risk-based | Required for a11y findings | Required |
| Offline/interruption/resume | Risk-based | Required when relevant | Required |
| Real data and control outcome | If central to finding | Required for core flow | Required |
| Failure and rollback behavior | Risk-based | Required when applicable | Required |
| Motion/gesture checkpoints | Risk-based | Required when motion or gestures exist | Required when motion or gestures exist |
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

For every finding include tag, route/component, reproduction or screenshot
evidence, proof level, user impact, recommendation, confidence, and verification
method. Use tags such as **FLOW**, **CONTENT**, **STRUCTURE**,
**EXPLICITNESS**, **STATE**, **NATIVE**, **SYSTEM**, **FUNCTIONAL**,
**ACCESS**, **MOTION**, or **TRUST**. Do not claim a fix from source
inspection alone.

For remediation, route design findings to `design-uiux-mobile` and Expo
implementation findings to `frontend-mobile-engineering`. This audit names the
problem and the proof needed; it does not replace implementation or device
verification.

## 6. Report

Return:

1. **Context brief** — user, goal, risk, platforms, scope, and mode.
2. **Executive summary** — top risks and the most important journey outcome.
3. **Coverage matrix** — routes, states, devices, evidence, and unknowns.
   Include a dedicated feedback coverage matrix for loading, refresh, pending,
   success, error, offline/stale, permission, interruption, and recovery.
4. **Reality check** — highest proof level, control reachability, data source,
   and gaps between rendered, interactive, connected, and failure-tested states.
5. **Principle scorecard** — status and evidence for each relevant principle.
6. **Findings table** — priority, tag/principle, route/state, evidence, proof
   level, impact, recommendation, owner, confidence, and verification method.
7. **AI-slop risk summary** — include only for Forensic audits; summarize
   observed product-generic, functional, native, system, and trust failures.
8. **Recommendation sequence** — scope boundaries and principle trade-offs.
9. **Checks and observations** — exact commands, runtime states, devices, and
   screenshots actually observed.
10. **Open gates** — native-device, provider, production, store, or review work.

Use this finding shape:

| Priority | Tag/principle | Route/state | Evidence + proof level | Impact | Recommendation | Owner | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0–P3 |  |  |  |  |  |  | High/Medium/Low |

If rendering is unavailable, say visual QA is not observed and keep confidence
lower rather than treating tests or source code as visual proof.
