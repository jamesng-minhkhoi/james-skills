---
name: seo-aeo-geo
description: Audit, scaffold, and optimize websites, SaaS landing pages, docs sites, and GitHub repositories for Search Engines (SEO), Answer Engines (AEO — Perplexity, ChatGPT Search, Google AI Overviews), and Generative/Coding Engines (GEO — llms.txt, Schema.org JSON-LD, 12-section READMEs, and 10-gate verification).
---

# SEO, AEO & GEO Discovery & Launch Engine (`seo-aeo-geo`)

Optimize any web product, SaaS landing page, documentation site, or GitHub repository for human conversion and 100% machine-readability across Google SEO, Answer Engines (Perplexity, ChatGPT Search, Google AI Overviews), and AI Coding Agents (`llms.txt`).

When NOT to use: organic short-form video distribution (`viral-distribution`), text social (`x-engagement` / `threads-engagement`), product positioning and specs (`product-discovery`), or interface design (`design-uiux`). This skill owns discoverability and machine readability, not the offer.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

---

## 1. Scope & Reference Routing

Load only the reference file matching the user's target surface:

| Target Surface | Primary Reference | CLI / Verification Script |
| :--- | :--- | :--- |
| **Web App, SaaS Landing Page, Docs Site, or Blog** | [web-seo-aeo-geo-playbook.md](references/web-seo-aeo-geo-playbook.md) | `scripts/scaffold-repo-pages.py` |
| **GitHub SEO / AEO / GEO 5-Gate Audit (`G1`–`G5`)** | [readme-seo-aeo-geo-harness.md](references/readme-seo-aeo-geo-harness.md) | `scripts/seo-aeo-geo-harness.py` |
| **12-Section Open-Source Repository `README.md` (`D1`–`D5`)** | [repository-readme-architecture.md](references/repository-readme-architecture.md) | `scripts/verify-repo-delivery.py` |
| **GitHub Personal or Organization Profile `README.md`** | [profile-readme-architecture.md](references/profile-readme-architecture.md) | `scripts/seo-aeo-geo-harness.py` |
| **Retina 2x Visual Assets, Light/Dark SVGs & `<2MB` GIFs** | [readme-visual-craft.md](references/readme-visual-craft.md) | `ffmpeg` two-pass palettegen |
| **GitHub Action Dynamic Auto-Updating Feeds** | [readme-dynamic-automation.md](references/readme-dynamic-automation.md) | `.github/workflows/` |
| **README Anti-Patterns & Conversion Killers** | [readme-anti-patterns.md](references/readme-anti-patterns.md) | Pre-delivery audit checklist |

---

## 2. The 3-Layer Machine Discovery Contract (Web & GitHub)

Every public web page, docs site, or repository must satisfy three distinct machine consumers without degrading minimalist human UX:

1. **SEO (Search Engine Optimization — Googlebot / Bingbot):**
   - Unique `<title>` (50–60 chars) and `<meta name="description">` (120–160 chars) using a clear Subject-Predicate-Object value proposition.
   - Canonical `<link rel="canonical">`, OpenGraph (`og:title`, `og:description`, `og:image`), Twitter `summary_large_image` card, valid `/sitemap.xml`, and zero `HTTP 404` internal/outbound links (`G1_LINKS_NO_404`).
   - For GitHub repos: populate repository `description`, `homepageUrl`, and `>= 3` semantic `repositoryTopics` (`G2_GITHUB_METADATA`).
2. **AEO (Answer Engine Optimization — Perplexity / ChatGPT Search / Google AI Overviews):**
   - Answer the primary query ("What is X?", "How does X compare to Y?", "When should you use X?") directly in the first 40–60 words using factual Subject-Predicate-Object prose.
   - Include a structured Markdown comparison table (`Dimension | Generic Alternative | Your Product`) and a `Schema.org` JSON-LD graph (`SoftwareApplication` / `Product` + `FAQPage`) on web pages ([web-seo-aeo-geo-playbook.md](references/web-seo-aeo-geo-playbook.md)).
   - On GitHub READMEs: include a collapsible `<details><summary>` AEO FAQ & Registry table at the footer with `>= 2` bold Q&A definitions (`**Question?**`) (`G4_AEO_FAQ_INDEX`).
3. **GEO (Generative Engine Optimization — `llms.txt` / Coding Agents / RAG):**
   - Publish `/llms.txt` at the domain or repository root following `llmstxt.org`: starts with `# Title`, `> 1–2 sentence entity definition`, categorized canonical links, and canonical Q&A (`G3_GEO_LLMS_TXT`).
   - Explicitly allow `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`, and `Google-Extended` in `robots.txt`.
   - Every non-badge `<img>` carries a descriptive `alt` attribute (`>= 25` characters) naming the system and capability (`G5_SEMANTIC_IMG_ALT`).

---

## 3. High-Converting 12-Section Repository README Standard (`D1`–`D5`)

When writing or upgrading a repository `README.md` ([repository-readme-architecture.md](references/repository-readme-architecture.md)), structure it for a 3-second human value hook and full agent installability:

1. **Top Fold:** `# Title`, 1-sentence bold hook, 2x Retina hero visual (`width="840"`), flat-square badge strip, and 6-anchor jump nav (`Quickstart · What it makes · Install · How it works · Commands · Limits`).
2. **Why This Exists:** Narrative problem statement + 5-row Before/After comparison table.
3. **Quickstart:** `1. Install` -> `2. Run / Ask in plain English` -> `3. Verify your setup`.
4. **What It Makes:** Visual specimen gallery with `<sub>Prompt / Command: ...</sub>` captions + deliverable matrix.
5. **Multi-Host Installation:** Copy-paste setup for the target runtimes/platforms + collapsible `<details><summary>Verify or uninstall</summary>`.
6. **Usage & Prompt / CLI Cookbook:** Concrete copy-paste recipes grouped by job.
7. **Commands & Diagnostics:** Reference table of CLI flags, scripts, and `/doctor` checks.
8. **How It Works + `### What loads when`:** Architecture flow and progressive context disclosure table.
9. **File Structure:** Annotated directory tree.
10. **Quality Bar & Limitations:** `### It's working if...` (observable pass criteria) and `### When not to use` (honest anti-scope boundaries).
11. **Ecosystem / Related Modules:** Cross-linked table of companion tools or packages.
12. **Contributing, Governance & License:** Links to `CONTRIBUTING.md`, `SECURITY.md`, `PRIVACY.md`, `CHANGELOG.md`, `llms.txt`, and `LICENSE`.

---

## 4. Deterministic Scaffolding & Verification Commands

### Audit SEO / AEO / GEO Gates (`G1`–`G5`)

```bash
python3 skills/seo-aeo-geo/scripts/seo-aeo-geo-harness.py \
  --target /path/to/repo <github-owner> \
  --check-links \
  --html-report ./seo-aeo-geo-scorecard.html
```

### Scaffold a 9-Tier Marketing & Docs Site (`index.html`, `llms.txt`, `sitemap.xml`, `robots.txt`, JSON-LD)

```bash
python3 skills/seo-aeo-geo/scripts/scaffold-repo-pages.py \
  --owner <owner> \
  --repo <repo> \
  --name "<Product Name>" \
  --tagline "<1-sentence proposition>" \
  --desc "<120-160 char meta description>" \
  --out-dir ./docs \
  --nojekyll
```

### Scaffold or Verify Full AI-Ready Repository Delivery (`D1`–`D5`)

```bash
python3 skills/seo-aeo-geo/scripts/scaffold-repo-delivery.py --repo-root /path/to/repo
python3 skills/seo-aeo-geo/scripts/verify-repo-delivery.py /path/to/repo
```

---

## 5. Pre-Delivery Gate Checklist

- [ ] Root `llms.txt` exists, starts with `# <Title>` and `> <Entity Definition>`, and is linked from `README.md` or site footer (`G3_GEO_LLMS_TXT`).
- [ ] Web pages include valid `<title>`, `<meta name="description">`, canonical URL, OpenGraph tags, `robots.txt`, `sitemap.xml`, and `Schema.org` JSON-LD (`SoftwareApplication`/`Product` + `FAQPage`).
- [ ] Every non-badge image has a descriptive `alt` attribute of at least 25 characters (`G5_SEMANTIC_IMG_ALT`).
- [ ] Comparison table (`Why this exists`) and honest boundaries (`It's working if...` / `When not to use`) are present.
- [ ] `seo-aeo-geo-harness.py` (and `verify-repo-delivery.py` when delivering an AI-ready repo) passes with exit code `0`.

---

> Adapts the [DESIGN:OS](https://github.com/jangtrinh) engines by Jang Trinh under the PolyForm Shield 1.0.0 license (<https://polyformproject.org/licenses/shield/1.0.0>).
> Required Notice: Copyright (c) 2026 Jang Trinh (https://github.com/jangtrinh)
> See [NOTICE](../../NOTICE.md).
