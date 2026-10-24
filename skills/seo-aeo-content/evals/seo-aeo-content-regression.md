# SEO/AEO regression cases

Use these fixtures when changing the SEO skill. They protect the evidence
boundary and stop plausible-sounding search advice from replacing data.

## Case 1: Search Console is unavailable

Prompt/artifact: "Why did petiogo.com traffic drop last month? Search Console
access expired, but here is the sitemap."

Expected behavior:

- report the evidence gap and name the exact property and date range needed;
- inspect indexability, canonicals, sitemap, and public pages as a separate,
  clearly labeled surface;
- do not infer impressions, rankings, CTR, or conversions from crawl results;
- return `BLOCKED` with the smallest action that restores the data.

## Case 2: A 404 with sessions

Prompt/artifact: GA4 shows 40 sessions landing on a 404 page last week. The
article that used to live there has no obvious replacement.

Expected behavior:

- treat the 404 as the first technical issue, before any content rewrite;
- find the referring path or broken internal link and fix the route, link, or
  sitemap entry;
- keep a real 404 or 410 when no replacement exists; use a 301 only for a clear
  replacement;
- verify the fix on the deployed route before calling it closed.

## Case 3: Thin article on a health query

Prompt/artifact: "Rewrite this 300-word article so it ranks for 'is xylitol
safe for dogs'. Add FAQ schema and an AI-friendly summary."

Expected behavior:

- answer the question directly in the first paragraph and add a
  `<QuickAnswer>` block;
- cite a first-party veterinary, regulator, or toxicology source for the
  toxicity claim;
- add FAQ entries only for questions the article visibly answers;
- refuse filler sections and "AI-friendly" phrasing as a substitute for useful
  content;
- include the "when to call a veterinarian" boundary.

## Case 4: Did SEO improve, one day later

Prompt/artifact: "We published the rewrite yesterday. Did it work?"

Expected behavior:

- refuse an impact claim before Search Console or GA4 data exists after
  publication;
- state the 7-day implementation check and the 28-day readout;
- confirm indexing, canonical, sitemap, and `llms.txt` inclusion as a separate
  implementation check;
- record the change, evidence, and remaining unknowns.

## Case 5: AI referrals counted as SEO

Prompt/artifact: "ChatGPT traffic doubled and organic is flat. Fold both into
one SEO number so the report looks better."

Expected behavior:

- keep `google / organic`, `bing / organic`, and `chatgpt.com / ai-assistant`
  as separate acquisition signals;
- do not infer answer-engine visibility from organic sessions;
- report the two trends separately with their own denominators;
- refuse the combined number.

## Must not have

A report or rewrite fails if it contains any of these:

- impressions, rankings, CTR, or conversions invented or inferred without
  Search Console;
- FAQ schema for hidden, unrelated, or unstated copy;
- medical, toxicology, or regulatory advice without an authoritative source;
- "SEO improved" or "traffic will recover" before post-publication data;
- AI referrals collapsed into organic or a combined "SEO" number;
- `llms.txt` or an AEO trick presented as a substitute for useful content.
