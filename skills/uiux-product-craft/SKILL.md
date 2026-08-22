---
name: uiux-product-craft
description: Research, design, implement, and verify product UI/UX across mobile and web applications. Use when auditing a user journey, redesigning a screen or component, resolving interaction or accessibility issues, translating visual references into runtime UI, or performing screenshot-based visual QA. Preserve existing business logic and data contracts when the request is UI/UX-only.
---

# UI/UX Product Craft

Treat UI/UX work as an evidence-backed product workflow. Improve the user's
journey and the interface together; do not stop at a token, color, or spacing
refresh.

## Operating principles

- Research the current product before changing it. Read the repository's
  design guidance, route/screen composition, tokens, shared primitives, real
  states, and existing visual references.
- Establish the boundary before editing. For UI/UX-only work, preserve data
  models, API behavior, persistence, permissions, analytics, navigation
  destinations, localization meaning, and feature contracts unless the user
  explicitly expands scope.
- Prefer the existing design system. Reuse the shipped primitive or component
  when it can express the change; add a new component only when the current
  system cannot.
- Make the hierarchy legible. Each screen needs a focal point and a primary
  action that a stranger can name quickly. Remove decorative elements that have
  no compositional or explanatory job.
- Design the state machine, not only the loaded happy path. Consider loading,
  empty, error, offline, disabled, submitting, success, crowded, and long-copy
  states where they apply.
- Treat accessibility, localization, and motion as part of the design. Every
  control needs an accessible role and useful label; interactive targets should
  be at least 44pt or have compensating hit area; motion must explain change and
  respect reduced-motion preferences.
- Keep evidence honest. Passing tests or seeing source code is not visual
  acceptance. If a screen was not rendered on a simulator, device, browser, or
  comparable visual harness, report that gate as open.

## Workflow

Follow this loop and record the result in the final handoff:

`Plan → Build → Run → Screenshot → Critique → Refine → Verify`

### 1. Frame the request

Identify the user, job, journey, entry point, desired outcome, affected routes,
and constraints. Mark each requirement as one of:

- **Direct** — explicitly requested or required by the product contract.
- **Supported** — strongly implied by existing behavior or platform norms.
- **Suggested** — a design improvement that needs agreement when consequential.
- **Deferred** — valuable but outside this pass.
- **Hidden** — intentionally not exposed because it would confuse or violate a
  constraint.

For consequential UX choices, present concrete directions with trade-offs
before implementing. Use the user's selection; do not silently replace it with
an earlier recommendation.

### 2. Build an evidence map

Inspect, in this order when available:

1. Project instructions and authoritative product/design documents.
2. The target route and screen composition, including loading and error paths.
3. Shared tokens, layout shells, controls, sheets/modals, typography, icons,
   and feedback primitives.
4. Existing screenshots, Figma references, seeded content, and the closest
   shipped screen.
5. Tests, lint/typecheck/build scripts, visual harnesses, and known regressions.

Separate facts from assumptions. A component or file proves implementation
exists; it does not prove that the runtime route is reachable, the provider
schema is deployed, or the user-facing behavior works.

When a request says “consistent with” another surface, render or reuse the
actual component and behavior rather than producing a lookalike.

### 3. Audit the journey and states

Map the primary journey and representative secondary routes. For each surface,
capture the state, user action, system response, recovery path, and evidence
needed. Use [the audit template](references/audit-template.md).

At minimum, check:

- first load, refresh, slow load, partial load, and retry;
- zero, one, typical, and many items;
- long names, translated copy, missing media, and unexpected data;
- keyboard/focus, permissions, disabled controls, validation, and submission;
- offline or provider failure where the product can encounter it;
- destructive actions, cancellation, back navigation, and interrupted flows.

Classify findings as P0–P3: P0 blocks use or causes serious harm; P1 breaks a
core journey; P2 meaningfully degrades clarity, access, or polish; P3 is a
minor refinement. Include route/component, evidence, impact, and reproduction.

### 4. Design the composition

Choose the smallest composition that makes the job obvious:

- establish one focal point using meaningful scale, weight, color, depth, or
  space;
- give the primary action clear visual priority and a visible pressed state;
- use cards only for genuinely distinct objects or separately actionable
  groups; do not wrap every row in a card;
- use a designed empty state with a next action, a shaped loading state that
  matches the final footprint, and a specific recoverable error;
- keep destructive actions separated from common actions;
- choose bottom sheets, inline feedback, or dedicated pages based on the
  decision's complexity and reversibility;
- avoid fixed-pixel assumptions that fail at smaller widths, larger text, or
  longer locales.

Do not accept a generic “icon + title + subtitle + rounded card” solution when
the product needs a stronger focal point, content hierarchy, or interaction
model.

### 5. Build safely

Use the repository's tokens and primitives for typography, spacing, radius,
icons, buttons, inputs, sheets, and feedback. Keep modules cohesive and split
large screens by meaningful visual subcomponents.

Preserve the existing business and data layer for UI/UX-only requests. Do not
silently change queries, schemas, writes, permissions, analytics, or route
destinations to make a visual change easier. If a UX problem genuinely
requires a contract change, stop and surface it separately.

Implement interaction states in place: pressed, focused, disabled, loading,
success, and error as applicable. Keep keyboard avoidance, safe areas, focus,
and sheet dismissal behavior explicit.

For motion, animate the subject of the change, keep user-initiated feedback
snappy, avoid decorative loops, and check reduced motion. Watch for native
surfaces such as blur, masks, and glass flattening or mispositioning under
animated transforms.

### 6. Run and render

Run the narrowest relevant automated checks first, then the project's standard
lint, typecheck, tests, i18n checks, and build when practical. Inspect failures
instead of treating an unrelated dirty-tree failure as proof the task is bad.

Render the primary route and representative secondary states in the real
runtime or the closest available visual harness. Capture before/after or
reference comparisons when a visual target exists. If rendering is unavailable,
keep the implementation scope conservative and explicitly leave visual QA
pending.

### 7. Critique and refine

Use the one-second test: after looking briefly, name the focal point and primary
action. Then use [the visual-QA checklist](references/visual-qa-checklist.md)
to inspect composition, fidelity, interaction, motion, states, edge cases, and
accessibility. Fix P0/P1 issues first, then refine P2/P3 issues that materially
affect comprehension or quality.

Repeat the render-and-critique loop after meaningful changes. A green test suite
does not replace this pass.

### 8. Verify and hand off

Report four separate evidence groups:

1. **Implementation** — files and behavior changed.
2. **Automated** — exact commands run and results.
3. **Visual/runtime** — routes, states, viewport/device, and screenshots
   actually observed.
4. **Open gates** — native-device, provider, production, dashboard, store, or
   review checks that were not observed.

Record the remaining risks and the next smallest verification step. Never say
“complete” when a required visual or external gate was not observed.

## References

- [Audit template](references/audit-template.md) — route/state matrix, findings,
  and decision records.
- [Visual QA checklist](references/visual-qa-checklist.md) — composition,
  interaction, accessibility, localization, motion, and edge-state review.
