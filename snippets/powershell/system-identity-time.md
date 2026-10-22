# Windows — System Identity and Time

**Use case:** triage | validation  
**Environment:** windows  
**Risk:** safe

## When to use
At the beginning of authorized live response, after documenting the untouched screen and physical state.

## PowerShell (read-only)

```powershell
Get-Date -Format o
Get-TimeZone | Select-Object Id, DisplayName, BaseUtcOffset
hostname
Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption, Version, BuildNumber, LastBootUpTime, OSArchitecture
Get-CimInstance Win32_ComputerSystem |
  Select-Object Manufacturer, Model, Name, UserName, TotalPhysicalMemory
Get-CimInstance Win32_BIOS | Select-Object SerialNumber, SMBIOSBIOSVersion
```

## Expected output
Local time with offset, configured timezone, system/OS identity, last boot, make/model, serial number, and user context where available.

## Example output — synthetic lab system

```text
2026-10-21T10:03:02.1531245-05:00
Id            : Central Standard Time
DisplayName   : (UTC-06:00) Central Time (US & Canada)
Hostname      : LAB-WS01
Caption       : Microsoft Windows 11 Enterprise
BuildNumber   : 26100
LastBootUpTime: 2026-10-20 07:42:11
SerialNumber  : LAB-SERIAL-001
```

### How to interpret it

- **The `-05:00` offset** is the example clock's current offset from UTC. Windows reports a local timestamp, so document both the reference time and any observed drift. The configured time-zone *ID* does not itself prove the clock is correct.
- **LastBootUpTime** helps explain why RAM/process artifacts from before the most recent boot may be absent.
- **Hostname and serial** tie the snapshot to a specific device, but names can be changed and virtual machines may report generic identifiers.
- For an intrusion timeline, reconcile this baseline against **server-side timestamps** such as EDR, authentication, and proxy events.

## Collection cautions
Record an independent trusted/reference time **before** comparing clocks. `Get-Date` reports the target's configured clock and can be wrong; do not alter it. A blank `UserName` does not prove nobody is logged on. Record collection command, privilege level, exact timestamp, and output location.
