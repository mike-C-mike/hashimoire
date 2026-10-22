# Hash Documentation — Field and Lab Template

**Use case:** acquisition | verification | evidence transfer  
**Risk:** caution

## Record the object and context

The hash value alone is not a defensible record. Document *which bytes* were tested, *how* they were obtained, and whether the comparison was source-to-image, copy-to-copy or export-to-export.

```text
Case/incident reference:
Evidence item ID:
Source object/device and identifiers:
Acquired object/file path:
Acquisition/collection tool and version:
Hash tool and version:
Hash algorithm:
Original/source hash if available:
Acquired image/export hash:
Verification hash and comparison result:
Collector/examiner:
Start and completion dates/times with offsets:
Storage destination and access restrictions:
Errors, excluded data or acquisition limitations:
Chain-of-custody/transfer record:
```

## Worked example — synthetic

```text
Item: LAB-001 (fictional)
Source: submitted USB flash drive — sealed Item 001
Acquired output: Item001.E01
Tool: validated imaging utility (version recorded in case worksheet)
Hash algorithm: SHA-256
Acquisition verification: reported successful, source/acquisition hashes match
Time completed: 2026-10-21 15:30 -05:00
Custodian: Examiner A
Notes: verification applies to acquired logical/physical scope stated in tool report
```

**Important:** Some forensic image formats include metadata/container details. Hashes shown in an image's internal verification record may be computed over source data and differ from a direct SHA-256 hash of the entire `.E01` container file. **Document exactly which digest and scope you're comparing**, not merely "hash matched."

## Transfer verification

1. Preserve the original acquisition/hash log.
2. Copy the evidence using approved storage and access controls.
3. Recalculate an appropriate hash of the same object after transfer.
4. Compare like with like (same algorithm, same bytes and hash scope).
5. Document success, failure, errors and custody details.

If digests differ, don't overwrite the original or erase the log. Record the discrepancy and investigate file completeness, container/hash scope and transfer errors.

## Windows quick check

```powershell
Get-FileHash -LiteralPath 'E:\CASE-EXAMPLE\export.zip' -Algorithm SHA256 |
  Format-List Algorithm, Hash, Path
```

## Reporting language

**Useful:** "The SHA-256 digest of the acquired export file matched the digest recalculated after transfer; the values and timestamps are preserved in the collection log."

**Too broad:** "The hash proves the original device was never changed."

[Hashing home](README.md) · [Windows hashing snippet](../../snippets/powershell/sha256-evidence.md)
