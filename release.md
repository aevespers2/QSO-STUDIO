# Release Plan

## Current Decision

Status: `BLOCKED — PRODUCT/UX CHARTER AND DOCUMENTATION INTEGRITY`

QSO-STUDIO currently contains an initial README for a proposed review/orchestration surface, not a verified application or documentation site. P0 is blocked on product/UX approval, `punchlist.md` is absent, the README still claims a Pages site under `docs/` and `.github/workflows/pages.yml` although those paths do not exist, and candidate head `4a321bc153e4525694a160eb64c20ed172df1325` lacks design, build, tests, accessibility, security/privacy, documentation, provenance, artifact, and rollback evidence.

## Versioning

- Scheme: Semantic Versioning after product scope, platforms, integration contracts, license, privacy model, and distribution identity are approved.
- First possible documentation candidate: `0.0.1-charter.1`.
- First UI candidate: `0.1.0-alpha.1`, remaining pre-release until accessibility, security, integration, packaging, and workflow gates pass.
- No version may imply a site, executable Studio, orchestration authority, or payment capability that is not present and verified.

## Release Scope

### Charter/documentation candidate
- Approved users, workflows, non-goals, platforms, data/privacy/license model, distribution target, ecosystem role, and authority boundaries.
- Accurate repository/publication map and removal or fulfillment of unsupported Pages claims.
- Explicit separation of visualization, editing, proposals, human approval, runtime execution, repository writes, and payment records.
- Reproducible accessible documentation artifact with security/privacy, checksums, provenance, and rollback.

### Later UI candidate
- Minimal accessible UI and one fixture-backed read-only evidence-review workflow.
- Versioned contracts for genomes, state/evidence, messages, proposals, freeze points, attribution, and errors.
- No direct credentials, execution, unrestricted repository writes, autonomous approval, or production payment authority.

## Selected Completed Work

None. The README is a candidate scope note but has not passed charter approval, accuracy verification, accessibility/security review, reproducible publication, or provenance gates.

## Planned Changelog Entries

- `Documentation`: approved product/UX charter, workflows, platforms, trust boundaries, and verification strategy.
- `Fixed`: remove or fulfill unsupported Pages/publication claims and reconcile capability statements with repository evidence.
- `Added`: reproducible documentation artifact and later one read-only workflow after approval.
- `Security`: credentials, untrusted rendering, parser, storage, network, dependencies, workflow permissions, repository writes, and privacy.
- `Accessibility`: keyboard, focus, semantics, contrast, scaling, motion, visualization alternatives, and error recovery.
- `Release`: artifacts, SBOM where applicable, checksums, provenance, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Product/UX charter | BLOCKED | Approve users, workflows, platforms, ecosystem role, privacy/license model, distribution, and authority boundaries. |
| Documentation integrity | FAIL | Every path, publication statement, workflow, and capability claim matches verified repository evidence. |
| Task completion | FAIL | P0 is `DONE`; `punchlist.md` exists and included work has evidence. |
| Documentation build | NO EVIDENCE | Real source/workflow or a documented manual process produces a reproducible artifact. |
| UI build/tests | NOT YET INCLUDED | Required for a later UI candidate: install/build/static, unit/component/contract/integration/smoke checks pass. |
| Security/privacy | NO EVIDENCE | Credential, rendering/parser, storage, network, dependency, secret, CI, repository-write, and privacy checks pass. |
| Accessibility | NO EVIDENCE | Keyboard, focus, semantics, labels, contrast, scaling, reduced motion, alternatives, and error states pass. |
| Documentation | FAIL | Approved setup, usage, integrations, limitations, accessibility, privacy, publication, and rollback guidance are absent. |
| Provenance | NO EVIDENCE | Commit, tools/platforms, commands, artifacts, hashes, SBOM, publication target, and attestations are retained. |
| Approval | PENDING | Explicit release approval after all included-scope gates pass. |

## Artifact Requirements

- Approved product/UX charter, authority model, architecture/workflow diagrams, privacy model, and contract map.
- Reproducible documentation artifact and source archive.
- Documentation-integrity, link, accessibility, security/privacy, build, and smoke reports.
- For later UI work: versioned schemas/fixtures, package artifacts, tests, SBOM, signing status where applicable, checksums, provenance, and rollback evidence.

## Rollback Criteria

Withdraw a charter candidate if it overlaps another repository, leaves execution/payment/privacy authority ambiguous, or publishes unsupported paths/capabilities. Roll back implementation if the primary workflow fails, contracts drift, untrusted content executes, credentials or personal data cross the boundary, accessibility blocks use, artifacts are non-reproducible, severe security findings remain, or hashes differ. Restore the prior verified artifact/tag and preserve failed-candidate evidence.

## Unresolved Blockers

- Approval is required for the product/UX charter, platform/distribution target, ecosystem role, privacy/license model, and authority boundaries.
- `punchlist.md` and accepted Builder evidence are absent.
- The README's `docs/` and Pages-workflow publication claim is unsupported by repository content.
- No documentation build, design system, implementation, schemas, fixtures, tests, CI, accessibility, security/privacy, provenance, checksums, or rollback artifact exists.
- Payment and orchestration views must remain read-only and evidence-based until upstream contracts and authority approvals exist.

## Release Log

- 2026-07-16: Aligned the candidate with the product/UX charter and documentation-integrity gate; no release-ready work selected.