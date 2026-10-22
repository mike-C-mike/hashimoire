# Windows — Volume Shadow Copy Inventory

**Use case:** triage | preservation | validation  
**Environment:** windows  
**Risk:** safe

## Why it matters

Existing Volume Shadow Copies (VSS) may contain prior versions of files, registry hives, logs, or other volume content. The first task in live triage is **inventory**, not creating, mounting, or deleting snapshots.

## Read-only inventory

```powershell
vssadmin list shadows
vssadmin list shadowstorage
```

Alternative provider view (administrator privileges may be needed):

```powershell
Get-CimInstance Win32_ShadowCopy |
  Select-Object ID, VolumeName, DeviceObject, InstallDate
```

## What to record

- Source volume, Shadow Copy ID, creation time, snapshot device path, and reported storage association.
- Whether snapshots were unavailable, inaccessible, or absent.
- System time/timezone and collector privilege context.

## Cautions

- **No snapshots returned** does not prove the volume never had snapshots.
- Windows may delete snapshots due to retention/storage pressure; creation timestamps require time-zone normalization.
- This is an inventory, not an acquisition. For defensible review, image the source and use validated lab tools to examine VSS.
- Avoid `vssadmin delete`, `resize`, `shadowcopy call create`, or other source-changing commands during initial evidence preservation.

## Official reference

[Microsoft — vssadmin list shadows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/vssadmin-list-shadows)

[Back to Windows snippets](README.md)
