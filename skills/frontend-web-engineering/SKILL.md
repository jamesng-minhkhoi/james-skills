---
name: frontend-web-engineering
description: Plan, implement, test, and verify production-ready frontend web application changes across routes, components, data fetching, forms, state, authentication boundaries, accessibility, responsive behavior, performance, and browser workflows. Prefer client-first SPA-style React/Next.js architecture with shadcn/ui, Framer Motion, TanStack when needed, and Zustand where appropriate. Use for React, Next.js, Vue, Svelte, and comparable web repositories when building features, fixing bugs, refactoring frontend architecture, or hardening a UI for release. Preserve existing contracts and do not claim completion without proportionate automated and runtime evidence.
---

# Frontend Web Engineering

Ship reliable web application behavior, not just a visually plausible screen.
Use this skill for product web features and fixes. Use `design-uiux-web` when the
main problem is interface design, and `audit-uiux-web` when the main problem is
review or diagnosis.

Load [the engineering workflow](references/engineering-workflow.md) for
architecture, implementation, and change planning. Load [testing and browser
proof](references/testing-and-browser-proof.md) for validation strategy. Load
[web accessibility and performance](references/web-accessibility-performance.md)
for release-sensitive quality work. Load [data, auth, and security
boundaries](references/data-auth-security.md) when the change crosses APIs,
sessions, permissions, storage, or user-controlled content.
Load [the preferred React/Next stack](references/preferred-react-next-stack.md)
when starting a new React web feature or choosing between client libraries.
Load [perceived performance](references/perceived-performance.md) when the
request involves speed, instant-feeling navigation, prefetching, caching,
service workers, resource priorities, or a “make it feel faster” critique.

## Non-negotiable order

Inspect → Model the contract → Plan the smallest change → Implement → Test →
Run the real route → Review the diff → Report evidence

Do not begin by rewriting a route, adding a dependency, inventing fixtures, or
replacing an existing primitive before understanding the repository's patterns.

## Preferred React/Next stack

For new React web work, prefer Next.js with a client-first, SPA-style App Router
experience, shadcn/ui for accessible composable primitives, Framer Motion for
light purposeful animation, TanStack libraries when client-side server-state
behavior needs them, and Zustand for React client state. Use GSAP only as a
secondary choice for heavy, timeline-based or scroll-triggered choreography
that Framer Motion does not fit.

Do not add `"use server"`, server actions, or server-component boundaries by
habit. Treat them as deliberate exceptions for secrets, authorization, server-
only data, SEO/initial-content requirements, or a measured performance need.
Keep the SPA fast through route-level code splitting, client caching, stable
loading states, and measured bundle/network behavior—not through an automatic
server-first architecture.

When optimizing perceived speed, keep a stable shell and update only the
changing route region; prefetch the next likely route or query only when its
intent, privacy, freshness, and cost are understood. Make hover, focus, touch,
viewport, and explicit-action triggers equivalent where relevant. Use the
same cache the destination reads, invalidate it after mutations and identity
changes, and measure hit rate, wasted bytes, transition duration, and Core Web
Vitals. Never turn “instant” into a justification for prefetching or
prerendering everything.

These are defaults, not permission to migrate an existing project. Preserve an
existing stack when it is working; introduce a preferred library only when it
solves a concrete problem and its dependency, bundle, accessibility, and
maintenance costs are justified.

## 1. Frame the engineering task

Write a short change brief:

- user goal and affected journey;
- current behavior, desired behavior, and acceptance criteria;
- affected routes, components, data sources, permissions, analytics, and
  provider boundaries;
- states: loading, empty, typical, long/dense, pending, success, error, retry,
  offline or stale when relevant;
- constraints: framework, browser support, localization, accessibility, visual
  system, performance budget, and backward compatibility;
- out of scope, migration risk, and the evidence needed to call it complete.

Classify the change as one or more of: presentation, interaction, route,
state, data contract, auth/permission, performance, accessibility, or build/
tooling. This prevents a visual request from silently changing business logic
or a data fix from being treated as a component-only change.

## 2. Inspect before editing

Start with read-only checks:

- `git status --short` and current branch; preserve unrelated dirty work;
- repository instructions such as `AGENTS.md`, package scripts, lockfile,
  framework configuration, environment requirements, and deployment commands;
- route/layout tree, shared primitives, tokens, data access, auth/permission
  checks, error boundaries, loading boundaries, and closest shipped feature;
- existing tests, fixtures, visual harnesses, analytics events, and API types;
- actual user-facing strings and realistic data shapes, including nullable,
  long, translated, and permission-limited values.

If a `.codegraph/` directory exists, use CodeGraph before broad text search to
trace relevant symbols and call paths. Use `rg` for focused text/file search
after the repository shape is known.

Separate evidence from inference:

- source proves implementation intent, not runtime reachability;
- a test proves only its covered behavior and environment;
- a local route does not prove deployed provider, auth, database, or browser
  behavior;
- a screenshot does not prove focus, timing, keyboard behavior, persistence, or
  recovery.

## 3. Model the contract and states

Before implementation, write the smallest useful contract:

| Boundary | Input | Output/state | Failure/recovery | Owner |
| --- | --- | --- | --- | --- |
| Route/component/API/store |  |  |  |  |

For every high-value interaction, model:

`idle → focused/edited → pending → success | recoverable error`

Add selected, disabled, empty, no-results, stale, permission-denied,
interrupted, resumed, rollback, and unsaved-change states when the product can
encounter them. Include URL/query/filter/sort/pagination and browser back/
refresh behavior when applicable.

Keep server/client boundaries explicit. Do not expose secrets, privileged
operations, service-role credentials, or trust decisions to client code. Do not
use a client-only guard as proof of authorization. Preserve the existing API,
database, analytics, localization, and permission contracts unless a contract
change is explicitly in scope.

## 4. Plan the smallest safe change

Create a file-level plan before editing:

1. shared primitive or data contract to reuse;
2. route/component/state changes;
3. loading, empty, error, accessibility, responsive, and recovery behavior;
4. focused tests and browser proof;
5. risks, migrations, feature flags, and rollback path.

Prefer a narrow vertical slice over a broad cleanup. Do not mix unrelated
formatting, dependency upgrades, generated files, or design-system rewrites.
If the requested behavior needs a backend, schema, provider, or auth change,
state that boundary and its verification gate rather than faking the result.

## 5. Implement production behavior

Follow the repository's framework and state-management conventions. During
implementation:

- keep route composition, data fetching, writes, and components understandable;
- use semantic HTML and existing design primitives before inventing variants;
- keep forms labeled, validated, keyboard-usable, duplicate-submit-safe, and
  recoverable;
- make loading stable, errors specific and actionable, and empty states useful;
- preserve URL state, browser history, focus, scroll, and unsaved work where
  the user expects continuity;
- use real or clearly labelled fixtures; never fabricate success, metrics,
  permissions, provider results, or production readiness;
- handle cancellation, retry, optimistic updates, rollback, stale data, and
  concurrent actions when relevant;
- respect localization, long content, reduced motion, responsive re-composition,
  and the existing visual system;
- keep route transitions stable and economical: preserve the shared shell,
  reserve media geometry, avoid request waterfalls, and use intent-aware
  prefetching only when the cache, privacy, invalidation, and bandwidth policy
  are explicit;
- add dependencies only when the repository pattern and benefit justify them.

When an interaction is asynchronous, make the transition observable and
idempotent where possible: disable or guard duplicate submission, preserve the
user's input, show pending state, reconcile the result, and provide recovery.

## 6. Validate in layers

Run the narrowest checks first, then expand based on risk:

- formatter/linter on changed files;
- unit tests for pure logic and state transitions;
- component/integration tests for forms, routes, permissions, and data states;
- browser tests for the primary journey, direct URL, refresh, back/forward,
  keyboard/focus, responsive layout, and failure recovery;
- typecheck, production build, and repository-required checks;
- accessibility and performance checks appropriate to the route and change.

Test both implementation and behavior. A passing build is not proof that a
button works, a modal returns focus, a provider is deployed, or a layout is
usable at intermediate widths.

## 7. Review the result before handoff

Review the diff for:

- accidental scope expansion or unrelated file changes;
- duplicated logic, missing error paths, stale dependencies, and dead code;
- authorization and user-controlled content boundaries;
- missing state coverage, misleading copy, or fabricated data;
- responsive overflow, keyboard/focus failures, layout shift, and visual drift;
- wasted prefetches, duplicate server-state caches, stale identity-sensitive
  data, service-worker cache hazards, and performance claims without field or
  production-build evidence;
- tests that assert implementation details instead of user-visible outcomes.

Run the real route in a supported browser when the change affects UI. Record
exact route, build, fixture, auth state, browser/OS, viewport, input method,
theme, interaction, and observed result. If the browser or provider was not
available, mark that evidence Unknown.

## 8. Completion contract

Only call the task complete when:

- acceptance criteria and relevant states are implemented;
- changed behavior is covered by proportionate automated checks;
- the primary route and important failure/recovery paths were observed when
  runtime access was available;
- typecheck/build/repository checks pass or failures are explicitly reported;
- the diff is scoped and unrelated user changes are preserved;
- unobserved native-browser, provider, production, analytics, or deployment
  gates are listed separately.

Report:

1. implemented behavior and files changed;
2. contracts preserved or intentionally changed;
3. checks run and their results;
4. browser/runtime states actually observed;
5. known limitations, unknown gates, and recommended follow-up.

Do not claim “fully verified” from source inspection, lint, typecheck, tests,
or one desktop screenshot alone.
