---
name: frontend-mobile-engineering
description: Implement, debug, test, and verify production-ready Expo React Native mobile application changes across navigation, screens, state, data fetching, authentication, native capabilities, permissions, offline behavior, performance, builds, and device workflows. Use only for mobile engineering; do not use it to make UI/UX design decisions or audit visual quality. Prefer Expo and preserve the repository's existing architecture.
---

# Frontend Mobile Engineering

Ship reliable Expo React Native behavior, not just a screen that looks correct
in a static preview. This skill owns implementation, data/state boundaries,
native integration, automated checks, device verification, and engineering
handoff. Use `design-uiux-mobile` for visual and interaction design; use
`audit-uiux-mobile` for independent UI/UX diagnosis; use the store-submission
skill for App Store or Google Play readiness.

## Non-negotiable order

`Inspect → Model contracts → Plan smallest change → Implement → Test → Run on a real mobile target → Build/check release boundary → Report evidence`

Do not begin by restructuring an existing Expo app, adding a native library,
rewriting navigation, or copying a web implementation. First understand the
project's SDK, native mode, route structure, data contracts, and verification
surface.

Load [Expo architecture](references/expo-architecture.md) for project shape,
SDK/native boundaries, dependencies, and Expo Router. Load
[data, state, and native boundaries](references/data-state-and-native-boundaries.md)
for networking, auth, storage, environment variables, lifecycle, and offline
behavior. Load [testing and device proof](references/testing-device-proof.md)
for automated tests, development builds, device matrices, performance, and
release evidence.
When companion Expo skills are available, load the overview first and then the
leaf skill for the boundary being changed (for example Router, data fetching,
animation, native UI, or EAS). Pin all advice to the project's exact SDK. When
changing this skill, use the [engineering regression cases](evals/expo-engineering-regression.md).

## 1. Frame the engineering change

Write a short change brief:

- user outcome and affected mobile journey;
- exact screens/routes, platform capabilities, data sources, and contracts;
- current behavior, desired behavior, acceptance criteria, and failure cost;
- states: loading, empty, pending, success, error, retry, stale, offline,
  permission-denied, backgrounded, resumed, and interrupted when relevant;
- iOS/Android differences, supported SDK/OS range, device constraints, and
  accessibility requirements from the approved design;
- out of scope: visual redesign, API/schema changes, store metadata, or native
  work not required by the change;
- evidence needed to call the change complete.

Treat approved UI/UX artifacts as implementation input. If the design is
ambiguous or conflicts with platform behavior, record the question and resolve
the smallest engineering constraint; do not silently redesign the product.

## 2. Inspect before editing

Run read-only checks first:

- `git status --short`, current branch, and repository instructions;
- `package.json`, lockfile, Expo SDK version, scripts, `app.json` or
  `app.config.{js,ts}`, `eas.json`, `tsconfig.json`, Metro/Babel config, and
  environment conventions;
- whether committed `ios/` or `android/` directories exist; classify the
  project as managed/CNG, prebuild, or bare and preserve that choice;
- route/layout tree, existing navigation, providers, screens, components,
  hooks, services, stores, API clients, auth/session code, and closest shipped
  feature;
- native modules, config plugins, permissions, URL schemes, push/deep-link
  configuration, and platform-specific files;
- unit, component, integration, E2E, build, and device harnesses.
- `npx expo-doctor` output after SDK, dependency, or app-config changes.

Detect the exact Expo SDK before version-specific advice. Use the matching Expo
documentation version; do not apply `latest` examples to an older project.
Use `npx expo install <package>` for Expo-compatible dependencies. Existing
repository conventions take precedence over a new template.

## 3. Model contracts and ownership

Map the change before implementation:

| Boundary | Input | Output/state | Failure/recovery | Owner |
| --- | --- | --- | --- | --- |
| Route/screen |  |  |  |  |
| API/query |  |  |  |  |
| Mutation |  |  |  |  |
| Native capability |  |  |  |  |
| Store/session |  |  |  |  |

Keep state in the smallest correct owner:

1. server truth remains in the API/database boundary;
2. TanStack Query, if present or justified, owns server-state cache,
   freshness, retries, invalidation, and optimistic reconciliation;
3. Zustand or the repository's existing store owns shared client workflow and
   preferences, not duplicate authoritative records;
4. React state owns component-local interaction and form drafts;
5. navigation params own shareable route state where the router supports it.

For every asynchronous action model:

`idle → active → pending → success | recoverable error → retry/cancel/undo`

Add cancellation, duplicate-submit protection, request races, stale results,
rollback, app backgrounding, token expiry, permission changes, and process
restart when the product can encounter them. Never treat a client-side guard as
authorization; enforce permission at the server boundary too.

## 4. Implement within Expo boundaries

### Project structure and routing

- Prefer Expo Router for new Expo navigation when the project does not already
  have a different stable router. Keep route files route-focused; place
  reusable components, screen bodies, hooks, services, utilities, and tests in
  their established sibling areas.
- Do not restructure an existing app to match a new template. For new apps,
  `src/app` may contain routes while `src/screens`, `src/components`,
  `src/hooks`, `src/services`, and `src/utils` hold non-route code.
- Use kebab-case filenames and path aliases when the repository supports them.
  After adding routes in a typed Expo Router project, regenerate the router
  types before typechecking.
- Preserve deep links, back behavior, tabs/stacks/modals, route params, state
  restoration, and notification links. Do not use direct external
  `@react-navigation/*` imports in SDK versions where Expo Router forbids them;
  follow the SDK-pinned router guidance.

### Native capabilities

- Prefer Expo modules and supported config plugins. Check the SDK-compatible
  install path before adding a package.
- A native dependency or native configuration change requires a new
  development build; a JavaScript reload cannot prove native behavior.
- Keep secrets out of JavaScript and app config that ships to clients. Use
  platform-secure storage for tokens and document sign-out/account-switch
  cleanup.
- Define permission request timing, denial, restricted state, retry, and
  settings recovery. Test both first request and previously denied states.
- For push notifications, model per-device/account registration, token
  rotation, offline retry, logout/account-switch deregistration, and first-run,
  denied, background, and opened-from-notification states.
- Keep platform differences explicit with `Platform.select` or platform files;
  shared behavior must not be weakened to hide an iOS/Android mismatch.

### OTA and build compatibility

- If `expo-updates` or EAS Update is present, inspect `runtimeVersion`, update
  URL, channel/branch, build profile, rollout, rollback, and code-signing
  configuration.
- Native code, native dependencies, config plugins, permissions, or SDK changes
  require a new compatible build before an update can be trusted. A JavaScript
  update must be tested against the exact runtime it targets.
- Verify a preview-channel update and rollback path before calling production
  delivery safe. Record the build ID, runtime, channel, update ID, and observed
  behavior as separate evidence.

### Implementation quality

- Reuse existing primitives and contracts; do not create a parallel data or
  navigation architecture for one screen.
- Keep effects cancellable and idempotent. Clean up listeners, timers,
  subscriptions, animations, and pending requests on unmount or scope change.
- Use semantic accessibility labels, roles, hints, and state from the approved
  design; do not substitute a visual screenshot for accessible behavior.
- Keep real fixtures and error responses representative. Never fake a native
  permission grant, network success, push delivery, or backend result.

### Responsiveness and loading conventions

Choose the smallest loading and computation scope that preserves continuity:

| Situation | Required behavior |
| --- | --- |
| Initial screen with no safe content to show | A screen-level skeleton or loading boundary may block the screen; match the final geometry. |
| Existing navigation shell or screen refresh | Keep stable navigation and usable content mounted; replace only the changing region. |
| Initial list/grid fetch | Use row/card skeletons with final-shape geometry; avoid a generic full-screen spinner. |
| Background refresh or stale cache | Keep stale content visible with a local refresh indicator and clear freshness status. |
| Field validation, autocomplete, or search/filter query | Show pending/error at the field or control; debounce query input and cancel stale requests. |
| Row/card mutation | Keep unrelated content interactive; mark only the affected row/action pending and reconcile or roll back locally. |
| Auth, account, permission, or route-wide context switch | A screen-wide boundary is acceptable when old content must be cleared to prevent leakage or an invalid action. |

Use a short, measured debounce for high-frequency query input (often about
250–400 ms for search/typeahead), cancel or ignore obsolete requests, and never
debounce an explicit submit, destructive action, or button press. Throttle or
`requestAnimationFrame` is usually a better fit for scroll/gesture work.

Treat memoization as a measured optimization: profile first; use `memo` for
expensive repeated components with stable props, `useMemo` for expensive
derived work, and `useCallback` only when referential stability matters to a
memoized child or hook dependency. Do not blanket-wrap components or memoize
cheap values to hide duplicated state, unstable props, or an unvirtualized
large list. Keep server cache ownership in the query/data layer and shared
client workflow in Zustand or the repository's existing store.

## 5. Validate in layers

Run the narrowest relevant checks, then expand according to risk:

- formatter/linter on changed files;
- unit tests for parsers, formatters, reducers, query keys, permission logic,
  and state transitions;
- component/integration tests for loading, errors, retries, forms, navigation,
  auth/session changes, and mutation reconciliation;
- typecheck, router-type generation when applicable, and production bundle or
  export checks required by the repository;
- `npx expo-doctor` and dependency/config validation after relevant changes;
- development-build or native-target tests for permissions, camera/location,
  notifications, deep links, secure storage, gestures, background/resume,
  keyboard, and platform-specific behavior;
- physical-device checks for the highest-risk journey when device access is
  available.

Automated checks prove only their covered behavior. Expo Go is useful for
JavaScript iteration but does not prove a custom native module, native config,
production signing, or store-like binary. Mark unavailable device/provider
evidence as Unknown.

## 6. Performance and reliability gates

Measure before claiming an improvement. Inspect:

- cold start, first usable screen, JS bundle size, memory, and long tasks;
- render frequency, expensive selectors, unnecessary subscriptions, and list
  virtualization for large datasets;
- image size/cache behavior, pagination, request waterfalls, retry storms, and
  duplicate fetches;
- animation/frame stability on the target device; keep interactive work off
  the JS thread when the chosen Expo-compatible animation system supports it;
- offline, slow-network, background/resume, process restart, and stale-cache
  behavior;
- crash/error logs and observable recovery rather than only happy-path timing.

Do not add `memo`, a global store, a service worker, a native dependency, or a
new cache merely because it sounds faster. Establish a baseline, make one
focused change, and compare the same device/build/data conditions.

## 7. Review the diff and handoff

Before reporting completion:

- confirm only task-owned files changed and generated/native files are
  intentional;
- review auth, secret exposure, permission, deep-link, and account-switch
  boundaries;
- check loading/error/offline/recovery behavior and platform divergence;
- separate implemented code, automated evidence, local simulator evidence,
  physical-device evidence, EAS build evidence, and provider/production gates;
- list remaining unknowns and the exact next verification action.

Never call a mobile feature fully verified from source inspection, lint,
typecheck, a passing unit test, Expo Go, or one simulator screenshot alone.

## Completion contract

Report:

1. implemented screens/routes, contracts, state transitions, and native changes;
2. dependencies/config plugins and why they were added;
3. commands and checks with results;
4. exact simulator/device, OS, build profile, fixture, permissions, network,
   and journeys actually observed;
5. EAS/dev-build/binary/provider/store gates not observed;
6. runtime version, channel/update, rollout or rollback evidence when OTA is
   present;
7. known limitations, rollback path, and recommended follow-up.

Keep App Store and Google Play metadata, rejection analysis, and submission
decisions in `audit-mobile-store-submission`; this skill may produce a binary
or build artifact as engineering evidence but does not certify store readiness.
