# Windows — SHA-256 Evidence Hashes

**Use case:** validation | acquisition  
**Environment:** windows  
**Risk:** safe

## PowerShell (reads evidence and prints a hash)

```powershell
Get-FileHash -LiteralPath 'E:\CASE-EXAMPLE\volatile\memory.raw' -Algorithm SHA256 |
  Format-List Algorithm, Hash, Path
```

For an existing evidence folder, generate a manifest stored **outside the folder being hashed**:

```powershell
$Evidence = 'E:\CASE-EXAMPLE\volatile'
$Manifest = 'E:\CASE-EXAMPLE\hashes\volatile-sha256.csv'
New-Item -ItemType Directory -Path (Split-Path $Manifest) -Force | Out-Null
Get-ChildItem -LiteralPath $Evidence -Recurse -File |
  Get-FileHash -Algorithm SHA256 |
  Select-Object Path, Algorithm, Hash |
  Export-Csv -LiteralPath $Manifest -NoTypeInformation
```

## Expected output
SHA-256 hex digests tied to actual captured files and paths.

## Example output — synthetic digest

```text
Algorithm : SHA256
Hash      : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Path      : E:\\CASE-EXAMPLE\\volatile\\memory.raw
```

### Why an examiner cares

- **SHA-256** produces a 64-character hexadecimal digest for the exact bytes read from the file.
- **Hash** is the value to compare after moving the evidence from the field to the lab. The sample `AAA...` value above is an **illustrative placeholder**, not a real calculated result.
- Matching hashes support **byte-for-byte integrity of that acquired file**. They do not prove a live memory image was captured without omissions, or that acquisition left the source unchanged.
- Store the manifest with your custody record, tool/version, and acquisition dates. Re-hash the transferred copy and compare using the same algorithm.

## Collection cautions
Replace example paths. Hashing verifies an acquired item's integrity over time; it does **not** make a live acquisition bit-for-bit identical to the source at all times. Preserve original evidence and hash again after transport, comparing manifests; document differences and acquisition-tool versions.
