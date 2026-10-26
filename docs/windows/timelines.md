# Windows Intrusion Timeline — From PID to Evidence-Based Finding

**Audience:** trained forensic examiners | DFIR analysts  
**Question:** *Did a specific process start, make a network connection, and relate to an incident — or are we connecting unrelated events?*  
**Use case:** Windows incident reconstruction | process/network correlation | courtroom-ready limitations  
**Risk:** caution — timestamps, missing logs and PID reuse  
**Sources reviewed:** October 26, 2026

> **This is a fictional Windows workstation incident, not an actual case.** No source event or IP below comes from real evidence. All procedures are for an **authorized, isolated lab workstation analyzing an acquired working copy**, unless explicitly labeled as a historical live collection. Document applicable authority, image verification, clock context and tools under [SWGDE 18-F-001-2.0 (Feb 28, 2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/).

## Case question and three independent questions

**Hypothesis:** An Office document may have caused PowerShell to launch, and that PowerShell instance may have connected to an external address.

Do not collapse this into “Word malware exfiltrated data.” Work through the distinct claims:

1. **Execution:** Did a particular binary/process instance start on this host at the relevant time?
2. **Relationship:** Was that process created by the suspected parent, and was it the *same* process associated with network activity?
3. **Interpretation:** Did any records establish malicious intent, a payload, data content, successful access or a specific human actor?

### Example event set — synthetic UTC timeline

| UTC time | Source | Observation | Strength / limitation |
| --- | --- | --- | --- |
| **15:02:14** | Sysmon Event 1 | `WINWORD.EXE` process **PID 4024** created; `ProcessGuid={LAB-WORD}` (symbolic placeholder). | Strong process-start observation **if log is genuine and correctly sourced**. |
| **15:03:02** | Security 4688 | `powershell.exe` new PID `0x17F0`, creator PID `0x0FB8`. | Indicates process creation; PIDs need hexadecimal → decimal conversion. |
| **15:03:02** | Sysmon Event 1 | `powershell.exe`, **PID 6128**, parent **4024**, `ProcessGuid={LAB-PS}` (symbolic placeholder). | Helps correlate the 4688 record and distinguish an instance, if Sysmon was enabled. |
| **15:03:10** | Sysmon Event 3 | Outbound TCP to **203.0.113.44:443** with `ProcessGuid={LAB-PS}`. | Connection metadata, **not the contents of network traffic**. |
| **15:03:02-ish** | Prefetch artifact | Recent recorded launch near incident window for `POWERSHELL.EXE`. | Historical supporting evidence; timestamps may not equal exact process creation. |
| **Later analysis** | Amcache inventory | An executable path appears in inventory. | A presence/inventory lead; **not** a timed launch by itself. |

**Documentation-only values:** `203.0.113.44` is reserved for examples; all accounts and GUIDs in this table are placeholders. The symbolic `{LAB-PS}` labels are **not literal Sysmon GUID syntax**. Real Sysmon records contain actual GUID values.

## 1. Preserve and verify the inputs

Review the handoff and acquisition metadata:

- Original evidence/image identifier, acquisition tool/build, access/encryption decisions and **SHA-256 integrity** records.
- System build and **system clock / time-zone offset** at collection. A logged UTC time and a system-wall-clock observation can legitimately differ.
- Source log paths, **full EVTX exports** where available, available event coverage, last write/creation information and obvious gaps.
- Memory image (if acquired) and process/network snapshots, with collection time and scope.
- Prefetch, Amcache, SYSTEM registry hive, and any transaction/companion files relevant to those sources.
- External DNS, firewall, proxy, EDR or identity records and their independent clocks **only if authorized and preserved**.

**Work from a protected duplicate** and record any parser-created CSV or timeline as **derivative material**. If event logs are absent, ask whether audit policy, configuration or retention explains it before interpreting absence as evasion.

## 2. Convert PIDs correctly — and avoid a false match

The example Security 4688 values use **hexadecimal**, but live API output is typically shown in decimal.

```powershell
# Run on a lab machine; no evidence source is modified.
[Convert]::ToInt64('17F0', 16)   # 6128: example new process PID
[Convert]::ToInt64('0FB8', 16)   # 4024: example creator PID
```

```text
explorer.exe (PID 2540)
└── WINWORD.EXE (PID 4024)
    └── powershell.exe (PID 6128) ← suspected network connection
```

**What this does NOT prove:** PIDs are temporary and can be **reused**. PID 6128 during an incident and PID 6128 a day later may describe *different processes*. Validate the host, source/log version, process creation time, session and parent. When available, correlate Sysmon **ProcessGuid** across Event 1 and Event 3 instead of relying solely on a PID.

**One more distinction:** The displayed tree is a **reconstruction from reported relationships**, not a complete unbroken timeline of every program that ever ran.

## 3. Read actual Security 4688 fields from an acquired EVTX

The following reads a **copied log on the lab** and exports derived results. Change the example paths first, and confirm the results directory exists on controlled lab storage.

```powershell
# PowerShell 5.1+ on an approved Windows analysis workstation
$Log = 'D:\CASE-EXAMPLE\evidence\evtx\Security.evtx'
$Output = 'D:\CASE-EXAMPLE\results\security-4688.csv'

Get-WinEvent -FilterHashtable @{ Path = $Log; Id = 4688 } -MaxEvents 500 |
  ForEach-Object {
    $Event = $_
    $Fields = @{}
    foreach ($Data in ([xml]$Event.ToXml()).Event.EventData.Data) {
      if ($Data.Name) {
        $Fields[[string]$Data.Name] = [string]$Data.'#text'
      }
    }
    $NewPid = $Fields['NewProcessId']
    $ParentPid = $Fields['ProcessId']  # Creator PID field in Event 4688 XML
    [pscustomobject]@{
      UtcTime       = $Event.TimeCreated.ToUniversalTime().ToString('o')
      Host          = $Event.MachineName
      NewProcess    = $Fields['NewProcessName']
      NewPIDHex     = $NewPid
      NewPIDDecimal = if ($NewPid) { [Convert]::ToInt64(($NewPid -replace '^0x',''),16) } else { $null }
      ParentPIDHex  = $ParentPid
      ParentPIDDec  = if ($ParentPid) { [Convert]::ToInt64(($ParentPid -replace '^0x',''),16) } else { $null }
      CreatorLogon  = $Fields['SubjectLogonId']
      CommandLine   = $Fields['CommandLine']
    }
  } |
  Export-Csv -LiteralPath $Output -NoTypeInformation -Encoding UTF8
```

### Interpreting the results

- **NewProcess / NewPID:** which process the 4688 event records starting, with IDs from the original event XML.
- **ParentPID:** the process identifier the event attributes as creator; match to its **own creation record**, not simply a currently running same-numbered process.
- **CreatorLogon:** a session/logon correlator; use identity and logon records to understand context, not to assert who physically initiated it.
- **CommandLine:** often blank unless the OS **was configured before execution** to include command lines. Even when present, it can contain secrets, tokens or PII; restrict access to the resulting CSV.
- **UtcTime:** derived from the event provider's reported timestamp; `TimeCreated` is displayed according to host/time-zone rules. An original incorrect clock remains incorrect after conversion.

**Cautions:** The sample exports only the **newest 500 matching events** returned by the query; it does **not** exhaust a busy log. To establish complete coverage, use the full EVTX, an appropriate time-bounded filter, documented count and a validated analysis tool. A missing CSV row is not proof no event occurred. Field names/availability vary by event version.

Reference: [Microsoft Security Event 4688](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688).

## 4. If Sysmon was already installed, correlate ProcessGuid

Sysmon produces Event 1 for process creation and Event 3 for some network connections **when its configuration collects them**. Event 3 is disabled by default. Confirm whether Sysmon existed on the source at the time and preserve its original operational EVTX. [Microsoft Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

```powershell
$Log = 'D:\CASE-EXAMPLE\evidence\evtx\Microsoft-Windows-Sysmon%4Operational.evtx'
Get-WinEvent -FilterHashtable @{ Path = $Log; Id = 1,3 } -MaxEvents 500 |
  ForEach-Object {
    $Event = $_
    $Fields = @{}
    foreach ($Data in ([xml]$Event.ToXml()).Event.EventData.Data) {
      if ($Data.Name) {
        $Fields[[string]$Data.Name] = [string]$Data.'#text'
      }
    }
    [pscustomobject]@{
      UtcTime     = $Event.TimeCreated.ToUniversalTime().ToString('o')
      EventID     = $Event.Id
      ProcessGuid = $Fields['ProcessGuid']
      PID         = $Fields['ProcessId']
      Image       = $Fields['Image']
      ParentGuid  = $Fields['ParentProcessGuid']
      ParentImage = $Fields['ParentImage']
      DestIp      = $Fields['DestinationIp']
      DestPort    = $Fields['DestinationPort']
    }
  } | Format-Table -AutoSize
```

**Interpretation:** A genuine matching `ProcessGuid` on Event 1 and Event 3 is stronger evidence tying the connection record to **that instance** than a PID alone. Still verify source host, timestamps, configuration, possible gaps, remote endpoint and alternative explanations.

**This prints up to 500 recent matches.** For complete time-window review and case reporting, use validated EVTX parsers, log coverage statistics and preserved records, not a truncated terminal output.

## 5. Add Prefetch and Amcache without overstating them

On an **acquired and verified copy**, parse Prefetch and Amcache following [Execution artifacts — Prefetch, Amcache and corroboration](execution.md).

- **Prefetch launch evidence** near 15:03 can support that PowerShell ran. It cannot establish that the 15:03 Sysmon process and a particular .pf record are necessarily the **same** instance on naming/time alone.
- **Amcache inventory** can be useful for locating a candidate executable or attribute; do not turn a path/hive timestamp into an asserted process start.
- **A network connection** can connect process activity to a destination, but without network content/provider records, it doesn't establish file transfer or exfiltration.
- **A document-parent relationship** may arise from benign automation, scripts, macros or other causes. Its suspiciousness depends on command line, provenance, security controls and independent corroboration.

## 6. State the evidence in a defensible finding

### Strongly supported (assuming genuine, consistent records)

> “Security 4688 and Sysmon Event 1 records show that a PowerShell process was created at approximately 15:03:02 UTC, with a Word process recorded as its parent. Sysmon Event 3 associates a network connection shortly afterward with the same ProcessGuid. The destination, port, source timestamps and original records are documented in the case exhibits.”

### NOT supported by these facts alone

> “The suspect opened a malicious document and PowerShell stole files from the system.”

The second statement jumps over **person attribution, content, intent, transferred bytes and maliciousness**. It would require additional independent evidence and consideration of alternatives.

### Reconciliation table

| Source | Observed fact | Independent check | Limitation / conflicting possibility |
| --- | --- | --- | --- |
| Security 4688 | PID / parent / process creation | Sysmon 1, EDR process graph | Auditing may be partial; command line missing |
| Sysmon 1 | ProcessGuid, parent, user | 4688, EDR, memory | Configured tool required |
| Sysmon 3 | ProcessGuid, destination, protocol | Firewall, proxy, PCAP | No payload; default-disabled event |
| Prefetch | Historic executable launch times | Process-creation events | Run count and time precision/retention limit |
| Amcache | File/app inventory reference | Hash/file system provenance | Presence **is not timed execution** |
| Login context | Logon session/account | Identity provider, host Security log | Account context **is not physical operator** |

## 7. Reporting / peer-review checklist

- [ ] Scope, authority, source devices and acquisition dates recorded.
- [ ] Image and relevant collected-file integrity hashes recorded.
- [ ] Each source's actual **coverage/retention** checked before negative findings.
- [ ] Original timestamp, timezone, UTC normalization and clock offset kept.
- [ ] Hex/decimal PID conversion verified; PID reused? Time/host confirmed?
- [ ] Any ProcessGuid correlation uses **real exact GUID values** and same source host.
- [ ] Clear distinction between process start, file reference, connection, bytes transferred and human intent.
- [ ] Alternative explanations and missing/countervailing evidence considered.
- [ ] Parser versions, command options, case results directory and original artifacts retained.
- [ ] Examiner conclusions constrained to evidentiary support; reviewed per SOP.

## Published references

- [SWGDE 18-F-001-2.0, Best Practices for Computer Forensic Examinations (Feb 28, 2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) — systematic examination, original protection, tool validation, documentation, defensible analysis.
- [Microsoft Security Event 4688, process creation](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688) — event XML, hexadecimal IDs, version-specific fields, audit configuration.
- [Microsoft Sysmon documentation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) — Event 1/3, ProcessGuid, UTC and default telemetry gaps.
- [Velociraptor, Evidence of Execution](https://docs.velociraptor.app/docs/forensic/evidence_of_execution/) — Prefetch and historic execution interpretation.

**Last source review:** October 26, 2026. This is a worked educational lab example—not a guarantee of tool compatibility or an agency-approved procedure.

[Windows workflow hub](README.md) · [Execution evidence reference](execution.md) · [Live process/PID snippet](../../snippets/powershell/processes-services.md) · [Live network correlation](../../snippets/powershell/network-state.md) · [Windows event triage](../../snippets/powershell/windows-event-triage.md)
