
---

## `docs/hashing/hash-documentation.md`

```markdown
# Hash Documentation

## Purpose

This note provides a practical checklist for documenting hash values in digital evidence and defensive security workflows.

A hash value is only useful if someone can understand what it applies to.

## Core Documentation Fields

When documenting a hash, capture:

```text
Item identifier:
Item description:
Source path or location:
Output path or location:
Hash algorithm:
Hash value:
Tool or command used:
Tool version:
Date and time calculated:
Person calculating hash:
Purpose of hash:
Verification result:
Notes or limitations:


Evidence-Oriented Example

Item identifier: Item001
Item description: Forensic image of submitted USB drive
Source evidence: USB drive, evidence tag PD-2026-001
Output file: Item001.E01
Hash algorithm: SHA-256
Hash value: [hash value]
Tool used: [tool name/version]
Date/time calculated: 2026-07-10 14:32 CST
Calculated by: [name/initials]
Purpose: Verify forensic image after acquisition
Verification result: Image verified successfully
Notes: Source device returned to evidence storage after acquisition

Export-Oriented Example

Item identifier: Export001
Item description: ZIP export of selected files for investigator review
Source: Working copy derived from Item001.E01
Output file: Export001_selected-files.zip
Hash algorithm: SHA-256
Hash value: [hash value]
Tool used: Get-FileHash / PowerShell
Date/time calculated: 2026-07-10 15:04 CST
Calculated by: [name/initials]
Purpose: Document integrity of review export before handoff
Verification result: Hash recorded before transfer
Notes: Hash applies to ZIP export only, not to the original device or full forensic image

Transfer-Oriented Example

Item identifier: Export001
Item description: ZIP export transferred to review storage
Original SHA-256: [original hash]
Post-transfer SHA-256: [post-transfer hash]
Tool used: Get-FileHash / PowerShell
Date/time verified: 2026-07-10 15:42 CST
Verified by: [name/initials]
Purpose: Confirm export did not change during transfer
Verification result: Hash values matched
Notes: Transfer completed to approved review location