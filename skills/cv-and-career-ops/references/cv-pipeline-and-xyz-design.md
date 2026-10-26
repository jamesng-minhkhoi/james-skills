# 5-Phase CV Engineering Pipeline, Google XYZ Formula & Design System

This reference combines the **Open-CV 5-Phase Engineering Pipeline** (`open-cv-pipeline`) and **ATS / LaTeX CV Builders** (`career-ops`) for crafting high-converting, fact-verified resumes and diagnostic audit reports.

---

## 1. The 5-Phase CV Engineering Lifecycle

```text
Phase 1: RESEARCH  ->  Phase 2: TAILOR  ->  Phase 3: BUILD  ->  Phase 4: EXPORT  ->  Phase 5: REPORT
(Role Signal Matrix)   (Google XYZ MD)      (HTML / LaTeX)     (Playwright PDF)     (Audit Scorecard)
```

### Phase 1 — RESEARCH (Understand the Target Role)
- Extract the **1-sentence root hiring signal** required by the target role (e.g., `Agentic Systems / LLMOps`, `Staff Frontend Architecture`, `Principal Product Designer`, `Technical Product Manager`).
- Build a **Role Signal Matrix & Trade-off Framing Table**:
  - Identify the candidate's top 10 verifiable accomplishments and metrics from their canonical `cv.md` / profile.
  - Decide what to emphasize (top 60% of visual real estate) vs. compress (older or non-aligned roles).

### Phase 2 — TAILOR (Google XYZ Formula & FAANG Power Verbs)
Every experience bullet MUST follow the **Google XYZ Formula**:

```text
[FAANG Power Verb] + [What you built / owned] -> [Quantified Impact or Scope Outcome]
```

- **Approved Power Verbs:** *Architected, Engineered, Spearheaded, Standardized, Automated, Reduced, Scaled, Shipped, Redesigned, Eliminated, Consolidated, Instrumented.*
- **Banned Weak Openers:** *Responsible for, Helped with, Worked on, Assisted, Participated in, Was involved in.*
- **Scope & Volume Indicators (when hard revenue/ROI metrics are private or unavailable):** Use verifiable engineering/product scope numbers instead of inventing percentages — e.g., platform surface count (`across 4 surfaces: iOS, Android, Web, CLI`), component/token count (`60+ design system tokens`), latency/bundle delta (`cut cold-start from 2.1s to 380ms`), test/gate coverage (`10-gate deterministic CI harness`).
- **Non-Fabrication Rule (MANDATORY):** Never invent employers, titles, dates, degrees, or metrics. Run `node skills/cv-and-career-ops/scripts/verify-cv-facts.mjs` to cross-check claims against the candidate's canonical `cv.md`.

### Phase 3 — BUILD (HTML / LaTeX Templates)
Select the template in `skills/cv-and-career-ops/templates/` that matches the target channel:

| Template | Best For | Visual & Typography Spec |
| :--- | :--- | :--- |
| **`v2-modern.html`** | Direct hiring-manager outreach, portfolio PDF, senior/staff design & engineering roles | High-contrast monochrome (`#000000` / `#ffffff` / `#4e4b66`), `DIN Condensed` 56px uppercase headers, `SF Pro Rounded` body, 5-column scope impact banner, `1811px × 2560px` (strict 2 pages) |
| **`v1-classic.html`** | Dense multi-role technical backgrounds | 2-column structured monochrome grid, `1811px × 2800px` (strict 2 pages) |
| **`ats-cv-template.html`** | Greenhouse, Ashby, Lever, Workday ATS uploads | Clean single-column A4 DOM (`Space Grotesk` + `DM Sans`), keyword-injected, machine-parsable headings |
| **`build-cv-latex.mjs`** | Overleaf / LaTeX `.tex` academic & SWE resumes | Generates clean single-column `.tex` source from structured CV sections |

### Phase 4 — EXPORT (Playwright Deterministic PDF Rendering)
Render HTML templates into pixel-perfect PDFs using `scripts/export-pdf.mjs`:

```bash
node skills/cv-and-career-ops/scripts/export-pdf.mjs
```

Critical Playwright PDF settings:
- Wait for `networkidle` and `await page.evaluate(() => document.fonts.ready)` before printing.
- Set `printBackground: true` and `margin: { top: 0, right: 0, bottom: 0, left: 0 }`.
- Verify that the exported PDF is **1–2 pages max** (never a trailing 3-line overflow page).

### Phase 5 — REPORT (Diagnostic & Multi-Role Audit Report)
Generate `templates/report.html` or `templates/report-multi-role.html` to show the candidate:
1. **Positioning Scorecard (Before vs. After)** across clarity, XYZ impact density, ATS keyword coverage, and seniority signal.
2. **Bullet Transformation Matrix** showing each original bullet alongside its XYZ-reframed version and the JD requirement it satisfies.
3. **Multi-Role Fit Comparison** (when targeting 2–3 adjacent tracks such as IC Staff Engineer vs. Engineering Manager vs. Solutions Architect).
