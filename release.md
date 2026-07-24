# Release Plan

`QSO-STUDIO-DOCS-CANDIDATE-001`

## Current decision

Status: `BLOCKED — DOCUMENTATION, ACCESSIBILITY-EVIDENCE, AND SYNTHETIC CONFORMANCE CANDIDATES IN REVIEW; PRODUCT CHARTER AND PUBLICATION APPROVAL REQUIRED`

QSO-STUDIO has a bounded documentation candidate, an exact-artifact accessibility review protocol, and two current-main synthetic consumers: an independently implemented QSO-FABRIC manifest consumer and an independently implemented QSO Field architecture-review consumer. The documentation includes a truthful front door, product and UX charter, architecture, accessible diagrams, read-only review workflow, integration map, onboarding, developer guidance, accessibility and security/privacy requirements, punch list, deterministic checks, and hostile regressions. The accessibility protocol is `DOCUMENTED_NOT_CERTIFIED`. Neither it nor either consumer is **an authorized Pages publication, accessibility certification, application, package, ecosystem admission, interface acceptance, reviewer registry, architecture authority, or release**.

## Versioning

- Scheme: Semantic Versioning after product scope, platforms, integration contracts, license, privacy model, and distribution identity are approved.
- First possible documentation candidate: `0.0.1-charter.1`.
- First UI candidate: `0.1.0-alpha.1`, remaining pre-release until accessibility, security, integration, packaging, and workflow gates pass.
- No version may imply a site, executable Studio, accessible certification, admitted component, accepted interface, reviewer appointment, real quorum, architecture decision, orchestration authority, repository authority, or payment capability that is not present and verified.

## Included documentation scope

- Product purpose, readers, first workflow, principles, non-goals, and open decisions.
- Architecture and trust boundaries with prose-equivalent diagrams.
- Fixture-oriented read-only evidence-review sequence and evidence-state vocabulary.
- Candidate integration corridors and exact contract-tuple requirements.
- Independent manifest-consumer documentation bound to QSO-FABRIC PR #21 at exact head `25036a5cfcea79e204a4660ddd1af09c054935b1`.
- Independent architecture-review consumer documentation bound to QSO Field PR #24 at exact head `a56b1fa93f151ee14f3cdd4183b89a10e268e352`.
- Onboarding and developer contribution paths.
- Accessibility requirements and an exact-artifact review-evidence protocol covering source Markdown, rendered Pages, synthetic consumers, and a future UI.
- Explicit evidence states, authority states, manual-review methods, documentation-only record template, fail-closed stop conditions, correction, withdrawal, supersession, and rollback.
- Security, privacy, licensing, attribution, correction, withdrawal, supersession, and rollback expectations.
- Aligned README, task chain, punch list, release plan, and changelog.
- Deterministic documentation and consumer checks with hostile regressions.

## Excluded scope

- UI or executable implementation.
- Accessibility certification without exact rendered and manual evidence.
- Production credentials, restricted source data, direct runtime controls, repository mutation, autonomous approvals, reviewer appointments, architecture decisions, ecosystem admission, namespace/schema acceptance, payment settlement, release signing, or deployment.
- GitHub Pages publication without a separate authorized source, workflow, review record, and rollback plan.
- Acceptance of upstream schemas, namespaces, adapters, conformance levels, governance semantics, reviewer populations, or ownership.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Product/UX charter | BLOCKED | Explicitly accept or revise users, workflow, platforms, ecosystem role, privacy/license model, distribution, and authority boundaries. |
| Documentation integrity | REVIEW | Required pages, links, planning controls, maturity labels, and authority notices pass at the final exact head. |
| Accessibility protocol | DONE | Requirements, evidence/authority states, exact-artifact binding, manual methods, record template, stop conditions, correction, supersession, withdrawal, and rollback are documented without claiming certification. |
| Rendered accessibility evidence | BLOCKED | One exact rendered artifact must receive keyboard, focus, screen-reader, zoom/reflow, contrast, reduced-motion, cognitive-comprehension, graph/timeline, and error-recovery review with limitations and correction links. |
| Security/privacy | REVIEW | Public materials remain synthetic and non-sensitive; final review and ownership remain required. |
| Ecosystem consumer source identity | REVIEW | Exact producer head, Git blob, SHA-256, local fixture bytes, resolver/verifier separation, and independent parser/evaluator agree. |
| Ecosystem consumer regressions | REVIEW | Duplicate keys, non-finite values, type confusion, unsafe defaults, unknown fields, identity drift, stale tuples, and authority promotion fail closed. |
| Architecture-review source identity | REVIEW | QSO Field PR #24 exact head, workflow, retained artifact, fixture blobs, local raw bytes, resolver/verifier separation, and supersession chain agree. |
| Architecture-review regressions | REVIEW | Stale or moved heads, wrong paths, historical evidence represented as current, duplicate keys, non-finite values, unknown fields, byte drift, self-review, missing appointment, quorum failure, dissent loss, appeal defects, emergency broadening, and decision promotion fail closed. |
| Integration consistency | BLOCKED | Runtime-local versus Fabric-level namespace and payload ownership, correction, withdrawal, migration, overlap, and rollback are unresolved. |
| Pages publication | BLOCKED | Source, permissions, approval, exact artifact, accessibility/security/privacy/license evidence, rollback, and resulting-route verification are not authorized. |
| Provenance | REVIEW | Exact-head workflows must retain source identity, deterministic input hashes, tests, artifact metadata, and correction or supersession links. |
| Approval | PENDING | Separate charter, architecture, publication, release, accessibility-certification, and later implementation decisions are required. |

## Artifact requirements

- Exact source commit and documentation file manifest.
- Exact QSO-FABRIC and QSO Field producer tuples and fixture digests.
- Documentation integrity and hostile-regression reports.
- Both consumer results and independent regression outputs.
- Internal-link and diagram-alternative results.
- Deterministic input hashes and retained evidence artifacts.
- Accessibility review record identifying exact source, build, artifact digest, route, environment, methods, results, reviewer role, limitations, and correction/supersession state.
- Security/privacy, licensing, and attribution review records.
- Publication target and rollback record if publication is later approved.
- Resulting-route verification after any authorized publication.

## Rollback criteria

Withdraw the documentation, accessibility claim, or either consumer candidate when it makes an unsupported publication, certification, capability, admission, appointment, quorum, decision, or compatibility claim; merges proposal and authority states; loses source provenance; binds a moved producer tuple without supersession; hides a correction or withdrawal; introduces inaccessible navigation or diagrams; presents partial, unknown, blocked, stale, or superseded accessibility evidence as a pass; includes restricted data; or cannot be reproduced. Restore the prior verified documentation state, mark affected routes stale or withdrawn, preserve failed candidate evidence, and require a new exact-head generation.

## Unresolved blockers

- Product/UX charter approval.
- Platform and distribution identity.
- License and contribution policy.
- Documentation, accessibility review/certification, privacy, security, integration, publication, evidence, and rollback ownership.
- Exact rendered accessibility evidence for any future public artifact or UI.
- Accepted exact upstream contract generations and the first synthetic fixture envelope.
- Runtime-local versus Fabric-level record-role collision.
- Neutral contract, namespace, schema, reason-code, correction, migration, review-governance, and evidence custody.
- Pages publication decision and resulting-route verification.

## Release log

- 2026-07-16: Established charter and documentation integrity as the release prerequisite.
- 2026-07-23: Added the `QSO-STUDIO-DOCS-CANDIDATE-001` documentation candidate; no publication, application, or release was authorized.
- 2026-07-23: Rebound the independent ecosystem-manifest consumer from stale PR #4 onto current `main` and the current QSO-FABRIC PR #21 head; no admission, interface acceptance, runtime authority, or release was authorized.
- 2026-07-23: Extracted the preserved architecture-review consumer from stale PR #4 onto current `main` and rebound it to current QSO Field PR #24 evidence; no appointment, real quorum, decision, activation, merge, or release authority was authorized.
- 2026-07-23: Added the exact-artifact accessibility review-evidence protocol; no rendered artifact, interface, publication, accessibility certification, or release was authorized.

This release plan is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
