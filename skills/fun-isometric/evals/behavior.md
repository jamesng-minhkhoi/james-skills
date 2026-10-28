# fun-isometric behavior cases

Review prompts with expected behavior, for changing this skill.

## Case 1: animated sticker icon

Prompt: "I need a playful animated rocket icon for my pricing page's empty
state," (React app provided).

Expected behavior:

- name the object and its verb (a rocket launches), pick the preset from the
  table by the verb, not the object;
- draw parts in the 500-unit square at palette slots (`fill: 'ok'`), never hex
  baked into fills, with the 5px ink outline and slab extrusion (`depth: 1`);
- motion comes from a preset or `spark()` — never a hand-written sine loop or
  CSS wobble; at least one child part lags (`at` +4 to +6, `k` .6–1.4);
- pop in with scale, never opacity;
- render and inspect with `fi sheet` / `fi frame` and iterate on `fi check`
  until it passes before calling it done.

## Case 2: pick a loop length

Prompt: "Let's fill the loop with a gentle wobble so it never stops moving."

Expected behavior:

- refuse: loops run 123–180 frames at 60fps with the action in the first half
  and a **still hold** after it — the hold is the feel, and idle wobble over
  the hold is explicitly forbidden by the skill's Rules section.
