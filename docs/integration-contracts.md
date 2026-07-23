---
layout: default
title: Integration Contracts
---

# Integration Contracts

QSO-STUDIO consumes evidence and contract descriptions from other repositories. It does not define those repositories' canonical schemas or appoint their owners.

## Candidate corridors

| Upstream area | Studio purpose | Required before integration |
|---|---|---|
| QuantumStateObjects | Inspect runtime-local state and evidence | Accepted record classes, schema identity, correction and rollback semantics |
| QSO-GENOMES | Inspect genome declarations and lineage | Stable identifiers, version rules, provenance, supersession, migration |
| QSO-FABRIC | Inspect collaboration and aggregate records | Runtime-versus-aggregate namespace separation and transformation receipts |
| QSO-SEEKER | Inspect retrieval results and source observations | Source tuple, privacy classification, deduplication, withdrawal handling |
| QSO-DIGITALIS | Inspect source interpretation and projections | Source/interpretation separation and archive/correction behavior |
| QSO-PAYMENTS | Display payment-related evidence | Environment and custody separation; no settlement or approval authority |

## Current bounded consumer

The [independent ecosystem conformance consumer](ecosystem-conformance-consumer.md) binds QSO-FABRIC PR #21 at exact head `25036a5cfcea79e204a4660ddd1af09c054935b1`, manifest Git blob `5070ac6615b8127b14a9f230678f58a081c6c2c4`, and SHA-256 `c5e6d2e42fdbe9703d9f28c7f65ffff02208bff52fa96ee7090bfcbcb5dea728`. Studio verifies the exact bytes before applying an independently authored strict parser and evaluator.

That result is synthetic declaration-level evidence only. It does not accept the producer's namespaces, payloads, conformance levels, governance semantics, adapters, or operational authority.

## Contract tuple

Every implemented adapter must bind:

```text
producer repository
+ immutable producer generation
+ contract identifier and version
+ canonical byte or normalization rules
+ adapter identifier and version
+ fixture generation
+ correction and withdrawal semantics
+ consumer behavior
+ rollback witness
```

A matching label or parser success is not sufficient evidence of semantic compatibility.

## Obstruction checks

Integration remains blocked when record roles collide, two paths produce different meanings, a required owner is missing, a correction cannot reach the viewer, a consumer cannot rebind across generations, or rollback cannot restore a supported state.

## Current architectural clarification

The labels `qso-event-ledger` and `qso-runtime-report` have been used across runtime-local and Fabric-level concepts. Studio must not combine or display them as one record family until upstream namespaces and payload ownership are resolved. The manifest consumer preserves this obstruction rather than interpreting declaration agreement as live gluing success.

This contract map is an observation and planning aid governed by `QSO-CONSENT-CAPACITY-LOCK-v1`; it creates no interface acceptance or operational authority.
