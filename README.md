# QSO-STUDIO

`QSO-STUDIO-DOCS-CANDIDATE-001`

QSO-STUDIO is the proposed read-only design, inspection, and evidence-review workspace for Quantum State Objects and the broader QSO ecosystem.

## Documentation candidate

The repository contains a reviewable documentation tree under [`docs/`](docs/index.md). **It is not published as an authorized GitHub Pages site.** Publication remains a separate decision requiring an approved target, exact-head evidence, accessibility/security/privacy/licensing review, rollback planning, and resulting-route verification.

Start with:

- [Documentation front door](docs/index.md)
- [Product and UX charter](docs/product-charter.md)
- [Architecture](docs/architecture.md)
- [Read-only evidence review](docs/read-only-review-workflow.md)
- [Integration contracts](docs/integration-contracts.md)
- [Independent ecosystem conformance consumer](docs/ecosystem-conformance-consumer.md)
- [Onboarding](docs/onboarding.md)
- [Developer guide](docs/developer-guide.md)
- [Punch list](punchlist.md)

## Product boundary

Studio may visualize governed records, genomes, messages, provenance, proposals, freeze points, experiment evidence, payment-related evidence, and release state. It does not bypass upstream authorization, execute QSO workloads, mutate repositories, approve proposals autonomously, hold production credentials, or settle payments.

The first bounded workflow is fixture-backed and read-only. An annotation or exported review packet remains a proposal artifact until a separate authorized process accepts and applies it.

## Current status

- Documentation: candidate, with deterministic checks.
- UI or executable: not implemented.
- Integrations: proposed and blocked on exact upstream contracts.
- Ecosystem manifest consumer: synthetic, independently implemented, and bound to `QSO-FABRIC#21@25036a5cfcea79e204a4660ddd1af09c054935b1`; it grants no admission or runtime authority.
- Pages publication: not authorized or represented as active.
- Release: blocked on charter and governance decisions.

The older QSO-STUDIO PR #4 consumer candidate diverged from the documentation baseline after `main` advanced. Its useful manifest-consumer work is being rebound on a current-main repair branch rather than force-updated or treated as current evidence.

This repository is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
