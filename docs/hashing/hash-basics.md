
---

## `docs/hashing/hash-basics.md`

```markdown
# Hash Basics

## Purpose

This note explains what hashing does, what it does not do, and why it matters in digital forensics and defensive security workflows.

## What a Hash Is

A hash is a fixed-length value generated from input data using a hashing algorithm.

The input can be:

- a file
- a forensic image
- a folder manifest
- an exported report
- a disk image segment
- a block of text
- a dataset
- a piece of malware
- almost any other digital content

The output is a value that acts like a fingerprint for that exact input.

If the input changes, the hash should change.

## Example

A file is hashed before transfer:

```text
File: evidence-export.zip
Algorithm: SHA-256
Hash: 3a7bd3e2360a3d29eea436fcfb7e44c735bfbec1b0e22cdd9b8c4f2fd6f78e92