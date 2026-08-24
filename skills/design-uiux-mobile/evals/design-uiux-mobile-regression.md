# Design UIUX Mobile regression evaluation

Use this benchmark when changing the skill. Compare the previous skill and the
candidate skill with the same prompt, product context, repository evidence,
and screenshots. Keep the evaluator blind to which version produced each
answer where practical.

## Benchmark cases

1. **Static settings form** — A privacy or notification settings screen with no
   meaningful navigation gesture. The candidate must not invent animation or
   gesture requirements.
2. **Swipe-to-archive list** — A frequent, reversible list action. Check
   discoverability, visible progress, commit/cancel behavior, undo, and a
   non-gesture alternative.
3. **Card-stack browsing** — A local exploration flow. Check within-page
   continuity, position awareness, partial next-content cues, and accidental
   swipe handling.
4. **List-to-detail route** — A durable detail destination. Check
   between-page hierarchy, back symmetry, source-context preservation, focus,
   and interruption.
5. **Sheet over a scroll view** — A contextual filter or editor. Check gesture
   ownership, nested scrolling, safe area, keyboard, dismissal, and apply/cancel.
6. **Offline submission** — A form that can fail after the user commits. Check
   pending, success, recoverable error, rollback, preserved input, and whether
   motion incorrectly implies success.
7. **Web dashboard translation** — A dense desktop reference moving to mobile.
   Check hierarchy, explicitness, content shape, and whether web hover behavior
   is translated into touch-accessible feedback.
8. **AI-generated card soup** — A visually busy mobile home screen. Check
   subtraction, focal point, primary action, progressive disclosure, and whether
   personality is earned rather than added as decoration.

## Scoring

Score each case from 0 to 3 on:

- intent and flow clarity;
- explicitness and discoverability;
- state and recovery coverage;
- appropriate motion choice;
- gesture ownership and conflict handling;
- cancellation and reversibility;
- accessibility and reduced motion;
- native implementation practicality;
- visual hierarchy and subtraction;
- preservation of product contracts.

Apply a penalty of 1 for each material instance of unnecessary animation,
gesture-only core behavior, speculative business-logic change, or a motion
instruction that cannot be implemented or verified.

## Acceptance gates

Accept the candidate only when:

- it improves the swipe, card-stack, route, and sheet cases;
- it does not regress the static settings or offline-submission cases;
- it explicitly chooses no motion when motion has no job;
- it defines progress, threshold, cancellation, conflict, fallback, and
  reduced-motion behavior for applicable gestures;
- it produces more actionable guidance, not merely a longer response.

After the text evaluation, validate at least one applicable interaction in the
real app. Observe rest, in-progress, threshold, completion, cancellation,
conflict, reduced motion, interruption, and runtime performance. Screenshots,
lint, and type checks support the review but cannot prove gesture quality.
