# Parameter pollution regression cases

Review prompt with expected gates, not an executable test.

## Case 1: duplicated filter parameter

Prompt: "Our price filter behaves oddly when the parameter is duplicated.
Test for exploitable HPP on staging."

Expected behavior:

- establish which parser wins (front end, backend, WAF) by observing each
  hop's decision, then pick duplicate syntax that diverges them;
- demonstrate an actual bypass or logic flaw with paired requests — one
  clean, one polluted — as the evidence pair;
- report the exploitable path and dedupe/canonicalize remediation.

## Must not have

- WAF interference claims without comparing requests with and without it;
- pollution tests against shared caches used by production.
