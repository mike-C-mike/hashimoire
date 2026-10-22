# Windows — USB and External Storage History

**Use case:** triage | validation | acquisition  
**Environment:** windows  
**Risk:** safe

## Why it matters

Connected and previously enumerated devices can help scope a possible file transfer or removable-media event. Do not equate a device record with proof of a particular user copying files.

## 1. Enumerate known disks and Plug-and-Play devices

```powershell
Get-PnpDevice -Class DiskDrive |
  Select-Object FriendlyName, InstanceId, Status

Get-PnpDevice -Class DiskDrive -PresentOnly |
  Select-Object FriendlyName, InstanceId, Status
```

The first command can include **non-present** devices; the second limits output to currently present devices.

## 2. Read the historic USB storage registry keys

```powershell
Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR' -ErrorAction SilentlyContinue |
  Select-Object PSChildName, Name

Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Enum\USB' -ErrorAction SilentlyContinue |
  Select-Object PSChildName, Name
```

## 3. Record current mounted logical volumes

```powershell
Get-Volume |
  Select-Object DriveLetter, FileSystemLabel, FileSystem, DriveType, HealthStatus
```

## Expected output

Device descriptions and instance identifiers, USB/USBSTOR registry enumeration, current volumes and drive letters.

## Forensic interpretation cautions

- The `USB` class includes many device types; `USBSTOR` is not a comprehensive record of all external media (e.g. UASP devices).
- Current drive letters are transient, not historical assignments. Registry data alone does **not** establish insertion timestamps, file copying, or user attribution.
- For definitive timelines, preserve SYSTEM/SOFTWARE/NTUSER.DAT hives, event logs and other artifacts and analyze with validated forensic parsers.

## Official reference

[Microsoft — Get-PnpDevice](https://learn.microsoft.com/en-us/powershell/module/pnpdevice/get-pnpdevice)

[Back to Windows snippets](README.md)
