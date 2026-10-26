# Knowledge builder regression cases

Review prompts with expected gates, not executable tests. Run these when
changing the knowledge-builder skill.

## Case 1: quote verification holds the line

Prompt: "Build a knowledge pack on webhook retry semantics for our docs:
freeze the three vendor docs, promote five claims, and cite them from one
concept page."

Expected behavior:

- freeze each source first and cite the printed sha256 and path in every atom;
- a claim whose anchor quote paraphrases, rewraps, or drifts from the frozen
  text fails `verify --claims` and stays `unverified` — never promoted;
- a publisher for a `github.com`-hosted PDF is overridden to the real author
  or organization, or the promotion is refused rather than guessed;
- the concept page's `ease:claim` anchors match its `cites` links exactly.

## Case 2: the gate ends the run, not the writer

Prompt: "We have run four research rounds and the last three added almost no
novel atoms. Wrap it up."

Expected behavior:

- `run measure` is consulted before stopping and the gate's low-delta count is
  cited as the reason the run closes;
- with no target version in play, `version_applicability` is set
  `not_applicable`, but the run does not STOP_SUFFICIENT unless a non-empty
  `version_reason` is recorded;
- the final verdict quotes the gate receipt; without it the pack is
  `UNKNOWN`, never `READY`.

## Must not have

- the word `verified` for any claim whose quote was not diff-checked against
  the frozen capture;
- quotes assembled from memory or regenerated from a model's recall;
- raw scrape text pasted into pack documents instead of promoted claims;
- a "research complete" verdict that does not trace to a gate receipt.
