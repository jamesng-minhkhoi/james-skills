---
name: knowledge-builder
description: Compile research into verified knowledge packs — sources frozen with sha256, claims promoted only when their verbatim quote verifies against the frozen capture, documents citing claims, and a research run that stops on a ledger-backed gate instead of a feeling. Drives the knowledge_builder CLI when installed. Use for building reusable knowledge bases, research digests, or source packs; not for freeform notes or brainstorming.
---

# Knowledge Builder

## When to use

Use when the output must survive a trust review: a durable knowledge base, a
research digest, a source pack another session will rely on. Do not use for
ephemeral answers, brainstorming, or journaling — the schema gates are friction
with no payoff there.

## The idea

Raw scrapes pollute agent context with unverified claims. A pack inverts that:
every claim quotes a frozen source, and a claim is only as good as the quote
and hash that back it. Research stops because the ledger said so, not because
the draft reads finished. Claims start `unverified` and become `verified` only
when the check passes — vocabulary from [`../_shared/ontology.md`](../_shared/ontology.md).

## Engine

The deterministic engine is the `knowledge_builder` CLI
(`python3 -m knowledge_builder.cli`) from
[design-os-knowledge-builder](https://github.com/jangtrinh/design-os-knowledge-builder)
(PolyForm Shield 1.0.0 — used per its license; this skill references the tool
and embeds none of it). Throughout this file, `kb <args>` is shorthand for
`python3 -m knowledge_builder.cli <args>` — type the full form; nothing here
asks you to invent an alias. Install it:

```sh
git clone https://github.com/jangtrinh/design-os-knowledge-builder /tmp/kb
pip install --user -e /tmp/kb
```

Without the engine: do the same discipline by hand — `curl -fsSL <url> -o
sources/<stem>.txt` plus `shasum -a 256` for freezing, quotes recorded as
`unverified`, and no `verified` word anywhere until a diff-style check compares
each quote against the frozen file. Flag commands with `kb --help` if a flag in
this skill drifts from the installed CLI.

## Workflow

1. **Freeze sources.** `kb ingest --freeze <url> --root <knowledge-root> --run
   <run> --stem <kebab-stem>` writes plain text under `sources/` and prints the
   sha256 and repo-relative path. Every atom that follows cites that hash and
   path. A quote is cut from the frozen file, never from recall.
2. **Loop with a ledger.** `kb run init` opens `_evidence/<run>/`; record one
   atom per finding with `kb run record` — each atom's evidence anchors a
   `source_anchor` carrying `uri`, `sha256`, and `quote` cut verbatim from the
   frozen file (never re-typed), plus `metadata.round` integer ≥ 1 and
   `metadata.novel` boolean; check `kb run record --help` if the installed
   shape differs. Measure per-round novelty with `kb run measure --material` —
   a novel atom counts only when a source anchor's quote is actually cited.
3. **Stop by gate, not vibes.** `kb gate` reads the ledger: three consecutive
   low-delta rounds yield `STOP_SUFFICIENT`, but only if version state is
   resolved — write `kb run state set` for `version_applicability` and, when
   no target version applies, set it `not_applicable` with a non-empty
   `version_reason`; without that reason the gate stays `DEEPEN`. Never end a
   run because the summary reads well.
4. **Promote claims.** In a pack root (`kb pack init`, ontology mode): `kb
   action promote-claim`. The tool refuses atoms whose hash or quote does not
   verify, double promotions, and publishers taken from hosting hosts
   (`github.com`, `arxiv.org`, mirrors — name the real publisher or the claim
   stays out). Promoting a `CONTRADICTION` atom records the contradiction;
   resolving it is a separate `resolve-contradiction` action.
5. **Cite from documents.** A document supports a claim with
   `<!-- ease:claim id=<claim-id> -->` under the block it backs plus a `cites`
   link. Anchor ids and `cites` targets must match one-to-one — `kb verify
   --claims` accepts no either-direction mismatch.
6. **Check before shipping.** `kb verify --claims` (every quote against every
   frozen capture), `kb pack check` (exit 0 only when verify passes, prints the
   gate plus the residue: claims no document cites, unresolved contradictions,
   and a stale index — take that printed list as findings `F-kb-<n>` with
   severity per the ontology, never your own eyeball scan). Fixing pack
   content is editing work with a fix report.

## What "done" means

Verify passes every quote, `pack check` exits 0, and the gate prints
`STOP_SUFFICIENT` with its receipt. That is a `READY` verdict; anything partial
is `READY_WITH_CONDITIONS` and names the unobserved part `NOT_RUN`.

## Anti-patterns

- Paraphrase dressed as a quote — the anchor quote must match the frozen text.
- Publisher inferred from where the PDF lives instead of who wrote it.
- Ending research when the summary *feels* complete — the gate is the checker.
- Copying raw scrape text into a pack document without promoting a claim.

## Source

Methodology credit:
[design-os-knowledge-builder](https://github.com/jangtrinh/design-os-knowledge-builder)
by Jang Trinh (PolyForm Shield 1.0.0): frozen sources, verbatim-quoted claims,
and the epistemic stopping gate. This text was written fresh for this library;
it drives the upstream tool rather than redistributing it.
