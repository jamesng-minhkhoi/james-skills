---
name: audit-uiux-web
description: Audit responsive web UI/UX with evidence-backed review of task flows, browser behavior, explicitness, progressive disclosure, information architecture, option-set coverage, native phone composition, accessibility, visual systems, motion, performance, trust, and functional reality. Use for React, Next.js, Vue, Svelte, static, SaaS, dashboard, settings, form, list, table, detail, and web-app interfaces, especially AI-generated, template-heavy, or polished-but-unproven projects. Do not implement fixes unless requested. Hand accepted fixes to frontend-web-engineering.
---

# Audit UIUX Web

Produce an evidence-backed web UI/UX audit before recommending changes. Judge the
observed product and user outcome, not the framework or tool that produced it.
Do not call a page “AI slop” as a finding; translate the observation into a
specific usability, visual, functional, accessibility, or trust failure.

Load [Web UX principles](references/web-ux-principles.md) for the review
standard. For Deep, Release, or data-heavy audits, load the [web quality
matrix](references/web-quality-matrix.md). For AI-generated, template-heavy, or
vibe-coded work, add the [web UI forensics](references/web-ui-forensics.md)
pass. For any rendered or visual review, use the [web visual proof
checklist](references/web-visual-proof.md).
For landing pages, portfolios, redesigns, or a supplied visual reference, load
[design direction and fidelity](references/design-direction-and-fidelity.md).
When changing this audit skill, use the [web audit regression cases](evals/ai-uiux-web-audit-regression.md).

Do not edit product code unless the user explicitly asks for implementation.

Two gates are easy to miss because everything around them looks clean: the
phone composition must be judged against native platform patterns (§4.1), and
every selectable option set must be compared to the domain's natural options
(§4.2). Both are required in Deep and Release audits.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

## 0. Select the audit mode

Choose the smallest mode that matches the request. If no mode is specified, use
**Deep** for a new, high-risk, or multi-route audit and **Quick** for a narrow
review.

- **Quick:** one route or journey; context brief, core principles, highest-risk
  states, and prioritized findings. Do not imply full responsive or release
  coverage.
- **Deep:** primary journey plus representative routes; full principle
  scorecard, content/structure review, state matrix, responsive matrix, and
  rendered proof where available.
- **Release:** Deep plus supported-browser/device matrix, accessibility checks,
  performance checks, direct URL/refresh/back/session checks, failure and
  recovery evidence, and explicit open gates.
- **Forensic overlay:** Add to any mode for AI-generated, template-heavy,
  suspiciously generic, or polished-but-nonfunctional UI. Inventory generic
  patterns, dead controls, fabricated data, state gaps, visual drift, and
  browser reality before rating polish.

### 0.1 Select audit directionality

Do not default blindly to only top-down or only bottom-up. Choose the direction based on the task trigger:

| Trigger / Task Scope | Primary Direction | Execution Order | Why |
|---|---|---|---|
| **Screen Redesign / New Screen / Structural Critique** | **Top-Down** | 1. Macro-Layout & Chrome Budget<br>2. IA & Hierarchy<br>3. Component & State Reality | Prevents the "AI slop polishing trap" where fragmented 3-row headers or stacked control sandwiches pass because individual buttons look polished. |
| **User Layout Smell / "Feels Clunky" / Cognitive Friction** | **Top-Down** | 1. Viewport Chrome & Gestalt Proximity<br>2. Density & Focal Point<br>3. Component Details | User friction is almost always macro (wasted space, dead rows, misplaced toggles). Auditing tokens first wastes time polishing controls that should be deleted or merged. |
| **Component Library / Design System Migration** | **Bottom-Up** | 1. Atomic Primitives & Tokens (tap target, contrast, radius)<br>2. State Matrix (hover, active, focus-ring)<br>3. Screen Composition Spot-Checks | Changes to `<Button>`, `<Select>`, or spacing tokens affect dozens of screens; atomic correctness must be verified first. |
| **Automated Pre-Commit / Regression Guards** | **Bottom-Up** | 1. AST / Code Checks (`no-inline-dropdowns`, 16px font)<br>2. Unit & Integration Tests<br>3. Snapshot Regressions | Fast, deterministic invariant checks run locally on every commit without full screen walkthroughs. |
| **Accessibility (WCAG 2.2 AA) Audit** | **Bottom-Up** | 1. Contrast Ratios & Target Geometry<br>2. Semantic Tags & ARIA Roles<br>3. Keyboard & Focus Order | A11y failures are fundamentally atomic (4.5:1 contrast, 44px bounds, label associations) before they become flow issues. |
| **Isolated Bug Fix / Edge Case** | **Bottom-Up** | 1. Local State, Form Validation, or Error Rollback<br>2. Immediate Container Boundary<br>3. Screen Context | Surgical fix for an edge case (e.g. NaN currency format, optimistic rollback desync) without destabilizing page structure. |
| **Comprehensive Feature Review (Deep / Release)** | **Sandwich (Bidirectional)** | 1. Top-Down: Macro Chrome Budget & Journey<br>2. Bottom-Up: Token, State, & A11y Verification<br>3. Convergence: Reconcile macro fit with edge cases | Guarantees both structural clarity (no chrome waste) and runtime robustness (no unhandled states). |

## 1. Establish context and evidence

Write a context brief before judging details:

- target user, situation, and job to be done;
- entry point, successful outcome, primary action, and failure cost;
- primary route and representative secondary routes;
- risk: ordinary, financial, privacy, safety, or irreversible;
- supported browsers, viewport ranges, input methods, locales, and themes;
- explicit scope boundary and available source, runtime, data, test, and
  screenshot evidence.

Inspect route configuration, layouts, shared primitives, tokens, content/data
fixtures, permissions, analytics where relevant, and closest shipped surface.
For Deep or Release, inventory routes, entry points, navigation destinations,
forms, tables, filters, overlays, dialogs, menus, and important states rather
than sampling only the prettiest page.

### 1.1 Data scale and control appetite

Two context items decide later gates and are the easiest to silently assume:
**data scale** (sparse and bounded, or large and growing) and **control
appetite** (glance-only consumption, or an operator who picks periods, tunes
filters, and drills in). When neither is stated and a judgment depends on it,
ask before concluding; if asking is impossible, record the assumption in the
report itself and lower confidence on the findings that rest on it. An
option-set or disclosure verdict issued without either is an audit defect.
The full rule and the gates that depend on the two items are in
[web-ux-principles.md](references/web-ux-principles.md), "Context: data scale
and control appetite".

Separate evidence from assumption:

- source proves intended or implemented behavior, not runtime reachability;
- tests prove tested behavior, not visual quality or complete browser behavior;
- a screenshot proves one rendered state for one route, fixture, viewport, and
  build;
- provider, production, analytics, and browser compatibility claims need their
  own evidence.

Label the highest rung actually reached on the shared ladder: **declared**,
**rendered**, **interactive**, **connected**, **failure-tested**, **device**,
**production**. A web audit normally stops at `connected` or `failure-tested`.
Never promote one rung into another by inference.

## 2. Map and walk the browser journey

For the primary flow and representative secondary routes, record:

`route → state/input → user action → expected response → outcome → recovery`

Check browser-specific behavior:

- direct URL, deep link, refresh, browser back/forward, new tab, and shared URL;
- query parameters, filters, sorting, pagination, scroll position, and history;
- authentication, session expiry, permission changes, and tenant/workspace
  boundaries;
- entry, first decision, primary action, result, next step, cancel, undo,
  retry, close, and destructive-action recovery;
- loading, slow/partial network, stale data, timeout, provider error, offline
  behavior if supported, and interrupted/resumed work;
- unsaved changes, duplicate submission, optimistic updates, rollback, and
  multi-tab or concurrent-edit behavior when relevant.

A visible control is not evidence of a working action. Verify reachability,
trigger, visible feedback, data or route change, failure behavior, and recovery.

## 3. Review web UX quality

Use the principles reference and rate each relevant area **Strong**, **Concern**,
**Critical**, **Unknown**, or **Not applicable**:

- **Outcome and flow:** Can the user complete the job and understand what
  happens next?
- **Explicitness:** Are primary actions, cost, status, consequences, and
  recovery visible? Are secondary actions progressively disclosed with a
  discoverable trigger?
- **Information architecture:** Do navigation, labels, route names, URLs,
  headings, breadcrumbs, tabs, search, filters, and back behavior preserve
  orientation and recognition over recall?
- **Hierarchy and scanability:** Is there one clear focal point, scan order,
  primary action, content density, grouping, and useful negative space?
- **Structure and data:** Does the task use the right list, table, grouped list,
  detail, editor, split view, dialog, sheet, or inline reveal? Do real and long
  values fit? Are empty, no-results, dense, and error states useful?
- **Option-set coverage:** Enumerate every user-selectable option set — time
  ranges, filters, sorts, page sizes, quantities, limits — and derive the
  domain's natural options from the user's job before judging. A set that
  misses natural options, has arbitrary endpoints, or exists only because the
  data model made it easy is a finding, not a default to accept. When an
  explicit design contract names the options, report the comparison as
  contract-conforming; a missing-natural-options finding applies only when
  the contract is silent or the offered set violates the contract.
- **Interaction completeness:** Are hover, focus-visible, pressed, selected,
  disabled, pending, success, error, tooltip, menu, dialog, form validation,
  and keyboard paths coherent?
- **Responsive composition:** Does the interface re-compose rather than merely
  shrink across narrow mobile, large mobile, tablet/intermediate, desktop, and
  zoom/large-text conditions?
- **Phone-native composition:** When the interface renders a phone viewport,
  is that composition judged against native platform conventions (iOS/Android
  patterns for navigation, grouped lists, segmented controls, sheets, safe
  areas, touch behavior) rather than only against the desktop page restacked?
- **Accessibility:** Are landmarks, headings, labels, names, roles, states,
  focus order, focus return, contrast, zoom, keyboard access, reduced motion,
  and non-color meaning adequate?
- **Visual system:** Are typography, semantic color, surfaces, icons, borders,
  radius, elevation, and visual restraint coherent? Are there too many colors,
  cards, gradients, shadows, or decorative effects?
- **Motion:** Does motion explain reveal, continuity, progress, hierarchy, or
  feedback? When requested, does it exist in meaningful state changes rather
  than only hover or page-load polish? Is reduced motion supported?
- **Performance:** Check image/font loading, layout shift, long tasks, input
  response, expensive effects, animation performance, and content stability.
- **Content and trust:** Does copy help decisions? Are terms, costs, defaults,
  consent, destructive actions, cancellation, urgency, and recovery honest?
- **Functional reality:** Identify dead links, disconnected controls, fake
  success, fabricated metrics, placeholder data, impossible combinations,
  duplicate routes, and behavior that only exists in static markup.

When principles conflict, state the trade-off: minimalism versus discoverability,
progressive disclosure versus transparency, brand differentiation versus
convention, or efficiency versus accessibility.

## 4. Inspect responsive and interaction conditions

Use the mode-appropriate matrix:

| Condition | Quick | Deep | Release |
| --- | --- | --- | --- |
| Narrow mobile and large mobile | Target state | Required | Required |
| Tablet/intermediate breakpoint | If layout changes | Required | Required |
| Desktop primary viewport | Required | Required | Required |
| 200% zoom or large text | If text-heavy | Required when relevant | Required |
| Keyboard traversal and focus return | If interactive | Required | Required |
| Touch and no-hover equivalent | If mobile-supported | Required when relevant | Required |
| Phone composition vs native platform patterns | If phone-supported | Required | Required |
| Selectable option sets vs domain-natural options | Risk-based | Required | Required |
| Loading, empty, dense, error, success | Risk-based | Required for core flow | Required |
| Direct URL, refresh, back/forward | Risk-based | Required for core routes | Required |
| Slow/failed/offline/interrupted | Risk-based | Required when supported | Required when relevant |
| Reduced motion and contrast | Risk-based | Required when relevant | Required |
| Supported browsers and themes | Target browser | Representative set | Full support set |

At minimum, capture representative widths around 390, 768, 1024, and 1440 CSS
pixels or the project's equivalent breakpoints. Add 320/375, 1280, 200% zoom,
dark mode, RTL, or localization where supported. Record the exact browser/OS,
viewport, DPR if relevant, fixture, theme, input method, and build.

If rendering or interaction is unavailable, mark visual/runtime findings
**Unknown** and lower confidence. Do not turn source inspection into visual
proof.

### 4.1 Phone composition must be judged against native patterns

A phone viewport is not a smaller web page. When the surface renders a phone
composition, load the `mobile-native` skill and any native-pattern
documentation the repository carries (for example `docs/uiux.md`) before
rating this area, then compare the composition against native platform
conventions: navigation and large-title treatment, inset grouped lists with
small section headers, segmented controls at intrinsic width, sheets, safe
areas, sticky regions, chevron affordances, 44-point targets, and scroll
behavior. A phone composition that re-stacks desktop content into full-width
bordered cards with floating full-width control tracks is a finding even when
every element re-composes "correctly". This is a coverage requirement in Deep
and Release, not a taste call. When a supplied design contract explicitly
specifies the phone composition, classify deviations from the native-pattern
comparison as design-contract deviations with consequences (or report them
contract-conforming) — never as an unconditioned native-pattern finding. If
the `mobile-native` skill and repository documentation are both unavailable,
proceed from native platform conventions alone and mark the gate `NOT_RUN`
with the platform-convention comparison still performed; do not silently skip
the gate or pass it without comparison.

### 4.2 Selectable option sets must be compared to the domain

Enumerate every user-selectable option set — time ranges, filters, sorts,
page sizes, limits — as a required Deep/Release row, then compare it to the
domain's natural options derived from the user's job and vocabulary (for a
food business: yesterday, this week, this month, last month, month-to-date).
Record a finding for every set that fails the comparison, unless an explicit
design contract names the options — then the comparison is
contract-conforming and only silence in the contract, or a violation of it,
is a finding. The full rules — including the custom-range requirement on a
data-heavy, control-seeking surface (§1.1), and the context-unconfirmed rule
when context was never established — are in
[web-ux-principles.md](references/web-ux-principles.md), "Option-set and
domain coverage".

## 5. Run the AI-generated UI forensic pass when relevant

Look for observable patterns, not provenance:

- colorful template palette that competes with meaning;
- card soup, repeated rounded containers, dashboard/KPI decoration, or generic
  hero-plus-grid structure that does not fit the task;
- gradients, blur, shadows, icons, avatars, or motion without a comprehension
  or interaction job;
- inconsistent tokens, typography, spacing, status meanings, or route chrome;
- hover-only actions, unlabeled icons, inaccessible menus, missing focus, or
  desktop layouts that collapse instead of re-composing;
- polished static states with dead controls, fake metrics, generic copy, no
  loading/error/recovery path, or impossible data combinations;
- copied interaction patterns that conflict with browser conventions or the
  user's domain mental model.

For each pattern, name the observable behavior, route/state, user impact,
proof level, confidence, and exact verification. Generic aesthetics without
user harm may be P3; a polished but broken core journey is P1.

Treat style patterns as prompts to investigate, not automatic failures. Record
the intended direction and compare against it. A font, color, repeated grid,
text-only hero, or absent dark theme is not a defect by itself. Separate
usability defects, deviations from an explicit design contract, and optional
style opportunities; optional preferences do not block completion.

## 6. Prioritize findings

- **P0:** blocks use, causes serious accessibility failure, or risks harm.
- **P1:** breaks a core journey or makes the primary task unreliable.
- **P2:** materially harms clarity, access, consistency, performance, trust, or
  responsive behavior.
- **P3:** minor refinement with limited user impact.

Use tags such as **FLOW**, **CONTENT**, **IA**, **EXPLICITNESS**, **STRUCTURE**,
**STATE**, **RESPONSIVE**, **BROWSER**, **FUNCTIONAL**, **ACCESS**, **SYSTEM**,
**MOTION**, **PERFORMANCE**, or **TRUST**.

Every finding must include route/component, state and reproduction, evidence and
proof level, user impact, recommendation, confidence, and verification method.
Do not claim a fix from source inspection alone.

For remediation, route design findings to `design-uiux` and implementation findings to
`frontend-web-engineering`. This audit names the problem and the proof needed;
it does not replace implementation or browser verification.

## 7. Report

Return:

1. **Context brief** — user, goal, risk, browser/platform scope, and mode.
2. **Executive summary** — top risks and primary journey outcome.
3. **Coverage matrix** — routes, states, viewports, browsers, evidence, and
   unknowns.
4. **Reality check** — highest proof level, control reachability, data source,
   and gaps between static, interactive, connected, and failure-tested states.
5. **Principle scorecard** — status and evidence for each relevant principle.
6. **Findings table** — priority, tag/principle, route/state, evidence, proof
   level, impact, recommendation, owner, confidence, and verification.
7. **Forensic summary** — only for the forensic overlay; summarize observed
   generic, functional, responsive, native-web, system, and trust failures.
8. **Recommendation sequence** — first fixes, dependencies, scope boundaries,
   and trade-offs.
9. **Checks and observations** — exact commands, browsers, viewports, states,
   screenshots/recordings, and tests actually observed.
10. **Open gates** — provider, production, analytics, browser, performance, or
    accessibility work not observed.

Give every finding a stable ID, `F-web-<n>` (for example `F-web-03`), and put it
in the first cell as `P1 · F-web-03`. The builder closes by ID; a re-audit
reopens or adds, and never renumbers.

Use this finding shape:

| Priority | Tag/principle | Route/state | Evidence + proof level | Impact | Recommendation | Owner | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0–P3 |  |  |  |  |  |  | High/Medium/Low |

Never call the audit complete because lint, typecheck, tests, or one desktop
screenshot passes. A visual or motion gate not observed remains **Unknown**.

A finding is open until the builder returns [a fix report](../_shared/fix-report.md)
with that ID and evidence at or above the rung it demanded. Re-audit by ID:
close, reopen, or add. Never renumber.

