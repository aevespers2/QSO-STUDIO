# Release Plan

## Current Decision

Status: `BLOCKED — PRODUCT/UX CHARTER AND PUBLICATION EVIDENCE`

QSO-STUDIO now has a static documentation candidate describing a proposed read-only evidence-review surface, but it does not have an approved product/UX charter, verified application, authorized Pages deployment, or release evidence. P0 remains blocked on approval; `punchlist.md` is absent; and the candidate lacks reproducible publication, link/HTML, accessibility, security/privacy, provenance, checksum, rollback, and repository-specific acceptance reports.

## Versioning

- Scheme: Semantic Versioning after product scope, platforms, integration contracts, license, privacy model, and distribution identity are approved.
- First possible documentation candidate: `0.0.1-charter.1`.
- First UI candidate: `0.1.0-alpha.1`, remaining pre-release until accessibility, security, integration, packaging, and workflow gates pass.
- No version may imply a deployed site, executable Studio, orchestration authority, repository-write authority, or payment capability that is not present and verified.

## Release Scope

### Charter/documentation candidate

- Approved users, workflows, non-goals, platforms, data/privacy/license model, distribution target, ecosystem role, and authority boundaries.
- Accurate repository and publication map.
- Explicit separation of visualization, annotation, proposals, human approval, runtime execution, repository writes, credentials, and payment records.
- Static project guide, architecture documentation, and Pages-ready source.
- Reproducible accessible documentation artifact with security/privacy, checksums, provenance, and rollback.

### Later UI candidate

- Minimal accessible UI and one fixture-backed read-only evidence-review workflow.
- Versioned contracts for genomes, state/evidence, messages, proposals, freeze points, attribution, and errors.
- No direct credentials, execution, unrestricted repository writes, autonomous approval, or production payment authority.

## Selected Completed Work

No work is selected for release. The README, project guide, architecture reference, static site source, and stylesheet are candidate documentation assets, but charter approval and retained verification evidence are absent.

## Planned Changelog Entries

- `Documentation`: approved product/UX charter, workflows, platforms, trust boundaries, onboarding, and verification strategy.
- `Fixed`: accurate Pages/publication wording and capability statements aligned with repository evidence.
- `Added`: reproducible documentation artifact and, after separate approval, one read-only workflow.
- `Security`: credentials, untrusted rendering, parser limits, storage, network, dependencies, workflow permissions, repository writes, and privacy.
- `Accessibility`: keyboard, focus, semantics, contrast, scaling, motion, visualization alternatives, and error recovery.
- `Release`: artifacts, SBOM where applicable, checksums, provenance, rollback evidence, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Product/UX charter | BLOCKED | Approve users, workflows, platforms, ecosystem role, privacy/license model, distribution, and authority boundaries. |
| Documentation integrity | PARTIAL | Current paths and capability wording are accurate in the candidate; final review must verify every statement against the merge commit. |
| Task completion | FAIL | P0 is `DONE`; `punchlist.md` exists and included work has evidence. |
| Documentation build | NO EVIDENCE | An approved workflow or documented manual process produces a reproducible artifact from one immutable commit. |
| Publication | NOT AUTHORIZED | Pages deployment target and workflow require approval before activation. |
| UI build/tests | NOT YET INCLUDED | Required for a later UI candidate: install/build/static, unit/component/contract/integration/smoke checks pass. |
| Security/privacy | NO EVIDENCE | Credential, rendering/parser, storage, network, dependency, secret, CI, repository-write, and privacy checks pass. |
| Accessibility | NO EVIDENCE | Keyboard, focus, semantics, labels, contrast, scaling, reduced motion, alternatives, and error states pass. |
| Documentation | PARTIAL | Purpose, authority, architecture, onboarding, and limitations are drafted; approval, publication commands, operations, and rollback evidence are incomplete. |
| Provenance | NO EVIDENCE | Commit, tools/platforms, commands, artifacts, hashes, SBOM, publication target, and attestations are retained. |
| Approval | PENDING | Explicit release approval after all included-scope gates pass. |

## Artifact Requirements

- Approved product/UX charter, authority model, architecture/workflow diagrams, privacy model, and contract map.
- Reproducible documentation artifact and source archive.
- Documentation-integrity, link, accessibility, security/privacy, build, and smoke reports.
- SHA-256 checksum manifest, provenance record, publication evidence, and rollback procedure.
- For later UI work: versioned schemas/fixtures, package artifacts, tests, SBOM, signing status where applicable, checksums, provenance, and rollback evidence.

## Rollback Criteria

Withdraw a charter candidate if it overlaps another repository, leaves execution/payment/privacy authority ambiguous, or publishes unsupported capabilities. Roll back documentation publication if links, accessibility, claims, privacy/security, artifact integrity, or reproducibility fail. Roll back later implementation if the primary workflow fails, contracts drift, untrusted content executes, credentials or personal data cross the boundary, accessibility blocks use, artifacts are non-reproducible, severe security findings remain, or hashes differ. Restore the prior verified artifact/tag and preserve failed-candidate evidence.

## Unresolved Blockers

- Approval is required for the product/UX charter, platform/distribution target, ecosystem role, privacy/license model, user groups, and authority boundaries.
- `punchlist.md` and accepted Builder evidence are absent.
- The static `docs/` source exists, but no Pages workflow or publication target is approved or verified.
- No documentation build, link/HTML report, accessibility report, security/privacy report, provenance manifest, checksum set, or rollback artifact exists.
- No UI implementation, schemas, fixtures, component tests, or executable integration is included.
- Payment and orchestration views must remain read-only and evidence-based until upstream contracts and authority approvals exist.

## Release Log

- 2026-07-16: Aligned the candidate with the product/UX charter and documentation-integrity gate; no release-ready work selected.
- 2026-07-19: Added a Pages-ready documentation candidate and corrected publication/capability wording; release remains blocked by approval and verification evidence.
