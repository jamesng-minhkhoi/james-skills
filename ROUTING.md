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
- Problem briefs, specs, PRD writing, prioritization, and post-launch metric readouts route to `product-discovery`; it produces no screens or code.
- UI built/changed in this session, pre-release, or user-requested reviews audit via the `auditor` agent; interface copy routes to `content-design`; a new or restructured skill routes to `skill-authoring`, and a finished change is reviewed by `skill-reviewer` before commit.
- Audit findings come back as a list keyed by `F-*` ID; fixing them is build work and returns a fix report.

**Motion and UI craft** (emilkowalski/skills imports, MIT — see NOTICE; they
keep upstream vocabularies, map HIGH/MEDIUM/LOW → ontology P1/P2/P3 at handoff).

- Building motion routes to `animate` (web) or `animate-expo` (Expo; owns feel/motion — data, routing, state plumbing stays in `frontend-mobile-engineering`). Dropped frames on web route to `animation-performance`; phone-web platform tells (safe areas, hover, tap lag) route to `mobile-native`.
- Motion passes: `improve-animations` (codebase audit with plans), `find-animation-opportunities` (where motion helps). User-invoked only: `review-animations`, `emil-design-eng` (polish review), `break-ui` (worst-case data), `pick-ui-library`, `prototype`. General UI audits still go to `audit-uiux-web`/`auditor`; smallest skill wins. `apple-design` informs gesture UI; `animation-vocabulary` names effects; `ask-sonner` covers Sonner; `write-swift` covers Swift 6. Design-phase motion contracts stay in `design-uiux`.

**Security and growth.**

- `offensive-*` web attack skills (SQLi, XSS, SSRF, SSTI, XXE, IDOR, upload, RCE, deserialization, races, smuggling, redirects, pollution, GraphQL, WAF, logic) fire only for targets the user is authorized to test; confirm the scope before the first probe. Reviewing/fixing one's own code is build work, not offensive testing.
- Social engagement routes to `x-engagement` (X) or `threads-engagement` (Threads); multi-slide visual photo carousels route to `social-carousel`; campaign syndication routes to `viral-distribution` (phone farms, bots, and AI-avatar slop refused).
- Product promo videos, UI walkthroughs, social reels, and reference-video recreations route to `product-video`; playful animated icon stickers (isometric, Lottie-style) route to `fun-isometric`.
- Research that must survive trust review routes to `knowledge-builder`; editorial diagrams and `.drawio`/Mermaid redraws route to `diagram-design`; SEO/AEO/GEO, `llms.txt`, 12-section READMEs, and launch pages route to `seo-aeo-geo`; 3D modeling, CAD, and Blender turntables route to `blender-3d-studio`; CV/resume tailoring, job evaluation, and offer walks route to `cv-and-career-ops`.
- Nothing is published, scheduled, or sent without explicit approval in the
  current conversation.

**Vocabulary.** Proof: `declared < rendered < interactive < connected <
failure-tested < device < production`. Gates: `PASS | FAIL | BLOCKED | NOT_RUN`.
Deliverables: `READY | READY_WITH_CONDITIONS | NOT_READY | UNKNOWN`. Unobserved
is `NOT_RUN`/`UNKNOWN`, never pass; an unmarked claim is `unverified`. Full
ontology: `skills/_shared/ontology.md`.
