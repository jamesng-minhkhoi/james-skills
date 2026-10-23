## James skills: routing

Skills load on demand from their descriptions; this is the order and the
boundaries between them. Pick the smallest skill that covers the request.

**Product work runs design → build → audit.**

| Phase | Web | Mobile |
|---|---|---|
| Design (specs, flows, handoff; no product code) | `design-uiux-web`, `design-uiux-dashboard-web`, `design-uiux-landing-page-web` | `design-uiux-mobile` |
| Build (code, tests, runtime proof; no design decisions) | `frontend-web-engineering` | `frontend-mobile-engineering` |
| Audit (evidence and findings; no fixes unless asked) | `audit-uiux-web` | `audit-uiux-mobile`, `audit-mobile-store-submission` |

- Skip design when the request is a bug fix or the design already exists.
- When an audit should be independent of the work that produced the UI — after
  you built it in this session, before a release, or when the user asks for a
  review — delegate it to the `auditor` agent rather than auditing inline.
- Audit findings come back as a list; fixing them is build work.

**Marketing never edits product code.**

- Petio social, outreach, and content planning start in `petio-marketing`; it
  picks the `x-engagement` or `threads-engagement` adapter and its rules take
  precedence over theirs. Petio website search work (petiogo.com SEO, Search
  Console, blog articles) goes straight to `seo-aeo-content`.
- `x-engagement` and `threads-engagement` stand alone for non-Petio accounts.
- Nothing is published, scheduled, or sent without explicit approval in the
  current conversation.
