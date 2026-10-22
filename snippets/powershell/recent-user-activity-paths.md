# Windows — Recent User-Activity Artifact Locations

**Use case:** triage | acquisition | validation  
**Environment:** windows  
**Risk:** caution

## Why it matters

Quickly identify candidate evidence locations for downloads, recently accessed files, Jump Lists, and other user-profile artifacts **without interpreting them as conclusive proof**.

## Inspect current profile paths

```powershell
$Recent = Join-Path $env:APPDATA 'Microsoft\Windows\Recent'
Get-ChildItem -LiteralPath $Recent -Force -ErrorAction SilentlyContinue |
  Select-Object Name, FullName, LastWriteTimeUtc

Get-ChildItem -LiteralPath (Join-Path $Recent 'AutomaticDestinations') -Force -ErrorAction SilentlyContinue |
  Select-Object Name, Length, LastWriteTimeUtc

Get-ChildItem -LiteralPath (Join-Path $Recent 'CustomDestinations') -Force -ErrorAction SilentlyContinue |
  Select-Object Name, Length, LastWriteTimeUtc
```

## Inspect current profile Downloads metadata

```powershell
$Downloads = Join-Path $env:USERPROFILE 'Downloads'
if (Test-Path -LiteralPath $Downloads) {
  Get-ChildItem -LiteralPath $Downloads -File -Force -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTimeUtc -Descending |
    Select-Object -First 30 Name, Length, LastWriteTimeUtc, FullName
}
```

## Example output — synthetic lab profile

```text
Name                           LastWriteTimeUtc          Length
----                           ----------------          ------
Report Draft.lnk               2026-10-21 14:08:17Z
9b9cdc69c1c24e2b.automaticDestinations-ms
                               2026-10-21 14:11:02Z       4096
```

### Interpretation

- **`.lnk`** files are Windows shortcuts that may contain target paths and metadata about a file or volume.
- **`.automaticDestinations-ms`** files are Jump List artifacts used by Windows and applications to represent recent or pinned activity.
- **LastWriteTimeUtc** is a filesystem timestamp for the artifact file, **not necessarily** the exact time a referenced document was opened.
- Correlate parsed target/entry timestamps with other sources before attributing file access or movement to a person.

## Cautions

- These examples inspect the **current account**. Other users, redirected folders, OneDrive, and browsers may use different locations.
- File timestamps and shortcuts may be modified or cleaned; no artifact implies neither absence of use nor exfiltration.
- Live browsing can alter access metadata. For full examination, preserve approved profile artifacts and parse on a forensic working copy.

## Official reference

[Microsoft — Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)

[Back to Windows snippets](README.md)
