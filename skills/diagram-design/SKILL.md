---
name: diagram-design
description: Generate editorial HTML/SVG diagrams, technical architecture figures, and data charts across 27 visual types — or redraw existing draw.io (.drawio) and Mermaid (.mmd) diagrams into publication-grade visuals with PNG/SVG export and brand onboarding.
---

# Editorial Diagram & Chart Design (`diagram-design`)

Generate clean, self-contained HTML + inline SVG diagrams and data charts with warm-paper editorial craft, strict 4px grid discipline, orthogonal `r=8` connectors, and deterministic geometry/accessibility verification.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

---

## 1. Visual North Star & Core Rules

- **Warm paper (`#f5f5f5`) default** (or onboarded brand tokens) — never sterile `#fff` or muddy dark gray unless using the minimal-dark (`template-dark.html`) or terminal (`template-terminal.html`) variant.
- **One primary focal accent (`--coral: #eb6c36`)** — used on **at most 2 focal elements** per diagram. If everything is highlighted, nothing is.
- **Three typefaces, three jobs:** `Instrument Serif` (display `h1` & italic callouts), `Geist` (human-readable node names, body, card titles), `Geist Mono` (eyebrows, rectangular `rx=2` badges, technical sublabels, arrow labels, legend). Never use JetBrains Mono.
- **Hairline 1px borders (`rgba(45,49,66,0.12)`)** — no drop shadows, no gradients, no 3D bevels, no rounded pill tags.
- **Strict 4px grid** — all font sizes, coordinates, widths, heights, and gaps must be divisible by 4.
- **Six mandatory connector rules** — orthogonal right-angle paths with `r=8` rounded elbows (never diagonal `<line>` slants between off-axis nodes), open chevron markers, arrows drawn *before* boxes, opaque `#f5f5f5` arrow-label masks with a 6–10px visible gap to the stroke, fanned shared-edge attach points (≥12px apart), and bridge hops on crossings. Full markup and checklist in [svg-primitives-and-checklist.md](references/svg-primitives-and-checklist.md).

---

## 2. Brand Onboarding & Preset Profiles

Check in order before drawing:

1. **Project brand profile:** Look for `.diagram-design/brand-profile.json` in the workspace or ask if the user named a website/company to match. If onboarding a brand or URL, load [onboarding.md](references/onboarding.md).
2. **Named style profile:** If the user names a preset (`default`, `editorial-light`, `minimal-dark`, `blueprint`, `monochrome-ink`, `warm-sepia`, `swiss-grid`, `whitegrid`, `dark-terminal`, `corporate-slate`), load [profiles.md](references/profiles.md).
3. **Default aesthetic:** Warm paper `#f5f5f5` + deep slate `#2d3142` + coral `#eb6c36` ([style-guide.md](references/style-guide.md) and [svg-primitives-and-checklist.md](references/svg-primitives-and-checklist.md)).

---

## 3. Semantic Pattern Selection (When Behavior Is Load-Bearing)

When the subject is a **runtime flow, protocol, pipeline, or state transition**, choose **one semantic pattern** before choosing the visual layout and load [semantic-patterns.md](references/semantic-patterns.md):

| If the subject is… | Semantic pattern | Load visual type |
|---|---|---|
| Synchronous call where caller blocks | `request-response` | [type-sequence.md](references/type-sequence.md) or [type-architecture.md](references/type-architecture.md) |
| Events published to a broker / topic / fan-out | `event-driven` | [type-data-flow.md](references/type-data-flow.md) or [type-architecture.md](references/type-architecture.md) |
| Ordered data transforms (`raw -> clean -> mart`) | `streaming-etl` | [type-data-flow.md](references/type-data-flow.md) or [type-medallion.md](references/type-medallion.md) |
| Lifecycle states + triggers / guards | `state-machine` | [type-state.md](references/type-state.md) or [type-it-state.md](references/type-it-state.md) |
| Closed cycle where output feeds input | `feedback-loop` | [type-loop.md](references/type-loop.md) |
| Phased rollout, cutover, or timeline | `deployment-train` | [type-timeline.md](references/type-timeline.md) or [type-process.md](references/type-process.md) |
| Trust zones, policy gates, identity boundary | `trust-boundary` | [type-architecture.md](references/type-architecture.md) or [type-dp-security-matrix.md](references/type-dp-security-matrix.md) |

---

## 4. Visual Type Catalog (27 Types — Load Before Drawing)

Always load the matching `references/type-<name>.md` before writing SVG:

| Visual Type | Best For | Reference File |
|---|---|---|
| **Architecture / System** | Services, infra, request/data flow across components (max 9 nodes) | [type-architecture.md](references/type-architecture.md) |
| **Flowchart / Decision** | Branching logic, yes/no diamonds, triage trees | [type-flowchart.md](references/type-flowchart.md) |
| **Sequence Diagram** | Time-ordered actor interactions, auth handshakes, API flows (max 5 lifelines) | [type-sequence.md](references/type-sequence.md) |
| **Timeline / Roadmap** | Chronological milestones, release phases | [type-timeline.md](references/type-timeline.md) |
| **Swimlane** | Cross-team / cross-service handoffs across horizontal lanes (max 5 lanes) | [type-swimlane.md](references/type-swimlane.md) |
| **Quadrant / 2×2 Matrix** | Positioning along 2 axes (editorial or BCG/McKinsey consultant special) | [type-quadrant.md](references/type-quadrant.md) |
| **State Diagram** | Object lifecycle, state transitions (`[●]` start, `[◉]` end) | [type-state.md](references/type-state.md) |
| **ER Diagram** | Database schema, tables, PK/FK crow's-foot relationships (max 8 entities) | [type-er.md](references/type-er.md) |
| **Nested Containment** | Zoom-in concentric shells (Kubernetes, OS, runtime scopes, max 6 levels) | [type-nested.md](references/type-nested.md) |
| **Tree / Hierarchy** | File systems, ASTs, taxonomies, org breakdown (max depth 4) | [type-tree.md](references/type-tree.md) |
| **Org Chart** | Reporting lines, agent command hierarchies, dashed escalation (max 12 nodes) | [type-org-chart.md](references/type-org-chart.md) |
| **Layer Stack** | Horizontal cake tiers (OSI, platform stack, max 6 layers) | [type-layers.md](references/type-layers.md) |
| **Venn Diagram** | Overlapping sets (2 or 3 circles) | [type-venn.md](references/type-venn.md) |
| **Pyramid / Funnel** | Narrowing hierarchy, DIKW, testing pyramid (max 6 tiers) | [type-pyramid.md](references/type-pyramid.md) |
| **Radar / Spider** | Multi-axis profile comparison (3–5 axes, max 5 series) | [type-radar.md](references/type-radar.md) |
| **Bar Chart** | Ranked quantities across categories (max 8 bars) | [type-bar.md](references/type-bar.md) |
| **Line Chart** | Metric trends over time with direct right-edge labels (max 5 series) | [type-line.md](references/type-line.md) |
| **Gantt Chart** | Scheduled tasks on a shared time axis (max 12 tasks) | [type-gantt.md](references/type-gantt.md) |
| **Scatter Plot** | Correlation & clusters on 2 numeric axes (max 30 points) | [type-scatter.md](references/type-scatter.md) |
| **Cycle / Feedback Loop** | Circular processes (`Build -> Measure -> Learn`, 3–6 nodes) | [type-loop.md](references/type-loop.md) |
| **High-Level Enterprise** | Multi-tier enterprise architecture with spine & bottom service bar | [type-high-level.md](references/type-high-level.md) |
| **Data Flow / Lineage** | End-to-end pipeline from sources to consumers | [type-data-flow.md](references/type-data-flow.md) |
| **Medallion Architecture** | Bronze -> Silver -> Gold lakehouse tiers + platform bar | [type-medallion.md](references/type-medallion.md) |
| **Data Platform Integration** | 6-column integration blueprint with numbering & protocol tags | [type-dp-integration.md](references/type-dp-integration.md) |
| **Data Platform Security Matrix** | Cross-tier governance, IAM, encryption, and audit matrix | [type-dp-security-matrix.md](references/type-dp-security-matrix.md) |
| **IT State Evolution** | Current -> Transitional -> Target state roadmap | [type-it-state.md](references/type-it-state.md) |
| **Numbered Process Flow** | Step-by-step workflow with numbered badges & decision gates | [type-process.md](references/type-process.md) |

Optional primitives:
- **Vendor / Tech Logos (Simple Icons & Devicon):** [primitive-icons.md](references/primitive-icons.md)
- **Italic Serif Annotation Callouts:** [primitive-annotation.md](references/primitive-annotation.md)
- **Sketchy Hand-Drawn Filter:** [primitive-sketchy.md](references/primitive-sketchy.md)
- **Terminal / CLI Window Variant:** [primitive-terminal.md](references/primitive-terminal.md)
- **Step / Loop / Reveal Motion:** [animation.md](references/animation.md)

---

## 5. Importing `.drawio` & Mermaid `.mmd` Diagrams

Never blindly copy coordinates from draw.io or Mermaid. Extract structure first, set the 4 output dials ([output-spec.md](references/output-spec.md)), and redraw cleanly:

- **draw.io (`.drawio`, `.drawio.xml`, `.drawio.svg`, `.drawio.png`):** Load [import-drawio.md](references/import-drawio.md) and run:
  ```bash
  python3 skills/diagram-design/scripts/drawio_extract.py path/to/file.drawio
  ```
- **Mermaid (`.mmd`, `.mermaid`, or Markdown fenced `mermaid` blocks):** Load [import-mermaid.md](references/import-mermaid.md) and run:
  ```bash
  python3 skills/diagram-design/scripts/mermaid_extract.py path/to/file.mmd
  ```

---

## 6. Execution & Deterministic Verification Workflow

1. **Select Template:** Copy the closest starter from `skills/diagram-design/assets/` (`template.html` for minimal light, `template-dark.html` for dark, `template-full.html` for editorial cards, `template-terminal.html` for CLI dark, `template-motion.html` when animation is requested).
2. **Load Type & Primitives:** Read the matching `references/type-<name>.md` and [svg-primitives-and-checklist.md](references/svg-primitives-and-checklist.md).
3. **Author Accessible Self-Contained HTML/SVG:** Ensure `<svg role="img" aria-labelledby="<slug>-title <slug>-desc">` has `<title>` as its first child before `<defs>`.
4. **Run Deterministic Verifiers (MANDATORY before delivery):**
   ```bash
   python3 skills/diagram-design/scripts/self_check.py path/to/diagram.html
   python3 skills/diagram-design/scripts/verify-geometry.py path/to/diagram.html
   ```
   If motion is enabled, also run:
   ```bash
   python3 skills/diagram-design/scripts/verify-motion.py path/to/diagram.html
   ```
5. **Optional PNG / SVG Export:** When the user asks for `.png` or `.svg` files, follow [export.md](references/export.md).
