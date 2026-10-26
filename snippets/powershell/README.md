# Windows Forensic Command Snippets

**Use case:** triage | acquisition | validation | response  
**Environment:** windows  
**Risk:** safe | caution

**Field rule:** Document the untouched system first. Only execute commands within authorized scope, preferably after confirming volatility and containment priorities. Even read-only commands leave traces on live systems. Unless a snippet explicitly says otherwise, commands only **query** state; exports write to the **approved external evidence destination**.

## How to read a snippet

Each command reference includes the command, an **invented example output**, and an explanation of what the fields mean to an examiner. When useful, the page also shows how to correlate an artifact with another source and what the output **cannot prove**.

**Start with this worked intrusion example:** [Running processes, PIDs, PPIDs, and a sample process tree](processes-services.md), then [match an owning PID to a live network connection](network-state.md). Both pages use the same fictitious PID **6128** to demonstrate correlation and why timestamps matter.

> **Example outputs are illustrative, not real forensic evidence.** Layout, available fields and administrative permissions vary by Windows version and configuration.

**After collection:** [Windows Examiner — execution artifacts and a worked intrusion timeline](../../docs/windows/README.md). Move from live command snapshots to validated offline EVTX, Prefetch, Amcache, process identity and defensible reporting. The live commands below are **not** full historical forensic analysis.

## 1. Preserve access before powering down

| Priority | Command reference | Why it matters |
| --- | --- | --- |
| **Critical** | [BitLocker recovery readiness](bitlocker-recovery-readiness.md) | Confirm unlocked/encrypted volumes, matching protector IDs, and approved recovery-password availability. |
| **High** | [Disk / partition / volume layout](disk-volume-layout.md) | Identify physical storage, mounted volumes and drive mapping while live. |
| **High** | [Volume Shadow Copy inventory](volume-shadow-copies.md) | Record existing snapshots for later lab review. |
| **High** | [Registry hive preservation](registry-hive-preservation.md) | Preserve selected machine hives to approved evidence storage. |

## 2. Capture volatile state

| Reference | Useful output |
| --- | --- |
| [System identity and time](system-identity-time.md) | Hostname, model, serial, time, timezone, uptime. |
| [Processes and services](processes-services.md) | Execution snapshot with process IDs and service paths. |
| [Network state](network-state.md) | TCP/UDP, local connections, routes, DNS, neighbor cache. |
| [Users and sessions](users-sessions.md) | Logon contexts, users and mapped shares. |

## 3. Preserve user and activity evidence

| Reference | Useful output |
| --- | --- |
| [USB and external storage history](usb-storage-history.md) | PnP disk identity and selected historical USB registry entries. |
| [PowerShell interactive history](powershell-command-history.md) | Candidate commands entered by a user at the console. |
| [Recent user activity locations](recent-user-activity-paths.md) | Recent items, Jump Lists, and Downloads metadata. |
| [Scheduled tasks and startup keys](persistence-inventory.md) | Selected startup/autorun surfaces for contextual review. |

## 4. Event records and integrity

| Reference | Useful output |
| --- | --- |
| [High-value Windows Event IDs](windows-event-triage.md) | Selected logon, execution, task, service and audit-log events. |
| [Windows event-log export](event-log-export.md) | Native EVTX preservation to evidence destination. |
| [Defender detection context](defender-detection-context.md) | Antivirus status, detection history and log availability. |
| [SHA-256 evidence hashes](sha256-evidence.md) | Integrity values and manifests for collected files. |

## Operational cautions

- **Encryption/recovery passwords:** Don't paste them into chat, ordinary notes, ticket systems, or transcripts. Store with controlled access according to SOP.
- **Source vs. destination:** Confirm external destination identifiers and free space; avoid writing collection output onto the evidence source.
- **Clock:** Record independent reference time and system offset; Windows timestamps vary by API and configuration.
- **Negative findings:** Empty output can reflect privileges, disabled auditing, log rotation, version differences, or absence of that specific artifact—**not proof nothing happened**.
- **Lab analysis:** Command results help triage. They do not replace validated memory acquisition, disk imaging, registry parsing, or chain of custody.

[Rapid Evidence Collection Playbook](../../playbooks/acquisition/0-rapid-evidence-collection.md) · [Field-to-Lab Tool Matrix](../../playbooks/acquisition/4-field-to-lab-tool-matrix.md) · [Examiner Toolkit](../../examiner/README.md)
