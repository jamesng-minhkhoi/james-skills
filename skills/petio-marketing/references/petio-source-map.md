# Petio marketing source map

Use this map to load the live source of truth. Do not copy an old plan into the
skill and assume it is still current.

## Required reading order

1. `petio-content/index.md`
2. `petio-content/CLAUDE.md`
3. `petio-content/voice/claims-and-safety.md`
4. `petio-content/proof/proof-ledger.md`
5. `petio-content/voice/brand-voice.md`
6. `petio-content/voice/platform-tone.md`
7. The relevant audience, platform, engine, research, and plan files below.

## Product truth

Petio is an English-first AI pet-health companion for North American and
European owners. The product's defensible story is continuity around one
specific pet, not “the only scanner” or “an AI vet.” Verified capability rows
include:

- Peti answers filtered through a specific pet profile;
- food barcode/photo analysis considered against that pet's profile;
- photo OCR fallback for ingredient panels;
- pet-specific ingredient warnings framed as flags for review;
- structured/streamed answers;
- remembered recent scans;
- separate multi-pet profiles and reminders;
- weight/vitals tracking;
- vaccine, medication, and vet-visit reminders;
- document storage with text recognition;
- family sharing and a memories timeline.

Use `proof/proof-ledger.md` for the current exact wording and status. Do not
publish the historical “no generic food-rating app can do this” comparison
without resolving the correction recorded in `index.md`; continuity is the safer
position.

## Voice and safety

Load:

- `voice/brand-voice.md` for tone, banned words, banned patterns, and formatting;
- `voice/platform-tone.md` for platform-specific adaptation;
- `voice/claims-and-safety.md` for the blocking health boundary;
- `proof/proof-ledger.md` for product capability and traction evidence.

Petio sounds calm, specific, warm, honest about limits, and useful in short
mobile-readable sentences. It does not diagnose, reassure medically, replace a
vet, invent a user story, or use fear as a lever. The safe transformation is
verdict → preparation: notice, track, flag for review, and bring a clearer
question to a veterinarian.

## Audience and engine

Choose exactly one audience node:

- `audience/new-pet-parents.md` — high anxiety and high question volume;
- `audience/senior-pet-owners.md` — record continuity and willingness to pay;
- `audience/multi-pet-households.md` — separate pets, food context, and reminders.

Load the relevant files from:

- `engine/hooks.md` — hook formulas and performance log;
- `engine/repurpose.md` — video-first, platform-native adaptation;
- `engine/scheduling.md` — cadence, target-market time windows, and timezone
  warnings;
- `engine/content-types.md` — native format definitions;
- `radar/hot-questions.md`, `radar/audience-pains.md`, and
  `radar/sources.md` — current demand language and external sources;
- `plans/` and `plans/EXECUTION-LOG.md` — prior decisions, scheduled batches,
  and execution evidence.

## Channel/account resolution

The content engine's active platform set and the authenticated Buffer workspace
are not guaranteed to match. Resolve the current account mapping in Buffer
before drafting or scheduling. A previous verified snapshot used:

| Buffer channel | Native surface | Default adapter |
| --- | --- | --- |
| `JamesNMK` | X | founder lane only, with `$x-engagement` and the explicit founder adapter |
| `PETIO` | LinkedIn Page | Petio product voice |
| `jamesk.zip` | Threads | Threads small-noticing voice |

This table is a starting hypothesis, not live proof. Recheck the channel name,
owner, platform, queue, timezone, and permissions every Buffer session.

## Precedence

When guidance conflicts, use this order:

1. current user authorization and task scope;
2. `voice/claims-and-safety.md`;
3. verified `proof/proof-ledger.md` and current app/source evidence;
4. `petio-content/index.md` and `CLAUDE.md`;
5. current platform node and tone;
6. adapter skills and copywriting heuristics;
7. Buffer performance patterns.

Metrics can select the next experiment. They cannot rewrite the safety boundary
or convert an unverified claim into proof.
