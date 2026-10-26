# Windows — Registry Hive Preservation

**Use case:** acquisition | preservation  
**Environment:** windows  
**Risk:** caution

> **Before examining:** `reg.exe save` obtains a **live logical hive snapshot** and affects the source's live environment. It may omit per-user `NTUSER.DAT`, `UsrClass.dat` and associated transaction logs. Forensic offline hive/ControlSet interpretation, log replay, UserAssist and BAM, see the [Registry examination guide](../../docs/windows/registry.md).

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

## Example output — synthetic acquisition

```text
E:\\CASE-EXAMPLE\\registry\\SYSTEM.hiv
E:\\CASE-EXAMPLE\\registry\\SOFTWARE.hiv
```

### What the files are

- **SYSTEM.hiv:** a logical snapshot of machine-level configuration including service/control-set and device-enumeration data.
- **SOFTWARE.hiv:** a logical snapshot of OS and application configuration.
- The returned **SHA-256 hashes** establish a reference for the collected snapshots, but not for the underlying registry at other points in time.
- These are **not text exports**; review them using a registry parser or a forensic suite in the lab. The output doesn't include user hives or all transaction logs.

## Cautions

- This writes acquired files to the designated destination. Confirm `E:\` is not the source volume before running.
- Registry exports can contain sensitive security configuration and identifying information. Store and restrict the evidence appropriately.
- Do not assume the live export has exactly the same state as an offline image at a different time.
- For more complete acquisition, favor validated tools such as KAPE (with appropriate targets) or full forensic imaging.

## Official reference

[Microsoft — reg save](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-save)

[Back to Windows snippets](README.md)
