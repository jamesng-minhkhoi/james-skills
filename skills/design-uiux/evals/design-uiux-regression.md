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
9. **Handoff as checkable rules** — repo `ugc/ugc`. "the creator info screen is
   approved. hand it to engineering." Expected: the plan above plus a
   handoff table that reuses the project's rule IDs and status, names how
   each rule is checked (static, rendered, manual), records existing
   violations as a shrink-only baseline, and marks what a static design
   cannot prove as `NOT_RUN` gates for engineering. No code.
10. **Correction becomes a rule** — repo `ugc/ugc`. "no scroll bar allow" on
    a filter row. Expected: rewrite the project's rule (the row fits the
    phone width; rarer cuts move to the bar's pull-down), apply it to the
    current options, and update the rule's reason. No separate log or
    appended contradiction. Promote it here only if it holds beyond this
    project.
11. **Deterministic diagnosis** — repo `cafe-web-next`. "the admin phone UI
    has a lot of issues. find what is wrong before redesigning it." Expected:
    the twelve-gate table before options, one verdict per gate with file:line
    evidence; `NOT_RUN` for rendered and device gates because no browser was
    run; findings sorted priority then gate. It finds the row body that looks
    pressed but only the title opens (`components/admin/mobile/mobile-list.tsx`),
    the duplicate create action in the toolbar and empty state on the mobile
    list screens, the row's own action repeated in its ⋯ sheet, the competing
    filled actions on an empty ingredients screen, and the raw palette and
    sub-12px map labels. No options before the table, and no `PASS` from taste.
12. **Rendered proof before a second showing** — repo `ugc/ugc`. "refine
    option B with my notes and show it to me again." Expected: rebuilds the
    picked option, then renders the real component (not the design canvas) at
    the widths the product ships, fills `L1`–`L5` with measured values, and
    states whether an independent critic scored the twelve gates at this
    showing or is deferred to handoff and why. Anything not rendered is
    `NOT_RUN`, never a pass.

13. **Touch-first edit sheet (neutral request)** — repo `petio/petio-mobile`.
    "redesign the medication edit sheet, show me via artifact." Fixture: the
    current sheet has − and + steppers, a Daily/Weekly/Monthly segmented
    control, a time chip, and a trash button beside Save. No hints in the
    prompt. Expected: values entered by drag, scrub, or swipe (any fitting
    control; a ruler is not prescribed); no segmented value entry in the
    sheet; Delete outside the Save row; a subject chip with the pet's name and
    photo in the sheet header; each gesture also has a visible control and an
    assistive path; new custom controls marked new; dividers between rows
    only; `rendered` not reached and gates `NOT_RUN` unless rendered.
14. **Rejected round and canvas hygiene** — repo `petio/petio-mobile`. "none
    of these work, try again", with a canvas holding boards A, B, C. Expected:
    the next publish removes A–C (keeping only references named). A variant
    where James picks B keeps B and removes A and C once he moves on.
15. **Project control wins** — repo with docs saying "use the iOS segmented
    control for frequency." Expected: keeps the segmented control, records the
    project rule as the reason, and does not apply the touch-first default.
16. **Glance sheet and picture hero** — repo `petio/petio-mobile`. "medications
    sheet with add and edit, and a weight screen." Expected: a glance sheet
    with an expand control to a dedicated screen; the weight screen's hero is
    an illustration or data picture, not a title, grey subtitle, and number
    stating the same thing.
17. **Combine two picks, add gestures** — repo `petio/petio-mobile`. After a
    round showing A (a viewer with a bottom toolbar: pet, Details, Share,
    More) and B (an info sheet dragged up over the document): "A and B look
    promising, though i dont want to limit only tap gesture. explore further
    to make it feel like iOS design and playful. remove unselected options
    first." The document is a multi-page PDF that scrolls vertically; the
    current screen shows a reading-status notice ("Peti is reading",
    "Peti couldn't read this"). Expected: the unpicked boards are removed; a
    gesture map precedes the gesture boards and names scroll as the owner of
    a vertical swipe on the page, so details open from a handle or the end of
    the last page, not a swipe up on the page; pull-to-close is live only at
    the top at normal zoom; a sideways next-file swipe either states its order
    for each entry point or is marked an open question; each destination
    keeps one standing control plus at most one custom gesture, and Delete
    has one visible home and is absent from press-and-hold; the current
    screen's status states are listed before the boards and each appears on
    one with its shipped string. A boundary-gated pull (at the top, past the
    end) passes; a swipe live mid-page fails.
18. **Assistant mark** — same repo, which has a mascot (Peti) drawn still on
    the sign-in screen. A board marks what the assistant read with a ✦
    sparkle; James once corrected that with "we can use peti mascot (without
    animation / like in login screen) here". The case prompt is a fresh
    "redesign the document detail screen, show me via artifact" with no
    correction given; score that first showing. Expected: the mascot's
    existing still art from the start, the same in every state, with state
    carried by a badge or text; no sparkle.
    Variant: the mascot exists only as an animated rig, so a still form is
    marked new and asked about, never invented.
19. **System gestures don't count** — "combine A and B" on a viewer where A
    closes by button plus pull-down and B adds the edge-swipe back. Expected:
    says edge back is a system gesture outside the limit, and ends with at
    most one custom gesture per destination. Variants: a list row with swipe
    for Edit and Delete plus a press-and-hold menu passes (the menu is a
    shortcut); a Details button plus a grabber on a separate sheet is two
    standing controls and is reduced to one.
20. **Single gesture on scrolling content** — repo `petio/petio-mobile`. "make
    the vaccine list feel more iOS: swipe up on the list to open the summary."
    The list scrolls vertically; one gesture is requested. Expected: a
    gesture map that names scroll as the owner of a vertical swipe; the
    summary moves to a handle or the end of the list, or the swipe is
    dropped with the reason.
21. **Second way in, no merge** — "refine option A, make the summary tappable
    too", where A already has a Details button opening the same view.
    Expected: names the second standing control into details and drops one;
    the slop check still runs before the showing.
22. **States in a gesture round** — "explore gestures for the document
    viewer", where the current screen shows reading and failed notices and
    the request mentions neither. Expected: the status states are listed
    before the boards and each is drawn with its shipped string.
23. **Seeded drift** — "refine option B" on a canvas whose note says "Hold
    menu: same items as More" while the boards differ, and whose menu board
    says "Change kind" where the locale file has "Change type". Expected: the
    next showing fixes the note to match the board and uses "Change type", or
    names the rename as a copy change.
24. **Promo card over artwork** — repo `petio/petio-mobile`. "the card
    background looks boring, add texture, and use the gradient from the
    other board but subtle so the text reads." James's corrections in the
    original session: "text on the card is hard to read", "the animation not
    clean enough and feel lazy work". Score the first showing. Expected: art
    at full strength with a scrim under the text (not the art faded to
    grey); faint texture; entry and loop on separate elements with one loop
    clock; stills at several timestamps; any ambient loop flagged against
    the project's motion doc.
25. **Pictures inside a sentence** — same card. "replace 'Unlock unlimited
    pets, memories, and documents' with inline chips." James's corrections:
    "avatars chips seem broken", "must use masked shapes here, not rounded",
    "more compact". Expected from the first showing: pets in their own
    shipped mask shapes, memory cards at the real card ratio, each picture no
    taller than the line and bound to its word, a 3× render checked, and an
    accessible label carrying the plain sentence.
26. **Short picker in a sheet** — same repo. "redesign the language sheet to
    include flags." James then asked for "scroll gesture like the iOS scroll
    selector". Expected on the first showing: a snapping wheel with flags,
    the title and Done previewing the centred language from the locale
    files, a haptic tick, tap-to-centre, an adjustable assistive path, and
    the trade-off (fewer options visible at once) stated; not a list of
    cards.
27. **"Clean like Apple" after rejections** — repo `petio/petio-mobile`.
    "improve this design for the vaccination screen", then "clean like apple
    would design a playful app". James rejected rings and a dial ("too
    childless and too playful"), then generic Apple Health cards ("its worse
    now than the inital versions"). Expected: refinement inside Petio's own
    sentence + chips, date tiles and tinted ground; after the second
    rejection the earliest liked round goes back on the canvas and James is
    asked what made it better.
28. **Optional details** — same flow, step 2 of the add sheet (clinic, lot,
    maker, notes). James called stacked text fields "not clean", then "bad,
    i prefer selectors/progressive disclosure pattern". Expected on the first
    showing: sentence chips opening menus (recents, makers for the chosen
    vaccine, Other…, a lot-sticker scan marked new), notes behind a link; no
    field stack.
29. **Menu in a sheet** — same board with a chip's menu open. The original
    showing drew the menu under the Lưu button and clipped by the sheet
    (James: "bad u can see the issue here"). Expected: the menu on the top
    layer, opening upward when the chip is low, uncut, no dim; a local
    capture looked at before publishing.
30. **Grouping by distance** — repo `LearningTime/emomo-redesign-task`
    (design docs in `docs/`, rule table `docs/global-rules.md`), Home: a question ("How was
    last night?") with three answer chips, then a row of four round shortcut
    buttons (Sleep, Feeding, Unwell?, Add), every block 20 pt apart. "fix
    spacing/padding please, show me on the canvas". James's corrections in the original session:
    "hard for me to understand what components relates/belong to what
    (Proximity Principle)". Expected on the first showing: gaps measured on
    a headless render of the board; the largest gap inside each group at most
    half the smallest gap between groups, in the project's spacing steps;
    the shortcut row set apart (wider gap, or a hairline because it does a
    different job) and shaped differently from the answers; gate 7 answered
    with the measured gaps and their rung stated as `declared` (a board
    capture), never `rendered`.
31. **Controls that do not read as controls** — same repo and screen;
    its rule table asks for skimming by picture (rule 56). "fix
    accessibility such as color / text" on the canvas. Input includes James's corrections: "these buttons
    needs icon or illustration its very hard to tell its an button", a
    growth icon nearly invisible on its tinted disc, and "padding issues" on
    a label touching its round button's edge. Expected: answers drawn as
    buttons in the product's own button style, with an icon each because the
    project's rule asks for it; icons and outlines measured
    against their real disc (3:1), with gradient-filled SVGs made solid;
    labels kept 8 pt clear of their shape's edge, with any reshaped control
    marked new; the answers and the round places still differ in shape; gate
    11 contrast given a measured verdict from the render (not `NOT_RUN` for
    lack of a device), with gate 11 left `NOT_RUN` if every measured part
    passes; the text audit not offered as proof of gate 11.
32. **Fade over the last content** — same repo. A Home board whose floating
    bottom bar carries a 116 px fade that starts above the bar and dims the
    last row of round buttons. "the bottom looks washed out". Expected:
    scroll to where the last content stops above the bar, measure the text
    there, move the fade to start at the bar's top edge, and re-measure.
In cases 33 onward, the quoted prompt is the input. "Corrections" are what
James said in the original session: context for the judge, never input.

33. **Words where a picture belongs** — repo `LearningTime/emomo-redesign-task`,
    Home: an "Emomo asks" caps label over the question, an answered state
    reading "You said: Not sure · today · Change", a source line "Prepared
    answer · checked by our paediatrician", and a sick card headed
    "Unwell · fever since this morning". Prompt: "make Home easier to
    parse, show me on the canvas". This is a screen redesign, so gates then
    options. Corrections: "use emomo avatar and make it like emomo saying
    without the text", "use visual over plain text like this. And align
    right", "use visual (such chips / icons etc..) and if its too confusing
    consider ... (?) info button", "use an icon/indicators instead of
    'unwell' text". Expected in every option shown, as a baseline rather
    than an option axis: the mascot avatar beside a speech bubble; her
    answer as a trailing reply bubble with the answer's icon and a visible
    way to change it; the source as one icon chip plus an (i) button that
    opens the full sentence; the sick label replaced by an icon indicator
    because "Fever since this morning" stays visible, so gate 9 still
    passes (the status explains the card; the action is "Check in now", so
    the label itself is not a state she must act on); each accessibility label written in the board's note. A judge
    accepts the one chip that replaces the source sentence and rejects a
    candidate that adds chips replacing no text.
34. **Main action on the leading side** — same repo. A health card with
    "Check in now" (primary) left of "What to watch for", and a left-aligned
    row "See the answer · Skip". Prompt: "main action must be on the
    right". A small fix. Correction: "should have been aligned right to
    comply uiux pattern for mobile". Expected: one proposal, with the
    secondary leading and the primary trailing in every pair, the
    text-button-plus-primary row aligned trailing, and every board swept
    and listed for other pairs. Single primaries stay centred or full width.
35. **One action where an object has several, and a vague edit mode** —
    same repo. A Journal cover with a "Change cover" pill, and an Edit Home
    board whose blocks keep their normal look, with an Add tile still in the
    shortcut row and 2 pt padding. Prompt: "fix the cover button and make
    Edit Home clearer". Corrections: "we can use ... icon here and have
    action change cover show in dropdown, we might also need action like
    remove, view and edit", "not good padding, confusing and unclear that
    we are in edit mode". Expected: the cover's action set derived and
    listed before drawing; a ••• button whose menu holds that set with
    remove last and apart; edit mode named in the header, with Done; every
    editable block carrying the same mark (a grabber, a badge, or a solid
    tinted outline, never dashes); out-of-mode controls removed; padding at
    least the normal screen's.
36. **Long progress as dots, placeholder as text** — same repo. "Nights
    plan · night 4 of 14" followed by 14 dots, and an Ask bar placeholder in
    ink 2 at medium weight. Prompt: "the nights dots and the Ask bar text
    look off". Corrections: "not good since too many dots. maybe ...
    circle progress bar", "this text is place holder, should have been
    dimmer". Expected: a small progress ring beside the count words, with
    dots kept only for counts of five or fewer; the placeholder at lower
    contrast than entered and secondary text, regular weight, 4.5:1 or
    better, on its own token marked new.
37. **A reference's feel flattened by the palette** — same repo; the
    moodboard screens are in `brand reference/Apps` (a health assistant,
    an AI UI kit, a planning app). Prompt: "they like Health assistant ·
    Good evening, AI UI kit, Planning app a lot. They want gradient blob,
    glass/neumorphic buttons to make the app feel modern and sleek. Show me
    options". Correction, after a first round drawn in the guideline's pale
    platform tints: "the blob still not design as how we vibe with the
    references". Expected on the first showing: the references' qualities
    named (a saturated core, two hues, a lit edge); each option on the
    canvas beside a board holding its reference; the palette's gap stated,
    with the nearest colours the guideline allows (its illustration
    palette) proposed and flagged as a stretch; text on the blobs measured.
38. **One-off tint and a missing material** — same repo, design-system
    board. The Add door alone has a pink disc. The "Picked" swatch lacks the
    corner sheen every other control has, because its fill is a raw hex.
    Prompt: "check the primitives board before I share it". Corrections:
    "why this one has pink color ?", "need faded edge (gradient like
    primary and tonal controls too)". Expected: the consistency count flags
    the single-use tint and the control missing its role's material before
    showing. The fix applies the material by role class or token, and
    either removes the tint or names it as a role marked new.
39. **Role collapse in a palette remap** — same repo. A repaint script maps
    an older palette onto the brand guideline's, and its map sends the
    placeholder grey `#74747B` onto ink 2 `#605E61`, which secondary text
    already uses. Prompt: "repaint every board to the new brand palette".
    Expected: before showing, the consistency count lists the role pairs an
    earlier fix separated (placeholder versus secondary text), flags this
    collapse, and proposes a distinct placeholder value at 4.5:1 or better.
40. **No photo yet** — any app with a user or child photo in its header.
    Prompt: "design the profile header". Expected: the states include no
    photo yet, drawn as a fallback illustration in the photo's shape plus an
    add control with a 44 pt hit area; never a grey silhouette or initials.
41. **A framing eyebrow** — same repo, the play-idea screen headed "Play
    idea for today · if you like · 3 min" above "Smile and wait". Prompt:
    "clean up this screen". Expected: the eyebrow removed per gate 8, with
    the 3 min kept in the idea's own meta line because nothing else shows it.
42. **Several actions on list rows** — any app. Prompt: "redesign my saved
    payment cards list; each card can be edited or deleted". Expected: swipe
    for Edit and Delete plus the detail screen with the same actions, per
    "Act on a list row"; no ••• button on every row.

## Rubric

Score each 0–2. The case number in brackets marks where a criterion matters
most; elsewhere score it only when it applies.

| Criterion | 2 means |
| --- | --- |
| Artifact | Proposes the Design artifact (canvas artboards at real device or viewport sizes); never an HTML page, Figma, or a doc; no code before approval |
| Options | Two to four genuinely different directions with a recommendation, then waits for the pick (1, 2, 4, 7, 8); a single scoped fix for a small fix (6) |
| Grounding | Reads the project's design docs, tokens, and real components first and rebuilds them faithfully; does not invent a new visual language or new components |
| Diagnosis | A redesign starts with the twelve-gate table, evidence beside every verdict, `NOT_RUN` where nothing was rendered, and findings sorted priority then gate; no `PASS` from taste (11) |
| Rendered proof | Before a repeat showing and at handoff, the sheet renders the real component at the shipped widths, `L1`–`L5` carry measured values, and `L6`–`L10` name what a fresh critic saw or `NOT_RUN`; a canvas screenshot is never offered as a render (12) |
| Research | Gathers references with a named question before designing creative or best-in-class work (3, 4, 7) |
| Slop | Avoids the tells James has named (shadows, borders, dividers, outlined wrappers, floating animation, decorative gradients, dashes, cluttered chips, stock-looking photos) and runs a consistency check |
| Fidelity | Final-quality design direction with real content and states, not a wireframe; static design locked before motion (3, 4) |
| Flow | Navigation map with what each step is and what back does; login only where an action needs it (5) |
| Proportion | Depth matches the request; no padding, no ceremony on a small fix |
| Handoff | The handoff carries rule IDs, status, and how each is checked, splitting static from rendered and manual; existing debt is a baseline, not a pass; unprovable behavior is a `NOT_RUN` gate (9) |
| Touch-first | Values and row actions are drag, swipe, scrub, or press-and-hold, each with a visible alternative; delete lives in a menu or swipe, not beside Save (13) |
| Subject | Entity-scoped screens and sheets show whose data it is visually (13) |
| Canvas hygiene | A rejected round is removed in the next publish; notes match their boards and labels match shipped strings (14, 23) |
| Gesture map | Each custom gesture names what already claims its motion and how it is resolved; no gesture is live mid-scroll in the scroll's direction (17, 20) |
| Destinations | One standing control per destination, at most one custom gesture, one visible home for delete, merged or not (17, 19, 21) |
| States carried | The current screen's status states are listed and drawn in every round (17, 22) |
| Grouping and affordance | Gaps measured on the render group parts before groups; every control looks tappable at rest; icons and outlines measured at 3:1 against their real background (30, 31) |
| Picture before words | Status, speaker, answer, and source lines are drawn as icon, avatar, bubble, or one chip, with a visible word wherever gate 9 needs one and each label in the board note; a long plan is a ring or bar; placeholder text has lower contrast than entered text (33, 36, 41) |
| Action order and action sets | Primary trailing in every pair; a standalone object with several actions gets a ••• menu with its derived set, while list rows keep swipe; an entered mode is named in the header and marked without dashes (34, 35, 42) |
| Reference feel | Options from named references are placed beside a board holding them; the qualities that make the reference are named and visible, and a palette gap is stated, not hidden (37) |
| Vocabulary | Names the highest proof rung reached and never calls an unobserved state pass |

## Must not have

A candidate fails regardless of rubric score if it contains any of these:

- an HTML page, Figma file, or doc in place of the Design artifact;
- product code before the direction is approved;
- one option when options were requested, or a single option dressed up as a
  choice;
- invented tokens, components, or type when the repository already has them;
- a wireframe or placeholder content presented as the final direction;
- any named slop tell, or a consistency check claimed without naming what was
  checked;
- a prose-only handoff when the project keeps a rule table or guard suite;
- a redesign critique with no gate verdicts, or a `PASS` on a rendered gate
  without a render;
- a canvas screenshot, thumbnail, or artboard export offered as rendered proof;
- a finding with no file:line evidence or measurement, or options offered
  before the diagnosis table;
- a new rule baselined, or an existing baseline raised, to make a check pass;
- a second rule minted where the project's doc already states one;
- a correction recorded only in chat, or appended as a contradiction;
- tap-steppers or a segmented control for entering a value in a sheet, or a
  standing Delete button next to Save, unless the project documents them
  (13, 15);
- a gesture with no visible control or no assistive path, or a rejected round
  left on the canvas (13, 14);
- a swipe on content that scrolls in the same direction, live mid-scroll (not
  gated to a boundary or a handle) as the trigger for another action (17, 20);
- two or more standing on-screen controls opening the same destination, or
  Delete in two visible homes (17, 21);
- a generic AI sparkle where the product has its own assistant character
  (18);
- text over artwork without a scrim, or the artwork faded to grey to make
  room for it; motion shown from a single still (24);
- an entity drawn in a default circle where the product has its own shape,
  or inline pictures taller than the line (25);
- a short choice in a sheet drawn as a tall list of cards when the request is
  about feel or polish (26);
- optional details drawn as a stack of text fields (28), or a menu under the
  primary button, clipped, or published without a capture being looked at
  (29);
- a third new direction drawn after two rejected rounds (27);
- a screen whose blocks all sit the same distance apart, or a spacing pass
  with no measured gaps (30);
- answer chips that read as labels, an icon under 3:1 on its disc, or a
  text-only contrast audit offered as proof that controls and icons pass
  (31);
- a fade judged at the top of the scroll only, or text left dimmed under
  it (32);
- a caps label, "You said:" line, or source sentence where the product has
  an avatar, bubble, icon, or chip to say it (33);
- a primary on the leading side of a pair, or a fix applied to one pair and
  not swept (34);
- a single-action pill on an object that has several actions, or an edit
  mode that looks like the normal screen (35);
- more than five progress dots for a plan, or placeholder text styled like
  entered text (36);
- reference-derived options shown without the reference beside them, or a
  palette limit applied silently until the reference's feel is gone (37);
- a tint used on one control only with no role, or a material missing from
  one control of its role (38);
- a palette remap that merges two roles an earlier fix separated (39);
- a grey silhouette or initials for a missing photo (40);
- a ••• button on every row of a list (42).

Accept a candidate only when its total is higher, it wins on Artifact,
Options, and Grounding in most cases, and it does not lose case 6.
