# Petio content contract

## MDX frontmatter

```yaml
title: "A specific search-intent title"
description: "A concise, accurate snippet description"
date: "YYYY-MM-DD"
updated: "YYYY-MM-DD" # only when materially revised
author: "James Nguyen"
image: "https://..."
tags: ["Health", "Guide"]
locale: "en"
faq:
  - question: "A question the page visibly answers"
    answer: "A concise answer that does not diagnose or prescribe"
```

Use `locale: "en"` for English posts. Vietnamese posts belong under the existing Vietnamese content convention. Do not change the repository's folder structure to add a second content system.

## Page shape

1. A direct answer in the opening paragraph.
2. One `<QuickAnswer question="..." answer="..." />` block.
3. A short, scannable body with question-shaped headings.
4. Evidence links near claims that need authority.
5. A visible boundary for urgent symptoms, poisoning, medication, or diagnosis.
6. Contextual links to Petio's food checker, records, relevant guides, and the App Store only where useful.
7. A short Petio CTA that explains the relevant workflow without promising clinical outcomes.

## Measurement contract

Track `app_store_click` with:

```js
gtag("event", "app_store_click", {
  page_path: window.location.pathname,
  placement: "article_cta",
  article_slug: "...",
  locale: "en",
});
```

Use `page_path`, `placement`, `article_slug`, and `locale` as dimensions. Measure article sessions and engagement separately from app-store clicks. A page with no Search Console data is not a failed page; label it `unknown` until it has had a reasonable crawl and measurement window.

For MDX articles, track raw App Store links in the shared article-link renderer as well as explicit CTA components. Otherwise the highest-intent paragraph in an article can send a reader to the store without producing an `app_store_click` event.

For small traffic samples, use a practical threshold of fewer than 10 sessions or 5 active users as `unknown`. Prioritize pages with a meaningful combination of reach and engagement, and fix any observed 404 page view before rewriting content.

## Health and safety boundary

Petio supports preparation, tracking, label review, and better questions for a veterinarian. It does not diagnose, prescribe, rule out emergencies, guarantee food safety for an individual pet, or replace veterinary care. For toxic ingestion, repeated vomiting, breathing trouble, collapse, suspected obstruction, or another urgent concern, direct the reader to immediate veterinary or poison-control help.
