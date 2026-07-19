# Task Chain

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Review and approve the QSO-STUDIO product/UX charter and documentation foundation before building an application.
- **User outcome:** A researcher or operator can understand the proposed read-only review workflow, supported evidence concepts, platform decision points, privacy boundaries, and integration contracts without being told that a released site or executable Studio exists.
- **MVP scope:** approved users and workflow; platform/distribution decision; data classification, privacy, license, and authority boundaries; reproducible accessible documentation artifact; one approved integration manifest; one deterministic fixture-backed read-only workflow.
- **Priority:** Documentation integrity and product authority boundaries precede design-system or UI implementation.
- **Success criteria:** every path, publication statement, workflow, and capability claim matches repository evidence; visualization, annotation, proposal, human approval, runtime execution, repository writes, and payment operations remain distinct; included documentation, accessibility, security/privacy, provenance, and rollback evidence pass.
- **Non-goals:** direct runtime execution, unrestricted repository writes, credentials, autonomous approvals, production payment control, untrusted-code execution, or live orchestration before separate contracts and decisions exist.
- **Release rationale:** A Studio surface can imply authority that belongs to runtime, payment, repository, or human systems. A truthful charter and read-only review contract prevent unsafe coupling before implementation.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve product/UX charter and documentation foundation | Architect | User approval | BLOCKED | Users, workflow, platform, ecosystem role, privacy/data/license model, distribution target, authority boundaries, ADR-0001, and repository claims are approved. |
| P1 | Verify a reproducible accessible documentation artifact | QSOBuilder | Documentation PR | REVIEW | `mkdocs build --strict` passes at exact head; links, semantics, keyboard path, privacy/security, artifact checksum, provenance, and rollback evidence are recorded. |
| P2 | Approve one read-only evidence-review contract | Architect | P0, P1, upstream manifest and fixtures | BLOCKED | Exact contract owner/version, parser limits, fixture hashes, review model, findings, comparison, export, and failure behavior are approved. |
| P3 | Build the minimal accessible UI skeleton | Builder | P2 | PROPOSED | The approved workflow passes unit, component, contract, integration, smoke, accessibility, and security tests with no credentials or direct execution/write/payment path. |

## Builder rules

Do not implement runtime, payment, signing, approval, or repository-write authority inside Studio. Unverified upstream concepts may appear only as clearly labeled mock fixtures. Documentation must describe unresolved architecture as proposed rather than silently selecting it.

## Builder log

- 2026-07-19 — Prepared a Pages-ready documentation foundation, strict build workflow, architecture/design/workflow/security/accessibility/onboarding/operations guidance, ADR-0001, and evidence punch list. Awaiting exact-head CI and human charter review.

Record approvals, commits, documentation/build/accessibility/security commands and results, contract/fixture hashes, artifact checksums, rollback evidence, and follow-ups below this line.
