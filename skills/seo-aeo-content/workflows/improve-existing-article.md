# Improve an existing article

Use this workflow after the daily check-in identifies a live page with a specific problem. Preserve what already works and make the smallest change that addresses the evidence.

## 1. Diagnose before editing

For the selected canonical URL, inspect:

- Search Console query and page data, if available;
- GA4 landing-page behavior and App Store CTA events;
- title, description, H1, opening answer, headings, date/updated date, and visible FAQs;
- canonical, hreflang, JSON-LD, sitemap inclusion, internal links, and HTTP status;
- factual freshness and authoritative sources for health, food safety, recalls, toxicology, travel, or regulatory claims.

Name one primary defect, such as `intent mismatch`, `weak opening answer`, `thin evidence`, `duplicate intent`, `poor internal path`, `missing CTA tracking`, or `indexability defect`. Do not use “traffic is low” as the diagnosis by itself.

## 2. Select the edit

- High reach and low engagement: revise the title/opening and answer the query immediately.
- Low reach and high engagement: improve specificity, internal links, related-post placement, and freshness signals.
- Good attention and no measured CTA clicks: first verify raw Markdown links and CTA instrumentation before changing the offer.
- Stale or unsupported claim: replace it with a cited, cautious explanation and a clear veterinarian boundary.
- Duplicate intent: strengthen the best canonical page and link to it; consolidate only when the replacement is clear.
- 404 or broken route: repair the route/link/sitemap, or use 301 only when a clear replacement exists. Keep removed content as a real 404/410 otherwise.

Avoid a full rewrite when the page has fewer than 10 sessions or 5 active users unless the defect is technical or safety-critical.

## 3. Edit to the Petio contract

Keep one clear H1, a direct first-paragraph answer, one `<QuickAnswer>`, question-shaped headings, useful internal links, visible FAQs that match FAQ schema, and a contextual Petio CTA. Use Petio as a workflow example, never as medical proof or a replacement for a veterinarian.

Set `updated` only for a material revision. Do not inflate dates, add filler for length, or add artificial “AI-friendly” wording. The same useful, original, people-first content should serve searchers and answer engines.

## 4. Verify and measure

Run lint/build and focused content checks. Fetch the built route and inspect metadata, alternates, JSON-LD, link targets, sitemap inclusion, and CTA event payload. Compare the page against its prior evidence, not against an arbitrary traffic target.

Schedule a 7-day implementation check for broken links and event firing, then a 28-day readout for reach, engagement, queries, and conversion. Mark results `unknown` when the sample is too small.
