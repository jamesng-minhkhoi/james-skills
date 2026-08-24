---
name: design-uiux-web
description: Design polished, usable responsive web UI/UX for SaaS products, settings, forms, workflows, navigation, search, detail views, and interactive components. Use when creating product-web flows, screen composition, content hierarchy, responsive rules, component/state specifications, prototypes, or design handoffs—not marketing landing pages or data-heavy dashboards. Do not implement product code or release checks.
---

# Craft Web UI

Design the web product journey first and the pixels second. This is a UI/UX
design skill, not an implementation, architecture, or release-verification
skill. Use it for interfaces where a visitor must complete a task, understand
system state, manage content, or make a decision inside a browser. Produce
flows, wireframes, visual systems, component/state specifications, responsive
rules, prototypes, and handoff notes. Do not edit product code, APIs, stores,
permissions, analytics, or deployment configuration.
Use [audit-uiux-web](../audit-uiux-web/SKILL.md) for independent diagnosis
afterward, and `frontend-web-engineering` for implementation.

Load [the web UI craft process](references/web-ui-craft-process.md) for a new
screen, route, workflow, or redesign. Load [web UI principles](references/web-ui-principles.md)
when making hierarchy, disclosure, content, interaction, accessibility, or
visual-language decisions. Load [the web pattern matrix](references/web-ui-pattern-matrix.md)
for navigation, forms, overlays, lists, search, and responsive behavior. Load
[the web UI critique and proof checklist](references/web-ui-critique-and-proof.md)
when reviewing rendered work or writing the handoff.

## Non-negotiable order

Intent → Evidence → Task Flow → Content/Data → Explicitness → Structure →
System → Interaction → Responsive → Accessibility/Performance → Proof

Do not begin with a component library, gradient, animation, or isolated
component polish while the user's task, information hierarchy, or state
coverage is unclear.

## 1. Frame the task

Write the target user, situation, entry point, intent, successful outcome,
primary action, secondary actions, irreversible actions, and failure cost.
Identify whether the surface is a route, detail view, form, editor, list,
search result, settings area, overlay, or reusable component.

Inspect the current route, closest shipped surface, design tokens, primitives,
content source, analytics, permissions, and provider contracts. Separate
evidence, hypothesis, and decision. Preserve business logic and data contracts
for UI-only work; surface required contract changes separately.

## 2. Map the complete browser flow

Include:

- entry, first decision, primary action, result, and next step;
- browser back, refresh, deep link, direct URL, and return-from-detail behavior;
- save, cancel, undo, retry, no-results, empty, permission, and recovery paths;
- loading, slow, partial, stale, offline, provider-error, and interrupted states;
- unsaved changes, duplicate submission, session expiry, and destructive action
  confirmation where relevant.

Do not validate only the route reached by manually typing an internal URL.

## 3. Let content and data shape the UI

Inventory realistic labels, descriptions, statuses, dates, counts, media,
nullable fields, errors, permissions, translated strings, and maximum practical
density before choosing containers.

Choose list, grouped list, detail, table, editor, split view, tabs, sheet,
dialog, or inline expansion from the user's task. For dense data or charts,
use the dashboard skill instead. Do not force every surface into cards or a
generic hero-plus-grid layout.

## 4. Apply explicitness and progressive disclosure

Place every action, explanation, and state on a spectrum:

Visible → Directly revealed → Contextual → Deferred → Advanced/hidden

Keep primary actions, current status, cost, permission effects, and
irreversible consequences visible. Reveal secondary actions through labels,
menus, tooltips, hover, keyboard focus, selection mode, or contextual surfaces
only when the trigger is discoverable and the user can recover context.

Never make a core action hover-only, keyboard-inaccessible, or dependent on an
unlabeled icon. Use progressive disclosure to reduce overload, not to hide
important information.

## 5. Compose hierarchy and rhythm

- Make the current location, main content, primary action, and next step clear.
- Use grids, whitespace, grouping, alignment, scale, and contrast before effects.
- Give each section or component a job and a meaningful relationship to others.
- Use cards only for distinct objects, decisions, or actionable groups.
- Avoid card soup, icon soup, repeated generic layouts, and equal emphasis for
  unrelated actions.
- Create rhythm through purposeful variation and restraint, not random novelty.
- Use human, domain-specific labels instead of internal or generated jargon.

## 6. Build the web system

Reuse or define tokens for typography, spacing, content width, color roles,
surfaces, borders, radii, elevation, icons, motion, and focus. Use semantic
HTML and the existing framework conventions. Design light/dark themes as
compositions, not hex inversions. Use semantic color roles and ramps for
neutral surfaces, functional accents, and status meanings; do not treat a
fixed 60-30-10 ratio as a product-UI requirement. If the stack supports it,
use perceptually uniform palette generation such as OKLCH, then verify actual
contrast and meaning in light and dark themes.

Use professional, consistent icons and meaningful signifiers. Check hover,
focus-visible, pressed, selected, disabled, visited, loading, success, error,
and permission states. Motion should clarify a change, preserve continuity,
show progress, or guide attention; remove decorative motion that delays work.
Every meaningful interaction needs a deliberate timing, easing, reduced-motion
alternative, and keyboard/touch equivalent where applicable.

## 7. Design the full interaction surface

For each important component, define:

- state map and transition cause;
- pointer, keyboard, touch, and screen-reader path;
- focus order and focus return after menus, dialogs, and route changes;
- validation timing, constraints, pending treatment, success, error, retry,
  rollback, and duplicate-submit behavior;
- user control: back, cancel, close, undo, escape, and unsaved-change recovery;
- URL, query, filter, sort, pagination, and browser-history behavior where
  applicable.

Maintain a state matrix for high-value controls and flows:

| Element/flow | User intent | Trigger | Visible feedback | Result | Recovery/alternative |
| --- | --- | --- | --- | --- | --- |
|  |  | pointer/keyboard/touch/route | pending/status/focus | success or error | undo/retry/cancel/accessible path |

Do not stop at the default state or a polished hover prototype. Include
focus-visible, loading, delayed feedback, success, failure, empty, stale,
permission, interruption, and resume behavior when the product can encounter
them. Tooltips, hover reveals, skeletons, toasts, and animations are part of
the interaction contract and must be tested without relying on pointer hover.

If the product genuinely includes AI, design AI-specific patterns only where
they serve the job: input and attachment preview, mode/context controls,
history or memory management, inline editing, progress transparency, and
uncertainty/confidence cues. Never add an AI prompt box, glass effect, or
confidence label merely because it is fashionable.

Use tooltips and contextual help for unfamiliar icons or dense controls, but
do not make essential meaning available only on hover.

## 8. Design responsive behavior as re-composition

Check narrow mobile, large mobile, intermediate/tablet, and desktop widths.
Reflow order, content density, navigation, media, columns, and disclosure when
the task requires it. Do not simply shrink a desktop interface into a phone.

Test long labels, translation, zoom, large text, missing media, slow loading,
keyboard open, pointer and touch input, horizontal overflow, sticky regions,
and fixed-height traps. Preserve orientation and task progress as the viewport
changes.

## 9. Prepare the design handoff

Use existing route, content, design-system, accessibility, and platform
constraints as design inputs. Document route assumptions, data states, content
fixtures, URL/history expectations, permission-dependent variants, analytics
questions, and unresolved provider behavior. Use real or clearly labelled
fixtures; never fabricate success, metrics, or data to make a design look
complete.

Do not change route code, data fetching, writes, permissions, analytics, or
provider configuration. Hand implementation to `frontend-web-engineering`.

## 10. Prove the design

Follow:

Plan → Model → Wireframe → Compose → Prototype → Critique → Handoff

Render or prototype the primary journey and representative non-happy states.
Walk the state matrix at representative widths and input methods. Review
keyboard/focus intent, screen-reader naming, responsive re-composition,
loading/error/recovery states, reduced motion, semantic color, contrast,
content fit, and interaction timing as design requirements. Do not claim the
implemented behavior works; record those engineering verification gates for
the handoff.

Report the design artifact, routes/states covered, content fixtures, viewport
and input matrix, design decisions, unresolved questions, and engineering
gates not observed. Do not call product UI complete because a static design or
one desktop prototype looks polished.
