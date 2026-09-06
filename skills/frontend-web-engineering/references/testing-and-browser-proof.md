# Testing and browser proof

Choose evidence according to risk. Do not test only the default render.

## Test pyramid

- **Unit:** pure formatting, validation, reducers, parsers, permission
  decisions, and state transitions.
- **Component/integration:** rendered semantics, form submission, loading/
  error/empty states, mock boundaries, optimistic rollback, and permission
  behavior.
- **Browser/E2E:** real route entry, primary journey, direct URL, refresh,
  back/forward, keyboard/focus, responsive composition, and recovery.
- **Build/release:** lint, typecheck, production build, bundle checks, and
  repository-specific CI or deployment checks.

Prefer user-visible assertions over internal implementation details. Mock only
at a declared boundary and keep fixtures representative, including long,
empty, invalid, stale, and failure responses.

## Browser evidence matrix

| Dimension | Required evidence when relevant |
| --- | --- |
| Entry | Direct URL and normal navigation both work |
| State | Typical, loading, empty, no-results, long/dense, error, success |
| Action | Pointer, keyboard, touch/no-hover equivalent, pending, result |
| Recovery | Cancel, close, escape, retry, undo, refresh, back/forward |
| Accessibility | Name/role/state, focus order/return, visible focus, announcements |
| Responsive | Narrow mobile, intermediate/tablet, desktop, zoom/large text |
| Browser | Supported browser/OS, theme, localization, session/permission |
| Performance | Layout stability, input response, image/font loading, animation |

For instant-feeling navigation or caching work, also record cold and warm
route entry, the exact prefetch trigger, whether it was a cache hit, bytes and
requests spent before activation, transition duration, and behavior after
mutation, logout, account switch, permission change, offline, or stale data.
Measure a production build on a representative device/network when making a
performance claim; local development and a warm desktop tab are not sufficient.

If a cell is not observed, mark it Unknown. A screenshot cannot prove timing,
focus return, keyboard behavior, persistence, or recovery.

## Browser test rules

For each primary journey:

1. open the real entry URL;
2. record route, build, fixture, auth/permission state, browser/OS, viewport,
   theme, and input method;
3. trigger the action with the primary input and an equivalent accessible path;
4. observe pending, success, error, URL/history, focus, scroll, and motion;
5. reload and use back/forward where the product supports it;
6. repeat the highest-risk state at representative responsive widths.

Do not claim browser proof if the local server, browser, provider, or auth state
was unavailable. Report the blocker and retain lower confidence.

## Design fidelity checks

For a visual build or redesign, record the design read, preserve/overhaul
scope, reference observations, and a small set of accepted visual rules. If
there is no handoff, derive these from the brief and existing surface. Do not
silently substitute a default hero, palette, library, or animation preset.

Capture the existing route before a redesign when available. Preserve content,
URLs, anchors, CTA destinations, forms, analytics, and accessible behavior
unless changes are in scope. Reuse the installed stack, tokens, icons, and
primitives; verify dependencies and current official documentation before
introducing a library. An aesthetic reference alone does not justify migration.

Implement actual product previews with real screenshots or components. Keep
illustrative fixtures visibly distinguishable from production evidence where
viewers could confuse them. Do not invent customer logos, quotes, metrics, or
results to complete a layout. Missing assets remain explicit dependencies.

Run the route and compare with the reference or accepted design at matching
viewports and states. Inspect hierarchy, type wrapping and glyph clipping,
spacing, image crop, role-based tokens, navigation, and CTA reachability.
Record measurements versus estimates; do not claim pixel accuracy from visual
guesswork. Recheck material mismatches after correction.

Use the browser matrix for responsive, zoom, keyboard, touch, loading, and
failure coverage relevant to the change. Keep essential content accessible
when motion is reduced or an effect is unavailable; verify sticky/scroll
effects do not trap focus or obscure actions. Preserve supported themes;
additional themes or motion are not prerequisites for visual quality.

Prefer a focused browser assertion for meaningful behavior or overflow where
useful. Do not write tests that ban font names, count decorative labels, or
mirror CSS values merely to certify taste. A screenshot can support fidelity;
working actions and performance need their own observations. Report remaining
design deviations and runtime gaps separately from passing build checks.

## Failure diagnosis

When a check fails, distinguish:

- product defect;
- test defect or brittle selector;
- environment/provider/configuration failure;
- unrelated pre-existing failure.

Record the command, exit status, relevant output, scope, and whether the failure
blocks the requested acceptance criteria.
