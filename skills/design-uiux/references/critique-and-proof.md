# Critique and proof

Use before drawing options for a redesign, a "fix the UI" request, or a
critique of shipped work, and again after the proposal is rendered. Source
inspection can answer most gates; it cannot replace looking at the rendered
work. Run [slop and consistency](slop-and-consistency.md) first.

## The twelve gates

Answer every gate before options, and re-answer the same table before handoff.
One row per gate, with the evidence that decided it:

| # | Gate | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Job | PASS / FAIL / BLOCKED / NOT_RUN | file:line or measurement |
| 2 | One primary |  |  |
| 3 | One way in |  |  |
| 4 | Row is the target |  |  |
| 5 | Disclosure |  |  |
| 6 | Structure |  |  |
| 7 | Hierarchy |  |  |
| 8 | Words |  |  |
| 9 | State and motion |  |  |
| 10 | System |  |  |
| 11 | Touch, platform, and access |  |  |
| 12 | Proof |  |  |

Verdicts are literal. `PASS` needs evidence. `FAIL` needs evidence and a user
cost. `BLOCKED` names the access or artifact that is missing. `NOT_RUN` names
what would prove it; for a gate that does not apply, write `N/A` in the
evidence. "Looks good", "seems clean", and "modern" are not verdicts.

1. **Job.** One sentence: user, job, primary action, success. Entry, next
   step, back, cancel, and recovery are part of it. Two jobs on one screen is
   a finding unless the screen names their order.
2. **One primary.** At most one filled/primary control per card, sheet, or
   screen. A second filled control is a finding even when it does a different
   thing. An empty screen does not repeat the toolbar's create action in its
   empty state, and does not keep a filled action for a task the empty state
   cannot yet do.
3. **One way in.** Each action has one trigger; each fact is said once. Count
   the controls that open the same sheet or write the same record. Two
   "Thêm" buttons, a row's own action repeated in its ⋯ sheet, a table chip
   plus a note with the same table, or a status badge under a status tab are
   findings.
4. **Row is the target.** A list row opens the record, not only its title.
   The whole row is tappable, with press feedback that matches the hit area.
   Keep the ⋯ button a sibling; an overlay button or link can make the row
   the target without nesting controls. Secondary actions sit behind one
   labelled ⋯, not on the row face. A switch or button in the row's figure
   column is a second action; justify it or move it.
5. **Disclosure.** Level one is complete for the frequent task; rare actions
   are one labelled control away. A cap is "+N món nữa", a control, not a
   fade. A ⋯ menu with one non-destructive item is a button, not a menu; a lone
   destructive action may stay in ⋯ as the safety rung. A disqualifying state
   (out of stock, unpaid, blocked) stays at level one.
6. **Structure.** The container fits the task: list for scan-and-act, table
   for comparison, sheet for a focused edit. No box inside a box for one
   item; no scroller inside a sheet's scroller; no table squeezed narrow. An
   empty field is an ordinary row, not a lone tile.
7. **Hierarchy.** One focal point per screen; one scan order. Rows in a group
   do not all lead with the same glyph unless the glyph is what is being
   scanned. Whitespace groups before borders or shadows.
8. **Words.** Labels are at most four words in English and five in the
   product's other language; verb + object; no sentence labels; one fixed
   term per concept; no caption that repeats the title. Real labels, data,
   nulls, errors, prices, and translations fit.
9. **State and motion.** Empty, loading, error, long, translated, dense, and
   first-use states exist where they can occur. State is glyph + word, not
   colour alone. Destructive actions climb rather than sit on the face. Each
   motion is necessary, classified, cancellable where a gesture drives it,
   and has a reduced-motion path.
10. **System.** Tokens only: no raw palette for semantic colour, no unitless
    line-height, no shadowed spacing token, no sub-12px text outside a
    documented exception. Run the project's guards and cite their output.
11. **Touch, platform, and access.** 44px targets on coarse pointers, 16px
    inputs, no hover-only action, safe-area clear, platform convention or a
    stated reason. Names, roles, focus order, contrast, zoom, and reduced
    motion preserve the task. Mark `NOT_RUN` without a device or emulator.
12. **Proof.** Rendered at the real sizes (390/768/1440 or the project's
    equivalent), with the primary flow's states. No render, no `PASS`: mark
    `NOT_RUN` and name the gate for engineering.

Walk the gates in order 1–12; do not reorder by taste. The table is coverage;
the findings table is triaged by severity.

### Determinism

- Same screen + same evidence = same verdicts. If a second run differs, the
  evidence was insufficient; fix the evidence, not the verdict.
- Stop when all twelve are answered, not when the screen looks good.
- Re-run the same table after refinement. A verdict that regresses is a new
  finding even if the screen looks better.
- Give the table and the rendered sheet to a fresh-context critic (a
  subagent or new session). The critic re-runs the gates blind; disagreement
  becomes `NOT_RUN` or a finding.
- At most two fix rounds after the first full diagnosis; then hand over what
  remains.

Surface-specific first questions:

- **Dashboard:** Does the first viewport serve a real decision rather than a
  KPI wall? Can users tell what changed, what is urgent, what is stale, and
  what to do?
- **Landing page:** Can a new visitor explain the offer after the first
  viewport? Does every major claim have nearby, credible proof? Is the CTA
  honest about what happens next?
- **Mobile:** Is the primary action reachable with one hand and named by its
  outcome? After each one-way door, does every back path fail to re-enter the
  old state?

## Rendered-state matrix

Render at least the rows that apply:

| Dimension | Evidence |
| --- | --- |
| Journey | Entry, primary action, result, next step, back/cancel |
| Content | Typical, longest realistic, translated, empty, no-results, dense, error |
| Network | Loading, slow, partial, success, recoverable error, offline if supported |
| Interaction | Pressed, hover, focus-visible, selected, disabled, keyboard, sheet or dialog |
| Platform | Small and large phone, safe areas, dark mode, large text (mobile); narrow, tablet, desktop, zoom (web) |
| Data (dashboard) | One, dense, null, stale, conflicting; search, filter, sort, pagination; permissions |
| Message (landing) | First viewport, headline wrapping, CTA, proof, form pending/success/error |
| Motion | Rest, in progress, threshold, completion, cancellation, reduced motion |
| Recovery | Retry, undo, rollback, permission denial, interruption and resume |

A static artboard cannot prove timing, focus return, keyboard behavior,
gesture feel, or recovery. Mark those as unknown and leave them as gates for
engineering.

## Interaction-state proof

For each primary action and important component, record:

| Check | Evidence |
| --- | --- |
| Intent | The goal it supports and why it is visible or disclosed |
| Trigger | Pointer, touch, keyboard, route, delay, or system event |
| Feedback | Pressed, focus, pending, progress, toast, or status |
| Outcome | Success, partial success, error, empty, stale, or permission result |
| Recovery | Cancel, close, undo, retry, resume, or alternate path |
| Accessibility | Name, role, state, focus order and return, non-color cue |
| Motion | Timing and easing, interruption, reduced-motion behavior |

## Finding shape

| ID | Priority | Gate | Screen/viewport/state | Evidence | User impact | Proposed fix | Rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-design-01 | P0–P3 | 1–12 |  | file:line or measurement |  |  | R-... |

Sort by P0–P3, then gate, then screen. Every finding keeps its ID from
diagnosis to fix to re-audit; use the project's prefix, or `F-design-<n>`.
Every finding names the gate and the rule it breaks; a rule the project has
not written gets `R-<surface>-<nn>` and is added to the project's doc.

## Completion report

State the artifact, the screens and states rendered, the content fixtures,
the device or viewport, the decisions made, and the gates left to
engineering. Do not call product behavior complete because a design or
prototype looks right.

### Handoff rules

When the design is approved, the plan ends with the rules the build must
keep. One row each: `ID | rule | status | checked by`.

- Reuse the project's rule IDs. Mint `R-<surface>-<nn>` only for a decision
  the project has not recorded; a rewritten rule keeps its ID.
- `status`: `proposed` until a shipped screen or a failing fixture proves it,
  then `established`.
- `checked by`: `static` (source scan), `rendered` (real layout), or
  `manual` (review). Manual is a to-do for a guard, not a resting place.
- Existing violations are a shrink-only baseline, never a pass. A new rule
  starts at zero.
- What a static design cannot prove — timing, focus return, gesture feel,
  recovery — is a `NOT_RUN` gate owned by engineering.

Labels are part of the handoff: at most four words in English (five in the
product's other language), one fixed term per concept, no sentence labels.

Checks static guards cannot see are worth naming for the build: runaway
leading (at most 3× the font size), icons collapsed by a shadowed size token,
a sheet inset under 16px, targets under 44px, clipped or wrapped labels,
sideways scroll at the narrowest width, pinned chrome left uncovered, and the
primary flow's round trip.

The build either passes these rules or the rule was wrong. If a rule keeps
being waived, change the rule and its reason; do not quietly stop checking
it.
