# QSO-STUDIO

QSO-STUDIO is the proposed domain-neutral operator and developer workspace for inspecting Quantum State Objects (QSOs), genomes, evidence, messages, proposals, freeze points, portable device-trust records, payment records, and release state across the QSO ecosystem.

The repository is currently **documentation-first**. It does not contain a verified Studio application, runtime executor, payment controller, repository writer, device inspector, remediation client, credential store, or autonomous approval system. The first bounded product target is a fixture-backed, read-only evidence-review workflow that preserves the authority of upstream runtimes, Repository `1`, and human reviewers.

## Current status

| Area | Status |
|---|---|
| Product/UX charter | Proposed; architectural approval required |
| Documentation source | Present in `docs/` |
| Documentation build | Defined by `mkdocs.yml` and `.github/workflows/pages.yml` |
| GitHub Pages publication | Not authorized by this repository change |
| Studio application | Not implemented |
| Read-only workflow | Specified, not implemented |
| Portable trust review profile | Candidate contract; not implemented or approved |
| Runtime, device-control, repository-write, or payment authority | Explicitly out of scope |

## Documentation

The Pages-ready documentation includes:

- [Project overview](docs/project-overview.md)
- [Architecture and trust boundaries](docs/architecture.md)
- [Design contracts](docs/design.md)
- [Portable trust review profile](docs/portable-trust-review-profile.md)
- [Obstruction and gluing analysis](docs/obstruction-and-gluing.md)
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

On Windows PowerShell, replace the environment-start command with `.venv\Scripts\Activate.ps1`.

## Portfolio role

QSO-STUDIO is the candidate owner of the **domain-neutral review contract**, normalized review model, accessibility requirements, and non-authoritative export semantics. AionUi may later host an optional compatible desktop or WebUI adapter, but the host shell must not redefine review state, approval, capability, correction, revocation, or canonical-state semantics.

For the portable device-trust foundation:

- observation adapters produce bounded evidence;
- Repository `0` prepares local proposals and verifies separately authorized work;
- Repository `1` owns candidate quarantine, disposition, capability, revocation, canonical reconciliation, checkpoint, and recovery authority;
- QSO-STUDIO displays and compares those records without creating authority;
- external human or approved services create any actual approval record.

## Product boundary

QSO-STUDIO may visualize and compare evidence, prepare non-authoritative proposals, and present review status. It must not bypass runtime authorization, Repository `1`, human approval, repository protection, settlement controls, or `QSO-CONSENT-CAPACITY-LOCK-v1`.

The following are not implied by this repository:

- direct execution of QSO workloads or host-remediation commands;
- device inspection, network probing, traffic interception, or remote administration;
- unrestricted writes to ecosystem repositories;
- credential storage or signing authority;
- Repository `1` disposition or capability issuance;
- production payment initiation or settlement;
- autonomous release approval;
- execution of untrusted code or content;
- a released desktop, web, or mobile application;
- use of public GitHub Pages as a privileged operations console.

## Repository controls

Planning and release evidence are maintained in:

- [`taskchain.md`](taskchain.md) — ordered objectives and acceptance criteria;
- [`punchlist.md`](punchlist.md) — documentation and future product gates;
- [`release.md`](release.md) — release posture, evidence requirements, and rollback;
- [`changelog.md`](changelog.md) — dated, evidence-oriented changes.

No implementation scope should be expanded merely to satisfy documentation. Where architecture remains undecided, documentation records the decision point rather than presenting a guess as an approved contract.
