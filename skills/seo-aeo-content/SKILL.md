---
name: seo-aeo-content
description: Audit and improve Petio website SEO and answer-engine visibility. Use when analyzing petiogo.com performance, indexing, structured data, llms.txt, sitemap coverage, blog intent, GA4/Search Console evidence, or when creating and revising English pet-care content in petio-landingpage.
---

# Petio SEO/AEO

Use this skill for an evidence-led search-content loop: audit, prioritize, implement, verify, and record what changed. It is designed for Petio's Next.js landing page and MDX blog, but the evidence rules generalize to similar content sites.

## Workflow

1. Establish scope and evidence before changing content.
   - Record the property, date range, geography, language, and the exact GA4/Search Console reports available.
   - Prefer Search Console for impressions, queries, CTR, position, and indexing. Use GA4 for sessions, engagement, landing pages, and conversion events.
   - If a report or property is inaccessible, say so and do not infer rankings, impressions, or conversions from crawl results.
   - Inspect the public homepage, representative article, `robots.txt`, XML sitemap, `llms.txt`, canonical URLs, hreflang, page titles, descriptions, Open Graph, and JSON-LD.

2. Build a performance matrix.
   - For each URL, capture topic, intent, date, sessions, active users, engagement time, conversions, indexability, and confidence.
   - Separate established winners, promising high-engagement pages with low reach, weak pages, and new pages without enough data.
   - Diagnose the mechanism, not just the number: intent mismatch, generic comparison copy, weak internal links, poor snippet answer, thin coverage, stale date, missing source, or missing CTA instrumentation.

### Small-sample decision rules

Use these as working guardrails for a small site, not universal SEO laws:

- Fewer than 10 sessions or 5 active users for a page: label performance `unknown`; inspect quality and indexability, but avoid a full rewrite based on one or two visits.
- High reach plus high engagement: preserve the search-intent match, then improve conversion with a visible contextual CTA, stronger next-step links, and fresh evidence.
- High reach plus low engagement: inspect the title, first answer, opening screen, and query-to-page match before adding more words.
- Low reach plus high engagement: improve internal links, hub-page placement, title specificity, and answer-engine discoverability before changing the core article.
- Low reach plus low engagement after a reasonable crawl window: check for 404s, canonical or hreflang errors, stale claims, duplicate intent, and thin coverage; then consolidate or rewrite only if the evidence supports it.
- Any 404 page view is an immediate technical issue. Find the referring URL or broken path and fix the route, redirect, sitemap, or internal link before judging content quality.

### Conversion and answer-engine signals

- Treat `google / organic`, `bing / organic`, and `chatgpt.com / ai-assistant` as separate acquisition signals. Do not collapse AI referrals into Google SEO or infer answer-engine visibility from organic sessions.
- Measure both dedicated CTA components and raw MDX App Store links. Content authors can add a direct App Store URL inside Markdown, so the renderer must track those links too.
- Review `app_store_click` by `article_slug`, `placement`, `locale`, and `page_path`. A page with attention but zero measured CTA clicks may have a tracking gap rather than a conversion problem.
- Use a 7-day implementation check, then a 28-day content readout. Keep Search Console query and index data separate from GA4 behavior data.

3. Choose content gaps with a job-to-be-done.
   - Prefer one primary query and one audience per article.
   - Prioritize clusters around proven Petio capabilities: food-label safety, pet records, multi-pet care, medication/vaccine tracking, vet-visit preparation, and careful AI-assisted questions.
   - Avoid near-duplicates and do not create a new page when a focused update or canonical consolidation is the better fix.

4. Write for searchers and answer engines.
   - Start with a direct answer in the first paragraph and a `<QuickAnswer>` block.
   - Use one clear H1, descriptive H2/H3 questions, concise definitions, checklists, tables when comparison helps, and a short “when to call a veterinarian” boundary.
   - Add 3 to 5 useful FAQs only when the article visibly answers them. Never add FAQ schema for hidden or unrelated copy.
   - Cite first-party veterinary, government, regulator, or standards sources for medical, food-safety, toxicology, regulatory, or travel claims.
   - Use Petio as a relevant workflow example, not as proof of medical efficacy. Never diagnose, prescribe, invent testimonials, or imply an app replaces a veterinarian.
   - Add 3 to 8 contextual internal links to existing canonical pages. Avoid repetitive exact-match anchors.
   - Every post needs accurate frontmatter: unique title, useful description, date, optional updated date, author, image, tags, locale, and FAQ entries.
   - Treat answer-engine optimization as a consequence of clear, original, trustworthy content and crawlable pages. Do not add filler sections, artificial "AI-friendly" phrasing, or files such as `llms.txt` as a substitute for useful content and standard SEO. Follow [Google's generative-AI search guidance](https://developers.google.cn/search/docs/fundamentals/ai-optimization-guide?hl=en), which prioritizes unique, people-first content and effective SEO over AEO/GEO hacks.

5. Fix technical discoverability in the same iteration.
   - Keep English canonical URLs at `/blog/...` and Vietnamese URLs at `/vi/blog/...`; make hreflang and `x-default` explicit.
   - Keep `robots.txt`, sitemap, RSS, and `llms.txt` aligned with actual canonical pages. New articles must appear in sitemap and the answer-engine index file.
   - Keep `BlogPosting`, `BreadcrumbList`, `Blog`, `WebSite`, `Organization`, `SoftwareApplication`, and visible FAQ content consistent. Do not add unsupported claims to schema.
   - Instrument meaningful CTA events such as `app_store_click` with page, locale, placement, and article slug. Mark the event as a key event in GA4 only after verifying it fires.

6. Verify and iterate.
   - Run the repository's lint, typecheck/build, and content/frontmatter checks.
   - Fetch the built or deployed routes and confirm 200 status, canonical, hreflang, JSON-LD, sitemap inclusion, RSS inclusion, and `llms.txt` inclusion.
   - Recheck the highest-risk article for unsupported health claims, broken links, duplicate intent, and missing CTA tracking.
   - Record the change, evidence, remaining unknowns, and the next measurement window. Do not claim SEO impact before Search Console or GA4 data exists after publication.
   - Use [Google's crawling-error guidance](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors) for observed 404s: preserve a real 404 or 410 for removed URLs, use a 301 only when a clear replacement exists, remove broken internal links, and do not treat a custom 404 page as an indexable content page.

## Petio references

Read [petio-content-contract.md](references/petio-content-contract.md) before editing Petio MDX or creating a new post. It contains the frontmatter shape, content safety boundary, link strategy, and measurement fields used by this site.

## Stop conditions

- Stop and report an evidence gap when Search Console is unavailable instead of guessing rankings or indexing coverage.
- Stop before making external dashboard changes, submitting indexing requests, or changing GA4 key-event settings unless the user explicitly authorizes that operation.
- Stop and ask for source review when a claim could materially affect a pet's health or safety and no authoritative source is available.
