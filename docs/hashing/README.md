# Hashing — Evidence Integrity

**Use case:** acquisition | copy verification | export transfer | reporting  
**Audience:** collectors and examiners

Hashing answers a precise question: **were the bytes in this item the same when checked at two different stages?** It does not prove authenticity, attribution, acquisition completeness or lawful custody.

## Start with the right reference

| Need | Page | What you get |
| --- | --- | --- |
| Understand what a hash proves | [Hash basics](hash-basics.md) | A worked acquisition-to-transfer example and limitations |
| Choose or interpret MD5/SHA-1/SHA-256 | [Hash algorithms](hash-algorithms.md) | Strength, compatibility and forensic use cases |
| Produce a defensible hash record | [Hash documentation](hash-documentation.md) | Practical fields, repeat verification and example notes |
| Run the command on Windows | [PowerShell SHA-256](../../snippets/powershell/sha256-evidence.md) | Copy-ready commands, output and lab meaning |

## Fast Windows example

```powershell
Get-FileHash -LiteralPath 'E:\CASE-EXAMPLE\evidence-export.zip' -Algorithm SHA256 |
    Format-List Algorithm, Hash, Path
```

**Expected:** algorithm, a 64-character SHA-256 hexadecimal digest and the file path. Re-running on an unchanged copy should produce the same digest.

**Important:** A command that hashes a *logical export* does not automatically prove a *source disk* was completely and accurately acquired. Record precisely what object was hashed.

## Core field documentation

Record case/item ID, source and output names, acquisition method, original hash (if available), verification hash, algorithm, tool/version, date/time with timezone, operator and handling/custody events.

## Interpretation

A hash match supports byte equality to very high confidence for the tested objects, but must be interpreted with the method used, acquisition logs, scope and errors. Hash values are not timestamps or digital signatures.

[Acquisition playbook](../../playbooks/acquisition/0-rapid-evidence-collection.md)
