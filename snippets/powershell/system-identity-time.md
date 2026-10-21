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

## Collection cautions
Record an independent trusted/reference time **before** comparing clocks. `Get-Date` reports the target's configured clock and can be wrong; do not alter it. A blank `UserName` does not prove nobody is logged on. Record collection command, privilege level, exact timestamp, and output location.
