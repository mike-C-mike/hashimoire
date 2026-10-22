# Windows — Disk, Partition, and Volume Layout

**Use case:** acquisition | triage | validation  
**Environment:** windows  
**Risk:** safe

## Why it matters

Record which physical/virtual disks, partitions, mounted volumes, and removable media are visible **before changing power state or attaching acquisition devices**. Drive letters alone are not stable physical identifiers.

## Read-only inventory

```powershell
Get-Disk |
  Select-Object Number, FriendlyName, SerialNumber, BusType, OperationalStatus, PartitionStyle, Size

Get-Partition |
  Select-Object DiskNumber, PartitionNumber, DriveLetter, Type, Offset, Size

Get-Volume |
  Select-Object DriveLetter, FileSystemLabel, FileSystem, DriveType, Size, SizeRemaining
```

Optional physical-device provider view:

```powershell
Get-CimInstance Win32_DiskDrive |
  Select-Object Index, Model, SerialNumber, InterfaceType, PNPDeviceID, Size
```

## Example output — synthetic lab scenario

```text
Number FriendlyName             BusType PartitionStyle Size
------ ------------             ------- -------------- ----
0      Example NVMe SSD         NVMe    GPT            512110190592
1      Example External SSD     USB     GPT            1000204886016
```

### What an examiner should notice

- **DiskNumber 0:** the example internal disk; number alone can change across boots and device reconfiguration.
- **DiskNumber 1:** the externally attached example drive; verify **serial number, physical connection and timing** before deciding it's acquisition media rather than the evidence source.
- **BusType / PartitionStyle:** hints at connection method and partitioning—not a complete volume map.
- **Size:** reported in **bytes**, not GB. Compare with imaging reports and partitions.
- Combine `Get-Disk`, `Get-Partition`, `Get-Volume` and external photos; never select a destructive target based on drive letter or number alone.

## Cautions

- The inventory may include virtual disks, Storage Spaces, removable media, and other logical devices; confirm before interpreting.
- Match drive number, device ID, serial, interface, and photo evidence—not letter alone.
- Running commands after connecting collection storage will include that new device; record the order of operations.
- No command here acquires a forensic disk image. Use approved tools and write blockers for applicable **offline** media acquisition.

## Official reference

[Microsoft — Get-Disk](https://learn.microsoft.com/en-us/powershell/module/storage/get-disk)  
[Microsoft — Get-Partition](https://learn.microsoft.com/en-us/powershell/module/storage/get-partition)

[Back to Windows snippets](README.md)
