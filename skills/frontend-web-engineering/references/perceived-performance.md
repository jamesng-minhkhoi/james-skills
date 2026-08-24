# Perceived performance and fast-feeling SPAs

Use this reference when a route should feel immediate, especially after a
video, design review, or product request says “make it fast.” The goal is not
to maximize background requests. The goal is to make the next likely action
ready at a bounded cost while preserving correctness, accessibility, and real
performance.

The McMaster-Carr/NextFaster discussion that motivated this guidance combines
server-rendered HTML, hover intent, CDN and service-worker caching, selective
resource loading, stable image geometry, and a persistent shell. In a
client-first Next.js application, translate that idea into soft navigation,
intent-aware route/data prefetching, selective code loading, and explicit
measurement. See the [Wes Bos transcript](https://www.linkedin.com/posts/wesbos_how-is-this-website-so-fast-a-tweet-about-activity-7253071128129089536-ZO3F)
and the [video that prompted this update](https://www.youtube.com/watch?v=fWfIf7Vfjec)
for context.

## The fast-feeling loop

Design the interaction as:

`stable shell → likely intent → bounded prefetch → client navigation → replace only the changing region → reconcile fresh data`

Apply it as follows:

- Keep navigation, headers, filters, and other shared shell elements stable
  while the route content changes. Preserve URL state, focus, scroll, and
  pending feedback deliberately.
- Prefer real client navigation over a full-document reload for application
  flows. In Next.js, use `Link` or the router according to the repository's
  conventions; do not build a second router or manually swap HTML.
- Give loading states a stable footprint. Reserve image space with dimensions
  or `aspect-ratio`; use skeletons or progress indicators that do not cause
  the page to jump; do not hide a slow request behind a permanently blank
  shell.
- Treat perceived speed and actual speed as separate acceptance criteria. A
  fast transition that shows stale, unauthorized, or incorrect data is a bug,
  not a performance win.

## Intent-aware prefetching

Prefetch only work that is both safe and plausibly useful. Choose a trigger
based on confidence:

| Trigger | Good use | Guardrail |
| --- | --- | --- |
| Viewport visibility | Small, public, high-probability next routes | Disable or reduce for large lists and low-bandwidth contexts |
| Pointer hover | Desktop links/cards where hover precedes activation | Add a short debounce; provide focus and touch equivalents |
| Keyboard focus | Menus and predictable next steps | Never make hover the only trigger |
| Touch intent | `pointerdown` or an explicit high-confidence action | Do not trigger expensive work for every scroll/touch |
| Explicit user action | Wizard next step, opened menu, selected item | Best default for private, large, or mutation-dependent data |

For each prefetch, define:

1. the route/data cache key and freshness window;
2. whether the request is public, user-specific, or permission-sensitive;
3. a cancellation/skip policy for slow networks, data saver, large payloads,
   inactive tabs, or low-confidence intent;
4. invalidation behavior after a mutation, logout, permission change, or
   context change;
5. metrics for prefetch hit rate, wasted requests/bytes, cache age, and the
   navigation time with and without a hit.

Next's `Link` may prefetch routes as they enter the viewport, and supports
`prefetch={false}` or a hover-only pattern for expensive links. Use those
controls deliberately rather than assuming every visible link deserves a
request. For server state, use TanStack Query's prefetch/query APIs so the
prefetch populates the same cache the destination reads; do not create a
second ad-hoc cache in a component or Zustand.

## Cache and delivery discipline

Use the smallest cache that solves the observed problem:

- browser/HTTP cache for versioned static assets and responses whose freshness
  and privacy policy are explicit;
- CDN caching for public, cacheable content and immutable assets;
- TanStack Query for client-owned server-state freshness, deduplication,
  invalidation, retries, and optimistic reconciliation;
- a service worker only when offline behavior, repeat-visit performance, or a
  PWA requirement justifies its lifecycle and invalidation complexity;
- Zustand for client workflow/preferences, never as a duplicate authoritative
  server cache.

Never publicly cache user-specific, permission-sensitive, or mutation-bearing
responses without an explicit security and invalidation design. A service
worker must have a versioned cache policy, logout/account-switch behavior,
update strategy, and a recovery path for stale or broken cached assets.

## Resource and JavaScript priorities

- Split code by route and interaction. Dynamically load heavy editors, charts,
  maps, rich previews, and rarely used dialogs; keep global providers and
  client-only dependencies small.
- Preload only resources required for the current above-the-fold experience.
  Use `preconnect` only for origins the route truly needs. Do not preload all
  fonts, images, or future routes.
- Give images explicit geometry and responsive sizes. Lazy-load below-fold
  media, prioritize the actual hero/LCP asset, and verify that the chosen
  format and dimensions match the rendered surface.
- Avoid request waterfalls: parallelize independent work, prefetch a known
  next query at the intent boundary, and avoid fetching the same record in
  route props, TanStack Query, and Zustand.
- Keep CSS and the initial shell small and stable. Use the framework's build
  pipeline before inventing manual critical-CSS extraction; measure whether a
  change improves LCP/INP/CLS in a production build.

## Speculation Rules and prerendering

Treat the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
as optional progressive enhancement, not a default SPA mechanism. It has
limited browser availability and is aimed primarily at document navigations.
`prefetch` downloads a document response; `prerender` also loads subresources,
runs JavaScript, and consumes substantially more memory and bandwidth. Only
consider it for a very high-confidence, same-origin navigation after measuring
cost, privacy, analytics, mutation, and activation behavior. Never prerender
logout, destructive, personalized, or mutation-triggering URLs.

## Proof required for a performance claim

Capture a production build under representative cold and warm conditions,
including a throttled network/device when relevant:

- LCP, INP, CLS, TTFB, long tasks, and route transition duration;
- initial JS/CSS/image/font bytes and the largest route dependencies;
- request waterfall before and after prefetch/cache changes;
- prefetch hit rate, wasted bytes, cache freshness, and invalidation behavior;
- loading footprint, image geometry, focus, keyboard, touch, and reduced-motion
  behavior during the transition;
- error, offline/stale, logout/account-switch, and permission-change behavior.

Report lab and field/RUM evidence separately. “It feels instant,” a Lighthouse
score, or a warm local navigation alone is not proof that the shipped route is
fast, correct, or economical.

## AI-slop traps to reject

- prefetching every route, every visible card, or every hover without a hit/
  waste budget;
- adding a service worker because “caching makes it faster” without an update
  and invalidation plan;
- prerendering personalized pages or pages with side effects;
- preloading every asset and increasing contention for the current route;
- replacing a stable loading state with a blank screen or an endless spinner;
- moving work to server actions or server components solely because they sound
  more performant, without a measured reason and a clear data boundary;
- claiming performance from a screenshot, local dev mode, or a single desktop
  run.
