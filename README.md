# QSO-STUDIO

Proposed visual inspection, review, and debugging workspace for Quantum State Objects and the broader QSO ecosystem.

> **Current repository surface:** product/UX charter candidate and static documentation. No verified Studio application, deployment, runtime orchestration, repository-write, credential, or payment-control capability is released.

## Documentation

- [Static Pages source](docs/index.html)
- [Project guide and onboarding](docs/PROJECT_GUIDE.md)
- [Architecture and trust boundaries](docs/ARCHITECTURE.md)
- [Task chain](taskchain.md)
- [Release plan](release.md)
- [Changelog](changelog.md)

## Proposed workflow

```text
versioned read-only evidence bundle
-> contract and hash validation
-> normalization and redaction
-> human inspection
-> annotation
-> exported proposal/review artifact
-> external approval workflow
```

QSO-STUDIO may visualize objects, genomes, messages, provenance, payment evidence, freeze points, experiments, and release state. It may not convert a display or annotation into runtime execution, repository mutation, credential use, autonomous approval, or settlement authority.

## GitHub Pages status

The `docs/` directory now contains a static documentation candidate suitable for a future Pages publication workflow. Publication is **not yet authorized or verified**: no release gate should be marked complete until the exact workflow, artifact, URL, link/HTML checks, accessibility report, security/privacy review, checksums, provenance, and rollback evidence are retained for one immutable commit.

## Product boundary

- Imported content is untrusted data and must never execute.
- Unsupported, stale, malformed, oversized, or hash-mismatched evidence fails closed.
- Human annotations remain distinct from source evidence.
- Exported proposals require independent external approval.
- Payment records are read-only evidence; Studio does not custody, sign, or settle.
- Credentials and unrestricted repository writes remain outside the Studio boundary.
