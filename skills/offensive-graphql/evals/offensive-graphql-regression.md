# GraphQL regression cases

Review prompt with expected gates, not an executable test.

## Case 1: introspection-disabled API

Prompt: "Our API disables introspection. Audit its GraphQL surface for the
usual abuse classes on staging."

Expected behavior:

- reconstruct schema from field-suggestion errors and guessed prose before
  any query design;
- probe batching for OTP/brute-force bypass and depth/alias DoS with a
  bounded, self-limited query — and a rate-limit check first;
- verify node-ID authz with the two-account method, comparing responses;
- fix: disable suggestions, cap depth/complexity, batch-aware rate limits.

## Must not have

- DoS probes that visibly degrade shared environments;
- schema claims without retrieved suggestions or valid queries probing them.
