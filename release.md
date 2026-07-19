# Release Plan

## Current decision

Status: `BLOCKED — CHARTER APPROVAL; DOCUMENTATION CANDIDATE IN REVIEW`

QSO-STUDIO remains a documentation-first repository. This candidate adds Pages-ready source, architecture and workflow specifications, onboarding, security/privacy and accessibility requirements, operations guidance, ADR-0001, and a strict documentation-build workflow. It does not create a Studio application, authorize GitHub Pages publication, add live integrations, or grant runtime, repository-write, signing, approval, or payment authority.

## Versioning

- Scheme: Semantic Versioning after product scope, platform, integration contracts, license, privacy model, and distribution identity are approved.
- First possible documentation candidate: `0.0.1-charter.1`.
- First UI candidate: `0.1.0-alpha.1`, remaining pre-release until accessibility, security, integration, packaging, and workflow gates pass.
- No version may imply a published site, executable Studio, orchestration authority, or payment capability that is not present and verified.

## Release scope

### Charter/documentation candidate

- Approved users, workflow, non-goals, platform, data/privacy/license model, distribution target, ecosystem role, and authority boundaries.
- Truthful repository and publication status.
- Explicit separation of visualization, annotation, proposals, human approval, runtime execution, repository writes, signing, and payment operations.
- Reproducible accessible documentation artifact with security/privacy, checksum, provenance, recovery, and rollback evidence.
- Accepted ADR-0001 and one approved integration-manifest template.

### Later UI candidate

- Minimal accessible UI and one fixture-backed read-only evidence-review workflow.
- Versioned contracts for the selected record type, integrity, attribution, findings, comparison, exports, and errors.
- No direct credentials, execution, unrestricted repository writes, autonomous approval, or production payment authority.

## Selected completed work

The documentation toolchain, strict MkDocs build, artifact upload, and repository Consent Capacity Lock have passed on the candidate branch. The first site artifact was retained with a SHA-256 digest in `punchlist.md`. These are documentation-build milestones only; charter approval, publication, accessibility/security review, and release approval remain incomplete.

## Planned changelog entries

- `Documentation`: Pages-ready project, architecture, design, workflow, onboarding, security/privacy, accessibility, and operations guides.
- `Fixed`: replace unsupported publication claims with a truthful distinction between source, build artifact, and deployed site.
- `Architecture`: establish the proposed read-only evidence-review boundary.
- `Security`: bounded input, inert rendering, no-secret/no-write design, diagnostic redaction, and immutable consent-capacity policy.
- `Accessibility`: keyboard, focus, semantics, contrast, scaling, motion, visualization alternatives, and error recovery requirements.
- `Release`: strict build, artifacts, checksums, provenance, approval, and rollback evidence.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Product/UX charter | BLOCKED | Approve users, workflow, platform, ecosystem role, privacy/license model, distribution, support, and authority boundaries. |
| Documentation integrity | REVIEW | Every path, publication statement, workflow, and capability claim matches repository evidence. |
| Task completion | REVIEW | P0/P1 decisions and evidence are recorded; `punchlist.md` accurately reflects status. |
| Documentation build | PASS — CANDIDATE | Pinned strict build and artifact upload pass; final-head checks remain required before merge. |
| UI build/tests | NOT YET INCLUDED | Required only for a later UI candidate. |
| Security/privacy | REVIEW | Consent lock passed; documentation/workflow review remains, and application controls require later evidence. |
| Accessibility | REVIEW | Documentation review remains; application controls require later evidence. |
| Documentation | REVIEW | Setup, scope, architecture, design, workflow, limitations, accessibility, privacy, operations, and rollback are present and await human approval. |
| Provenance | REVIEW | Workflow, artifact, and digest are recorded; final review and source archive remain. |
| Publication | BLOCKED | Owner, canonical URL, environment approval, deployment verification, and rollback are approved. |
| Approval | PENDING | Explicit human approval after all included-scope gates pass. |

## Artifact requirements

### Documentation candidate

- exact commit SHA and source archive;
- pinned MkDocs configuration and strict build log;
- static-site artifact and checksum;
- link, accessibility, security/privacy, and authority-language review;
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

Withdraw a documentation candidate if it overlaps another repository, leaves execution/payment/privacy authority ambiguous, publishes unsupported capabilities, fails the strict build, exposes sensitive content, or cannot reproduce its artifact. Roll back a future implementation if the primary workflow fails, contracts drift, untrusted content executes, credentials or personal data cross the boundary, accessibility blocks use, artifacts are non-reproducible, severe security findings remain, or hashes differ.

Restore the prior verified artifact or remove publication, preserve failed-candidate evidence, and require full re-review before republishing.

## Unresolved blockers

- Approval of users, first workflow, platform/distribution, ecosystem role, privacy/retention, license, support/security ownership, and authority boundaries.
- Selection of one canonical record type, contract owner/version, integration manifest, and deterministic fixture set.
- Documentation accessibility, security/privacy, and authority-language reviews.
- Publication owner, canonical URL, environment reviewers, verification, and rollback rehearsal.
- Application architecture, implementation, tests, packaging, and release evidence remain future work.

## Release log

- 2026-07-16 — Established charter approval and documentation integrity as the first release gate.
- 2026-07-19 — Prepared a Pages-ready documentation candidate and strict build workflow without adding application or publication authority.
- 2026-07-19 — Strict documentation build, artifact upload, and Consent Capacity Lock passed on the candidate branch; human and architectural review remain required.
