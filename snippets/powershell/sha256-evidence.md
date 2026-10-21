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

## Collection cautions
Replace example paths. Hashing verifies an acquired item's integrity over time; it does **not** make a live acquisition bit-for-bit identical to the source at all times. Preserve original evidence and hash again after transport, comparing manifests; document differences and acquisition-tool versions.
