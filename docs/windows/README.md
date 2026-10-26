# Windows Examiner — Execution, Registry & Correlation

**Audience:** trained examiners and DFIR analysts  
**Current workflows:** *Analyze program activity, registry/user context, USB history and process/network timelines without overstating what artifacts prove.*  
**Evidence types:** acquired Windows image, registry hives/transaction files, setupapi logs, EVTX, Prefetch, Amcache and RAM/EDR where within scope  
**Risk:** caution — sensitive data, clock assumptions, false attribution  
**Guidance reviewed:** October 26, 2026

> **Start with an investigative question, not a list of artifacts.** This Windows workstream now supports **execution, offline Registry examination, removable storage correlation and process/network timelines**. Browser and filesystem/$MFT topics remain hidden until they have substantive content. All examples are synthetic; work on verified evidence copies under appropriate authority. [SWGDE 18-F-001-2.0](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/).

## A disciplined artifact-first investigation

**Evidence** (capital E) is the submitted device or dataset. During examination, we identify individual **artifacts**—process events, Prefetch records, registry entries, connection logs. Those artifacts become **evidence** (lowercase e) *for or against particular hypotheses* when their context, source reliability and limitations are evaluated. A finding must not go further than the support allows.

An allegation may set the **scope**, but it does not set the result. **Do not start with “this was malware” and seek only confirming records.** Test benign explanations, clock errors, PID reuse, missing logs and other contradictory observations. See our [editorial terminology and anti-confirmation-bias guidance](../../planning/TERMINOLOGY.md).

## Choose your current question

| I need to know… | Open now | Outcome |
| --- | --- | --- |
| **What Registry artifacts describe a program or user profile?** | [Registry examination: UserAssist, BAM, hives](registry.md) | Offline hive acquisition and parsing, transaction logs, SID/profile context, supported claims and alternatives. |
| **Was a USB device connected and was a file copied?** | [USB device-to-user correlation](usb-device-history.md) | USBSTOR/UASP, SetupAPI, volume mapping, MountPoints2, file-activity evidence and a worked unresolved case. |
| **Did a program execute?** | [Execution artifacts — Prefetch, Amcache and logs](execution.md) | Evidence matrix; controlled PECmd/AmcacheParser workflow; accurate claims and limitations. |
| **Did Word launch PowerShell, which then connected outward?** | [Worked intrusion timeline](timelines.md) | Security 4688 hex-to-decimal PIDs; Sysmon 1/3 ProcessGuid correlation; sample timeline and defensible reporting. |
| **What is running right now?** | [Live process/PID commands](../../snippets/powershell/processes-services.md) | ProcessID/ParentProcessID tree, services, command line and current-state limitations. |
| **What network connections exist now?** | [Live network-state commands](../../snippets/powershell/network-state.md) | OwningProcess PID, endpoints, listeners and current snapshot caveats. |
| **Which events should I preserve?** | [Event IDs](../../snippets/powershell/windows-event-triage.md) and [native EVTX export](../../snippets/powershell/event-log-export.md) | Select high-value logs and preserve raw records before quick parsing. |
| **Could a reboot lock the source drive?** | [BitLocker recovery readiness](../../snippets/powershell/bitlocker-recovery-readiness.md) | Volume/protector status and properly protected recovery-credential handling. |

Each path leads directly to a working reference; we do **not** create empty intermediate categories simply to make navigation look complete.

## How to extend the execution timeline using Registry artifacts

For a utility suspected of accessing removable storage, begin with the **submitted Evidence item's acquisition and integrity**. Inspect [offline Registry hives](registry.md) to contextualize UserAssist/BAM, confirm the active ControlSet and check how a profile maps to a SID; then [reconstruct USB-device history](usb-device-history.md) using SetupAPI, volume, mount and user-activity artifacts. Test the hypothesis with logs, filesystem context and any acquired destination drive **rather than presuming a copy occurred**.

## A ten-step examination workflow

1. **Define authority and objective.** “Investigate a possible malicious connection from this host between 14:45–15:30 UTC,” not “look through everything.”
2. **Inspect evidence handoff.** Determine whether device was powered on/unlocked, whether RAM or live network snapshots were captured, and what collection actions may have modified it.
3. **Verify image and source coverage.** Confirm original and working-copy hash record, partition/encryption access, source collection method and whether logs/prefetch/registry data were in scope.
4. **Record system metadata.** Windows edition/build; machine clock and measured offset where available; time zone and DST context; log retention.
5. **Create a source timeline.** Preserve original date strings and the parsed UTC equivalent. Separate event time, process time, file times and export time.
6. **Start with process telemetry if present.** Security Event **4688**, Sysmon **1** (and its ProcessGuid), EDR. No telemetry is a possible **coverage gap**, not proof nothing happened.
7. **Review Prefetch.** Identify named binaries, their launch-related timestamps, stored run counts and referenced paths using a parser validated for that OS build.
8. **Review inventory evidence.** Amcache/ShimCache provide leads and corroboration; their presence alone is **not** proof of execution.
9. **Correlate network activity.** Where present, associate Sysmon **3** to Sysmon **1** by ProcessGuid; in live snapshots use OwningProcess with PID creation time and host context. Confirm with firewall, DNS, proxy or PCAP if in-scope.
10. **Write a constrained finding.** Report both directly observed facts and the inferences/alternatives; retain original EVTX, parser outputs and working-copy integrity notes.

## What is worth capturing — artifact priority

| Type | Source example | Why it helps | Caveat |
| --- | --- | --- | --- |
| **System identity** | SYSTEM registry, OS build, time configuration | Keeps timeline and parser interpretation tied to the correct system | Device clock might be wrong or adjusted. |
| **Event logs** | `Security.evtx`, Sysmon operational EVTX | Event time, process and logon metadata, process GUID | Only if configured and retained. |
| **Prefetch** | `Windows\Prefetch\*.pf` | Historic launch-related observations, up to eight recent times where supported | A count of 3 isn't necessarily the entire history. |
| **Amcache** | `AppCompat\Programs\Amcache.hve` and OS-dependent companions | File/application inventory, candidate executable paths | Not a process execution event. |
| **Live memory / telemetry** | RAM, live PIDs/sockets, EDR | Active contexts and some volatile connection/process information | Image/snapshot time differs from historic source times. |
| **Independent records** | Proxy, firewall, DNS, authentication provider | Tests whether local observations agree with external systems | Scope, provider time zone and log retention may differ. |

## Example — a single question, five different interpretations

Consider a **fictional** Windows host where an examiner discovers the following:

```text
1. Prefetch: POWERSHELL.EXE shows a recorded launch near 15:03 UTC.
2. Security 4688: PowerShell PID 0x17F0, creator PID 0x0FB8, at 15:03:02Z.
3. Sysmon 1: PowerShell PID 6128 and parent WINWORD.EXE PID 4024.
4. Sysmon 3: a connection from the same ProcessGuid to 203.0.113.44:443.
5. Amcache: an executable path reference elsewhere in inventory.
```

The careful interpretation is that Windows and Sysmon **report process creation**, relevant Prefetch evidence may support execution, and configured Sysmon networking telemetry attributes a connection to the same process instance. The Amcache reference is not a substitute for an actual process-start event. The examiner must still investigate **how the document was obtained**, what the command line did, network traffic/content, account and actor context, and innocent alternatives.

The **IP is documentation-only**, the PIDs and events are invented, and nothing here establishes an actual compromise.

**Next step:** [Follow the fully worked timeline and commands](timelines.md).

## Evidence/reporting standards for this workstream

The minimum lab worksheet records:

```text
Source item and case/authority:
Acquisition method and verified SHA-256 values:
Host identity, Windows version/build, reference clock:
Event log sources, retention windows and relevant gaps:
Prefetch and Amcache acquired paths / parser versions:
Each observed artifact and its original event/time representation:
UTC conversion method and uncertainty:
Process match method (ProcessGuid or PID + creation time):
Network endpoint evidence and limitations:
Alternative explanations and contradictory sources:
Final statement and confidence/remaining unknowns:
Working-copy analysis outputs, reviewer and report exhibits:
```

**Do not treat a parser warning as noise.** Record which artifacts failed to parse, which image partitions were inaccessible, and which event sources never existed or rolled off before the relevant period.

## Source ledger

- **SWGDE [18-F-001-2.0](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/), Best Practices for Computer Forensic Examinations (July 28, 2025):** exam scope, integrity, tool validation, documentation, working-copy examination and sound interpretation. This is a professional best-practice document, **not statute**.
- **[Microsoft Event 4688](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688):** process-start XML, PID representations and conditional command-line fields.
- **[Microsoft Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon):** ProcessGuid correlation and configurable network telemetry.
- **[PECmd](https://github.com/EricZimmerman/PECmd) and [AmcacheParser](https://github.com/EricZimmerman/AmcacheParser):** tool-specific CLI capabilities; confirm actual parser version with `--help`.
- **[Velociraptor execution artifact reference](https://docs.velociraptor.app/docs/forensic/evidence_of_execution/):** prefetch artifact interpretation and limitations.

## Where Windows Examiner goes next

The main Windows roadmap still includes **browser/user activity, filesystem/$MFT, richer registry persistence/logon investigation, execution activity over longer windows, and volume-shadow-copy context**. We are deliberately not showing those future pages as clickable published links yet.

[← Examiner Toolkit](../../examiner/README.md) · [Windows Snippets](../../snippets/powershell/README.md) · [Collector → Computer handoff](../../collector/computer-collection.md) · [Hash verification](../hashing/README.md)
