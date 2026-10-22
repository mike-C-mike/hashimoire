# Hash Algorithms — Choosing a Forensic Digest

**Use case:** acquisition verification | file integrity | compatibility  
**Risk:** safe

| Algorithm | Digest length | Forensic position |
| --- | --- | --- |
| MD5 | 128 bits / 32 hex digits | Common in older evidence/hash-set workflows; collision-weak. |
| SHA-1 | 160 bits / 40 hex digits | Legacy interoperability; collision-weak. |
| SHA-256 | 256 bits / 64 hex digits | Strong general-purpose modern default. |
| SHA-512 | 512 bits / 128 hex digits | Valid SHA-2 option; use when supported or required. |

## Practical guidance

**Use SHA-256 as the default** for newly calculated forensic integrity values, provided acquisition tooling and policy permit it. Document any required legacy MD5/SHA-1 values as compatibility hashes rather than claiming they are stronger than SHA-256.

A SHA-256 match demonstrates very high confidence that the **same bytes** were hashed twice. It is not a source-authentication proof or substitute for case documentation.

### Why MD5/SHA-1 are treated differently

Researchers demonstrated practical collision attacks against these algorithms. That matters particularly where adversarial manipulation is plausible. A historical MD5 value may still be useful for comparison with a legacy report or tool hash set, but use a modern hash alongside it where supported.

## Example using PowerShell

```powershell
Get-FileHash -LiteralPath 'E:\CASE-EXAMPLE\memory.raw' -Algorithm SHA256
```

**Expected output fields:** Algorithm, Hash and Path. The hash applies to that image file's bytes. Changing even a small portion of the file is expected to change a secure digest.

## Hashing a collection

There is no universal hash for "a folder" unless the workflow defines a byte representation or manifest method. For a file-set manifest, record each relative path, file size and individual digest; preserve the manifest and the original directory context. If files are added/removed, the manifest must be recomputed.

## References

- [NIST FIPS 180-4 — Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)
- [NIST SP 800-131A Rev. 2 — Algorithm transitions](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final)

[Hash basics](hash-basics.md) · [Documentation](hash-documentation.md)
