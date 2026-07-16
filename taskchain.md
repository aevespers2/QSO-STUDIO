# Task Chain

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Approve the QSO-STUDIO product/UX charter and make repository documentation accurate before building an application.
- **User outcome:** A researcher or operator can understand the proposed read-only review workflow, supported platforms, data/privacy boundaries, and integration contracts without being told that a site or executable Studio exists when it does not.
- **MVP scope:** approved users, workflows, non-goals, platform/distribution target, data classification, privacy/license model, authority boundaries; correct repository map; remove or fulfill unsupported Pages claims; reproducible accessible documentation artifact; one fixture-backed read-only workflow specification.
- **Priority:** Documentation integrity and product authority boundaries precede design-system or UI implementation.
- **Success criteria:** every path, publication statement, workflow, and capability claim matches repository evidence; the charter separates visualization/editing/proposals/human approval/runtime execution/repository writes/payments; documentation builds reproducibly; accessibility, security/privacy, checksums, provenance, and rollback pass.
- **Non-goals:** direct runtime execution, unrestricted repository writes, credentials, autonomous approvals, production payment control, untrusted-code execution, or full visual orchestration before contracts are available.
- **Release rationale:** A Studio surface can easily imply authority that belongs to runtime, payment, or repository systems. An accurate charter and read-only review contract prevent unsafe coupling before implementation begins.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve product/UX charter and repair documentation integrity | Architect | User approval | BLOCKED | Users, workflows, platforms, ecosystem role, privacy/data/license model, distribution target, authority boundaries, and all repository/publication claims are approved and accurate. |
| P1 | Produce a reproducible accessible documentation artifact | QSOBuilder | P0 | PROPOSED | Real source/build or Pages workflow exists; links, semantics, keyboard path, contrast, privacy/security, checksums, provenance, and rollback pass. |
| P2 | Specify one read-only evidence-review workflow | Architect | P1 and upstream contract manifests | BLOCKED | Deterministic fixtures define display of genomes, state/evidence, messages, proposals, freeze points, attribution, and errors without execution or write authority. |
| P3 | Build the minimal accessible UI skeleton | Builder | P2 | PROPOSED | The approved workflow passes unit/component/contract/smoke/accessibility/security tests with no credentials or direct execution path. |

## Builder rules

Do not implement runtime, payment, or repository-write authority inside Studio. Unverified upstream concepts may be shown only as clearly labeled mock fixtures.

## Builder log

Record approvals, commits, documentation/build/accessibility/security commands and results, contract/fixture hashes, artifact checksums, rollback evidence, and follow-ups.