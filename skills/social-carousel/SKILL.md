---
name: social-carousel
description: Design, script, verify, and render high-signal visual carousels and multi-slide photo posts for TikTok, Instagram, and LinkedIn. Enforces anti-slop gates: concrete visual proof (real UI, code diffs, data, or exact diagrams), mobile safe-zone compliance, verifiable claims, and zero synthetic AI filler. Use for product breakdowns, technical explainers, case studies, and visual teardowns. Not for pure text threads (→ x-engagement, threads-engagement) or video (→ product-video).
---

# Social Carousel

Build visual photo carousels and multi-slide decks that deliver immediate,
high-density signal. Every slide is grounded in concrete visual artifacts—real
application interfaces, code diffs, data charts, and structural diagrams—rather
than generic generative AI art, empty curiosity gaps, or filler text.

Shared vocabulary: [ontology](../_shared/ontology.md). Deliverables report
proof ladder rungs (`declared < rendered < interactive < connected < failure-tested < device < production`)
and standard gate verdicts (`PASS | FAIL | BLOCKED | NOT_RUN`).

Load [anti-slop rubric](references/anti-slop-rubric.md) when evaluating slide
storylines and asset quality. Load [safe zones and dimensions](references/safe-zones-and-dimensions.md)
before composing layouts for TikTok 9:16 or Instagram 4:5.

## When NOT to use

- Writing text-only threads or founder replies on X → `x-engagement`.
- Writing builder posts or ranked-feed replies on Threads → `threads-engagement`.
- Recording 1080p60 product demos, UI walkthroughs, or motion video → `product-video`.
- Structuring paid creator bounties or clipping campaigns → `viral-distribution`.
- Generating pure SVG technical architecture diagrams → `diagram-design`.

---

## Operating Modes

Choose one mode before beginning:

1. **Draft & Storyboard:** Define the single thesis, select primary visual
   artifacts, script headlines, body copy, and safe-zone layouts in a structured
   `carousel.json` manifest. Do not render.
2. **Render & Export:** Generate publication-ready PNG slides (1080×1920 for
   TikTok Photo Mode, 1080×1350 for Instagram/LinkedIn 4:5) using reproducible
   HTML/CSS or image compositing scripts.
3. **Anti-Slop Audit:** Inspect an existing carousel deck or draft against the
   five anti-slop gates. Return findings keyed with `F-carousel-*` IDs.

---

## Five Non-Negotiable Anti-Slop Gates

Every carousel produced or audited must satisfy all five gates.

### Gate 1 — Proof Over Filler (Zero Generative AI Slop)
Every slide must feature a concrete primary artifact:
- Real product UI screenshot with highlighted callouts.
- Side-by-side code diff or syntax-highlighted snippet.
- Quantitative data chart, metric table, or latency graph.
- Structural architecture diagram (via `diagram-design`).
- Authentic human photograph or unedited interface capture.

**Prohibited:** Decorative generative AI filler (floating 3D shapes, glowing
neon brains, generic futuristic robots, cybernetic faces, or stock handshake
visuals). If a concept lacks a concrete artifact, produce a clean typographical
card or structural diagram, never decorative AI imagery.

### Gate 2 — Information Density & Verified Claims
- Slide 1 must state the exact subject, mechanism, and payoff. Prohibit empty
  curiosity-gap clickbait (*"99% of developers do this wrong"*).
- Every quantitative claim, benchmark, or quoted result must carry an explicit
  attribution source (author, organization, or repo proof ledger).
- Prohibit artificial cliffhangers (*"Wait until slide 7 for the secret"*). The
  core finding must be stated upfront; subsequent slides provide depth.

### Gate 3 — Platform Safe Zones & Mobile Legibility
- Strictly observe [safe zones](references/safe-zones-and-dimensions.md):
  - **TikTok (9:16 — 1080×1920):** Top margin >= 160 px, bottom margin >= 320 px,
    right margin >= 130 px, left margin >= 60 px.
  - **Instagram (4:5 — 1080×1350):** Top margin >= 80 px, bottom margin >= 100 px,
    horizontal margins >= 70 px.
- All body text >= 24 px equivalent at 1080p resolution.
- WCAG AA contrast ratio (>= 4.5:1) for all text against backgrounds.

### Gate 4 — Single-Idea Slide Architecture
- Maximum 1 primary headline and 1 primary visual artifact per slide.
- Body copy capped at <= 3 concise bullet points or <= 45 words per slide.
- Prohibit unedited ChatGPT paragraphs or wall-of-text listicles.

### Gate 5 — Explicit Authorization & Local Output
- All carousels are drafted, verified, and rendered locally into the target
  project directory (`dist/<slug>/`).
- Never attempt to auto-publish, schedule, or interact with third-party social
  APIs without explicit in-session user authorization.

---

## Workflow

```
1. Thesis & Target → 2. Proof Sourcing → 3. Slide Scripting → 4. Safe-Zone Layout → 5. Anti-Slop Validation → 6. Export Package
```

### 1. Define Thesis, Audience, and Canvas
Determine:
- Target platform: TikTok Photo Mode (9:16, 1080×1920) or Instagram/LinkedIn (4:5, 1080×1350).
- One clear audience and one verifiable technical or product insight.
- Slide count: 4 to 8 slides maximum. Reject bloated 12+ slide decks.

### 2. Source Concrete Visual Artifacts
Collect or generate the core assets before writing slide copy:
- Capture real screenshots from running code, web apps, or terminal logs.
- Obtain SVGs or architectural topologies from `diagram-design`.
- Export code diffs with clear before/after highlighting.
- Record every asset's origin in the brief.

### 3. Script the Slide Progression
Follow high-signal content architecture:
- **Slide 1 (Hook & Payoff):** Specific tension + the proven outcome.
- **Slide 2 (The Failure Mechanism / Status Quo):** Why conventional methods fail.
- **Slide 3–5 (The Proof & Implementation):** Step-by-step forensic teardown
  with visual artifacts.
- **Final Slide (Actionable Takeaway):** Summary rule of thumb and high-signal CTA
  (e.g., links to open-source repository or documentation).

### 4. Compose Safe-Zone Layout
Assemble slides using reproducible HTML/CSS templates or canvas renderer:
- Enforce padding according to target platform safe zones.
- Align headlines, subheaders, and artifact frames to a consistent 8px grid.
- Keep background neutral, dark, or brand-specific with high contrast.

### 5. Run the Anti-Slop Validation
Validate the slide manifest using the internal validator:

```bash
python3 skills/social-carousel/scripts/validate_carousel.py <path/to/carousel.json>
```

Ensure 0 errors before proceeding to export.

### 6. Deliver the Export Package
Generate the delivery folder:
- Numbered slide images (`slide-01.png`, `slide-02.png`, etc.).
- `contact-sheet.png` displaying all slides side-by-side for rapid review.
- `copy.md` containing caption, slide transcript, alt text, and source citations.
- Preflight anti-slop verification report.

---

## Failure Modes & Corrections

| Failure Mode | Root Cause | Correction |
|---|---|---|
| **F-SLOP-1: Decorative AI imagery** | Agent generated a Midjourney/DALL-E futuristic graphic to fill white space. | Delete image. Replace with a real code diff, UI crop, or a structural SVG diagram. |
| **F-SLOP-2: Clickbait headline** | Hook withholds the subject (*"You won't believe what happens when..."*). | Rewrite headline to name the exact technology, metric, and mechanism. |
| **F-SLOP-3: Text covered by TikTok UI** | Text placed below y: 1600 px or to the right of x: 950 px. | Shift content into the 890×1440 px active safe canvas. |
| **F-SLOP-4: Wall-of-text slide** | Exceeded 45 words or copied multiple generic bullet points. | Cut copy down to one takeaway and maximum 3 bullet points (<= 25 words). |
| **F-SLOP-5: Unsourced statistic** | Quoted "80% faster" without citation. | Attach verified benchmark link or remove the numerical claim. |

---

## Hand-over

Return the completed run block:

```markdown
### Social Carousel Hand-over

- **Platform & Format:** <TikTok 9:16 | Instagram 4:5 | LinkedIn>
- **Slide Count:** <N slides>
- **Primary Proof Artifacts:** <Real UI screenshots | Code diffs | SVG diagrams>
- **Anti-Slop Gates:**
  - Gate 1 (Proof Over Filler): PASS
  - Gate 2 (Information Density): PASS
  - Gate 3 (Safe Zones & Contrast): PASS
  - Gate 4 (Single-Idea Architecture): PASS
  - Gate 5 (Authorization): PASS
- **Proof Level:** rendered (contact sheet + slide PNGs inspected)
- **Publishing Status:** DRAFT_ONLY (waiting for user review)
```
