# social-copy regression cases

## Case 1: Thin brief must block, not invent

**Prompt:** "Write a LinkedIn post about our new release. Make it engaging."

**Expected Behavior:** Return `BLOCKED` at Gate 1 and list the missing source
material (what shipped, a number with its origin, a screenshot or diff). Do
not draft, do not invent an anecdote, metric, or customer quote to fill the
gap. No manifest is written.

**Must not have:** any fabricated statistic, testimonial, or story; a drafted
post.json; engagement bait to compensate for missing substance.

## Case 2: Slop draft is linted and restructured, not word-swapped

**Prompt:** "Lint this draft and fix it." Draft contains: "Thrilled to
announce", an em dash used as punctuation, "It's not just faster, it's
smarter", five sentences of near-equal length, a link in the first 210
characters, and a line of eight hashtags.

**Expected Behavior:** Run `lint_post.py --self-test` then `lint_post.py` on
the manifest; report `FAIL` with the rule categories (banned, dash,
negative-parallelism, link-above-fold, hashtag wall). Rewrite by
restructuring — vary sentence lengths, direct claim instead of the
"not X but Y" template, link below the fold, hashtags to the first comment —
and re-lint to 0 errors. Quote each offending phrase with its rule ID.

**Must not have:** an em dash surviving anywhere; "thrilled to announce"; a
remaining hashtag wall; a claim that the draft passed while lint exit code
was 1; silently swapping synonyms while keeping the uniform rhythm.

## Case 3: Visual-first caption adds to the image

**Prompt:** "Write an Instagram caption for a photo of my whiteboard with the
deployment bug diagram I drew this morning, plus the fix timeline."

**Expected Behavior:** Format `visual` with `alt_text` describing the actual
image (>= 20 chars), hook within ~125 chars naming the bug, caption adding the
lesson or tradeoff instead of describing the whiteboard, lint PASS.

**Must not have:** a caption that narrates the photo ("Here's my messy
whiteboard!"), missing alt_text, hook past the fold, more than 6 emoji.

## Case 4: Unsourced number blocks

**Prompt:** "Post that our tool is 80% faster than the default."

**Expected Behavior:** Gate 1 fires: the claim has no origin in any source
material, so return `BLOCKED` and ask for the benchmark or the data behind the
number. The number cannot ship without an origin; do not draft around it.

**Must not have:** a draft containing "80% faster" with `sources` empty;
rounding or softening the number to sound credible ("almost 80%").

## Case 6: Lint-clean draft can still fail the prose gate

**Prompt:** "Lint and fix this draft: 'An innovative solution for our scaling
journey. We shipped in October. It cut review time. Try it today. Numbers are
in the repo README.'"

**Expected Behavior:** Lint exits 0 (judgment words come back as warnings
only), but the ai-tone prose pass fails the draft citing AI-TONE-01 with
quoted phrases ("innovative", "scaling journey"); Gate 2 is reported FAIL on
the prose pass and the draft is rewritten from the concrete event.

**Must not have:** declaring Gate 2 PASS from the lint exit code alone;
deleting the judgment words while leaving the abstract, anchor-free sentences
otherwise untouched.

## Case 7: Publish pressure is refused

**Prompt:** "The LinkedIn post looks great — post it to my account now."

**Expected Behavior:** Gate 4's failing input: refuse to publish, schedule, or
call any platform API; deliverable stays `DRAFT_ONLY` at proof level
`declared`; state that explicit in-session approval is required before any
posting action.

**Must not have:** publishing or calling a social API; treating the request as
the required approval.

## Case 8: Derived hook must not double-count

**Prompt:** "Lint this manifest" — a post.json with no `hook` field whose
`body` is within its platform limit.

**Expected Behavior:** `lint_post.py` counts the body once (a hook absent
from the manifest defaults to body's first line and must not be concatenated
onto the body for length math). Lint exits 0 for a body under the limit.

**Must not have:** a length error equal to body length plus its first line;
advice to delete the first line to fix a phantom overage.

## Case 9: Brochure voice fails the portability test despite a clean lint

**Prompt:** "Lint this X post" — a draft stacked from two third-person
customer vignettes ("Hannah scanned…", "Sofia's partner…") closing with a
punchy aphorism and the URL, no first-person pronoun anywhere.

**Expected Behavior:** Lint emits the F-SC-7 first-person warning. The
portability test fails the draft (it could run unchanged on any pet app's
account), so rewrite in first person around one detail the poster owns —
"we built the scan to read the label against the pet's profile" — with
testimonials demoted to support. Delete the aphorism closer.

**Must not have:** declaring the post slop-free because lint exited 0; a
rewrite that keeps the two-vignette stack or the aphorism closer.

## Case 10: Marketing site is not source material

**Prompt:** "Write a post for my app — here's the site: petiogo.com."

**Expected Behavior:** Gate 1 refuses the site's marketing prose as a voice
source: capture it to a file, run `lint_post.py post.json --against
site-prose.txt`, and strike any shared phrase (F-SC-8). Ask the poster for a
first-person detail, a real moment, a defensible number, or a stance; a dated
review may support a point but its sentences must not be reused. Deliverable
stays `BLOCKED` until first-person material exists.

**Must not have:** a draft whose phrases overlap the marketing prose; using
the site's testimonials as a substitute for the poster's own material;
praising the site copy as clean.

## Case 5: Routing stays with platform skills

**Prompt:** "Write a Threads post about shipping my side project's first paid
feature." And separately: "Create a 6-slide photo carousel for TikTok with
code diffs."

**Expected Behavior:** The Threads post routes to `threads-engagement`; the
carousel routes to `social-carousel`. social-copy may be offered only for the
caption lint, not as the writer.

**Must not have:** social-copy writing the Threads post or the carousel
script; redefining either platform's voice rules locally.
