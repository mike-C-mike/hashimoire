# Windows — Defender Detection and Status Context

**Use case:** triage | response | validation  
**Environment:** windows  
**Risk:** safe

## Why it matters

Antivirus and EDR records can indicate detection timing, actions taken and files involved. The live Defender cmdlets are a **quick look**, not a substitute for preserved platform logs or EDR telemetry.

## Read-only status

```powershell
Get-MpComputerStatus |
  Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated
```

## Recorded detections (if available)

```powershell
Get-MpThreatDetection |
  Select-Object InitialDetectionTime, LastThreatStatusChangeTime, ThreatID, ActionSuccess, Resources
```

## Available Defender event logs

```powershell
Get-WinEvent -ListLog 'Microsoft-Windows-Windows Defender/Operational' |
  Select-Object LogName, IsEnabled, RecordCount, MaximumSizeInBytes
```

## Cautions

- Defender may be inactive or managed in passive mode on machines using other protection software.
- Defender detections may reflect quarantined or blocked items rather than successful malware execution.
- Missing results do not prove the endpoint was clean; logs and telemetry may be unavailable or expired.
- Paths and resources may contain identifying or sensitive data.
- Export relevant `.evtx` and EDR records to evidence media under the incident's approved collection plan.

## Official reference

[Microsoft — Get-MpComputerStatus](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpcomputerstatus)  
[Microsoft — Get-MpThreatDetection](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatdetection)

[Back to Windows snippets](README.md)
