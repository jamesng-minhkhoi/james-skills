# Loading, responsiveness, and memoization

Load this when choosing a loading scope, debounce behavior, or memoization.
The rule is the same on web and mobile; only the noun changes (route/screen,
tenant/account, page/screen).

## Choose the smallest loading scope

| Situation | Required behavior |
| --- | --- |
| Initial route or screen with no usable shell or safe content | A route/screen skeleton or loading boundary may block; match the final geometry. |
| Existing app shell, navigation, or client navigation | Keep navigation, header, filters, and stable content mounted; replace only the changing region. |
| Initial list, table, or grid fetch | Use row/card skeletons with final-shape geometry; never a giant page spinner. |
| Refresh, background revalidation, or stale cache | Keep usable stale content visible with a local refresh indicator and clear freshness status. |
| Field validation, autocomplete, or filter query | Show pending/error at the field or control; debounce query input and cancel stale requests. |
| Row/card mutation | Keep the rest of the page or screen interactive; mark only the affected row/action pending and reconcile or roll back locally. |
| Auth, tenant, account, permission, or route-wide context switch | A route/screen-wide boundary is acceptable when old content must be removed to prevent leakage or an incorrect action. |

## Debounce

Use a short, measured debounce for high-frequency query input (often about
250–400 ms for search/typeahead), cancel or ignore obsolete requests, and never
debounce an explicit submit, destructive action, or button press. Throttle or
`requestAnimationFrame` is usually a better fit for scroll, resize, or gesture
work.

## Memoization

Treat memoization as a measured optimization: profile first; use `memo` for
expensive repeated components with stable props, `useMemo` for expensive
derived work, and `useCallback` only when referential stability matters to a
memoized child or hook dependency. Do not blanket-wrap components or memoize
cheap values to hide duplicated state, unstable props, or an unvirtualized
large list.

Keep server cache ownership in the query/data layer (TanStack Query when
present) and shared client workflow in Zustand or the repository's existing
store. Preserve the same query-key ownership across reads and writes.
