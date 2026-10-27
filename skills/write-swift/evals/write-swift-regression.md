# Write Swift regression cases

Use these forward-test fixtures when changing the `write-swift` skill. They
are review prompts with expected gates, not executable tests.

## Case 1: Swift 6 strict concurrency migration

Prompt: "Migrate this Swift service to Swift 6 strict concurrency without
breaking behavior." (code provided)

Expected behavior:

- model data with value types first; fix sharing before adding actors;
- use structured concurrency and the modern attributes (`@concurrent`,
  main-actor-by-default) rather than scattering `@MainActor` and
  `DispatchQueue` patches;
- resolve Sendable errors by reducing sharing, not by blanket
  `@unchecked Sendable`;
- keep failure paths visible (typed errors over optional flattening).

## Case 2: retain cycle / hang diagnosis

Prompt: "This Swift feature hangs on the main actor after the refactor."

Expected behavior:

- name the blocking call chain before proposing a fix;
- distinguish a genuine data race from an actor-hop deadlock;
- propose the smallest correct concurrency shape, with the reasoning.

## Must not have

A completion claim fails if it contains any of these:

- `@unchecked Sendable` or `nonisolated(unsafe)` as a first resort;
- a migration that "compiles" without addressing shared mutable state;
- deprecated patterns (completion handlers over async, global queues) when a
  modern equivalent exists in the skill.
