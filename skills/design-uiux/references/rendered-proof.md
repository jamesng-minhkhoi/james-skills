# Rendered proof

Use before every showing after the first, and again before handoff. The twelve
gates decide whether the design is right; this sheet proves what was actually
rendered, at which widths, and what a second pair of eyes saw. Source
inspection cannot answer either.

## Build the sheet

Render the real page or artboard, not a thumbnail, at the widths the product
ships:

- mobile: 375 and 390 wide;
- web: 390, 768, and 1440;
- plus any width the project names, or where the layout changes.

Put the captures in one sheet, in that order, and keep the page itself open for
anything the sheet shrinks. A screenshot of a design canvas is not a render;
the browser must run the real component with real content.

## Measured items

These are facts, not taste. Record the value beside the verdict.

| # | Check | Passes when |
| --- | --- | --- |
| L1 | No sideways page scroll | `scrollWidth` ≤ `clientWidth` at every width; a wide table scrolls inside its own region |
| L2 | Targets are reachable | Every visible control is at least 24 px in both directions; 44 px on touch; inline text links exempt |
| L3 | Clean load | No console error, blocked request, missing local file, broken socket, or failed image |
| L4 | Images resolve | Every image has a non-zero natural width; lazy images are forced eager and the page scrolled before measuring |
| L5 | Not blank | The body has text and visible content, not an empty shell or a spinner that never settles |

A failed measured item is fixed at the source and re-rendered. Never waive it
with a judgment, and never hide an error handler to make the count zero.

## Eye items

These need a person or a fresh-context critic. Cite the element or measurement
that decided each one.

| # | Check | Passes when |
| --- | --- | --- |
| L6 | Shape reads at 375 | The screen's job and its one primary action are clear without hunting |
| L7 | Copy is honest | No invented metric, logo, quote, person, or placeholder that reads as real |
| L8 | States exist | Empty, loading, error, long-content, and first-use are built or declared out of scope |
| L9 | Density and rhythm hold | At 25% zoom the page reads as deliberate groups; type, radius, and spacing share one scale |
| L10 | Someone else scored it | A critic who did not build it scored the twelve gates with cited evidence, once before handoff and again after any gate regresses |

Each eye item maps to a gate: L6 → 1 (Job) and 2 (One primary); L7 → 8 (Words);
L8 → 9 (State and motion); L9 → 7 (Hierarchy) and 10 (System); L10 → 12
(Proof). A disagreement between the critic and the builder becomes `NOT_RUN` or
a finding, never a tie.

## Hand-over block

Return these fields, keeping failures and skipped checks visible:

```text
EVIDENCE: <sheet path, plus the page path>
WIDTHS: <the widths rendered>
MEASURED: <L1-L5 lines with values, or NOT_RUN with the reason>
EYE_ITEMS: <L6-L10: what was seen, per width, or NOT_RUN>
CRITIC: <who scored it and their verdict, or NOT_RUN>
NOT_VERIFIED: <screen readers, real devices, states not built, anything skipped>
```

Without a browser, write exactly:

```text
LOOK: NOT_RUN (no browser) — capture the widths the product ships with the host's own tool
```

Then capture the same widths by hand, look at them, and list `L1`–`L5` as
`NOT_RUN` with the reason. A zero exit never means "looks good"; it means the
machine items ran.

## Failure modes

| Symptom | Correction |
| --- | --- |
| Only the design canvas was captured | Render the real component in a browser at the listed widths |
| The sheet passes but the page is blank | Check L5 and L3; a clean screenshot of an empty shell is still blank |
| Fine detail is unreadable on the sheet | Open the page at that width and crop; never grade thumbnails |
| The builder scored their own work | Hand the sheet and rubric to a fresh subagent or session |
| A state was described but not built | Build it as its own entry and render it, or declare it out of scope |
| An external font or image was blocked | Bundle the asset into the page folder and re-render |

## Changing this reference

Add an item only when a real handoff missed something a person could see or a
browser could measure. Keep the measured and eye items separate; a machine
check must never be used to claim taste.
