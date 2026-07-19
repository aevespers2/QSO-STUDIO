# QSO-STUDIO

QSO-STUDIO is a proposed visual workspace for reviewing evidence about Quantum State Objects and related ecosystem records. Its first bounded outcome is not a general-purpose orchestration console; it is a **read-only, fixture-backed review surface** that helps a researcher or operator understand what an upstream system reports without granting Studio authority to execute, approve, write, sign, or settle anything.

## Documentation status

This site describes a product charter and architecture candidate. It is designed to make the repository truthful and reviewable before application development begins.

| Capability | Documentation status | Implementation status |
|---|---|---|
| Project scope and non-goals | Defined | Not applicable |
| Architecture and authority boundaries | Proposed | Not implemented |
| Evidence-review workflow | Specified | Not implemented |
| Accessible interaction requirements | Defined | Not implemented |
| Security and privacy controls | Defined | Not implemented |
| Documentation build | Configured | Verified by CI when a run succeeds |
| GitHub Pages deployment | Prepared | Not authorized here |

## The essential boundary

Studio receives versioned, attributable records and renders them for review. Any proposal produced in Studio remains non-authoritative until an external, authorized system and designated human reviewer accept it.

```text
Versioned evidence inputs
          |
          v
+-------------------------+
| QSO-STUDIO review model |
| parse -> validate ->     |
| normalize -> display     |
+-------------------------+
          |
          v
Non-authoritative notes and proposals
          |
          v
External human review and authorized systems
```

Studio does not become the source of truth simply because it offers a convenient interface.

## Start here

1. Read the [project overview](project-overview.md) for users, goals, and scope.
2. Review the [architecture](architecture.md) for data flow and trust boundaries.
3. Examine the [design contracts](design.md) and [evidence-review workflow](workflows/evidence-review.md).
4. Use the [developer onboarding guide](development/onboarding.md) to build and review the documentation.
5. Consult [operations and recovery](operations.md) before publishing any documentation artifact.

## Approval still required

The product/UX charter still needs an explicit decision on target users, first supported platform, distribution model, privacy and retention defaults, license, ecosystem ownership, and the upstream contracts that are authoritative for the first fixture-backed workflow. Until those decisions are recorded, this site must be treated as a review candidate rather than a product release.
