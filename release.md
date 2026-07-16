# Release Plan

## Current Decision
Status: `BLOCKED — PRODUCT/UX CHARTER APPROVAL REQUIRED`

QSO-STUDIO is empty. It has no `taskchain.md`, `punchlist.md`, product charter, source, design system, schemas, tests, workflows, accessibility evidence, security/privacy review, documentation, provenance, artifacts, or rollback baseline. No release is eligible.

## Versioning
- Use Semantic Versioning only after the product surface, supported platforms, integration contracts, and distribution identity are approved.
- First possible documentation-only candidate: `0.0.1-charter.1`.
- First UI implementation candidate should remain a pre-release, such as `0.1.0-alpha.1`, until accessibility, security, integration, packaging, and primary-workflow gates pass.

## Candidate Scope
### Charter candidate
- Purpose, users, primary workflows, non-goals, supported platforms, data classification, privacy model, license, distribution target, and relationship to QuantumStateObjects, QSO-GENOMES, QSO-SEEKER, QSO-FABRIC, and QSO-PAYMENTS.
- Explicit boundary between visualization/editing, proposal generation, human approval, runtime execution, and any simulated economic records.

### Later UI candidate
- Minimal application skeleton and design system.
- Versioned read-only contracts for genomes, canonical records, QSO state/evidence, and proposal review.
- One bounded end-to-end workflow with deterministic fixtures.
- Accessibility, error-state, offline/online behavior, security/privacy, packaging, documentation, provenance, and rollback evidence.
- No direct credentials, autonomous execution, unrestricted repository writes, or production payment authority.

## Selected Completed Work
None. The repository contains no releaseable content.

## Planned Changelog Entries
- `Documentation`: approved QSO-STUDIO product charter, workflows, trust boundaries, platform support, and verification strategy.
- `Added`: minimal accessible UI skeleton and one verified review workflow after approval.
- `Security`: credential, content-rendering, parser, local-storage, network, dependency, workflow-permission, and privacy findings.
- `Accessibility`: keyboard, focus, labels, contrast, scaling, reduced-motion, and error-recovery evidence.
- `Release`: reproducible artifacts, SBOM, checksums, provenance, and approval decision.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Product/UX charter | BLOCKED | Approve users, workflows, platforms, ecosystem role, data/privacy model, license, and distribution target. |
| Task completion | FAIL | `taskchain.md` and `punchlist.md` exist; included work is `DONE` with linked evidence. |
| Build/static validation | NO EVIDENCE | Clean install/build, formatting, lint, type/configuration, and package checks pass. |
| Tests/integration | NO EVIDENCE | Unit, component, contract, integration, and primary-workflow smoke tests pass. |
| Security/privacy | NO EVIDENCE | Credential, parser/rendering, local-storage, network, dependency, secret, CI, and privacy checks pass. |
| Accessibility | NO EVIDENCE | Keyboard, focus, semantics, labels, contrast, scaling, reduced-motion, and error-state checks pass. |
| Documentation | FAIL | Setup, usage, integrations, limitations, accessibility, privacy, operations, and rollback are absent. |
| Provenance | NO EVIDENCE | Commit, platform/tool versions, commands, artifacts, hashes, SBOM, and attestations recorded. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements
- Approved product/UX charter, architecture, workflow diagrams, and integration-contract map.
- Versioned schemas and deterministic fixtures for every included integration.
- Reproducible application/source artifacts for approved platforms.
- Build, static-analysis, test, integration, accessibility, security, privacy, and smoke reports.
- SBOM, SHA-256 checksums, provenance manifest, signing/notarization status where applicable, and rollback instructions.

## Rollback Criteria
Withdraw a charter candidate if the product overlaps another repository or leaves execution/payment/privacy authority ambiguous. Roll back implementation if the primary workflow fails, integration contracts drift, untrusted content executes, credentials or personal data cross the approved boundary, accessibility regressions block use, artifacts are non-reproducible, severe security findings remain, or hashes differ. Restore the previous verified tag and preserve failed-candidate evidence.

## Unresolved Blockers
- Approval is required for the product/UX charter, supported platforms, ecosystem role, privacy/data model, license, and distribution target.
- Repository is empty; `taskchain.md` and `punchlist.md` do not exist.
- No design, implementation, schemas, fixtures, tests, CI, accessibility, security/privacy review, documentation, provenance, or artifacts exist.

## Release Log
- 2026-07-16: Empty UI repository evaluated and held `BLOCKED — PRODUCT/UX CHARTER APPROVAL REQUIRED`.