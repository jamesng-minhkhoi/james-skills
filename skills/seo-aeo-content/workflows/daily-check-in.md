# Daily SEO/AEO check-in

Use this workflow when the request is “check SEO today,” “what should we improve,” or “review traffic and write the next blog.” The goal is one trustworthy decision, not a large batch of speculative edits.

## 1. Establish the evidence window

Read the Petio content contract, then record:

- date checked, property, site, locale, geography, and GA4/Search Console date ranges;
- GA4 sessions, active users, engagement, landing pages, and `app_store_click` events;
- Search Console impressions, clicks, CTR, position, queries, and indexing data when available;
- whether the public homepage, selected article, `robots.txt`, sitemap, RSS, and `llms.txt` are reachable.

Keep these signals separate:

- Search Console answers whether Google searchers saw or clicked a result;
- GA4 answers what visitors did after arriving;
- `chatgpt.com / ai-assistant` is a referral signal, not proof of answer-engine rankings;
- a crawl check proves technical behavior, not organic visibility.

If Search Console is unavailable, label rankings, impressions, CTR, and index coverage `unknown`. Never fill the gap with GA4 or a manual search.

## 2. Build a small performance matrix

For the top landing pages and any page under review, capture:

`URL | topic/intent | sessions | active users | engagement | app-store clicks | GSC evidence | indexability | confidence | decision`

Apply these guardrails:

- fewer than 10 sessions or 5 active users: `unknown`, inspect but do not rewrite solely from the sample;
- high reach and high engagement: preserve the intent match and improve the next step;
- high reach and low engagement: fix title, opening answer, or query match before adding length;
- low reach and high engagement: improve internal links, hub placement, title specificity, and discoverability;
- low reach and low engagement after a reasonable crawl window: check technical, duplicate, stale, or thin-content causes first;
- any 404 view: investigate the path, internal link, sitemap, canonical, or redirect before judging the article.

## 3. Choose one action

Prioritize in this order:

1. technical/indexability blocker;
2. existing article with meaningful reach and a clear conversion or answer gap;
3. existing article with strong engagement but weak reach;
4. new article for a distinct, evidence-supported search job.

If no page meets the threshold and no technical defect is present, make no content rewrite. Document the observation and wait for more data.

## 4. Verify the action

After the change, run the repository checks and fetch the affected route. Confirm:

- HTTP 200 for the intended page and a real 404 for an invalid slug;
- one canonical URL and valid locale alternates;
- visible H1, direct answer, FAQ only where visible, and matching JSON-LD;
- internal links resolve and sitemap/RSS/`llms.txt` remain aligned;
- App Store links fire `app_store_click` with `page_path`, `placement`, `article_slug`, and `locale`.

Do not change GA4 key-event settings, submit indexing requests, or alter external dashboards as part of this routine unless the user explicitly authorizes it.

## Daily handoff

Record this compact result in the project’s existing log or plan location:

```text
Date and window:
Evidence available:
Top finding:
Decision: fix technical | improve existing | write new | wait
Changed:
Validation:
Unknowns:
Next check: 7-day implementation check, 28-day content readout
```
