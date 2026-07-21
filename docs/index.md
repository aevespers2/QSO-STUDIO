# QSO-STUDIO

QSO-STUDIO is a proposed visual workspace for reviewing evidence about Quantum State Objects, portable device-trust records, and related ecosystem artifacts. Its first bounded outcome is not a general-purpose orchestration console; it is a **read-only, fixture-backed review surface** that helps a researcher or operator understand what upstream systems report without granting Studio authority to execute, approve, write, sign, remediate, issue capabilities, or settle anything.

## Documentation status

This site describes a product charter, review contract, and architecture candidate. It is designed to make the repository truthful and reviewable before application development begins.

| Capability | Documentation status | Implementation status |
|---|---|---|
| Project scope and non-goals | Defined | Not applicable |
| Architecture and authority boundaries | Proposed | Not implemented |
| Evidence-review workflow | Specified | Not implemented |
| Portable trust review profile | Proposed | Not implemented |
| Obstruction and gluing analysis | Defined as engineering review | Not an operational compatibility claim |
| Accessible interaction requirements | Defined | Not implemented |
| Security and privacy controls | Defined | Not implemented |
| Documentation build | Configured | Verified only at exact heads where CI succeeds |
| GitHub Pages deployment | Prepared | Not authorized here |

## The essential boundary

Studio receives versioned, attributable records and renders them for review. Any annotation, comparison, proposal, or export produced in Studio remains non-authoritative until an external authorized system and designated human reviewer create the applicable disposition or approval record.

```text
Observation / interpretation / proposal / disposition / receipt
                         |
                         v
              +-------------------------+
              | QSO-STUDIO review model |
              | parse -> validate ->     |
              | normalize -> compare ->  |
              | display -> annotate      |
              +-------------------------+
                         |
                         v
             Non-authoritative review records
                         |
                         v
        Repository 1 and external human authority
```

Studio does not become the source of truth simply because it offers a convenient interface. Display, selection, annotation, export, or execution success cannot become approval or canonical acceptance.

## Portable device-trust role

For the portable first-install security and recovery foundation:

- observation adapters produce bounded evidence;
- Repository `0` creates local proposals and verifies separately authorized work;
- Repository `1` owns candidate quarantine, disposition, capability, revocation, canonical reconciliation, checkpoint, and recovery authority;
- QSO-STUDIO provides a domain-neutral review model;
- AionUi may later host an optional compatible desktop/WebUI adapter but must not redefine authority semantics.

The current material obstruction is that QSO-STUDIO and AionUi overlap as review surfaces without one accepted contract for annotations, comparison, exports, approval references, correction, revocation, caching, and recovery state.

## Start here

1. Read the [project overview](project-overview.md) for users, goals, and scope.
2. Review the [architecture](architecture.md) for data flow and trust boundaries.
3. Examine the [design contracts](design.md) and [evidence-review workflow](workflows/evidence-review.md).
4. Read the [portable trust review profile](portable-trust-review-profile.md) for Repository `0`/`1`, adapter, executor, AionUi, correction, revocation, and recovery boundaries.
5. Review the [obstruction and gluing analysis](obstruction-and-gluing.md) for active incompatibilities and required pairwise and triple-overlap fixtures.
6. Use the [developer onboarding guide](development/onboarding.md) to build and review the documentation.
7. Consult [operations and recovery](operations.md) before publishing any documentation artifact.

## Approval still required

The product/UX charter still needs an explicit decision on target users, first supported platform, distribution model, privacy and retention defaults, license, ecosystem ownership, QSO-STUDIO versus AionUi responsibilities, generic envelope and profile-registry ownership, Repository `1` disposition semantics, and the upstream contracts authoritative for the first fixture-backed workflow.

Until those decisions and exact-head validation are recorded, this site remains a review candidate rather than a product release.
