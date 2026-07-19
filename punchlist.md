# QSO-STUDIO Punch List

Statuses: `OPEN` · `BLOCKED` · `IN PROGRESS` · `REVIEW` · `DONE` · `NOT APPLICABLE`

This checklist records evidence. A documentation file existing is not by itself proof that a product or release gate has passed.

## P0 — Charter and documentation integrity

| Item | Status | Evidence required |
|---|---|---|
| Approve target users and primary workflow | BLOCKED | Recorded human decision |
| Approve first supported platform and distribution model | BLOCKED | Accepted ADR |
| Approve ecosystem role and canonical contract owners | BLOCKED | Versioned integration map |
| Approve data classification, privacy, and retention defaults | BLOCKED | Privacy decision and reviewer |
| Approve license and support/security ownership | BLOCKED | Repository metadata and policy |
| Separate display, proposal, approval, execution, repository writes, and payment authority | REVIEW | Architecture and ADR review |
| Replace unsupported Pages claim with truthful build status | REVIEW | README, workflow, strict build result |
| Add project overview, architecture, design, workflow, onboarding, security, accessibility, and operations docs | REVIEW | Documentation PR |

## P1 — Reproducible documentation artifact

| Item | Status | Evidence required |
|---|---|---|
| Strict MkDocs configuration | DONE | `mkdocs.yml` and successful exact-branch build |
| Pinned CI documentation toolchain | DONE | Successful Documentation workflow run |
| Internal link and navigation validation | DONE | `mkdocs build --strict` completed successfully |
| Accessibility review of documentation | OPEN | Keyboard, heading, link, and diagram-alternative review |
| Security/privacy review of documentation and workflow | OPEN | Permission and dependency review |
| Artifact checksum and provenance | REVIEW | Exact-head artifact digest and workflow metadata retained in the pull request evidence |
| Publication owner, environment, and canonical URL | BLOCKED | Charter decision |
| Publication verification and rollback rehearsal | BLOCKED | Approved deployment evidence |

## P2 — First read-only workflow contract

| Item | Status | Evidence required |
|---|---|---|
| Select one record type and exact contract owner/version | BLOCKED | Approved manifest entry |
| Define bounded parser limits | OPEN | Versioned design and tests |
| Define normalized review model | REVIEW | Design review |
| Define finding and compatibility model | REVIEW | Design review |
| Create deterministic fixture matrix | BLOCKED | Upstream contract and fixture hashes |
| Define accessible summary, detail, comparison, and error states | OPEN | UX specification and test cases |
| Define non-authoritative review-note export | REVIEW | Contract and wording review |
| Prove absence of write/execution/payment clients | BLOCKED | Implementation and dependency evidence |

## P3 — Future UI candidate

| Item | Status | Evidence required |
|---|---|---|
| Minimal application skeleton | BLOCKED | P0–P2 acceptance |
| Unit, component, contract, integration, and smoke tests | BLOCKED | Exact-head test reports |
| Hostile-input and resource-limit tests | BLOCKED | Security report |
| Keyboard and assistive-technology workflow tests | BLOCKED | Accessibility report |
| Build artifacts, SBOM, checksums, and provenance | BLOCKED | Release evidence bundle |
| Recovery and rollback rehearsal | BLOCKED | Recorded result |
| Human release approval | BLOCKED | Named reviewer and decision |

## Evidence log

- 2026-07-19 — Documentation workflow passed the pinned strict build and produced the `qso-studio-site` artifact; exact-head identifiers and digest are retained in the pull request evidence.
- 2026-07-19 — Consent Capacity Lock passed on the documentation candidate. Charter, publication, application, and release approval remain blocked or in review.
