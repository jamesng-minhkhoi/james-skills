## James skills: routing

Skills load on demand from their descriptions; this is the order and the
boundaries between them. Pick the smallest skill that covers the request.

**Product work runs decide → design → build → audit: what to build gets decided
before what it looks like.**

| Phase | Web | Mobile |
|---|---|---|
| Design (specs, flows, handoff; no product code) | `design-uiux` | `design-uiux` |
| Build (code, tests, runtime proof; no design decisions) | `frontend-web-engineering` | `frontend-mobile-engineering` |
| Audit (evidence and findings; no fixes unless asked) | `audit-uiux-web`, `code2flow` | `audit-uiux-mobile`, `audit-mobile-store-submission`, `code2flow` |

- Skip design when the request is a bug fix or the design already exists.
- Route-graph extraction, Mermaid user flows, PRD-vs-code drift checks, and 11-heuristic structural UX gap scans route to `code2flow`.
- Problem briefs, specs, PRD writing, prioritization, and post-launch metric readouts route to `product-discovery`; it produces no screens and no code.
- UI built/changed in this session, pre-release, or user-requested reviews audit via the `auditor` agent; changed skills, agents, or `ROUTING.md` get a zero-context pre-ship review from `skill-reviewer` before commit.
- Audit findings come back as a list keyed by `F-*` ID; fixing them is build
  work and returns a fix report.

**Security and growth.**

- `offensive-*` web attack skills (SQLi, XSS, SSRF, SSTI, XXE, IDOR, upload, RCE, deserialization, races, smuggling, redirects, pollution, GraphQL, WAF, logic) fire only for targets the user is authorized to test; confirm the scope before the first probe. Reviewing/fixing one's own code is build work, not offensive testing.

- Social engagement routes to `x-engagement` (X) or `threads-engagement` (Threads).
- Product promo videos, UI walkthroughs, 9:16 social reels, and reference-video
  recreations route to `product-video`.
- Editorial HTML/SVG/PNG architecture diagrams, sequence charts, data charts, and `.drawio`/Mermaid redraws route to `diagram-design`.
- SEO, AEO (Perplexity/ChatGPT Search citations, `Schema.org` JSON-LD), GEO (`llms.txt`), 12-section READMEs, and launch pages route to `seo-aeo-geo`.
- 3D modeling, CAD/3D-printable STL solids, image-to-3D reconstruction, procedural Three.js props, and Blender turntables route to `blender-3d-studio`.
- CV/resume tailoring (Google XYZ, 2-page PDF), A–G job offer evaluation, cover letters, LinkedIn outreach, interview prep, and offer-contract walks route to `cv-and-career-ops`.
- Nothing is published, scheduled, or sent without explicit approval in the
  current conversation.

**Vocabulary.** Proof: `declared < rendered < interactive < connected <
failure-tested < device < production`. Gates: `PASS | FAIL | BLOCKED | NOT_RUN`.
Deliverables: `READY | READY_WITH_CONDITIONS | NOT_READY | UNKNOWN`. Unobserved
is `NOT_RUN`/`UNKNOWN`, never pass; an unmarked claim is `unverified`. Full
ontology: `skills/_shared/ontology.md`.
