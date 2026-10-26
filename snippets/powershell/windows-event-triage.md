# Windows — High-Value Event IDs for Rapid Triage

**Use case:** triage | validation | response  
**Environment:** windows  
**Risk:** safe

## Why it matters

Event logs help correlate activity and can guide deeper evidence collection. IDs are **clues, not proof**: events exist only if the relevant audit configuration, provider, and retention were in effect.

## Security log quick look (recent three days)

```powershell
$Since = (Get-Date).AddDays(-3)
Get-WinEvent -FilterHashtable @{
  LogName = 'Security'
  Id = 4624,4625,4648,4672,4688,4698,1102
  StartTime = $Since
} -MaxEvents 120 |
  Select-Object TimeCreated, Id, ProviderName, Message
```

| Event ID | Common meaning | Qualification |
| --- | --- | --- |
| 4624 | Successful logon | Check logon type and account; not necessarily an interactive user. |
| 4625 | Failed logon | Repeated failures require context. |
| 4648 | Logon using explicit credentials | May be legitimate use of alternate credentials. |
| 4672 | Special privileges assigned at logon | Routine for some administrative/service accounts. |
| 4688 | Process creation | Requires relevant audit configuration; command line may not be present. |
| 4698 | Scheduled task created | Requires appropriate auditing; not a full task history. |
| 1102 | Security audit log cleared | Examine operational/admin context and related records. |

## Service installation (System log)

```powershell
Get-WinEvent -FilterHashtable @{
  LogName = 'System'
  Id = 7045
  StartTime = $Since
} -MaxEvents 50 |
  Select-Object TimeCreated, Id, Message
```

## Example output — synthetic lab scenario

```text
TimeCreated             Id    ProviderName
-----------             --    ------------
2026-10-21 10:03:02    4688  Microsoft-Windows-Security-Auditing
2026-10-21 10:02:55    4624  Microsoft-Windows-Security-Auditing
2026-10-21 10:06:41    1102  Microsoft-Windows-Eventlog
```

### What it could mean

- **4624:** a logon succeeded; examine account, logon type and source. It does **not** always represent someone physically signing in.
- **4688:** a process was created, *if that audit subcategory was enabled*. The full event may record process and parent IDs; command-line detail requires additional configuration.
- **1102:** a Security audit log was cleared. This deserves context and corroboration rather than an automatic malicious classification.

**Intrusion example:** If an Event 4688 records process ID **6128** running PowerShell at 10:03:02, and a captured connection shows **OwningProcess 6128** at approximately the same time, the two sources may describe the same executing process. Confirm process IDs' representation (Windows event fields can use hexadecimal), clocks, session, parent, command line and EDR. **Event timestamps and the fact that a process existed are separate questions from what the process actually did.**

## Cautions

- `Get-Date` uses **target system time**; record clock offset separately.
- Queries can be slow and messages may expose account names, hostnames, or command lines.
- The absence of events may reflect retention, missing providers, privilege limits, filtering, or disabled auditing.
- For preservation, export original `.evtx` files before relying on screenshots or excerpts: [event-log export](event-log-export.md).

## Move from triage to forensic interpretation

For a verified **acquired** Security or Sysmon EVTX, use the [Windows worked process/network timeline](../../docs/windows/timelines.md) to extract Event 4688 named XML fields, convert hexadecimal PIDs, and compare configured Sysmon ProcessGuid values. For corroboration with Prefetch and Amcache inventory, see [Windows execution artifacts](../../docs/windows/execution.md). Document whether audit policies were active; truncated query output does not establish a complete history.

## Official reference

[Microsoft — Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent)  
[Microsoft — wevtutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)

[Back to Windows snippets](README.md)
