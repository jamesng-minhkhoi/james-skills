# AI-generated UI forensic pass

Use this overlay for AI-generated, vibe-coded, template-heavy, or suspected
AI-slop mobile projects. Do not penalize a product for using AI. Flag observable
failures and their user impact, not aesthetic dislike or assumed provenance.

## Contents

- [Forensic sequence](#forensic-sequence)
- [Proof ladder](#proof-ladder)
- [Failure families](#failure-families)
- [Adversarial checks](#adversarial-checks)
- [Reporting](#reporting)

## Forensic sequence

1. **Inventory reality:** list relevant routes, entry points, navigation
   destinations, actionable controls, data sources or fixtures, shared
   primitives, and visible states.
2. **Trace the core job:** start from a realistic entry and complete the primary
   task without manually jumping to internal routes.
3. **Build a control ledger:** for each visible control, record expected action,
   observed response, resulting state/data change, and failure/cancel path.
4. **Trace data provenance:** distinguish real provider/database data,
   deterministic fixtures, hard-coded examples, placeholders, and fabricated
   values. Do not assume realistic-looking content is real.
5. **Exercise transitions:** observe pending, success, validation, provider
   failure, retry, rollback, offline, interruption, and resume where applicable.
6. **Stress native conditions:** keyboard, safe areas, back behavior, small and
   large phones, large text, dark mode, permissions, and touch alternatives.
7. **Inspect system drift:** look for one-off components, arbitrary tokens,
   duplicate routes, inconsistent terminology, repeated layouts, and visual
   states unsupported by product logic.

## Proof ladder

Use the highest level directly observed:

| Level | What it proves | What it does not prove |
| --- | --- | --- |
| Source-declared | Code or docs intend a behavior | Route reachability, rendering, or successful interaction |
| Rendered-static | A state appeared for one build/data/viewport | Control behavior or real data connection |
| Interactive-local | A control responded in the local runtime | Durable data change or provider behavior |
| Data-connected | A real read/write was observed | Failure recovery, native device, or production behavior |
| Failure-observed | A real or controlled failure and recovery were observed | Every provider or production failure |
| Device-observed | Behavior was observed on a named native device/build | Production schema, provider, or store state |
| Production-observed | Named production behavior was directly observed | Unobserved routes, users, devices, or future reliability |

Never infer upward. A screenshot can prove visual appearance only for the state
shown. A mocked success path does not prove a write occurred.

## Failure families

### Product-generic

- The screen could belong to any app after changing the logo and color.
- Information architecture follows a generic dashboard or card template rather
  than the user's job.
- CTAs use vague language such as “Continue,” “Explore,” or “Get started” when
  the outcome can be named.
- Placeholder copy, fake testimonials, invented metrics, or implausible records
  are presented as product truth.
- Every route repeats the same hero, card grid, icon-title-description block, or
  oversized empty space regardless of task.

### Functional

- Visible controls are dead, navigate nowhere, or change only local appearance.
- The primary flow is reachable only by manually opening an internal route.
- Loading, success, error, or empty states are static demonstrations rather
  than outcomes of real transitions.
- The UI reports success without a durable data change, or data changes without
  visible pending/success/error feedback.
- Only the happy path exists; back, cancel, retry, offline, validation,
  interruption, and duplicate submission are missing.
- Optimistic updates have no rollback, retry, conflict, or stale-data behavior.

### Structural

- Cards, charts, tables, or sheets are chosen for appearance rather than the
  user's comparison or decision.
- Decorative charts have no units, honest scale, labels, range, or accessible
  summary.
- Dense desktop data is compressed, truncated, or fragmented into arbitrary
  cards without search, filter, sort, selection, or detail access.
- Navigation contains duplicate destinations, orphan routes, inconsistent
  back behavior, or unrelated actions at equal visual weight.

### Native and accessible

- Web sidebars, hover interactions, tiny popovers, pointer-sized targets, and
  desktop spacing are transplanted to mobile.
- The keyboard covers input or actions; safe areas, system bars, and back
  behavior are ignored.
- Core actions depend on swipe, long press, color, motion, or an unlabeled icon
  without an equivalent alternative.
- Large text, screen-reader names/states, reduced motion, localization, and
  narrow devices expose missing hierarchy or clipped content.

### System and visual semantics

- Tokens are consistent but hierarchy, behavior, terminology, or component
  meaning is not.
- Gradients, glass, glow, shadows, borders, and animations have no grouping,
  affordance, depth, state, or brand purpose.
- Component variants proliferate with arbitrary radius, spacing, color, icon,
  or motion values.
- Dark mode is a color inversion that loses contrast, elevation, or semantic
  status meaning.
- Motion decorates replacement screens instead of explaining cause,
  continuity, progress, or result.
- Swipe or drag behavior has no visible progress, understandable commitment,
  cancellation, recovery, or accessible alternative.
- A custom gesture silently competes with scrolling, a sheet, a slider, or the
  system-edge back gesture.
- Reduced motion removes status, focus, cause, or result feedback instead of
  only reducing travel and decorative effects.
- A polished animation implies success while the underlying data change is
  static, mocked, delayed, or failed.

### Trust and risk

- Generated copy makes unsupported health, financial, privacy, security, or
  performance claims.
- Recommendations, confidence indicators, progress, or system status imply
  certainty unsupported by the product state.
- Consent, paid behavior, destructive actions, or data sharing are hidden by
  optimistic copy, weak alternatives, or fabricated urgency.
- Failure is disguised with playful copy, disappearing feedback, or a fake
  success state.

## Adversarial checks

- Replace realistic records with nulls, long values, duplicate values, and
  unexpected statuses.
- Slow or fail the central read/write and observe whether pending and recovery
  remain understandable.
- Tap every visible action in the core flow and record no-op, wrong-route, and
  visual-only responses.
- Navigate using only visible entry points and platform back behavior.
- Background and resume during input, upload, processing, and confirmation.
- Exercise motion at rest, during a slow drag, at the threshold, after a quick
  flick, after reversal/cancellation, and during scroll or system-gesture
  conflict.
- Increase text size, open the keyboard, use the smallest supported phone, and
  switch theme where supported.
- Compare repeated screens for copy, component, token, and interaction drift.
- Check whether displayed metrics, recommendations, or status have a traceable
  data source or are clearly labelled examples.

## Reporting

Do not write “looks AI-generated” as a finding. Use:

| Field | Required content |
| --- | --- |
| Tag | FLOW, CONTENT, STRUCTURE, EXPLICITNESS, STATE, NATIVE, SYSTEM, FUNCTIONAL, ACCESS, or TRUST |
| Observation | Specific visible or behavioral failure |
| Evidence | Route/state/control/data plus proof level |
| Impact | What the user cannot understand, decide, complete, trust, or recover from |
| Recommendation | Smallest useful product or UI change |
| Verification | Exact state, interaction, data, device, or provider evidence needed |

Summarize the forensic result by failure family. Keep untested behavior
**Unknown**; absence of evidence is not evidence that a feature is broken.
