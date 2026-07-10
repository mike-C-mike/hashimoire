# Hashing

Hashing is one of the core integrity tools in digital forensics and defensive security.

A hash can help show whether a file, image, export, or dataset changed between two points in time. It can support acquisition verification, working copy validation, export review, malware triage, file identification, and handoff documentation.

A hash does not prove everything.

It does not prove who created a file. It does not prove a file is true. It does not prove an acquisition was complete. It does not replace chain of custody. It is a scoped integrity check, and its value depends on documenting what was hashed, when, how, with what tool, and why.

## Contents

- [Hash Basics](hash-basics.md)
- [Hash Algorithms](hash-algorithms.md)
- [Hash Documentation](hash-documentation.md)

## Common Uses

Hashing is commonly used to:

- verify a forensic image after acquisition
- compare a copy against a source
- confirm that an export has not changed
- identify known files
- support malware or suspicious file triage
- document evidence transfers
- detect accidental corruption
- support repeatable review

## What to Document

When using a hash in an evidence or security workflow, document:

- what was hashed
- where it was located
- when it was hashed
- who performed the hashing
- what tool or command was used
- what algorithm was used
- the resulting hash value
- what the hash is meant to prove
- any limitations or exceptions

## Practical Rule

A hash is strongest when the scope is clear.

Bad documentation:

```text
Hash verified.