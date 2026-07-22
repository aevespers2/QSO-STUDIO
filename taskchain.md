# Task Chain

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Review and approve the QSO-STUDIO product/UX charter, portable-trust review profile, architecture-review quorum consumer, obstruction/gluing analysis, ADR-0001, ADR-0002, and documentation foundation before building an application.
- **User outcome:** A researcher or operator can understand the proposed read-only review workflow, supported evidence concepts, portable device-trust lifecycle, architecture-review status, AionUi boundary, privacy rules, platform decision points, and integration contracts without being told that a released site, executable Studio, reviewer registry, approval service, or device-control system exists.
- **MVP scope:** approved users and workflow; platform/distribution decision; domain-neutral review-contract ownership; AionUi adapter boundary; data classification, privacy, license, and authority boundaries; reproducible accessible documentation artifact; one approved integration manifest; one deterministic fixture-backed read-only workflow.
- **Priority:** Documentation integrity, review-surface ownership, gluing compatibility, and product authority boundaries precede design-system or UI implementation.
- **Success criteria:** every path, publication statement, workflow, and capability claim matches repository evidence; source observation, interpretation, proposal, quarantine, disposition, capability, receipt, canonical reconciliation, annotation, export, correction, revocation, recovery, reviewer qualification, appointment, acceptance, disposition, quorum, dissent, appeal, architecture decision, and activation remain distinct; visualization, annotation, proposal, human approval, runtime execution, repository writes, and payment operations remain separate; included documentation, accessibility, security/privacy, provenance, rollback, and gluing evidence pass.
- **Non-goals:** direct runtime or host execution, device inspection, network probing, remote administration, unrestricted repository writes, credentials, reviewer appointment or quorum authority, Repository `1` disposition, autonomous approvals, production payment control, untrusted-code execution, or live orchestration before separate contracts and decisions exist.
- **Release rationale:** A Studio surface can imply authority that belongs to runtime, Repository `1`, payment, repository, reviewer, architecture-decision, or human systems. A truthful charter and read-only review contract prevent unsafe coupling before implementation.

## Material obstruction

QSO-STUDIO and AionUi overlap as evidence-review surfaces without one accepted contract for review records, annotations, comparison, exports, approval references, corrections, revocations, caches, and recovery state. ADR-0002 records the lowest-coupling candidate: QSO-STUDIO owns the domain-neutral review contract while AionUi remains an optional compatible desktop/WebUI host adapter. The architecture-review quorum consumer now closes the missing second synthetic implementation for one immutable proposed contract payload, but contract acceptance, reviewer classes, appointments, real quorum, and architecture decisions remain unresolved.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve product/UX charter and documentation foundation | Architect | User approval | BLOCKED | Users, workflow, platform, ecosystem role, privacy/data/license model, distribution target, authority boundaries, ADR-0001, and repository claims are approved. |
| P0A | Approve review-surface ownership and AionUi boundary | Architect | ADR-0002, QSO-STUDIO and AionUi profiles | BLOCKED | ADR-0002 is accepted or revised; QSO-STUDIO, AionUi, external approval, and Repository `1` responsibilities are approved without overlapping authority. |
| P1 | Verify a reproducible accessible documentation artifact | QSOBuilder | Documentation PR | REVIEW | Strict build and artifact creation pass; links, semantics, keyboard path, privacy/security, provenance, rollback, and human documentation review are recorded. |
| P2 | Approve one read-only evidence-review contract | Architect | P0, P0A, P1, upstream manifest and fixtures | BLOCKED | Exact contract owner/version, parser limits, fixture hashes, review model, findings, comparison, export, correction, revocation, and failure behavior are approved. |
| P2A | Validate portable-trust pairwise and triple-overlap gluing | Contract owners | P2, Repository `0`/`1`, adapter and executor profiles | PROPOSED | Wrong-device, wrong-workspace, stale, replay, partial, conflicting, privacy, broadened-capability, expiry, revocation, correction, rollback, and recovery fixtures pass. |
| P2B | Reproduce the proposed architecture-review quorum corpus independently | QSOBuilder + QSO Field governance consumer | Immutable proposed contract generation | REVIEW | Both repositories calculate matching outcomes for the same canonical twelve-case payload; exact-head workflows and retained evidence pass; no claim of real reviewer, quorum, decision, or activation authority is made. |
| P3 | Build the minimal accessible UI skeleton | Builder | P2, P2A | PROPOSED | The approved workflow passes unit, component, contract, integration, smoke, accessibility, and security tests with no credentials or direct execution/write/payment path. |

## Builder rules

Do not implement runtime, device-control, payment, signing, approval, reviewer appointment, quorum, Repository `1` disposition, or repository-write authority inside Studio. Unverified upstream concepts may appear only as clearly labeled mock fixtures. Documentation must describe unresolved architecture as proposed rather than silently selecting it. AionUi compatibility work must not redefine the review contract or infer authority from a UI session.

## Builder log

- 2026-07-23 — Added an independent rule-pipeline consumer for the proposed architecture-review quorum boundary, a canonical twelve-case synthetic payload, adversarial tests, retained-evidence workflow, Pages documentation, and release/task-chain alignment. This closes only the second synthetic implementation sub-gate for the recorded contract generation.
- 2026-07-21 — Added ADR-0002 proposing separation of the domain-neutral QSO-STUDIO review contract from the optional AionUi host shell, with explicit acceptance and rollback conditions.
- 2026-07-21 — Added the portable-trust review profile and obstruction/gluing ledger. Documented QSO-STUDIO as the candidate domain-neutral review-contract owner and AionUi as an optional compatible host adapter; no implementation or authority was added.
- 2026-07-19 — The documentation and Consent Capacity Lock workflows passed on the documentation candidate; the static-site artifact and digest are recorded in `punchlist.md`.
- 2026-07-19 — Prepared a Pages-ready documentation foundation, strict build workflow, architecture/design/workflow/security/accessibility/onboarding/operations guidance, ADR-0001, and evidence punch list. Awaiting human charter and documentation review.

Record approvals, commits, accessibility/security review results, contract/fixture hashes, rollback evidence, and follow-ups below this line.
