# Break UI regression cases

Use these forward-test fixtures when changing the `break-ui` skill. They are
review prompts with expected gates, not executable tests.

## Case 1: worst-case stress test

Prompt: "Stress-test this member row."

Expected behavior:

- use plausible or schema-backed worst cases (longest real name pattern,
  unbreakable email, one-letter name, missing fields, huge count, zero items,
  non-Latin text, emoji) — not `aaaa…` nonsense;
- build one mixed fixture, not a pile of separate pages;
- render behind a dev-only "Demo data / Worst case" toggle, never shipped;
- report in the required format: what broke, why, and the fix for each;
- propose fixes but apply them only when asked.

## Must not have

A completion claim fails if it contains any of these:

- invented data patterns with no plausible real-world counterpart;
- worst-case data wired into the real app state without a toggle;
- "passed" without rendering the fixture (a code read is not a render);
- fixes applied to source during the stress-test run without a request.
