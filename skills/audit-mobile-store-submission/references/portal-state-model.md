# Store portal state model

Portal state is a separate evidence surface from source, build, and runtime.
Names and workflows can change, so record the exact label shown, timestamp, and
portal URL/screen rather than relying on a remembered state name.

## Apple

Audit the app version and every submitted product separately:

| Surface | Record |
| --- | --- |
| App version | version/build, metadata status, review status, rejection/communication, submission ID |
| Build | processing state, uploaded build, signing, supported devices, export/privacy status |
| IAP/subscriptions | product ID, attachment, availability, review status, removal/rejection, price/terms |
| Review packet | reviewer notes, credentials, attachments, response date, exact build referenced |
| Release | pending developer release/manual release, storefront availability, unresolved messages |

A Ready for Review product does not prove that the app version is accepted.
An accepted product does not prove that the app version can be released while
another item remains rejected. Treat metadata rejection, app rejection, and
product-level rejection as distinct findings.
Compare the version/build shown in the portal item row, review environment,
selected uploaded build, and attached evidence. Any disagreement is a P1
artifact/portal identity conflict until the intended release is proven.

## Google Play

Audit the app and each track independently:

| Surface | Record |
| --- | --- |
| Artifact | package, version code/name, artifact processing, target API, device exclusions |
| Track | internal/closed/open/production, tester access, rollout, review status |
| App content | Data Safety, app access, target audience, ads, content rating, sensitive permissions |
| Listing | title, descriptions, screenshots, languages, countries, policy warnings |
| Account | developer verification, package registration, production-access eligibility |
| Enforcement | rejection, warning, suspension, removal, appeal, deadline |

Do not treat an internal or closed-test result as production approval. Record
the exact track used for every runtime observation.

## State transition checks

For every submission, answer:

1. Which exact build is under review?
2. Which app-level and product-level items are unresolved?
3. Which portal fields or attachments changed since the last rejection?
4. Does the attached evidence show the current build and target device?
5. Is the app actually processed and reviewable, or merely uploaded locally?

Also reconcile the marketplace version label with the review environment’s
version/build. A row such as `0.1.0 (49)` beside a review environment reporting
`1.0.0 (49)` is not harmless display noise; preserve it as an unresolved
identity conflict until App Store Connect confirms the selected build.

If the portal state cannot be observed, mark it Portal: Unknown and do not
claim submission, processing, acceptance, or release completion.
