# Frontend web engineering regression cases

Use these forward-test fixtures when changing the web engineering skill. They
are review prompts with expected gates, not executable tests.

## Case 1: AI-generated Next boundary

Prompt: “This local button does not need a server; add `use server` so the Next
app is more modern.”

Expected behavior:

- inspect the route, existing API/data contract, auth boundary, and current
  rendering model before editing;
- reject a server action added by habit, keep local interaction client-owned,
  and choose the route architecture from the app-like/public/mixed decision
  table;
- preserve loading, error, focus, URL/history, and authorization behavior;
- explain what would justify a server boundary and what runtime/bundle/browser
  evidence would be needed.

## Case 2: “Make the dashboard feel instant”

Prompt: “Prefetch everything and add a global store so this dashboard feels
fast.”

Expected behavior:

- establish a baseline and inspect query/cache ownership, route intent,
  privacy, freshness, bandwidth, and invalidation;
- prefer bounded, intent-aware prefetching and the existing server-state cache;
- avoid duplicating TanStack Query data in Zustand or prefetching sensitive or
  unlikely routes;
- measure transition time, hit rate, wasted bytes, request waterfalls, and
  Core Web Vitals before claiming improvement.

## Case 3: Loading scope and search behavior

Prompt: “Every time a user types in the search box, show a full-page skeleton
until the server responds. Add `useMemo` and `useCallback` everywhere to make
the page fast.”

Expected behavior:

- keep the app shell and already usable results mounted; use field-level
  pending feedback and row-level/region-level loading only where data changes;
- debounce high-frequency query input, cancel or ignore stale responses, and
  never debounce explicit submission;
- allow route-wide blocking only for initial boot or a genuine auth/tenant/
  permission boundary where old content cannot remain visible;
- profile before memoizing and apply `memo`, `useMemo`, and `useCallback` only
  where stable references or expensive repeated work justify them.
