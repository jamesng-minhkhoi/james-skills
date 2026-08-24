# X content audit schema

Use this schema when running a performance audit across original posts,
replies, quote posts, and reposts. It is designed for CSV or JSON exports and
for manually captured public snapshots. Do not invent values that are not
visible or sourced.

## Contents

- [Sampling contract](#sampling-contract)
- [Required fields](#required-fields)
- [Content and media coding](#content-and-media-coding)
- [Outcome fields](#outcome-fields)
- [Confidence and source rules](#confidence-and-source-rules)
- [Report interpretation](#report-interpretation)

## Sampling contract

For one account, aim for:

- 10 apparent winners, 10 ordinary posts, and 10 weak or distraction
  candidates;
- 15 replies and 15 reposts/quote posts when the account has enough activity;
- a comparable time window, with older evergreen posts kept in a separate
  cohort;
- original posts, replies, quote posts, and reposts analyzed separately;
- public engagement counts separated from private analytics and downstream
  product events.

If a smaller sample is unavoidable, report the sample size and downgrade the
confidence. Never use one viral post as the account formula.

## Required fields

The report script accepts these column names. Blank optional values remain blank
and are excluded from rate calculations.

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | yes | Post URL or stable identifier |
| `date` | yes | Timestamp or date captured |
| `format` | yes | `original`, `reply`, `quote`, or `repost` |
| `text` | no | Text or a short transcription |
| `topic` | yes | Primary topic cluster |
| `classification` | yes | `winner`, `ordinary`, `weak`, or `distraction` |
| `media_type` | no | `none`, `image`, `video`, `gif`, `chart`, `screenshot`, `carousel`, or `unknown` |
| `media_role` | no | `proof`, `demo`, `explanation`, `emotion`, `status`, `humor`, `decoration`, or `unknown` |
| `hashtag_use` | no | `none`, `branded`, `topical`, `campaign`, or `irrelevant` |
| `mention_type` | no | `none`, `peer`, `large_account`, `product`, or `community` |
| `audience_job` | no | `learn`, `laugh`, `compare`, `discover`, `participate`, `trust`, or `unknown` |
| `evidence_status` | no | `measured`, `estimated`, `projected`, `anecdotal`, or `unknown` |
| `experiment_surface` | no | `product`, `seo`, `social_video`, `paid_ads`, `app_store`, `personal`, or `none` |

## Content and media coding

### Hook and topic

Capture the dominant hook tension in notes even if the script does not score it:

- surprising result or novelty;
- time saved or money made;
- identity or status challenge;
- frustration or failure;
- curiosity or open question;
- personal stake or aspiration;
- humor or controversy.

Use one primary topic per row. If a post mixes MRR, family life, an app launch,
and social views, choose the stated main job and note `mixed_variables` in the
free-text notes field.

### Media inspection

Inspect the actual media when possible, not just the platform's media flag.
Record:

- whether the first frame communicates the claim without the caption;
- whether the asset proves, explains, humanizes, signals status, creates humor,
  or merely decorates;
- screenshot readability and whether sensitive data is visible;
- before/after or sequence structure;
- visual novelty, emotional salience, and product visibility;
- whether the media and copy create complementary curiosity or redundant text.

If a mirror exposes only `Download Image`, `Download Gif`, or `Download Video`,
record the media type as `unknown` until the actual asset is inspected.

### Replies and reposts

For replies, record whether the creator answers, extends, questions,
disagrees, jokes, thanks, or promotes. A one-word acknowledgement is not the
same as a useful reply.

For reposts and quote posts, record whether the action is:

- endorsement or signal boosting;
- useful commentary or disagreement;
- community support;
- product discovery or launch amplification;
- humor, lifestyle, or unrelated reach seeking.

Do not treat a creator's reposted content as evidence of the creator's own
product expertise unless the quote adds a clearly owned observation.

## Outcome fields

Use numeric fields when sourced:

| Field | Meaning |
| --- | --- |
| `impressions` | Views/impressions for the post |
| `likes` | Likes |
| `replies` | Replies received |
| `reposts` | Reposts/retweets |
| `quotes` | Quote posts |
| `bookmarks` | Bookmarks |
| `profile_visits` | Profile visits attributed to the post |
| `link_clicks` | Attributed link clicks |
| `qualified_replies` | Replies matching the intended audience or job |
| `conversions` | Signups, installs, activations, or another named outcome |

Calculate only when denominators match:

```text
engagement rate = (likes + replies + reposts + quotes + bookmarks) / impressions
qualified response rate = (qualified replies + link clicks) / impressions
conversion rate = conversions / link clicks
```

Do not combine clicks from SEO, social, paid ads, and app-store sources unless
their attribution window and denominator are explicitly compatible.

## Confidence and source rules

Use `source_confidence` values:

- `first_party`: account analytics, platform export, or creator-owned report;
- `primary_public`: public X post metrics or a directly inspectable asset;
- `secondary_snapshot`: mirror or analytics site with a crawl date;
- `inference`: interpretation not directly measured.

Record `captured_at`, `source_url`, and `notes` when possible. Treat public
counts as time-bound. If impressions are absent, call normalized rates
`confounded`; follower count is only a rough denominator.

## Report interpretation

The report must distinguish:

- high attention, low qualified response;
- high conversation, low conversion;
- low reach, high conversion signal;
- trust/credibility content;
- distraction candidate;
- insufficient or confounded evidence.

Report a repeated driver only when it appears across multiple comparable posts,
not because it appears in the single highest-reach item. End with one or two
controlled tests that change one major variable at a time.
