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

## Cautions

- These examples inspect the **current account**. Other users, redirected folders, OneDrive, and browsers may use different locations.
- File timestamps and shortcuts may be modified or cleaned; no artifact implies neither absence of use nor exfiltration.
- Live browsing can alter access metadata. For full examination, preserve approved profile artifacts and parse on a forensic working copy.

## Official reference

[Microsoft — Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)

[Back to Windows snippets](README.md)
