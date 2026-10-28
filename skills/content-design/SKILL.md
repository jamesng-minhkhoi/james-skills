---
name: content-design
description: Write and review the words inside a product interface — voice, tone, errors, empty states, confirmations, and claims. Use when wording a screen, fixing a confusing error, defining a product voice, or checking copy before release. Not for visual layout (→ design-uiux), marketing pages (→ copywriting), or UI audits (→ audit-uiux-web / audit-uiux-mobile).
---

# Content Design

Own the words inside the product: the voice that stays constant, the tone that
changes with the user's state, and the exact strings for errors, empty states,
permissions, and destructive actions. The artifact is a copy deck the build can
paste in, plus the rules that keep the next screen consistent.

Shared vocabulary: [ontology](../_shared/ontology.md).

## When NOT to use

- Layout, hierarchy, or where the copy sits → `design-uiux`.
- Landing pages, ads, launch posts, SEO pages → the `copywriting` or
  `seo-aeo-geo` skill.
- A full interface review that happens to mention words → `audit-uiux-web` or
  `audit-uiux-mobile`; this skill fixes the copy they flag.
- Translation vendor management or legal review → outside this skill.

## 1. Read the product before writing

Collect, in this order:

1. The product's existing voice: three screens the team considers good, and
   the terms already fixed in the repo (glossary, `AGENTS.md`, design docs).
2. The screen's job: user, situation, primary action, success, failure cost.
3. The states the screen can reach: first use, typical, empty, loading, long
   content, error, offline, permission denied, destructive confirm.
4. Locales in play. Take the list from the brief; if it is missing, ask once
   and mark the locale set `UNKNOWN` until answered. Never assume the source
   string expands safely into the longest one.

If a term is already fixed, use it. Do not introduce a synonym because it reads
better in one sentence; that is how one concept becomes three.

## 2. Pin voice, flex tone

**Voice** is constant: the product's personality. **Tone** flexes with the
user's emotional state.

| Dimension | Pick one per product | Example |
| --- | --- | --- |
| Formality | casual ↔ formal | "Hey" vs "Good morning" |
| Warmth | objective ↔ friendly | "Saved" vs "Saved — nice work" |
| Directness | terse ↔ elaborate | "Try again" vs "That didn't work. Try again in a minute." |
| Humour | none ↔ playful | Never on billing, security, or data loss |

Voice constants that are not tunable: active voice, plain language, second
person, verb-first actions, sentence case, positive framing where it is honest.

## 3. Match tone to the moment

| Situation | User state | Tone |
| --- | --- | --- |
| Success | satisfied | warm, short, celebrate once |
| Neutral form | focused | plain, direct, verb-first |
| First run | unsure | teach the why, encourage |
| Loading | impatient | honest about duration |
| Empty | lost | orient, then one verb CTA |
| Warning | cautious | calm, state the consequence |
| Recoverable error | frustrated | blame-free: what happened, why, the fix |
| Destructive / billing / security | anxious | serious, precise, humour = 0 |
| Permission request | wary | state the value exchange plainly |

Humour and enthusiasm move inversely to user stress. A pun in a failed-payment
screen is a defect, not a personality.

## 4. Write the states

Every data surface needs copy for the states it can reach. Name the state, then
the string.

- **Empty (first use):** what this is, why it is empty, one action. Do not
  apologise for a state the user has not caused.
- **Empty (cleared/filtered):** say what is hidden and how to clear it. Keep
  the filter chip visible; do not blame the data.
- **Loading:** say what is loading if it takes more than a moment. No fake
  progress, no "Please wait..." with no object.
- **Error:** identify, explain, fix. Never a bare code. Place it at the source;
  add a summary at the top of a failed form.
- **Destructive confirm:** name the object and the consequence, make the
  destructive verb the button, and offer the safe path. "Delete 12 posts?" not
  "Are you sure?".
- **Permission:** state what is asked, why, and what happens on refusal. Never
  pre-ask at launch for a permission the first action does not need.
- **Success:** confirm the thing that changed, once. No confetti sentence.

## 5. Keep claims honest

- No invented metrics, testimonials, logo walls, review counts, or user
  numbers. A missing number is `—` with "to confirm", or a layout that does not
  lead with a number.
- A number is never a headline alone; it sits beside what it measures and its
  period.
- Do not upgrade a claim's status in copy. "Customers want" requires evidence;
  "we think" does not become "users love" because the layout has room.
- If the product cannot do the thing the sentence implies, rewrite the sentence
  or remove the feature claim.

## 6. Write for every shipped locale

- Measure the longest shipped string in the real container — browser, device,
  or the design file's text box. No render available: mark the Length gate
  `NOT_RUN` and say so; a percentage guess is not a measurement.
- No concatenated strings. Use ICU MessageFormat for plurals; never `item(s)`.
- Use logical properties for RTL; do not bake text into images.
- Format dates, numbers, and currency per locale. A rate typed in one currency
  and displayed in another says which currency it is.
- Keep one term per concept across locales. A glossary entry is a product
  decision, not a translator preference.

## 7. Check before hand-over

Run this table on every string. A failure is a rewrite, not a note.

| Gate | Passes when | Fails when |
| --- | --- | --- |
| Meaning | A first-time user can say what happened and what to do | The reader needs the previous screen to decode it |
| Action | Buttons start with a verb and name the object | "OK", "Yes", "Submit", "Continue" alone |
| Length | Fits the real container in the longest locale, measured | Truncates, wraps under a control, or needs a smaller font |
| Consistency | One term per concept, same as the glossary | Two words for the same thing on adjacent screens |
| Honesty | Every claim is `verified` or `attributed`, or marked `unverified` | A number, quote, or logo the brief did not supply |
| Tone | Matches the matrix row for the user's state | Jokes or exclamation marks on a high-stress screen |
| Accessibility | The string makes sense read aloud, without colour or position | "Click the green button" or an icon-only label |

## 8. Hand over

Return the copy deck in this shape:

```text
SCOPE: <screens and states covered>
VOICE: <three constants chosen, one line each>
DECK: <state → string, per screen>
GLOSSARY: <term → the one wording, per locale>
CHANGED: <files or strings replaced>
GATES: <Meaning / Action / Length / Consistency / Honesty / Tone / Accessibility → verdict, with the reason for every NOT_RUN>
NOT_VERIFIED: <states not rendered, locales not reviewed, claims without a source>
```

## Failure modes

| Symptom | Cause | Correction |
| --- | --- | --- |
| Copy sounds like a different product on each screen | Voice was never pinned; each writer chose a tone | Pin three voice constants and a glossary; rewrite the outliers |
| Error blames the user | Sentence starts with "You" and a failure | State what happened, then the fix; never "invalid user" |
| Empty state is an apology | Writer described the absence, not the next action | Say what the screen is for and give one verb |
| String overflows in the longer locale | Only the source locale was measured | Test the longest locale at the real width; shorten the source |
| Numbers feel invented | Layout needed a figure and none existed | Remove the figure or mark it "to confirm" |
| Destructive action is a joke | Tone matrix ignored | Humour = 0 on billing, security, data loss |

## Changing this skill

Start from a real string that shipped wrong — an error that confused a user, a
label that overflowed in a longer locale, a claim that could not be sourced. Add the
case to `evals/`, then rewrite the rule it points at. Keep the tone matrix and
the error standard stable; they are the load-bearing parts.
