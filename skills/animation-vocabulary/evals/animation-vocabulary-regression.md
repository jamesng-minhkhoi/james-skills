# Animation vocabulary regression cases

Use these forward-test fixtures when changing the `animation-vocabulary`
skill. They are review prompts with expected gates, not executable tests.

## Case 1: reverse lookup

Prompt: "What's it called when a popover grows out of the button?"

Expected behavior:

- lead with the glossary term verbatim (Origin-aware animation);
- keep the output tight: the term, one line of what it is, and where to use
  the word when prompting an AI or designer;
- do not redesign the effect or start writing animation code.

## Case 2: vague mobile motion

Prompt: "What do you call the rubber-band effect when you overscroll on
iPhone?"

Expected behavior:

- return the exact term (rubber-banding) from the glossary;
- name the closest web equivalent if the effect has no direct CSS
  implementation, without turning the answer into a tutorial.

## Must not have

A completion claim fails if it contains any of these:

- an invented term not in the glossary;
- implementation code or a redesign offered unprompted;
- a paragraph-length answer where one term and a line was asked for.
