# Data, state, and native boundaries

Use for API work, authentication, persistence, caching, lifecycle, offline
behavior, or native capabilities. Preserve existing contracts unless a change
is explicitly in scope.

## Server state and client state

- Keep API responses in the API/query layer. Use TanStack Query when the app
  needs cache, deduplication, invalidation, polling, optimistic updates, or
  dependent queries.
- Use Zustand or the existing store only for shared client workflow,
  preferences, or transient state. Do not copy authoritative server records
  into a second store without a reconciliation reason.
- Keep form drafts and local disclosure in component state when one component
  owns them. Keep shareable route state in navigation params when appropriate.
- Define query keys, stale time, garbage collection, retry policy, cancellation,
  invalidation, and mutation rollback explicitly.

## Networking

Prefer the platform/Expo-supported `fetch` path unless the repository already
has a justified client. Every request needs:

- typed input/output and safe parsing;
- timeout or cancellation behavior;
- status/error normalization without leaking tokens or personal data;
- duplicate-submit protection and idempotency for writes;
- retry only for safe/transient failures, with bounded backoff;
- loading, empty, stale, offline, authorization, validation, and server-error
  recovery;
- observability that distinguishes user cancellation, network failure, and
  provider failure.

Avoid request waterfalls and duplicate fetches caused by route, screen, and
component effects all loading the same record. Cancel old requests when the
screen identity or query changes.

## Auth, storage, and environment

- Treat `EXPO_PUBLIC_*` and values in the JavaScript bundle as public. Never
  put private keys, service-role credentials, or authorization decisions there.
- Store refresh/access tokens only through the repository's secure storage
  boundary, commonly `expo-secure-store`, with expiry and sign-out cleanup.
- Model boot, authenticated, unauthenticated, expired, refreshing, and
  account-switch states. Clear user-specific caches when identity changes.
- Keep environment selection explicit for development, preview, and production.
  Confirm the resolved API URL and app config in the actual build profile.

## Lifecycle and native capabilities

For camera, location, notifications, biometrics, files, media, or background
work, define:

`not requested → requesting → granted | denied | restricted → usable/retry/settings`

Also cover app foreground/background, process restart, interrupted permission
requests, missing services, revoked permissions, and platform differences.
Use config plugins and development builds when native configuration is involved.
For push, additionally cover token registration per device/account, token
rotation, offline retry, logout/account-switch cleanup, and notification-open
deep links. A token fetch failure or Expo Go limitation is not proof that push
delivery works.

## Offline and stale data

Choose one explicit policy: block with recovery, read cached data, queue a
mutation, or allow a local-only draft. Define freshness, conflict resolution,
retry, duplicate prevention, and user-visible status. Do not imply a write was
saved while it is only queued locally.

## References

- [Expo environment variables](https://docs.expo.dev/guides/environment-variables/)
- [Expo development builds](https://docs.expo.dev/develop/development-builds/use-development-builds/)
- [Expo EAS environments](https://docs.expo.dev/eas/environment-variables/)
