# Developer onboarding

## Repository state

QSO-STUDIO is currently a documentation and design repository. Do not assume an application framework, package manager, API, schema, or distribution target until the charter and first workflow contracts are approved.

## Prerequisites

- Git
- Python 3.13 or another version accepted by the documentation workflow
- a shell capable of creating a virtual environment

## Documentation setup

```bash
git clone https://github.com/aevespers2/QSO-STUDIO.git
cd QSO-STUDIO
python -m venv .venv
. .venv/bin/activate
python -m pip install "mkdocs==1.6.1"
mkdocs serve
```

Open the local address printed by MkDocs. Before committing, run:

```bash
mkdocs build --strict
```

The generated `site/` directory is an artifact and should not be committed unless a future release procedure explicitly requires it.

## Source map

```text
README.md                         Repository entry point and status
mkdocs.yml                        Documentation build and navigation
docs/                             Pages-ready documentation source
  index.md                        Site entry point
  project-overview.md             Users, goals, scope, ecosystem map
  architecture.md                 Components, trust boundaries, failures
  design.md                       Record, finding, manifest, and UI contracts
  workflows/evidence-review.md    First bounded workflow specification
  security-privacy.md             Threats, controls, and privacy defaults
  accessibility.md                Interaction and verification requirements
  development/onboarding.md       Contributor setup and workflow
  operations.md                   Build, evidence, incident, recovery, rollback
  decisions/                      Architecture decision records
taskchain.md                      Ordered objectives and acceptance criteria
punchlist.md                      Evidence checklist
release.md                        Release posture and gates
changelog.md                      Dated changes and evidence references
```

## Contribution workflow

1. Read `taskchain.md`, `release.md`, and the relevant ADR before changing documentation.
2. Create a narrowly named branch.
3. Keep claims tied to repository evidence.
4. Record unresolved design choices as questions or ADR status, not as approved facts.
5. Add or update diagrams and textual explanations together.
6. Run the strict documentation build.
7. Review links, headings, keyboard readability, and plain-text diagram alternatives.
8. Update `changelog.md` and `punchlist.md` with the exact evidence produced.
9. Open a draft pull request until CI and human review are complete.

## Writing rules

- Use “proposed,” “candidate,” or “future” for unapproved architecture.
- Use “not implemented” when the repository lacks the capability.
- Distinguish a build artifact from a published site.
- Distinguish display from proposal, approval, execution, repository mutation, and settlement.
- Link to canonical upstream contracts rather than duplicating them once they exist.
- Avoid screenshots as the only source of product behavior; pair them with structured text.

## Adding an ADR

Create `docs/decisions/NNNN-short-title.md` with:

```markdown
# ADR-NNNN: Decision title

- Status: Proposed | Accepted | Superseded | Rejected
- Date: YYYY-MM-DD
- Decision owners: ...

## Context
## Decision
## Consequences
## Evidence required
## Supersedes / Superseded by
```

An ADR may document an approved change in scope only when the authorized decision is cited. Documentation should not use an ADR to invent authority.

## Future application bootstrap

When the charter approves a platform, the first implementation change should add only what is required for the fixture-backed workflow: a minimal application skeleton, versioned fixtures, parsers, validators, accessible views, deterministic tests, and build evidence. Remote connectors, credentials, writes, and execution remain separate future decisions.
