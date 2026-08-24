# Expo engineering regression cases

Use these forward-test fixtures when changing the mobile engineering skill.
They are review prompts with expected gates, not a substitute for running the
target repository's tests or build.

## Case 1: Native capability in an existing Expo app

Prompt: “Add camera and push notifications to this Expo app and make it work.”

Expected behavior:

- inspect the exact SDK, managed/CNG/prebuild/bare mode, app config, config
  plugins, existing permissions, and current notification/deep-link contract;
- use SDK-compatible Expo packages and distinguish Expo Go iteration from a
  custom development build and production binary;
- model first request, denied/restricted, settings recovery, background/opened
  notification, token rotation, offline retry, and logout/account switching;
- require `npx expo-doctor`, a new native build where needed, and device evidence
  rather than claiming success from a JavaScript reload.

## Case 2: Offline mutation plus account switch

Prompt: “Let users create records offline, sync later, and switch accounts.”

Expected behavior:

- define whether the product queues, drafts locally, blocks, or reads cached
  data, including freshness, conflict, idempotency, retry, and user-visible
  pending status;
- keep server truth, query cache, Zustand/client workflow, and form draft
  ownership distinct;
- clear identity-sensitive cache and queued work safely on logout/account
  switch, and handle token expiry, restart, cancellation, and duplicate taps;
- verify offline, reconnect, conflict, failure, and recovery on the supported
  mobile target.

## Case 3: Search and mutation responsiveness

Prompt: “Show a full-screen loader whenever search or a row action waits for the
server, and memoize every component to improve performance.”

Expected behavior:

- keep the navigation shell and unrelated rows usable; use field-level query
  pending state, row/action pending state, and local rollback/reconciliation;
- debounce high-frequency search input, cancel or ignore obsolete requests, and
  never debounce explicit submit or destructive actions;
- reserve screen-wide blocking for initial boot or an auth/account/permission
  transition where old content must be removed;
- profile render cost and list behavior before adding `memo`, `useMemo`, or
  `useCallback`, and preserve server-cache versus client-workflow ownership.
