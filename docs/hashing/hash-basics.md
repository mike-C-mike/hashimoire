# Hash Basics — What Matching Values Mean

**Use case:** evidence integrity | lab verification  
**Risk:** safe

## The concept

A cryptographic hash algorithm converts input bytes into a fixed-length digest. For SHA-256, the result is 256 bits, commonly displayed as **64 hexadecimal characters**. Repeating the calculation on *identical bytes* produces the same value.

A strong hash algorithm makes it computationally difficult to find different data with the same digest. For forensic use, prefer SHA-256 unless an applicable tool, policy or interoperability requirement specifies otherwise.

## Example — synthetic two-step verification

```text
Item: logical export of reviewed files
File: export.zip
Algorithm: SHA-256
At collection: 1111111111111111111111111111111111111111111111111111111111111111
After transfer: 1111111111111111111111111111111111111111111111111111111111111111
Result: hashes matched (illustrative placeholder digest, not real evidence)
```

This supports that the **two hashed versions of export.zip** matched. It does not show whether the export contains every relevant file, whether the original source was altered during collection, or which person created those files.

## Windows and Linux/macOS commands

```powershell
Get-FileHash -LiteralPath 'E:\CASE-EXAMPLE\export.zip' -Algorithm SHA256
```

```bash
sha256sum export.zip         # Linux
shasum -a 256 export.zip    # macOS
```

For evidence, use an approved storage location and record tool versions and timestamps. Never rely on filenames alone to identify what was hashed.

## What hashes cannot prove

- **Authenticity:** a hash does not prove content is truthful or unmodified before acquisition.
- **Completeness:** a hash of one file says nothing about missing items elsewhere.
- **Attribution:** no hash identifies an author, user or examiner.
- **Custody:** hashes supplement—not replace—chain-of-custody documentation.
- **When:** the hash algorithm does not encode a time. A separately documented timestamp is needed.

[Algorithm comparison](hash-algorithms.md) · [Documentation template](hash-documentation.md)
