# Windows Execution Evidence — Prefetch, Amcache & Corroboration

**Audience:** trained digital forensic examiners | DFIR analysts  
**Question:** *What ran, when, from where, and what can the evidence actually establish?*  
**Environment:** acquired Windows image / approved forensic collection; isolated **Windows lab workstation** for parser commands  
**Risk:** caution — potential personal data, clock differences, unsupported tool/OS versions  
**Sources reviewed:** October 26, 2026

> **Laboratory workflow, not a live collector checklist.** Confirm scope and authority, preserve the original acquisition, verify its hash, record collection circumstances and analyze an approved **working copy**. Use validated tool builds and log exact versions/options. SWGDE [18-F-001-2.0](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) calls for examination objectives, controlled workstations, preservation, documentation, and defensible interpretations.

> **Interpretation convention:** A collected laptop or acquired dataset is an **Evidence** item for our records; Prefetch, Amcache and event-log entries are **artifacts** discovered within it. Examining and correlating those artifacts can develop **evidence** for or against narrowly stated hypotheses. An artifact can itself have legal evidentiary value, but its presence is **not automatically proof of a crime**. [Terminology and alternatives](../../planning/TERMINOLOGY.md).

## What does each artifact support?

| Source | Typical location or log | Good for | Does **not** establish alone |
| --- | --- | --- | --- |
| **Prefetch** | `%SystemRoot%\Prefetch\*.pf` | Strong historical **executable launch** indicator on supported/configured systems; stored recent run times, run count and referenced paths. | Which human ran it, successful malicious action, or complete execution history. |
| **Security event 4688** | `Security.evtx`, if process creation auditing enabled | A specific **process-start event** at an event time; binary, PID, creator PID; optional command line. | That the command succeeded, that every execution was logged, or the person at the keyboard. |
| **Sysmon event 1** | `Microsoft-Windows-Sysmon/Operational`, if installed/configured | Process creation with **ProcessGuid**, user, parent, command line, and configured hashes. | That Sysmon was active or that its telemetry covers the full incident. |
| **Sysmon event 3** | Same log, if **network telemetry enabled** | Connection metadata linked with process GUID/PID. | Payload contents or that any particular bytes were exfiltrated. |
| **Amcache** | Typically `%SystemRoot%\AppCompat\Programs\Amcache.hve`; version-dependent companion files | Application/file inventory, paths and attributes; some hashes/metadata depending on OS/version. | **That a particular executable ran at a particular time** just because a record exists. |
| **ShimCache / AppCompatCache** | SYSTEM registry hive, active control set dependent | Historical file-path compatibility/cache references useful for corroboration. | **Execution on modern Windows** merely from the presence of an entry or its timestamps. |
| **BAM / UserAssist** | Per-user Windows registry locations (version-specific) | Additional potentially useful recent activity or GUI-launch indicators. | Universal/full execution history or definitive human attribution. |
| **Live process + socket snapshot** | RAM/current process APIs and TCP tables | Whether a PID was running and associated with an active connection **when collected**. | An earlier event at a different time without checking for PID reuse. |

**Report the strongest supported statement, not the strongest imaginable one.** For example, “the acquired image contains a Prefetch artifact associated with a program” is different from “the suspect deliberately ran malware.”

## 1. Preserve source files and relevant context

In the acquired **lab copy** or validated forensic export, look for:

```text
<Windows root>\Prefetch\*.pf
<Windows root>\AppCompat\Programs\Amcache.hve
<Windows root>\AppCompat\Programs\Inventory*.db    (where present)
<Windows root>\System32\config\SYSTEM
<Windows root>\System32\winevt\Logs\Security.evtx
<Windows root>\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx
```

Record the system **build**, acquisition method, source-image hash, collected paths, each file's hash, tool names/versions and any log/hive transaction files. Some acquisition methods omit deleted/unallocated artifacts or relevant transaction logs. When registry hives or SQLite files have pending transactions, use validated parsers and acquire matching `LOG*`, `-wal` / `-shm` files where relevant; don't discard them.

**Do not mount a forensic source read/write**, alter registry keys, run suspect binaries, enable logging on the original, or copy a potentially malicious executable into an uncontrolled computer just to identify it.

## 2. Prefetch — strong launch-related evidence, with limits

A typical file resembles:

```text
POWERSHELL.EXE-1A2B3C4D.pf
```

This is a **fictional filename**. The suffix is a Windows Prefetch identifier related to executable launch characteristics; it is **not a cryptographic hash of the executable content**. A matching executable name does not uniquely identify which binary ran; correlate additional paths, device/volume details and collected file hashes.

On Windows 8 and later, a supported Prefetch record can contain **up to eight recent run timestamps**, a run count and referenced file/directory paths. The stored run count and .pf creation time are **not a full history**, and creation time can reset if the file is evicted or recreated. [Velociraptor: Evidence of Execution](https://docs.velociraptor.app/docs/forensic/evidence_of_execution/).

### Analyze an already-collected Prefetch directory (PECmd)

Run these commands on an isolated, validated **Windows forensic lab workstation**. Replace the illustrative paths with approved case working paths:

```powershell
# Read acquired source files. Write CSV only into a lab results directory.
.\PECmd.exe -d "D:\CASE-EXAMPLE\evidence\Prefetch" --csv "D:\CASE-EXAMPLE\results\Prefetch" --csvf prefetch.csv

# Check one acquired file when you need detailed referenced-path information:
.\PECmd.exe -f "D:\CASE-EXAMPLE\evidence\Prefetch\POWERSHELL.EXE-1A2B3C4D.pf"
```

These are supported `-d`, `-f`, `--csv` and `--csvf` options from the [PECmd maintained tool repository](https://github.com/EricZimmerman/PECmd). Create the **results** directory in advance and verify it is on controlled writable **lab output storage**, not the evidence source. Run `PECmd.exe --help` and record the actual installed version; parser behavior depends on Windows/Prefetch format.

### Example parsed result — synthetic, not an actual PECmd export layout

```text
Executable       : POWERSHELL.EXE
RecordedRuns     : 3
RecentRunUTC     : 2026-10-21T15:03:02Z
PriorRunUTC      : 2026-10-20T14:15:30Z
ReferencedPath   : C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
PrefetchFile     : POWERSHELL.EXE-1A2B3C4D.pf
```

**How to read this:** The artifact provides evidence consistent with launches of an executable. The `RecentRunUTC` is **not necessarily the exact instant of process creation**; parsing precision and timestamp interpretation vary. Referenced paths represent items touched/reported by prefetch monitoring, **not proof that a person opened or read every referenced file**.

**Negative finding:** No `POWERSHELL*.pf` does **not** prove it never ran. Prefetch may be disabled, unavailable, unsupported on that system type, aged out/evicted, or removed. Examine current Prefetch policy, image scope and other telemetry.

## 3. Amcache — inventory evidence, not a launch log

Amcache can record software/file inventory entries with paths, metadata and in some versions hash-related fields. Its structures **vary by Windows release and updates**.

### Working-copy parser example

```powershell
# Folder input helps current parser builds find applicable companion artifacts.
.\AmcacheParser.exe -f "D:\CASE-EXAMPLE\evidence\AppCompat\Programs" --csv "D:\CASE-EXAMPLE\results\Amcache"
```

The official [AmcacheParser repository](https://github.com/EricZimmerman/AmcacheParser) documents `-f` for the `Amcache.hve` file or its directory and `--csv` for output. Its October 2026 documentation also notes certain recent Windows 11 configurations use **Inventory*.db SQLite companion records**. Verify the parser release you installed and collect any associated journal/WAL files; do not assume the hive alone captures all applicable recent Windows inventory data.

### Synthetic inventory observation

```text
Source           : Amcache file inventory
Path             : C:\Users\Public\tools\example.exe
RecordedMetadata : filename / inventory values; hash if available in build
Observation      : a file inventory record refers to this path
```

**Supported interpretation:** The system maintained an inventory reference to that file/path under conditions requiring OS/build-specific interpretation.

**Unsupported without corroboration:** “User A launched `example.exe` at 10:03” merely because the Amcache entry exists. The same distinction holds for modern ShimCache records; registry last-write values do not simply become timestamps of executable launch.

## 4. Process-creation events — the timing and parent question

**Security 4688** can provide new-process ID/name, creator PID, logon context and optionally command line **if the relevant auditing and inclusion settings were enabled beforehand**. The event's process IDs are commonly stored in **hexadecimal**. [Microsoft: 4688 process creation event](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688).

**Sysmon 1** includes a `ProcessGuid` designed for more reliable correlation than PID alone. **Sysmon 3** can connect network activity to the same `ProcessGuid`, but **Event 3 network monitoring is disabled by default** and needs prior configuration. [Microsoft Sysmon reference](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

### Examine preserved EVTX on a Windows lab copy

```powershell
# This READS the copied EVTX. It does not enable auditing or change the source.
$security = "D:\CASE-EXAMPLE\evidence\evtx\Security.evtx"
Get-WinEvent -FilterHashtable @{Path=$security; Id=4688} -MaxEvents 100 |
  Select-Object TimeCreated, Id, MachineName, Message
```

For exact process identifiers and comparison, use event XML **named fields**, not positional `Properties[5]` indexes, which may vary across event versions. The companion [timeline walkthrough](timelines.md) includes a field-safe parsing example and decimal/hex conversion.

### Example events — synthetic

```text
2026-10-21T15:02:14Z | Sysmon 1  | WINWORD.EXE   | PID 4024 | ProcessGuid {EXAMPLE-WORD}
2026-10-21T15:03:02Z | 4688      | powershell.exe | NewPID 0x17F0 | ParentPID 0x0FB8
2026-10-21T15:03:02Z | Sysmon 1  | powershell.exe | PID 6128 | ProcessGuid {EXAMPLE-PS}
2026-10-21T15:03:10Z | Sysmon 3  | connection    | ProcessGuid {EXAMPLE-PS} | 203.0.113.44:443
```

**Interpretation:** `0x17F0` converts to decimal **6128**. `0x0FB8` converts to **4024**. Where genuine provider/clock fields corroborate this, the records support a PowerShell process launched with Word reported as parent and a connection attributed to the same Sysmon process GUID. They **do not** on their own establish maliciousness, successful exfiltration or who caused the execution. The `203.0.113.44` address is reserved for documentation.

**Further artifact context:** Compare [UserAssist and BAM from acquired registry hives](registry.md) when investigating user-associated execution, and use the [USB device examination guide](usb-device-history.md) before drawing conclusions about removable-storage activity. Both explain important absence, LastWrite and account-attribution limits.

## 5. Build a testable finding, not just an indicator list

1. **Define the hypothesis**: e.g., “A document initiated a scripting process that made an outbound connection.”
2. **Identify and validate source artifacts**: process records, relevant Prefetch, Amcache inventory, endpoint logs, memory and independent network/EDR records.
3. **Normalize clocks**: maintain original timestamps, source timezone/offset, event formats, conversion method, OS clock uncertainty.
4. **Compare the same process instance**: PID + creation time + host/session; favor Sysmon ProcessGuid when available. Beware PID reuse and process exit.
5. **State alternative explanations**: approved IT automation, legitimate document add-ins, management tooling, service processes, misconfigured detection rules or a stale Prefetch artifact.
6. **Document conclusions and limitations**: what execution is supported, what needs additional evidence and which logs/records were absent.

### Reusable examiner note (fictional)

```text
Question: Did a document launch a scripting process that accessed a remote host?
Evidence source/image SHA-256:
Scope and acquisition limits:
Time sources and UTC normalization:
Prefetch item/path and parser version:
Amcache inventory and OS/build-specific interpretation:
Security/Sysmon records, Event IDs and original field values:
Process correlation method (GUID, PID+start time, parent and account):
Network evidence and exactly what it records:
Alternative explanations and missing sources:
Supported finding:
Unsupported or unresolved claims:
Examiner, review date and evidence outputs:
```

## Published-source ledger

| Reference | Edition / publisher | What it supports |
| --- | --- | --- |
| [SWGDE Best Practices for Computer Forensic Examinations](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) | **18-F-001-2.0**, July 28, 2025 (SWGDE) | Scope, validated tools, isolation, examination on copies, interpretation and documentation; **not an artifact-specific rulebook**. |
| [Microsoft Security Event 4688](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688) | Microsoft technical documentation, reviewed Oct 2026 | New process and creator IDs, command-line configuration, account/logon context, event versions. |
| [Microsoft Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) | Microsoft Sysinternals, reviewed Oct 2026 | Event 1 process creation, Event 3 network telemetry and ProcessGuid correlation; configuration constraints. |
| [PECmd](https://github.com/EricZimmerman/PECmd) | Maintainer CLI documentation, reviewed Oct 2026 | Valid parser options and outputs for Prefetch; not a normative standard. |
| [AmcacheParser](https://github.com/EricZimmerman/AmcacheParser) | Maintainer CLI documentation, reviewed Oct 2026 | Parser options and format/OS-version caveats; not a normative standard. |
| [Velociraptor: Evidence of Execution](https://docs.velociraptor.app/docs/forensic/evidence_of_execution/) | Velociraptor project technical guide, reviewed Oct 2026 | Prefetch recent runs, run count and historical interpretation caveats. |

**Current-version note:** SWGDE 18-F-001-2.0 supersedes the older 2018 18-F-001-1.0 guidance. Confirm vendor parser compatibility with the **actual evidence OS build**, not simply today's marketing or changelog.

[Windows Examiner workflow](README.md) · [Worked correlation timeline](timelines.md) · [Process/PID commands](../../snippets/powershell/processes-services.md) · [Windows event triage](../../snippets/powershell/windows-event-triage.md)
