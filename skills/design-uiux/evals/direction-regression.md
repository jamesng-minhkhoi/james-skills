# Design direction regression cases

Review prompts and expected decisions, not executable tests or evidence that
a generated page was verified. Use when revising visual-direction guidance.

## Case 1: Preserve the existing brand

Prompt: “Refresh our purple landing page. Keep the logo, approved copy, signup
path, and calm feel. The current page uses Inter and a text-led hero.”

Expected behavior:

- inspect the existing page and declare preservation;
- retain purple, Inter, approved copy, and signup behavior unless an observed
  problem warrants a scoped proposal;
- refine hierarchy, spacing, and composition from evidence;
- no mandatory imagery, font substitution, dark mode, or increased motion.

## Case 2: Reference screenshot, no mobile artifact

Prompt: “Match the feel of this desktop screenshot. Its dimensions and font
are unknown. Design mobile too.”

Expected behavior:

- inspect the supplied screenshot and extract relevant proportions, type
  hierarchy, spacing, color placement, shapes, media, and restraint;
- distinguish measured image-space values, estimates, and proposed CSS rules;
- propose mobile behavior rather than claiming to have observed it;
- specify checks at target widths; do not claim exact font or runtime fidelity.

## Case 3: Trust assets are missing

Prompt: “Make the page feel established. We have no testimonials or customer
logos yet, and the feature preview is only a concept.”

Expected behavior:

- expose the proof gap and use available authentic evidence;
- never turn generated logos, quotes, numbers, or a concept preview into proof;
- make illustrative status visible where necessary, not just in an HTML comment;
- retain content-owner boundaries and allow a credible text-led design.

## Case 4: Dense product surface

Prompt: “Improve the design of our inventory dashboard with 20 comparable
rows, warning/success states, and a working table. Make it less templated.”

Expected behavior:

- route to dashboard design, preserving the comparison and action task;
- retain useful tables, repetition, and semantic colors;
- do not substitute carousels, sparse hero sections, or a single-accent rule;
- request realistic dense-state and responsive proof in the handoff.

## Case 5: Long content and restrained motion

Prompt: “Our approved German heading wraps to four lines on mobile. Keep all
the wording. The site is light-only and should work with reduced motion.”

Expected behavior:

- make the layout grow and tune hierarchy without clipping or shrinking body
  text to fit an arbitrary hero cap;
- preserve the light-only scope and provide usable reduced-motion behavior;
- verify target widths and zoom in the rendered design when available;
- keep unobserved interaction and production claims explicit.

## Case 6: "As good as the best in the category"

Prompt: “Redesign our pricing page so it holds up against the best SaaS
pricing pages.”

Expected behavior:

- name the research questions first (plan count, anchor plan, annual toggle,
  comparison depth, proof placement) instead of collecting inspiration;
- compare the same surface across three to five strong products and separate
  convention (where they converge) from choice (where they diverge);
- keep durable notes and three to eight picks with reasons, then measure them;
- borrow structure, not another brand's identity, claims, or assets;
- define done as a side-by-side that reads at least as good, and name any
  remaining gap rather than stopping at "better than before".
