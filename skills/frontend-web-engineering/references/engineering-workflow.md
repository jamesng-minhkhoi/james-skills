# Engineering workflow

Use this reference when a frontend change crosses more than one route,
component, state, or data boundary.

## Repository reconnaissance

Inspect in this order:

1. repository instructions and current dirty state;
2. package scripts, lockfile, framework/runtime, and build configuration;
3. route/layout tree and server/client boundaries; identify whether the project
   is client-first SPA-style or server-first;
4. shared primitives, tokens, error/loading boundaries, and conventions;
5. data access, API types, auth/permissions, analytics, and fixtures;
6. tests and existing browser/visual harnesses;
7. closest shipped surface and adjacent flows.

Prefer the project's established abstraction. A new hook, store, component,
fetching library, or validation package needs a concrete problem and a clear
maintenance benefit.

For the user's preferred Next.js approach, begin with a client-first SPA-style
route for application experiences. Treat `"use server"`, server actions, and
server-component boundaries as exceptions that need a concrete security,
server-only data, SEO/initial-content, or measured performance reason. Do not
confuse a server boundary with authorization or assume it is faster without
measuring waterfalls, hydration, bundle, cache, and input behavior.

## Change brief

Use:

> When [situation], [user] needs to [job] so they can [outcome].

Then record acceptance criteria as observable outcomes, not implementation
tasks. Include the primary success path and the highest-cost failure path.

## Contract map

For each changed boundary, document:

| Layer | Questions |
| --- | --- |
| Route | Does direct URL, refresh, back/forward, query, and permission behavior remain correct? |
| Component | What inputs, states, semantics, and callbacks are stable? |
| Data | What is nullable, stale, pending, paginated, or user-controlled? |
| Auth | Where is authorization enforced and what is safe to expose to the client? |
| Analytics | Which events or payloads must remain compatible? |
| Provider | Which behavior needs deployed schema, service, environment, or dashboard proof? |

## State-first implementation

Build the state machine before polishing the default state:

`idle → active → pending → success | error → retry/cancel/undo`

Add only states the product can really encounter, but do not omit a failure or
recovery state merely because the happy path is visually easier. Stable loading
footprints and preserved user input reduce layout shift and loss of work.

## Performance intent map

When the change is described as “instant,” “fast,” or “smooth,” write down the
likely next intent before choosing an optimization:

| Intent | Candidate | Required guardrail |
| --- | --- | --- |
| Next route is highly predictable | route prefetch or client transition | privacy, freshness, hit/waste measurement |
| Next data is known after an interaction | TanStack cache prefetch | query key, cancellation, invalidation |
| Repeat visits must work offline | service worker | versioning, logout/account-switch, recovery |
| Public document navigation is nearly certain | speculation/prerender hint | browser support, bandwidth, side-effect audit |
| Current screen is visually unstable | geometry/loading correction | LCP/INP/CLS evidence, keyboard/touch proof |

Do not add all candidates at once. Choose the smallest mechanism, establish a
baseline, and verify that the optimization improves both perceived and actual
performance without creating stale data, privacy leaks, duplicate requests, or
new maintenance ownership.

## Scope discipline

Keep unrelated user changes untouched. Avoid opportunistic formatting, broad
renames, dependency upgrades, and generated-file churn. If a refactor is
required for correctness, explain why, isolate it, and validate its consumers.

## Handoff evidence

Separate:

- implemented in the working tree;
- committed on the branch;
- automated checks passed;
- local browser behavior observed;
- real data/provider behavior observed;
- production/deployment behavior observed.

These are different claims and should not be collapsed into one completion
statement.
