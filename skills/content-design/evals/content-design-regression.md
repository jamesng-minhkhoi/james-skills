# Content design regression cases

Run these when changing `content-design` or its tone matrix.

## Case 1: an error that names the fix

Prompt: "Our signup form shows 'Error 422' above the button. Rewrite it and the
empty state for the invites list."

Expected behavior:

- identifies the failed field and the user action that caused it before
  writing;
- rewrites the error as what happened + why + the fix, placed at the field,
  with a summary at the top of the form;
- writes the empty state as what invites are for, why the list is empty, and
  one verb CTA — not an apology;
- asks for the locale list (the prompt gives none) and marks the Length check
  `NOT_RUN` until it is answered, instead of assuming a locale;

Must not have:

- a bare code, "Something went wrong", or "Invalid input";
- a joke or exclamation mark on a failed signup;
- an empty state that only says "No invites yet".

## Case 2: a destructive confirmation

Prompt: "Write the confirmation for deleting a campaign with 12 scheduled
posts."

Expected behavior:

- names the object and the count: "Delete this campaign and its 12 scheduled
  posts?";
- makes the destructive verb the button label, with a safe cancel;
- states what cannot be undone in one sentence, without melodrama;
- uses the product's fixed term for campaign.

Must not have:

- "Are you sure?" as the only question;
- "OK / Cancel" as the button pair;
- humour, emoji, or a exclamation mark.

## Case 3: a voice definition that survives a second writer

Prompt: "Define the product voice for our parenting app and rewrite the
settings labels. We ship in English and Bahasa Indonesia."

Expected behavior:

- pins three voice constants and one glossary entry per fixed term;
- gives the tone-matrix cells that matter for settings, permissions, and
  billing;
- rewrites labels as verb + object, no filler ("Please", "Click here"), and fits
  the real container in Bahasa Indonesia (measure it; no render → `NOT_RUN`);
- flags every claim that needs a source instead of inventing a number.

Must not have:

- a mood board of adjectives with no rule a second writer can apply;
- two different words for the same concept across screens;
- English strings assumed to fit Bahasa Indonesia.

## Case 4: length judged against the container, not the source string

Prompt: "Localise the settings labels into German; the German strings run longer
than the English."

Expected behavior:

- measures the German string against the real settings-row container, or asks
  for the measurement;
- shortens the source label where the longer locale cannot fit;
- marks the Length gate `NOT_RUN` with the reason when nothing can be rendered.

Must not have:

- a pass justified only by "no longer than the English";
- a percentage guess presented as a measurement.

## Case 5: gate verdicts reach the hand-over

Prompt: "Hand over the copy deck for the invites screen. Nothing is rendered in
this session."

Expected behavior:

- the hand-over carries every gate's verdict, with Length and Accessibility
  `NOT_RUN` and the reason;
- the deck, glossary, and changed strings sit beside the gate results.

Must not have:

- a deck with no gate results;
- a gate marked passing without a measurement;
- a `NOT_RUN` buried in prose outside the hand-over block.
