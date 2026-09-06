# Write a new Petio article

Use this workflow only when the content inventory and performance matrix show a distinct search job that an existing page should not own.

## 1. Prove the gap

Inspect the existing `content/blog` slugs, titles, tags, internal links, and overlapping intent. Define:

```text
Primary query/job:
Audience:
Why the current site does not answer it:
Closest existing pages:
Canonical slug:
Conversion path:
```

Do not create a near-duplicate to chase a keyword, a trend, or presumed ChatGPT traffic. Prefer a practical job around food-label safety, pet records, multi-pet care, reminders, vet-visit preparation, or careful AI-assisted questions when it fits the product.

## 2. Research the answer

Research current, authoritative sources for any claim that could affect a pet’s health or safety. Use first-party veterinary, government, regulator, standards, or manufacturer sources near the relevant claim. Separate confirmed facts, cautious product guidance, and unknowns.

Outline the article before drafting:

1. direct answer in the opening paragraph;
2. `<QuickAnswer>` with the same answer in concise form;
3. scannable question-shaped sections;
4. checklist/table only when it improves the decision;
5. “when to call a veterinarian” boundary when relevant;
6. 3 to 8 contextual internal links;
7. one relevant Petio CTA, without unsupported efficacy claims.

## 3. Draft the MDX

Follow `petio-content-contract.md` exactly:

- English content uses `locale: "en"` and the existing `content/blog` structure;
- title and description are specific, accurate, and unique;
- date reflects publication; `updated` is only for later material revisions;
- FAQ entries are visible and directly answered;
- App Store links and CTA components use the shared tracking path;
- no diagnosis, prescription, invented testimonial, guaranteed outcome, or implication that Petio replaces a veterinarian.

Use natural language. Avoid keyword stuffing, generic comparison lists, unsupported “best” claims, and sections written only to satisfy an answer-engine format.

## 4. Verify before calling it ready

Run lint/build and the content checks. Fetch the new route and verify HTTP 200, one canonical, locale alternates, Open Graph, BlogPosting/Breadcrumb/FAQ JSON-LD, sitemap/RSS/`llms.txt` inclusion, working internal links, and the App Store event payload.

Record the target query/job, sources, files changed, checks passed, and the 7-day and 28-day measurement dates. Publication does not prove indexing or ranking; those remain unknown until Search Console evidence exists.
