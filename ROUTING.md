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

**Motion and UI craft** (imported from emilkowalski/skills, MIT — see NOTICE;
these skills keep their upstream vocabularies, map severities HIGH/MEDIUM/LOW →
ontology P1/P2/P3 at handoff).

- Building an animation from scratch routes to `animate` (web) or
  `animate-expo` (React Native/Expo). Motion that stutters or drops frames
  routes to `animation-performance` on web; on a phone web app, platform-layer
  tells (safe areas, sticky hover, tap lag, viewport bugs) route to
  `mobile-native` and true frame-budget causes stay with
  `animation-performance`.
- `review-animations` (single review) and `improve-animations` (codebase audit
  with plans) and `find-animation-opportunities` (where motion would help)
  own motion-specific passes; `review-animations` is user-invoked only.
  `audit-uiux-web` and the `auditor` agent still own general UI audits; pick
  the smallest skill that covers the request.
- `emil-design-eng` and `break-ui` are user-requested craft passes (polish
  review, worst-case data stress test): route there when the user names the
  job, otherwise general review still goes to `audit-uiux-web` / `auditor`.
- In Expo, motion feel (gestures, sheets, transitions, haptics,
  thread strategy) routes to `animate-expo`; data, routing, state, and
  non-motion features stay with `frontend-mobile-engineering`; a gesture with
  both plumbing and feel is a joint build where `animate-expo` owns the feel
  decisions.
- `apple-design` informs principles when building or reviewing gesture-driven
  UI; `animate` / `animate-expo` still own the build.
- `mobile-native` makes a web app feel native on a phone (safe areas, 100vh,
  hover states, tap behavior); `break-ui` stress-tests UI with worst-case
  data; `apple-design` covers Apple-style motion principles; `pick-ui-library`
  and `prototype` run only when explicitly invoked; `animation-vocabulary`
  names unnamed motion effects; `ask-sonner` covers the Sonner toast library;
  `write-swift` covers modern Swift (Swift 6 concurrency, value types).
- Design-phase motion decisions (contracts, gesture ownership, thresholds)
  stay in `design-uiux` (`references/motion-and-gesture.md`); the craft skills
  above implement and review against them.

**Security and growth.**

- `offensive-*` web attack skills (SQLi, XSS, SSRF, SSTI, XXE, IDOR, upload, RCE, deserialization, races, smuggling, redirects, pollution, GraphQL, WAF, logic) fire only for targets the user is authorized to test; confirm the scope before the first probe. Reviewing/fixing one's own code is build work, not offensive testing.

- Social engagement routes to `x-engagement` (X) or `threads-engagement` (Threads).
- Product promo videos, UI walkthroughs, social reels, and reference-video recreations route to `product-video`.
- Organic short-form viral video distribution, clipping campaigns, UGC/AI-UGC creator programs, and account fleet/phone farm scaling (TikTok, Instagram Reels, YouTube Shorts) route to `viral-distribution`.
- Research that must survive trust review — frozen sources with sha256, verbatim-quoted claims, ledger-backed stopping — routes to `knowledge-builder`.
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
