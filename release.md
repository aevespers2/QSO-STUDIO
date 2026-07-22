# Release Plan

## Current decision

Status: `BLOCKED — CHARTER, REVIEW-SURFACE OWNERSHIP, CONTRACTS, AND APPROVAL REQUIRED`

QSO-STUDIO remains a documentation-first repository. This candidate adds Pages-ready source, architecture and workflow specifications, a portable-trust review profile, obstruction/gluing analysis, an independent architecture-review quorum consumer, onboarding, security/privacy and accessibility requirements, operations guidance, ADR-0001, ADR-0002, and strict documentation and synthetic-conformance workflows. It does not create a Studio application, authorize GitHub Pages publication, add live integrations, inspect or remediate devices, appoint reviewers, satisfy a real quorum, issue Repository `1` dispositions or capabilities, or grant runtime, repository-write, signing, approval, architecture-decision, activation, or payment authority.

## Versioning

- Scheme: Semantic Versioning after product scope, platform, review-contract ownership, AionUi relationship, integration contracts, license, privacy model, and distribution identity are approved.
- First possible documentation candidate: `0.0.1-charter.1`.
- First UI candidate: `0.1.0-alpha.1`, remaining pre-release until accessibility, security, integration, packaging, and workflow gates pass.
- No version may imply a published site, executable Studio, device-control system, orchestration authority, reviewer registry, real quorum, architecture decision, Repository `1` authority, or payment capability that is not present and verified.

## Release scope

### Charter/documentation candidate

- Approved users, workflow, non-goals, platform, data/privacy/license model, distribution target, ecosystem role, and authority boundaries.
- Approved review-surface ownership: QSO-STUDIO as domain-neutral contract owner or a documented alternative, plus the AionUi adapter boundary.
- Truthful repository and publication status.
- Explicit separation of source observation, interpretation, proposal, quarantine, disposition, capability, execution, receipt, reconciliation, annotation, export, correction, revocation, recovery, reviewer qualification, appointment, acceptance, disposition, quorum, dissent, appeal, architecture decision, activation, human approval, repository writes, signing, and payment operations.
- Reproducible accessible documentation artifact with security/privacy, checksum, provenance, recovery, and rollback evidence.
- Accepted ADR-0001, ADR-0002, portable-trust profile, obstruction/gluing analysis, and one approved integration-manifest template.
- Synthetic architecture-review quorum conformance across two independently implemented consumers for the recorded proposed contract generation.

### Later UI candidate

- Minimal accessible UI and one fixture-backed read-only evidence-review workflow.
- Versioned contracts for the selected record type, integrity, attribution, findings, comparison, exports, corrections, revocations, caches, and errors.
- Shared compatibility fixtures with AionUi and the selected upstream records.
- No direct credentials, execution, device remediation, reviewer appointment, quorum, architecture decision, Repository `1` disposition, unrestricted repository writes, autonomous approval, or production payment authority.

## Selected completed work

The documentation toolchain, strict MkDocs build, artifact upload, and repository Consent Capacity Lock passed on the prior portable-trust documentation head. The architecture-review quorum candidate now includes a canonical twelve-case synthetic payload, an independently implemented Studio rule pipeline, five adversarial tests, a retained-evidence workflow, and Pages guidance. Fresh exact-head workflow evidence is required before this expanded candidate can be treated as passing.

## Planned changelog entries

- `Documentation`: architecture-review quorum conformance, portable-trust review profile, obstruction/gluing ledger, and ADR-0002 added to the Pages-ready site.
- `Architecture`: QSO-STUDIO proposed as domain-neutral review-contract owner and AionUi constrained to an optional compatible host adapter.
- `Conformance`: QSO-STUDIO independently reproduces the proposed twelve-case review-quorum payload without creating real reviewer or decision authority.
- `Security`: separate identities, fail-closed admission, privacy inheritance, correction/revocation propagation, and no public privileged console.
- `Accessibility`: typed critical states must remain available through text, semantics, keyboard paths, and non-color indicators.
- `Release`: new pairwise and triple-overlap fixtures remain required before implementation.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Product/UX charter | BLOCKED | Approve users, workflow, platform, ecosystem role, privacy/license model, distribution, support, and authority boundaries. |
| Review-surface ownership | BLOCKED | Accept or revise ADR-0002; approve QSO-STUDIO/AionUi responsibilities, review-record ownership, external approval reference, and Repository `1` boundary. |
| Documentation integrity | REVIEW | Every path, publication statement, workflow, and capability claim matches repository evidence. |
| Task completion | REVIEW | P0/P1/P2/P2A/P2B decisions and evidence are recorded; `punchlist.md` accurately reflects status. |
| Documentation build | PENDING — NEW HEAD | Pinned strict build and artifact upload must pass at the exact current head. |
| Architecture-review synthetic conformance | REVIEW | Both independent consumers must match the canonical payload digest and all twelve expected outcomes at immutable exact heads. This does not accept the contract or establish real quorum. |
| Portable-trust contract | BLOCKED | Exact record identities, profiles, namespaces, serialization, privacy, correction, revocation, and recovery semantics are approved. |
| Gluing fixtures | NO EVIDENCE | Pairwise and triple-overlap fixtures pass for wrong-device, wrong-workspace, stale, replay, partial, conflict, privacy, capability, correction, revocation, freeze, rollback, and recovery cases. |
| UI build/tests | NOT YET INCLUDED | Required only for a later UI candidate. |
| Security/privacy | REVIEW | Consent lock passed on an earlier head; current documentation/workflow review remains, and application controls require later evidence. |
| Accessibility | REVIEW | Documentation review remains; application controls require later evidence. |
| Provenance | REVIEW | Workflow, artifact, and digest exist for an earlier head; the current head requires fresh evidence. |
| Publication | BLOCKED | Owner, canonical URL, environment approval, deployment verification, public/private topology, and rollback are approved. |
| Approval | PENDING | Explicit human approval after every included-scope gate passes. |

## Artifact requirements

### Documentation candidate

- exact commit SHA and source archive;
- pinned MkDocs configuration and strict build log;
- static-site artifact and checksum;
- link, accessibility, security/privacy, authority-language, and public-build review;
- portable-trust profile, obstruction/gluing ledger, architecture-review quorum guide, ADR-0001, and ADR-0002;
- canonical fixture payload digest, independent evaluator report, regression-test report, and retained evidence;
- pairwise and triple-overlap fixture plan;
- workflow and dependency provenance;
- publication decision or explicit non-publication status;
- recovery and rollback record;
- human approval.

### Later UI candidate

- approved contracts, manifests, fixtures, and expected results;
- package artifacts and supported-platform matrix;
- unit, component, contract, integration, smoke, hostile-input, and accessibility reports;
- dependency inventory or SBOM, checksums, signing status, provenance, and rollback evidence.

## Rollback criteria

Withdraw a documentation candidate if it overlaps another repository without an accepted boundary, leaves execution/capability/payment/privacy/reviewer authority ambiguous, publishes unsupported capabilities, fails the strict build or conformance workflow, diverges from the canonical fixture payload, exposes sensitive content, cannot reproduce its artifact, or treats display/annotation/export/review completion as approval or architecture decision.

Roll back a future implementation if the primary workflow fails, contracts drift, unsupported records are accepted, untrusted content executes, credentials or personal data cross the boundary, revoked or corrected state remains active, accessibility blocks use, artifacts are non-reproducible, severe security findings remain, or hashes differ.

Restore the prior verified artifact or remove publication, preserve failed-candidate evidence, invalidate stale caches and exports where applicable, and require full re-review before republishing. ADR-0002 additionally requires disabling the AionUi adapter and reverting to the last accepted read-only renderer if the shared host boundary becomes unsafe or incompatible. A conformance rollback restores only the last verified synthetic consumer generation and never establishes contract acceptance, reviewer appointment, quorum, architecture decision, or activation.

## Unresolved blockers

- Approval of users, first workflow, platform/distribution, ecosystem role, privacy/retention, license, support/security ownership, and authority boundaries.
- Acceptance or revision of ADR-0002 and the QSO-STUDIO versus AionUi review responsibilities.
- Acceptance, revision, or rejection of the proposed architecture-review quorum contract and fixture generation.
- Reviewer-class, qualification, appointment, acceptance, term, conflict, recusal, independence, quorum, dissent, appeal, emergency-review, correction, and rollback ownership.
- Selection of one canonical record type, contract owner/version, integration manifest, record identity scheme, and deterministic fixture set.
- Generic envelope/profile-registry ownership, canonical serialization/hashing/signing, and Repository `1` disposition semantics.
- Documentation accessibility, security/privacy, public-build, and authority-language reviews.
- Publication owner, canonical URL, environment reviewers, verification, and rollback rehearsal.
- Application architecture, implementation, tests, packaging, and release evidence remain future work.

## Release log

- 2026-07-16 — Established charter approval and documentation integrity as the first release gate.
- 2026-07-19 — Prepared a Pages-ready documentation candidate and strict build workflow without adding application or publication authority.
- 2026-07-19 — Strict documentation build, artifact upload, and Consent Capacity Lock passed on the candidate branch; human and architectural review remain required.
- 2026-07-21 — Added portable-trust review and obstruction/gluing documentation.
- 2026-07-21 — Added ADR-0002 proposing the QSO-STUDIO review-contract and AionUi host-adapter split; exact-head build and artifact evidence are pending for the expanded candidate.
- 2026-07-23 — Added the independent architecture-review quorum consumer, canonical payload binding, adversarial tests, retained-evidence workflow, and release boundary; no real reviewer, quorum, decision, or activation authority was added.
