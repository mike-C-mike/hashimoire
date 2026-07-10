
---

## `docs/hashing/hash-algorithms.md`

```markdown
# Hash Algorithms

## Purpose

This note summarizes common hash algorithms used in digital forensics and defensive security workflows.

It is not a cryptography deep dive. The goal is practical decision support for documentation, acquisition, verification, and review.

## Common Algorithms

Common hashing algorithms include:

- MD5
- SHA-1
- SHA-256
- SHA-512

Older workflows and tools may still use MD5 or SHA-1. Modern workflows should prefer stronger SHA-2 or SHA-3 family algorithms when available and appropriate.

## MD5

MD5 produces a 128-bit hash.

It is:

- fast
- widely supported
- common in older forensic workflows
- still present in legacy reports and hash sets
- useful for some compatibility purposes

MD5 also has known collision weaknesses.

A collision means two different inputs can produce the same hash value. MD5 collisions have been publicly demonstrated, and MD5 should not be treated as the preferred modern integrity algorithm when adversarial manipulation is a realistic concern.

That does not mean every historical MD5 value is useless. MD5 may still appear in legacy workflows, old reports, or existing hash sets. It can still help detect accidental changes in many routine contexts.

The limitation should be understood and documented.

## SHA-1

SHA-1 produces a 160-bit hash.

It is stronger than MD5 historically, but it also has known collision weaknesses and is being phased out across modern security practice.

SHA-1 may still appear in:

- older forensic tools
- historical reports
- existing file reputation systems
- legacy hash sets
- older acquisition workflows

Current workflows should move toward SHA-2 or SHA-3 family algorithms where possible.

## SHA-256

SHA-256 is part of the SHA-2 family and produces a 256-bit hash.

It is commonly preferred in modern forensic and security workflows because it provides stronger collision resistance than MD5 or SHA-1.

SHA-256 is a strong default choice for:

- forensic image verification
- export verification
- file integrity documentation
- evidence transfer documentation
- malware sample identification
- modern defensive security workflows

The tradeoff is time. Hashing large devices, images, exports, or datasets with SHA-256 can take noticeable time depending on:

- data size
- storage speed
- tool behavior
- whether multiple hashes are being calculated
- whether the workflow is read-limited or write-limited

The time cost is usually worth it where stronger integrity documentation matters.

## SHA-512

SHA-512 is also part of the SHA-2 family and produces a 512-bit hash.

It may be used in some security and forensic contexts, but SHA-256 is often the more common practical default for broad compatibility and documentation.

SHA-512 may be useful when:

- the tool already supports it
- the workflow requires it
- policy requires it
- stronger SHA-2 output is desired
- compatibility is not a concern

## Practical Algorithm Guidance

Use stronger algorithms where possible.

Practical default:

```text
Prefer SHA-256 for modern integrity documentation.