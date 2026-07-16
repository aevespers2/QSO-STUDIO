# Release Plan

## Current Decision
Status: `BLOCKED — PRODUCT/UX CHARTER AND DOCUMENTATION INTEGRITY`

QSO-STUDIO is not completely empty: reviewed documentation head `0613fd39da3ee6f6911c4e40e7ee75420c5b4f7a` contains a README describing an operator/developer visualization and orchestration surface. The README also states that a site is published from `docs/` through `.github/workflows/pages.yml`, but those paths are absent. No release is eligible because `taskchain.md` and `punchlist.md` are absent, the product/UX charter and integration boundaries are unapproved, the publication claim is not backed by repository content, and no design, implementation, tests, accessibility, security/privacy, documentation verification, provenance, artifacts, or rollback evidence exists.

## Versioning
- Use Semantic Versioning only after the product surface, supported platforms, integration contracts, license, privacy model, and distribution identity are approved.
- First possible documentation candidate: `0.0.1-charter.1`.
- First UI implementation candidate should remain a pre-release, such as `0.1.0-alpha.1`, until accessibility, security, integration, packaging, and primary-workflow gates pass.
- No version may imply a published site, executable studio, orchestration authority, or payment capability that is not present and verified.

## Candidate Scope
### Charter/documentation candidate
- Approved purpose, users, primary workflows, non-goals, supported platforms, data classification, privacy model, license, distribution target, and ecosystem relationships.
- Explicit boundary between visualization/editing, proposal generation, human approval, runtime execution, repository writes, and simulated economic records.
- Accurate repository map and publication instructions that correspond to files and workflows actually present.
- Reproducible documentation artifact with links, accessibility, security/privacy, checksums, provenance, and rollback.

### Later UI candidate
- Minimal accessible application skeleton and design system.
- Versioned read-only contracts for genomes, canonical records, QSO state/evidence, proposals, freeze points, and release state.
- One bounded end-to-end review workflow with deterministic fixtures.
- Accessibility, error-state, offline/online behavior, security/privacy, packaging, documentation, provenance, and rollback evidence.
- No direct credentials, autonomous execution, unrestricted repository writes, or production payment authority.

## Existing Candidate Assets
- `README.md` states a proposed operator/developer role and identifies visualization targets including objects, genomes, messages, provenance, payment flows, freeze points, experiments, and release state.
- The README states that Studio must not bypass runtime authorization or safety controls.

The README is an initial scope note, not a verified charter or releasable documentation site. Its GitHub Pages statement is currently inaccurate because the referenced `docs/` content and workflow are absent.

## Selected Completed Work
None selected for release. The initial README has not passed charter approval, accuracy review, accessibility/security/privacy verification, publication reproduction, or provenance requirements.

## Planned Changelog Entries
- `Documentation`: approved QSO-STUDIO product/UX charter, workflows, trust boundaries, platform support, repository map, and verification strategy.
- `Fixed`: remove or fulfill unsupported Pages/publication claims and reconcile all capability wording with repository evidence.
- `Added`: minimal accessible documentation site or UI skeleton and one verified review workflow after approval.
- `Security`: credential, untrusted-content rendering, parser, local-storage, network, dependency, workflow-permission, repository-write, and privacy findings.
- `Accessibility`: keyboard, focus, labels, contrast, scaling, reduced-motion, visualization alternatives, and error-recovery evidence.
- `Release`: reproducible artifacts, SBOM where applicable, checksums, provenance, and approval decision.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Product/UX charter | BLOCKED | Approve users, workflows, platforms, ecosystem role, data/privacy model, license, distribution target, and authority boundaries. |
| Documentation integrity | FAIL | Every path, workflow, publication statement, capability, and integration claim corresponds to present, verified repository evidence. |
| Task completion | FAIL | Create `taskchain.md` and `punchlist.md`; included work is `DONE` with linked commits, commands, results, and rollback notes. |
| Documentation build/publication | NO EVIDENCE | A real documentation source and workflow or documented manual build exists and produces a reproducible artifact. |
| Build/static validation | NO IMPLEMENTATION | Required for a UI candidate: clean install/build, formatting, lint, type/configuration, and package checks pass. |
| Tests/integration | NO IMPLEMENTATION | Required for a UI candidate: unit, component, contract, integration, and primary-workflow smoke tests pass. |
| Security/privacy | NO EVIDENCE | Credential, parser/rendering, local-storage, network, dependency, secret, CI, repository-write, and privacy checks pass. |
| Accessibility | NO EVIDENCE | Keyboard, focus, semantics, labels, contrast, scaling, reduced motion, visualization alternatives, and error-state checks pass. |
| Documentation | FAIL | Approved setup, usage, integrations, limitations, accessibility, privacy, operations, publication, and rollback guidance are absent. |
| Provenance | NO EVIDENCE | Candidate commit, platform/tool versions, commands, artifacts, hashes, SBOM where applicable, publication target, and attestations are recorded. |
| Approval | PENDING | Explicit release approval after all included-scope gates pass. |

## Artifact Requirements
- Approved product/UX charter, architecture, workflow diagrams, data/privacy model, and integration-contract map.
- Reproducible documentation or application/source artifact for approved platforms.
- Versioned schemas and deterministic fixtures for every included integration.
- Documentation-integrity, link, build, static-analysis, test, integration, accessibility, security, privacy, and smoke reports appropriate to the selected scope.
- SBOM where applicable, SHA-256 checksums, provenance manifest, signing/notarization status where applicable, and rollback instructions.

## Rollback Criteria
Withdraw a charter/documentation candidate if the product overlaps another repository, leaves execution/payment/privacy authority ambiguous, or publishes unsupported paths or capabilities. Roll back implementation if the primary workflow fails, integration contracts drift, untrusted content executes, credentials or personal data cross the approved boundary, accessibility regressions block use, artifacts are non-reproducible, severe security findings remain, or hashes differ. Restore the previous verified artifact/tag and preserve failed-candidate evidence.

## Unresolved Blockers
- Approval is required for the product/UX charter, supported platforms, ecosystem role, privacy/data model, license, distribution target, and authority model.
- `taskchain.md` and `punchlist.md` do not exist.
- `README.md` claims publication from `docs/` through `.github/workflows/pages.yml`, but the referenced site and workflow are absent.
- No design system, application implementation, schemas, fixtures, tests, CI, accessibility review, security/privacy report, verified documentation build, provenance, checksums, or rollback artifact exists.
- The proposed visualization of payment flows and orchestration state must remain read-only and evidence-based until corresponding contracts and approval boundaries exist.

## Release Log
- 2026-07-16: Corrected the prior empty-repository assessment and recorded the unsupported Pages claim; candidate remains `BLOCKED — PRODUCT/UX CHARTER AND DOCUMENTATION INTEGRITY`.
