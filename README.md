# QSO-STUDIO

QSO-STUDIO is the proposed operator and developer workspace for inspecting Quantum State Objects (QSOs), genomes, evidence, messages, proposals, freeze points, payment records, and release state across the QSO ecosystem.

The repository is currently **documentation-first**. It does not contain a verified Studio application, runtime executor, payment controller, repository writer, or autonomous approval system. The first bounded product target is a fixture-backed, read-only evidence-review workflow that preserves the authority of upstream runtimes and human reviewers.

## Current status

| Area | Status |
|---|---|
| Product/UX charter | Proposed; architectural approval required |
| Documentation source | Present in `docs/` |
| Documentation build | Defined by `mkdocs.yml` and `.github/workflows/pages.yml` |
| GitHub Pages publication | Not authorized by this repository change |
| Studio application | Not implemented |
| Read-only workflow | Specified, not implemented |
| Runtime, repository-write, or payment authority | Explicitly out of scope |

## Documentation

The Pages-ready documentation includes:

- [Project overview](docs/project-overview.md)
- [Architecture and trust boundaries](docs/architecture.md)
- [Design contracts](docs/design.md)
- [Read-only evidence-review workflow](docs/workflows/evidence-review.md)
- [Security and privacy model](docs/security-privacy.md)
- [Accessibility requirements](docs/accessibility.md)
- [Developer onboarding](docs/development/onboarding.md)
- [Operations, recovery, and rollback](docs/operations.md)
- [Architecture decision record](docs/decisions/0001-read-only-review-boundary.md)

Build the documentation locally with:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install "mkdocs==1.6.1"
mkdocs build --strict
```

On Windows PowerShell, replace the environment-start command with `.venv\\Scripts\\Activate.ps1`.

## Product boundary

QSO-STUDIO may visualize and compare evidence, prepare non-authoritative proposals, and present review status. It must not bypass runtime authorization, human approval, repository protection, settlement controls, or `QSO-CONSENT-CAPACITY-LOCK-v1`.

The following are not implied by this repository:

- direct execution of QSO workloads;
- unrestricted writes to ecosystem repositories;
- credential storage or signing authority;
- production payment initiation or settlement;
- autonomous release approval;
- execution of untrusted code or content;
- a released desktop, web, or mobile application.

## Repository controls

Planning and release evidence are maintained in:

- [`taskchain.md`](taskchain.md) — ordered objectives and acceptance criteria;
- [`punchlist.md`](punchlist.md) — documentation and future product gates;
- [`release.md`](release.md) — release posture, evidence requirements, and rollback;
- [`changelog.md`](changelog.md) — dated, evidence-oriented changes.

No implementation scope should be expanded merely to satisfy documentation. Where architecture remains undecided, documentation records the decision point rather than presenting a guess as an approved contract.
