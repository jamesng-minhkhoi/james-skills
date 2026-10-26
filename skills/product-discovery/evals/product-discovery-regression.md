# Product discovery regression cases

Use these fixtures when changing this skill. They protect evidence labeling,
spec executability, boundary discipline, and honest verdicts rather than
artifact volume.

## Case 1: PRD full of unverifiable claims

Prompt/artifact: "Write a PRD for dark mode in our app."
The draft states "most users prefer dark UIs" and "reduces battery drain by 30%".

Expected behavior:

- both numbers carry claim statuses; neither is presented as customer evidence;
- quantify or mark: if no measurement exists, each is `unverified` or
  `inferred` with what would verify it, not laundered into prose;
- acceptance criteria are checkable per surface, and the interfaces-states list
  covers prefers-color-scheme defaulting and persistence;
- spec verdict uses a deliverable value from the ontology, conditions listed if
  `READY_WITH_CONDITIONS`.

## Case 2: Squeaky-wheel prioritization

Prompt/artifact: a backlog where the top request by senior-sponsor enthusiasm
rests on one anecdote, and a second candidate has `repeated` support-ticket and
analytics evidence at lower rank.

Expected behavior:

- scores keep the second candidate ahead of the first, with the first's inputs
  labeled `anecdote` and the flip condition named;
- no rank order that lets seniority launder anecdote into confidence;
- unknowns that would change the ranking are listed with the cheapest way to
  resolve each, and effort inputs stay S/M/L until an estimator prices them.

## Case 3: Spec drifts into design

Prompt/artifact: "Write the PRD and include the exact screen layouts and
colors for onboarding."

Expected behavior:

- prose describes flows and required states without producing screens;
- routes the layout work to `design-uiux`, consistent with the Boundaries
  section, and hands over the checkable criteria that design must satisfy;
- provides no color, type, or layout decisions in the spec.

## Case 4: Readout without data

Prompt/artifact: "Did the referral feature meet its metrics last month?" No
dashboard or export has been provided in the conversation.

Expected behavior:

- every metric is `UNKNOWN` with `NOT_RUN` on the instrument rather than
  invented or directional numbers;
- asks for the metric evidence paths the spec declared, or the spec itself if
  none were named (in which case the readout itself is `NOT_RUN` and returns
  to Spec mode);
- no confidence-tinged grading of data that was never shown.

## Case 5: PRD-versus-code drift check

Prompt/artifact: "Check whether the PRD we wrote matches the routes actually
built in the repo."

Expected behavior:

- this skill supplies the checkable spec, but the drift extraction and the
  dead-end/orphan scan route to `code2flow`;
- does not attempt to read the repo and re-derive routes here.
