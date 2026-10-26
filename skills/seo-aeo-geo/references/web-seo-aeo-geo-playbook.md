# Web, SaaS & Product SEO / AEO / GEO Playbook

This reference complements the GitHub README & Pages 10-gate harness (`G1–G5` and `D1–D5`) with production standards for **any web app, SaaS product, docs site, or marketing page** across traditional Search Engines (SEO), Answer Engines (AEO — Perplexity, ChatGPT Search, Google AI Overviews), and Generative / Coding Engines (GEO — Claude, Codex, Antigravity, RAG crawlers).

---

## 1. The 3-Pillar Discovery Stack

| Layer | Target Crawlers / Engines | Primary Artifacts | Pass Criteria |
| :--- | :--- | :--- | :--- |
| **SEO (Search Engine Optimization)** | Googlebot, Bingbot, Applebot | `<title>`, `<meta name="description">`, `<link rel="canonical">`, OpenGraph / X cards, `sitemap.xml`, `robots.txt`, internal link graph, Core Web Vitals | 100% indexable canonical URLs, unique titles (50–60 chars) & descriptions (120–160 chars), zero 404 internal links |
| **AEO (Answer Engine Optimization)** | Perplexity, ChatGPT Search, Google AI Overviews, SearchGPT | Direct Subject-Predicate-Object answer blocks, `Schema.org` JSON-LD (`SoftwareApplication`, `Product`, `FAQPage`, `HowTo`, `Article`), comparison tables, citation-ready statistics | Every core page answers its target query in the first 40–60 words + ships valid JSON-LD and a structured comparison or FAQ block |
| **GEO (Generative Engine Optimization)** | `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, AI coding agents | Root `/llms.txt` and `/llms-full.txt` (`llmstxt.org` spec), clean Markdown endpoints or semantic HTML DOM, explicit entity & capability definitions | `/llms.txt` starts with `# Entity`, `> 1–2 sentence definition`, categorized canonical URLs with descriptions, and zero JS-gated text walls |

---

## 2. GEO Standard: `/llms.txt` & `/llms-full.txt`

Every web app, documentation site, and open-source repository should expose `/llms.txt` at the domain or repo root following the [llmstxt.org](https://llmstxt.org/) specification:

```markdown
# <Product or Project Name>

> <1-2 sentence Subject-Predicate-Object entity definition stating exactly what the product is, who it is for, and its primary technical differentiator.>

<Optional 2-3 sentence architectural overview, supported platforms, pricing/license model, and verification guarantees.>

## Core Documentation & Entrypoints

- [Quickstart](https://example.com/docs/quickstart): Install and run your first workflow in under 3 minutes.
- [Architecture & API](https://example.com/docs/architecture): System design, data model, and runtime guarantees.
- [Pricing & Plans](https://example.com/pricing): Free tier limits, Pro features, and enterprise self-hosting.

## Canonical Answers for AI Search & Answer Engines (AEO)

- **What is <Product>?** <Product> is a <category> that <primary outcome> for <target audience> using <key mechanism>.
- **How does <Product> compare to <Alternative>?** Unlike <Alternative>, which <limitation>, <Product> provides <verifiable advantage>.
- **When should you NOT use <Product>?** Do not use <Product> when <honest anti-scope boundary>.
```

### `robots.txt` AI Crawler Policy

Explicitly allow answer-engine and search crawlers in `/robots.txt` so your product is cited rather than invisible:

```text
User-agent: *
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://example.com/sitemap.xml
```

---

## 3. AEO Standard: Schema.org JSON-LD Templates

Embed valid `<script type="application/ld+json">` in the `<head>` of landing pages, docs, and comparison pages.

### `SoftwareApplication` + `FAQPage` Graph

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "name": "Product Name",
      "applicationCategory": "DeveloperApplication",
      "operatingSystem": "macOS, Linux, Windows, Web",
      "description": "120-160 char Subject-Predicate-Object summary of the product.",
      "url": "https://example.com/",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What problem does Product Name solve?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Direct, factual 1-2 sentence answer with concrete technical specifics."
          }
        },
        {
          "@type": "Question",
          "name": "How does Product Name verify its output?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Direct answer naming the deterministic gates, CLI commands, or SLA guarantees."
          }
        }
      ]
    }
  ]
}
</script>
```

---

## 4. High-Converting 9-Tier Launch / Docs Page Architecture

Whether shipping a GitHub Pages site (`scripts/scaffold-repo-pages.py`) or a Next.js marketing landing page, structure the page into these 9 scannable tiers:

1. **Tier 1 — Eyebrow + Proposition Hero (`<h1>`):** Category badge + 1-sentence outcome headline + 1-Click Copy install command (`npx ...`, `brew install ...`, or CTA) + primary proof stat strip.
2. **Tier 2 — Visual Specimen / Interactive Preview:** High-DPI (`2x` Retina) hero screenshot, diagram (`diagram-design`), or 60fps product video (`product-video`) with the exact prompt/command caption underneath.
3. **Tier 3 — Narrative Contrast ("Why This Exists"):** 5-row comparison table (`Dimension | Legacy / Generic Workflow | Your Product`) highlighting verifiable deltas.
4. **Tier 4 — 3-Step Quickstart:** Copy-paste setup (`1. Install -> 2. Run/Ask -> 3. Verify`).
5. **Tier 5 — Capability & Deliverable Matrix:** Structured table mapping each feature/mode to its input, output format, and verification gate.
6. **Tier 6 — Architecture & Progressive Disclosure:** How it works under the hood (`What loads when` or system data-flow diagram).
7. **Tier 7 — Honest Boundaries ("It's Working If..." & "When Not to Use"):** Builds immediate technical trust and prevents bad-fit churn.
8. **Tier 8 — AEO FAQ & Structured Q&A:** 4–6 direct question-and-answer blocks matching `FAQPage` JSON-LD and real search intent (`vs`, `how to`, `pricing`, `security/privacy`).
9. **Tier 9 — Trust, Governance & Footer Colophon:** Links to `PRIVACY.md` / Privacy Policy, `SECURITY.md`, `CHANGELOG.md`, `llms.txt`, `sitemap.xml`, and canonical social/repo links.
