# Platform specs

Per-platform limits, folds, and format recipes for social posts. Load when
step 2 or step 3 of the workflow needs numbers. Every claim carries source,
date, and status per the ontology claim rule; figures compiled from multiple
sources are `attributed`, and the lint's constants are the enforcement copy.

## Limits and folds

| Platform | Post/caption limit | Fold ("more" cut) | Hashtags rec/max | Emoji max |
|---|---|---|---|---|
| X (free) | 280 | no fold (280) | 1 / 2 | 2 |
| X (Premium) | 25,000 | ~280 | 1 / 2 | 2 |
| LinkedIn | 3,000 | ~210 desktop / ~140 mobile | 3 / 5 | 2 |
| Instagram | 2,200 | ~125 | 5 / 30 | 6 |
| TikTok | 4,000 | ~150 | 3 / 10 | 4 |
| Facebook | 63,206 | ~477 | 3 / 5 | 4 |
| Threads | 500 | 500 (no fold) | 3 / 10 | 2 |
| Bluesky | 300 | 300 (no fold) | 1 / 3 | 3 |
| YouTube description | 5,000 | ~157 | 3 / 15 | 2 |

- Source: SocialSwiss character-limit table, 2026 (https://www.socialswiss.tech/guides/social-media-character-limits) — `attributed`.
- Source: Buffer character-limit article (https://support.buffer.com/en-us/articles/character-limits-for-each-social-network-mNDqsEV9Nf) — `attributed`.
- On X every URL counts as 23 characters (t.co) and every emoji as 2. The lint applies this weighting on all platforms as a conservative rule.

## Why the fold decides the post

- LinkedIn: ~210 chars on desktop, ~140 on mobile before "see more". AuthoredUp's
  study of 372,126 personal-profile posts (Sept 2025–Feb 2026, reported by
  LigoSocial, 2025/2026) frames the post as Trailer → Meat → Summary: the
  trailer earns the "see more" click, the re-hook after line 1 promises what
  finishing earns, and the close invites a comment rather than a click. `attributed`.
- Instagram: ~125 chars visible before "more" on mobile; the hook does
  headline work. TypeCount, 2026 (https://typecount.com/blog/instagram-caption-character-limit). `attributed`.
- LinkedIn has no banned-word list; its classifier marks *slop* (recycled,
  generic ideas) and reported views of flagged content down ~40% after the
  "seems like AI slop" feedback option, 2026 (Commentify blog,
  https://blog.commentify.co/linkedin-banned-words/). The unit of judgment is
  the idea, not the wording — which is why Gate 1 is source material, not
  vocabulary. `attributed`.

## Hashtags in 2026

Instagram now recommends 3–5 and reads captions, on-screen text, and
interaction signals instead of relying on tags (First Ascent, 2026,
https://firstascentdesign.com/hashtag-strategy-2026). X rewards 0–2; walls of
hashtags on any platform read as spam and as slop. Default: no hashtag line in
the body; put a few in the first comment when the platform indexes them there. `attributed`.

## Format recipes

**text** — hook names subject + payoff within the fold; re-hook line promises
what finishing earns; body carries one idea; close with an invitation to
comment on a specific tension, not "Agree?".

**thread** — first post is standalone and complete within the fold (the rest
of the thread is depth, not the setup); each post makes sense alone; last post
invites the specific conversation.

**visual** (caption + image/video) — the visual carries the information; the
caption must not describe it. Caption answers "what did I learn / why does
this matter", hook lands in the first 125 (IG) or 150 (TikTok) chars, on-screen
text stays brief, and alt text describes the actual image (accessibility plus
a second indexing surface).

**link** — the commentary carries the value: one line naming what it is, one
specific takeaway you verified by reading it. Link below the fold on LinkedIn;
never a bare link with "thoughts?".

**story** — a narrative post (not ephemeral Stories frames; those are
`visual` posts with per-frame text): a concrete scene with a real decision and
outcome, built only from the source material. No invented dialogue, no
"journey" vocabulary, no "lessons learned" list of three. End before the
moral, not after it.

## Evidence base for the lint rules

- Antislop (arXiv 2510.15061, Oct 2025, ICLR 2026): some LLM phrases appear
  1,000×+ more often than in human text; pattern suppression preserves quality. `verified` (peer-reviewed).
- Huy Tieu's audit of 600 Reddit posts on spotting AI writing (Sept 2026,
  https://huytieu.com/blog/ai-slop-after-the-em-dash): ranked tells — em dash
  7.1%, uniform sentence rhythm 4.0%, "not just X, it's Y" 2.8%, five-paragraph
  essay shape and sycophancy 2.5%, "delve" 1.3%. Rhythm and shapes outrank
  vocabulary. `attributed`.
- Algorithmic Bridge, "10 Signs of AI Writing" (Dec 2025): surface tells
  migrate; the deeper ones are the abstraction trap (nothing concrete to
  picture), equivocation seesaw, treadmill effect (no thesis advancement),
  length over substance, and the subtext vacuum. These live in the edit
  passes, not the lint. `attributed`.
