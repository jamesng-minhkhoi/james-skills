# Data, auth, and security boundaries

Use when frontend work touches API calls, forms, user content, sessions,
permissions, billing, files, or sensitive data.

## Data contracts

Document the actual shape and lifecycle:

- required, nullable, optional, stale, paginated, and partial fields;
- loading, retry, timeout, validation, conflict, and rollback behavior;
- optimistic assumptions and server reconciliation;
- date, currency, locale, timezone, and numeric formatting;
- ownership, tenant scope, and row-level visibility;
- analytics event names and payload compatibility.

Do not silently coerce an unsafe or ambiguous value in the UI. Preserve the
source of truth and show uncertainty or stale state when it affects a decision.

## Authentication and authorization

- enforce authorization at the trusted server/provider boundary;
- treat client state, hidden fields, route guards, and disabled buttons as UX,
  not security;
- avoid leaking tokens, secrets, privileged error details, or other tenants'
  identifiers into client bundles, logs, URLs, or analytics;
- handle expired sessions, revoked access, missing membership, and permission
  changes without exposing protected content or losing recoverable work;
- verify destructive, financial, or irreversible actions with the server-side
  permission and business rule.

## User-controlled content

Review rendering, escaping/sanitization, URLs, redirects, uploads, filenames,
HTML/Markdown, rich text, and third-party embeds. Do not introduce `dangerouslySetInnerHTML`
or equivalent bypasses without a trusted sanitization contract and tests.

## Safe change boundary

If the frontend depends on a schema, function, provider, environment variable,
webhook, or deployment change, list it as an explicit gate. Do not claim the
frontend is production-ready because a local mock returns the expected shape.
