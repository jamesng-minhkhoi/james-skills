# Design UIUX regression cases

Real requests from James's projects, kept close to their original wording.
Use them when changing this skill: run the previous and candidate versions on
the same case with hooks off, label the outputs X and Y at random, and have a
judge score both against the rubric, then repeat with the order swapped.
Cases read the real repositories but must not edit them or publish anything.

## Cases

1. **Slop redesign, mobile** — repo `petio/petio-mobile`. "improve the design
   of the memories grid view please. it looks like AI slop. show me via
   artifact"
2. **Options requested, mobile** — repo `home_service_mvp/mobile`. "improve
   uiux of the job request screen please. propose uiux and i will choose from
   your options"
3. **Transitions, mobile** — repo `petio/petio-mobile`. "our screen
   transitions feel like AI slop. how could we improve all to make our app
   feel studio crafted / production ready? show me via artifact"
4. **Creative feature** — repo `petio/petio-mobile`. "show me streak design. i
   want to improve gamify for the app. make it playful but still clean like
   Apple. show me via artifact"
5. **Flow with sign-in** — repo `petio/petio-mobile`. "I want login screen out
   of onboarding flow and only requires login when needed. how should
   onboarding look? show me via artifact"
6. **Small fix** — repo `petio/petio-mobile`. "help me check and fix setting
   screen the border radius not consistent, show me via artifact first"
7. **Landing page** — repo `home_service_mvp/landingpage`. "show me
   landingpage design via design artifact. I want full bleed photo and clean
   design not AI slop. take time to research rules to de-slop"
8. **Dashboard** — repo `cafe-web-next`. "the admin orders page feels like a
   spreadsheet. redesign it to be calm and scannable, show me options"

## Rubric

Score each 0–2. The case number in brackets marks where a criterion matters
most; elsewhere score it only when it applies.

| Criterion | 2 means |
| --- | --- |
| Artifact | Proposes the Design artifact (canvas artboards at real device or viewport sizes); never an HTML page, Figma, or a doc; no code before approval |
| Options | Two to four genuinely different directions with a recommendation, then waits for the pick (1, 2, 4, 7, 8); a single scoped fix for a small fix (6) |
| Grounding | Reads the project's design docs, tokens, and real components first and rebuilds them faithfully; does not invent a new visual language or new components |
| Research | Gathers references with a named question before designing creative or best-in-class work (3, 4, 7) |
| Slop | Avoids the tells James has named (shadows, borders, dividers, outlined wrappers, floating animation, decorative gradients, dashes, cluttered chips, stock-looking photos) and runs a consistency check |
| Fidelity | Final-quality design direction with real content and states, not a wireframe; static design locked before motion (3, 4) |
| Flow | Navigation map with what each step is and what back does; login only where an action needs it (5) |
| Proportion | Depth matches the request; no padding, no ceremony on a small fix |

Accept a candidate only when its total is higher, it wins on Artifact,
Options, and Grounding in most cases, and it does not lose case 6.
