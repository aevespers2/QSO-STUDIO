# Task Chain

`QSO-STUDIO-DOCS-CANDIDATE-001`

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Review the QSO-STUDIO product/UX charter and exact-head documentation candidate before any application or Pages publication is authorized.
- **User outcome:** A researcher or operator can understand the proposed read-only review workflow, supported boundaries, data/privacy expectations, and integration dependencies without being told that a site or executable exists when it does not.
- **MVP scope:** approved users, workflows, non-goals, platform/distribution target, data classification, privacy/license model, authority boundaries; accurate repository map; accessible documentation candidate; one fixture-oriented read-only workflow specification; deterministic documentation checks.
- **Priority:** Documentation integrity and product authority boundaries precede design-system or UI implementation.
- **Success criteria:** every path, publication statement, workflow, and capability claim matches repository evidence; the charter separates visualization, annotation, proposal, human review, runtime execution, repository writes, and payments; links and diagrams are accessible; documentation validation, provenance, and rollback evidence pass.
- **Non-goals:** direct runtime execution, unrestricted repository writes, credentials, autonomous approvals, production payment control, untrusted-code execution, or visual orchestration before contracts are available.
- **Release rationale:** A Studio surface can imply authority belonging to runtime, payment, or repository systems. A truthful read-only contract prevents unsafe coupling before implementation.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve product/UX charter and authority boundary | Architect | Explicit review | BLOCKED | Users, workflows, platforms, ecosystem role, privacy/license model, distribution target, authority boundaries, and unresolved ownership are accepted or revised. |
| P0.1 | Produce accurate documentation and navigation candidate | QSOBuilder | Repository evidence | REVIEW | Front door, charter, architecture, workflow, integration, onboarding, developer, accessibility, security/privacy, punch-list, and planning controls agree. |
| P0.2 | Validate documentation candidate at exact head | QSOBuilder | P0.1 | REVIEW | Required pages, links, diagrams, markers, planning alignment, hostile regressions, deterministic evidence, and clean-tree checks pass. |
| P0.3 | Decide Pages publication target and rollback | Architect + publication reviewer | P0-P0.2 | BLOCKED | Authorized source, workflow, permissions, accessibility/security/privacy/license review, rollback, and resulting-route verification are recorded. |
| P1 | Specify one read-only evidence-review fixture | Architect | P0 and accepted upstream contracts | BLOCKED | Deterministic synthetic fixtures define records, provenance, conflicts, corrections, withdrawals, annotations, and errors without execution or write authority. |
| P2 | Build the minimal accessible UI skeleton | Builder | P1 | PROPOSED | Approved workflow passes unit, component, contract, smoke, accessibility, and security tests without credentials or direct execution paths. |

## Builder rules

Do not implement runtime, payment, repository-write, publication, or approval authority inside Studio. Unverified upstream concepts may appear only as clearly labeled mock or synthetic fixtures. Passing documentation checks does not approve the product charter or publication.

## FYSA-120 mapping

Applied capability areas: CAT-011 narrative and diagram integrity; CAT-012 technical writing and documentation architecture; CAT-013 knowledge graphs and contradiction detection; CAT-017 onboarding; CAT-019 accessibility and plain language; CAT-031 documentation validation and regressions; CAT-040 migration and rollback; CAT-052 least-privilege workflow design.

Proposed non-authoritative subdivision: `012-L — evidence-state interface documentation`, covering read-only review narratives, proposal-versus-authority separation, accessible provenance views, and documentation-to-interface traceability.

## Builder log

Record approvals, commits, documentation/accessibility/security commands and results, contract/fixture hashes, artifact checksums, publication decisions, rollback evidence, and follow-ups.

This task chain is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
