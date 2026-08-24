---
name: audit-uiux-web
description: Audit responsive web UI/UX with evidence-backed review of task flows, browser behavior, explicitness, progressive disclosure, information architecture, responsive composition, accessibility, visual systems, motion, performance, trust, and functional reality. Use for React, Next.js, Vue, Svelte, static, SaaS, dashboard, settings, form, list, table, detail, and web-app interfaces, especially AI-generated, template-heavy, or polished-but-unproven projects. Do not implement fixes unless requested.
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

Do not edit product code unless the user explicitly asks for implementation.

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

Separate evidence from assumption:

- source proves intended or implemented behavior, not runtime reachability;
- tests prove tested behavior, not visual quality or complete browser behavior;
- a screenshot proves one rendered state for one route, fixture, viewport, and
  build;
- provider, production, analytics, and browser compatibility claims need their
  own evidence.

Label the highest proof level actually reached: **source-declared**,
**rendered-static**, **interactive-local**, **data-connected**,
**failure-observed**, or **production-observed**. Never promote one level into
another by inference.

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
- **Interaction completeness:** Are hover, focus-visible, pressed, selected,
  disabled, pending, success, error, tooltip, menu, dialog, form validation,
  and keyboard paths coherent?
- **Responsive composition:** Does the interface re-compose rather than merely
  shrink across narrow mobile, large mobile, tablet/intermediate, desktop, and
  zoom/large-text conditions?
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
   level, impact, recommendation, confidence, and verification.
7. **Forensic summary** — only for the forensic overlay; summarize observed
   generic, functional, responsive, native-web, system, and trust failures.
8. **Recommendation sequence** — first fixes, dependencies, scope boundaries,
   and trade-offs.
9. **Checks and observations** — exact commands, browsers, viewports, states,
   screenshots/recordings, and tests actually observed.
10. **Open gates** — provider, production, analytics, browser, performance, or
    accessibility work not observed.

Use this finding shape:

| Priority | Tag/principle | Route/state | Evidence + proof level | Impact | Recommendation | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 |  |  |  |  |  | High/Medium/Low |

Never call the audit complete because lint, typecheck, tests, or one desktop
screenshot passes. A visual or motion gate not observed remains **Unknown**.
