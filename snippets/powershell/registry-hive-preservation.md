# Windows — Registry Hive Preservation

**Use case:** acquisition | preservation  
**Environment:** windows  
**Risk:** caution

## Why it matters

Registry hives contain durable system configuration, services, known devices and other Windows artifacts that can be examined with specialist forensic parsers. This is a **logical live snapshot**, not an offline raw image.

## Export selected machine hives to authorized acquisition media

Run in elevated PowerShell. **Change the example destination** to a prepared external evidence drive and record its identity before execution.

```powershell
$Out = 'E:\CASE-EXAMPLE\registry'  # CHANGE to approved external evidence media
New-Item -ItemType Directory -Path $Out -Force | Out-Null

reg.exe save 'HKLM\SYSTEM' (Join-Path $Out 'SYSTEM.hiv') /y
reg.exe save 'HKLM\SOFTWARE' (Join-Path $Out 'SOFTWARE.hiv') /y

Get-ChildItem -LiteralPath $Out -Filter '*.hiv' |
  Get-FileHash -Algorithm SHA256
```

## Why these two?

- **SYSTEM:** services, control sets, enumerated devices, and other machine configuration.
- **SOFTWARE:** application and Windows configuration.

User-profile registry artifacts (`NTUSER.DAT`, `UsrClass.dat`) and transaction logs require an **additional approved acquisition workflow**; `reg save` alone is not a complete registry collection.

## Cautions

- This writes acquired files to the designated destination. Confirm `E:\` is not the source volume before running.
- Registry exports can contain sensitive security configuration and identifying information. Store and restrict the evidence appropriately.
- Do not assume the live export has exactly the same state as an offline image at a different time.
- For more complete acquisition, favor validated tools such as KAPE (with appropriate targets) or full forensic imaging.

## Official reference

[Microsoft — reg save](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-save)

[Back to Windows snippets](README.md)
