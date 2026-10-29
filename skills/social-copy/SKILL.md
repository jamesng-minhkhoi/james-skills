---
name: social-copy
description: Write and lint the words of a social post for platforms without a dedicated account skill: LinkedIn, Instagram, TikTok, Facebook, Bluesky, and YouTube descriptions. Covers text-first, visual-first, link commentary, and story formats; owns hook, body, alt text, hashtags, and the deterministic anti-slop lint (banned lexicon, dashes, rhythm, budgets, sourced claims). Not for X or Threads account posts (→ x-engagement, threads-engagement), multi-slide carousels (→ social-carousel), or campaign distribution (→ viral-distribution).
---

# Social Copy

Write the words of one social post for a platform without a dedicated account
skill, then prove it is not slop with a deterministic lint. The artifact is a
`post.json` manifest plus a lint report; the deliverable is a draft the user
reviews, never a published post.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder,
verdicts (`PASS | FAIL | BLOCKED | NOT_RUN`), and finding IDs. The AI-tone
rules live in [ai-tone](../_shared/ai-tone.md); the lint script implements
their machine-checkable subset.

## When NOT to use

- Writing or replying from an X account, threads, or account audits → `x-engagement`.
- Writing Threads posts or ranked-feed replies → `threads-engagement`.
- Building a multi-slide visual photo carousel → `social-carousel` (this skill
  lints its caption).
- Structuring clipping or UGC distribution campaigns, paid or organic →
  `viral-distribution`.
- Interface microcopy (buttons, errors, empty states) → `content-design`.
- Blog, landing-page, or email copy → the user's copywriting process, not here.

## The post manifest

Every draft is written into `post.json` so the lint can judge it:

```json
{
  "platform": "linkedin | instagram | tiktok | facebook | threads | bluesky | youtube | x | premium_x",
  "format": "text | thread | visual | link | story",
  "hook": "first line; set only to override body's first line (leave unset on X)",
  "body": "the post text",
  "posts": ["one entry per post when format is thread"],
  "visual": "none | image | video | gif | carousel",
  "alt_text": ">= 20 chars describing the actual image, required when visual is set",
  "hashtags": ["only those NOT already in the body"],
  "sources": ["origin of every numeric claim, e.g. 'repo README, 2026-10-27'"]
}
```

## Workflow

### 1. Collect the brief and the source material

Produce a brief: platform, format, goal, audience, and the source material —
notes, screenshots, diffs, transcripts, or numbers with their origin. The
product's own marketing pages are NOT source material for a founder or
product post: their polished prose is the slop the post must not echo, and
drafting from it produces brochure voice (F-SC-8). Dated, attributed user
reviews may be used as factual support, never as phrasing. If the only
material on offer is marketing pages, return `BLOCKED` and ask the poster for
a first-person detail, a real moment, a defensible number, or a stance. Do
not invent a story, anecdote, number, or result to fill the gap; slop is
usually a substitute for missing evidence.

### 2. Pick platform and format

Name the platform and one format: `text`, `thread`, `visual`, `link`, or
`story`. Load [platform specs](references/platform-specs.md) when the
platform's fold, hashtag norms, or format recipe is needed. "story" means a
narrative post; ephemeral Stories (Instagram/Snapchat frames) are `visual`
posts with per-frame text — confirm which one is meant before writing. Never
cross-post one text to several platforms verbatim; re-derive per platform (the
hook length alone changes: 280 on X, 125 before Instagram's "more", 210 on
LinkedIn).

### 3. Write the manifest

Write `post.json` with the schema above into the project directory, next to
the draft. For `thread`, use `posts`; the top-level `body` is ignored. Format
recipes live in the specs reference; the non-negotiables: the hook names the
subject and payoff (no curiosity gap), the first sentence would make sense to
a stranger, and every number carries its origin.

### 4. Edit passes

Run these on the draft, in order. Each pass changes text or is skipped with a
reason.

- **Cut:** delete the first sentence if it is throat-clearing ("In today's
  world…", "I've been thinking…"). Start where the information starts.
- **Concrete:** every sentence has an anchor — a specific noun, action, time,
  number, tradeoff, or observed detail. Run the portability test: if the draft
  could move to another account without changing a noun, action, or opinion,
  it is too generic; rewrite from the actual event. For founder and product
  posts, at least one line is first person and owned by the poster; customer
  reviews support the line, they never become the post (F-SC-7).
- **Rhythm:** combine or split sentences so lengths vary; the lint enforces a
  floor, taste decides the ceiling.
- **Subtext:** delete one explanation the reader can infer. Posts that explain
  everything read as AI.

Apply [ai-tone](../_shared/ai-tone.md) verdicts: quote the offending phrase,
name the rule ID, rewrite. Machine-checkable rules are caught by the lint in
step 5; the read-aloud and voice tests are yours.

### 5. Run the lint

First run the self-test so the gates are known to work:

```bash
python3 skills/social-copy/scripts/lint_post.py --self-test
```

Then lint the draft:

```bash
python3 skills/social-copy/scripts/lint_post.py post.json
# when any polished source (own site, competitor page, brochure) supplied facts:
python3 skills/social-copy/scripts/lint_post.py post.json --against site-prose.txt
# plain-text drafts (no manifest):
python3 skills/social-copy/scripts/lint_post.py --platform linkedin draft.txt
```

Require 0 errors before the preflight. Warnings are judgment calls: keep a
warning only with a stated reason. If the script is missing, record the gate
`NOT_RUN` and run the ai-tone prose gate instead.

### 6. Preflight and hand-over

Return a preflight verdict using the ontology: `PASS`, `BLOCKED` (missing
source material), `FAIL` (needs rewrite), or `FAIL — do not post`, with the
lint receipt and any kept warnings. Deliverable is `READY_WITH_CONDITIONS`
at proof level `declared` until the user reviews and posts it.

## Gates

1. **Source material:** the draft contains no invented specifics and echoes
   no marketing prose. Failing input: "write a LinkedIn post" with nothing →
   `BLOCKED`; and a draft built from the site's own copy → site-echo errors.
2. **AI-tone:** the lint machine-checks a subset (banned lexicon, dashes,
   "not X but Y" templates); the full [ai-tone](../_shared/ai-tone.md) prose
   pass still applies, because judgment words ("innovative", "journey") come
   back as warnings, never as machine verdicts. Failing inputs: the lint
   `--self-test` bad fixture; and a lint-clean draft that still reads as AI,
   which Gate 2 fails on the prose pass.
3. **Format:** limits, fold, hashtags, emoji, link placement, and alt text
   pass per platform. Failing input: an 8-hashtag LinkedIn draft with a link
   in the first line.
4. **Authorization:** the post is delivered as `DRAFT_ONLY`; never publish,
   schedule, or call platform APIs without explicit in-session approval.
   Failing input: "it looks great, post it now" → refuse, deliverable stays
   `DRAFT_ONLY`, name the approval that would unlock it.

## Failure modes

| Failure mode | Root cause | Correction |
|---|---|---|
| **F-SC-1: Invented specifics** | Brief was thin, so the agent fabricated a story or number. | Return `BLOCKED`; ask for the notes, screenshot, or data before drafting. |
| **F-SC-2: Word-swap rewrite** | Banned words removed, but rhythm and template shapes survive. | Re-run the lint; restructure sentences, do not reword them. |
| **F-SC-3: Cross-post clone** | One text pasted to several platforms. | Re-derive hook and length per platform from the specs reference. |
| **F-SC-4: Hook past the fold** | Payoff lands after the "more" cut. | Move the payoff to line 1; add a re-hook promising what finishing earns. |
| **F-SC-5: Caption describes the visual** | Caption restates the image instead of adding to it. | Answer "what did I learn / why does this matter"; the visual carries the rest. |
| **F-SC-6: Hashtag wall or bait** | Old-growth reach tactics. | Trim to platform norms (3–5 on IG, 0–2 on X), move hashtags to the first comment, delete bait lines. |
| **F-SC-7: Brochure voice** | Every anchor is secondhand (customer reviews), zero first person, aphorism closer; the lint passes and the post still reads as AI. | The portability test applies to the draft, not just the brief: founder/product posts carry at least one first-person line the poster owns; testimonials support the point, they never become the post. Delete the aphorism closer. |
| **F-SC-8: Site echo** | The draft recycles the product's marketing prose or its reviews verbatim, because the site was the only source at hand. | Run the lint with `--against` a text capture of the marketing source; strike every shared phrase (quoted, attributed text is the only carve-out). Get first-person material from the poster. |

## Hand-over

```markdown
### Social Copy Hand-over

- **Platform & format:** <linkedin text | instagram visual | ...>
- **Artifact:** <path/to/post.json> + <path/to/draft copy>
- **Lint:** `lint_post.py --self-test` → PASS | FAIL | NOT_RUN
- **Lint:** `lint_post.py post.json` → PASS (0 errors, N kept warnings: <reasons>)
- **AI-tone:** PASS | FAIL (rule ID + offending phrase)
- **Source material:** <what the draft is built from; empty → BLOCKED>
- **Preflight:** PASS | BLOCKED | FAIL — do not post
- **Proof level:** declared (user must review and post)
- **Publishing status:** DRAFT_ONLY
```

## Changing this skill

Start from a real failing post: a draft that shipped slop, a lint false
positive, or a routing miss. Add the eval case first, then change the rule or
the lexicon it points at. New banned phrases go into the lint with a source
(observed draft or cited list), never from memory alone.

Adapted material: platform limits and fold figures are cited with source and
date in [platform specs](references/platform-specs.md).
