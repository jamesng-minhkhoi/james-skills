# Preferred React/Next stack

Use these preferences for new React work or when an existing project needs a
clear library decision. Existing repository conventions and user constraints
take precedence; do not migrate merely for preference. The default Next.js
shape is client-first and SPA-like; server features must earn their boundary.

## Default choices

| Need | Preferred default | Use when | Avoid |
| --- | --- | --- | --- |
| Web application framework | Next.js App Router with client-first SPA behavior | New React product routes, client navigation, code splitting, and explicit server/client boundaries | Rebuilding an existing stable framework without a concrete need |
| UI primitives | shadcn/ui | Accessible composable controls that should live in the repository and match project tokens | Copying a whole library blindly or overriding primitives per page |
| Light animation | Framer Motion | Enter/exit, layout continuity, gesture feedback, dialogs, menus, and short state transitions | Decorative animation everywhere or motion without reduced-motion behavior |
| Heavy animation | GSAP, optionally with the React integration | Timeline choreography, scroll-triggered storytelling, pinned sequences, or effects requiring GSAP's control model | Replacing simple transitions with GSAP or adding both animation systems by default |
| Server state | TanStack Query when needed | Client-side caching, deduplication, invalidation, mutations, polling, optimistic updates, or complex dependent queries | Duplicating server data in Zustand, or forcing server fetching when the SPA needs client ownership |
| React client state | Zustand | Cross-component client state, persisted preferences, transient workflow state, or complex local state shared across routes | Globalizing every input, duplicating server cache, or using a store for one-component state |
| Local ephemeral state | React state/hooks | Form draft, disclosure, focus, menu, hover, and component-local interaction | Creating a global store for state with one owner |

## State ownership rule

Keep each state in the smallest owner that can correctly coordinate it:

1. server truth stays in the server/data layer;
2. TanStack Query owns client-side server cache when query behavior is needed;
3. Zustand owns shared React client state, not authoritative server records;
4. component state owns local ephemeral interaction;
5. URL/search params own shareable navigation state such as filters, sort, and
   pagination.

When a mutation changes server truth, invalidate or reconcile the server cache,
then update any Zustand/UI state that only represents the interaction. Do not
let two stores silently become competing sources of truth.

## Architecture selection

The client-first SPA preference is strong for application-like routes, but it
is not a blanket rule. Choose per route and record the reason:

| Route constraint | Default shape | Verify |
| --- | --- | --- |
| Authenticated/product application shell | Client-first SPA-like route with client data ownership | cache ownership, loading/error states, bundle and interaction latency |
| Public, shareable, SEO/initial-content route | Static or server-rendered initial content with client islands | metadata/indexing, payload, hydration, and navigation behavior |
| Mixed route | Static/server shell plus client-owned interactive/data regions | boundary size, request waterfalls, auth, and cache behavior |
| No clear constraint or existing stable route | Preserve the current architecture | measure before migration |

Next App Router pages and layouts default to Server Components, while Next also
officially supports strict SPAs. Treat this as a deliberate boundary choice,
not a reason to add server actions to ordinary UI interactions.

## Next.js boundaries

Choose server and client components deliberately:

- default to a client-first route and SPA-style navigation for authenticated or
  application-like experiences;
- use client data fetching and TanStack Query when the route needs client cache,
  invalidation, polling, optimistic updates, or interactive synchronization;
- use server components or server actions only for secrets, authorization,
  server-only data, SEO/initial content, or a measured performance benefit;
- do not add `"use server"` to simple client interactions merely to appear more
  “Next.js-native”; use the existing API/server boundary when it is clearer;
- add `"use client"` at the interactive boundary that needs browser APIs, hooks,
  animation, or client state;
- do not pass secrets or privileged data into client props;
- preserve loading, error, and not-found boundaries at the route level;
- use API routes, server endpoints, or server actions according to the existing
  project contract, with server-side validation and authorization.

Measure before choosing server-first or client-first for a performance claim.
Inspect bundle size, request waterfalls, hydration cost, cache behavior, input
latency, and real navigation rather than assuming one rendering mode is always
faster.

## Common AI-generated Next.js mistakes

Flag these as engineering risks when observed:

- unnecessary `"use server"` directives or server actions for local UI state;
- server-fetching every route and passing large serialized props into a client
  tree, causing waterfalls or hydration complexity;
- duplicating the same records in server props, TanStack Query, and Zustand;
- using a client guard as authorization or exposing privileged data to support a
  server-first pattern;
- adding server/client boundaries without loading, error, pending, and retry
  behavior;
- claiming “better performance” without bundle, network, or runtime evidence.

## shadcn/ui rules

- inspect existing primitives before generating a new one;
- keep accessible names, keyboard behavior, focus management, and state props;
- customize tokens and variants centrally where possible;
- avoid page-local copies that drift from the shared primitive;
- do not treat shadcn/ui defaults as a substitute for task-specific hierarchy,
  content, empty/error states, or responsive behavior.

## Animation rules

Use Framer Motion first for product motion. Define trigger, purpose,
duration/easing, interruption, reduced-motion fallback, and proof. Use GSAP only
when a genuine timeline or scroll-trigger requirement justifies the additional
runtime and ownership model. Keep a route's animation ownership clear; do not
make Framer Motion and GSAP animate the same DOM subtree without an explicit
reason and lifecycle plan.

## Dependency decision record

Before adding one of these libraries, record:

- the concrete behavior it enables;
- why existing framework primitives are insufficient;
- bundle/runtime cost and tree-shaking impact;
- accessibility and reduced-motion behavior;
- test strategy and ownership;
- removal or fallback path if the feature is disabled.

## Official references

- [Next.js single-page applications](https://nextjs.org/docs/app/guides/single-page-applications)
- [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js use client directive](https://nextjs.org/docs/app/api-reference/directives/use-client)
