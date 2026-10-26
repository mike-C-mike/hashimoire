# Windows USB & Removable Storage — Device-to-User Correlation

**Audience:** Windows forensic examiners / DFIR analysts  
**Question:** *Was a removable storage device connected, to which workstation and profile, and is there independent support for file activity?*  
**Evidence:** acquired SYSTEM/SOFTWARE/user hives, device-installation logs, Windows EVTX and user-activity artifacts  
**Risk:** caution — device identity, drive-letter reuse, user attribution and timestamp traps  
**Published sources reviewed:** October 26, 2026

> **Don't jump from “USB device recognized” to “the suspect copied files.”** A device connection trace is an **artifact**, not a record of which files were transferred. Link the same physical Evidence item to device instances, volumes, user context and file-activity records **only when their underlying identifiers and time windows agree**. Assess alternative explanations and missing data. [SWGDE examination guidance, 18-F-001-2.0 (July 28, 2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) · [Hashimoire terminology](../../planning/TERMINOLOGY.md).

## The six questions to keep separate

| Question | Where to look | What you must not assume |
| --- | --- | --- |
| **Was a device enumerated?** | SYSTEM `Enum\USBSTOR`, `Enum\USB`, `Enum\SCSI`, device-installation log | All USB storage is recorded under USBSTOR or that an old key proves recent connection |
| **Which specific device?** | Vendor/product, instance ID, device-reported serial, volume/partition identifiers | A serial is always unique, trustworthy or even present |
| **Which volume/letter?** | SYSTEM `MountedDevices`, SOFTWARE portable-device labels, volume IDs | `E:\` always meant the same external device |
| **When was it present?** | SetupAPI install section, device-property timestamps if parsed correctly, system events (when logged) | Driver-install date equals every connection time |
| **Which profile saw it?** | User `NTUSER.DAT\...\Explorer\MountPoints2`, SIDs and Windows logons | Profile entry identifies the person who physically plugged it in |
| **Were files accessed or copied?** | LNK, Jump Lists, Recent, filesystem journals, file audit/EDR/proxy, user reports | A registry record alone proves copying, direction or file contents |

**Treat each answer independently.** You can confidently find a storage device enumerated while honestly leaving user attribution and file-copy activity unresolved.

## 1. What to preserve from the Evidence image

On a **controlled working copy**, obtain the relevant paths under authorized scope:

```text
Windows\System32\config\SYSTEM       (+ SYSTEM.LOG1 / LOG2)
Windows\System32\config\SOFTWARE     (+ SOFTWARE.LOG1 / LOG2)
Users\<profile>\NTUSER.DAT            (+ NTUSER.DAT.LOG1 / LOG2)
Windows\INF\setupapi.dev.log
Windows\System32\winevt\Logs\*.evtx (device/system/security if available)
Users\<profile>\AppData\Roaming\Microsoft\Windows\Recent\*.lnk
Users\<profile>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\*
```

Supplement from `UsrClass.dat`, `$MFT` / USN journal and recovered volume artifacts where appropriate to the question and authority. The examples on this page **read copied material in the laboratory**, not live registry keys of a seized host.

Preserve acquisition hashes and parser versions. A 2026 source might no longer retain 2023 USB event logs; a negative record only limits what this collection can tell you.

## 2. Identify the device without assuming USBSTOR is complete

Open the offline SYSTEM hive in [Registry Explorer](https://ericzimmerman.github.io/) or a comparable validated registry parser. Determine actual active `ControlSet00x` using `SYSTEM\Select` rather than searching only literal `CurrentControlSet`, which is a live-registry alias.

Inspect likely locations:

```text
SYSTEM\ControlSet00x\Enum\USBSTOR
SYSTEM\ControlSet00x\Enum\USB
SYSTEM\ControlSet00x\Enum\SCSI
SYSTEM\MountedDevices
SOFTWARE\Microsoft\Windows Portable Devices\Devices
```

- **USBSTOR:** useful for common USB mass-storage devices; **not an inventory of every USB storage mode**.
- **USB:** USB device enumeration; hubs and other non-storage devices also appear.
- **SCSI:** may include USB-attached storage exposed through UASP or other SCSI-style adapters; entries aren't necessarily external USB.
- **MountedDevices:** can relate volume identifiers to drive-letter mappings, but mappings are historical/configuration-dependent and may be reused.
- **Windows Portable Devices:** labels and IDs that can help contextualize a volume or portable device; do not use the friendly name as a unique physical identifier.

### Example registry observations (invented)

```text
SYSTEM\ControlSet001\Enum\USBSTOR\Disk&Ven_EXAMPLE&Prod_FLASH&Rev_1.00\LABSERIAL001
SYSTEM\MountedDevices\DosDevices\E:     -> binary volume mapping
SOFTWARE\Microsoft\Windows Portable Devices\Devices\<device-ID> -> "LAB USB"
```

**Observation:** acquired Windows Registry contains device/volume-related references. **Unresolved:** whether the serial truly uniquely identifies an individual unit; exactly when it arrived; who used it; whether any file crossed the device boundary.

The value data under MountedDevices can require binary decoding and correlations to volume GUIDs, mount-manager identifiers and partition information. Don't interpret a raw blob or a single drive letter without a validated parser and cross-check.

## 3. Install ≠ each connection: examine SetupAPI and logs

`C:\Windows\INF\setupapi.dev.log` describes driver/device **installation** actions. Its "Section start" dates are recorded as **local clock time** in typical Windows formats. Convert using the **source computer's** time-zone context and clock-offset documentation, not the examiner's workstation timezone.

### Invented SetupAPI excerpt

```text
>>>  [Device Install (Hardware initiated) - USBSTOR\Disk&Ven_EXAMPLE&Prod_FLASH\LABSERIAL001]
>>>  Section start 2026/10/21 10:02:14.000
```

That might support driver installation activity at the stated device-local time. It is **not** a complete ledger of every attach/detach since then. Device properties and relevant Windows events may help reconstruct additional arrival/removal times; their fields, retention and presence vary by Windows version and logging configuration.

**Do not silently translate** `10:02 local` into `10:02 UTC`. Preserve the original timestamp representation and record how any conversion was made.

### Using an offline copy to inspect installation sections

```powershell
$log = 'D:\CASE-EXAMPLE\working\Windows\INF\setupapi.dev.log'
Select-String -LiteralPath $log -Pattern 'USBSTOR','UASPStor','Section start' -Context 2,2 |
  Out-File -LiteralPath 'D:\CASE-EXAMPLE\results\usb-setupapi-excerpts.txt' -Encoding UTF8
```

This creates a **derived working-file excerpt**, not a replacement for the full original log. Document the exact extraction method and retain source context; text search is only preliminary triage, not complete parsing.

For events, collect actual `.evtx` files and use a validated Event Log parser or [Windows Event triage](../../snippets/powershell/windows-event-triage.md). **Do not assume** a named event channel exists, is enabled, or covers the incident window.

## 4. MountPoints2: profile association is not person attribution

For each potentially relevant user hive:

```text
Users\<profile>\NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2
```

This can record that Windows Explorer maintained mount-related data in a profile. Some entries represent network shares rather than USB storage.

**Synthetic observation:**

```text
Source user hive: D:\CASE-EXAMPLE\working\Users\ProfileA\NTUSER.DAT
Mapped SID: S-1-5-21-...-1001
MountPoints2: volume GUID related to suspected external volume
Key LastWrite: 2026-10-21T15:03:40Z  (fictional)
```

**Cautious interpretation:** An artifact associated with a **Windows profile** references the relevant volume. It may strengthen an inference of a volume being available within that profile's context. It does **not** independently establish who physically connected it, whether the person opened a document, or a precise connect/disconnect timestamp. The key LastWrite may describe multiple registry interactions.

Correlate the SID to `SOFTWARE\...\ProfileList`, Windows logon events and source collection time. Account context is not human attribution.

## 5. File transfer requires file-activity evidence

Suppose an investigator believes someone moved a report from a Windows laptop to a USB device. What independent artifacts might help **test**, not automatically prove, that claim?

| Artifact | May support | Interpretation limit |
| --- | --- | --- |
| `.lnk` shortcut | A path, volume identity and metadata referring to a target | Not proof the linked file existed at the same path throughout the incident |
| Jump List | App-related recent or pinned file activity | Not automatically proof a file was copied |
| `$MFT` and USN journal | File/directory events and timing on a volume within acquired coverage | Source changes don't by themselves establish an external destination |
| Device registry / SetupAPI | Presence, installation or profile-mounted context | Not a record of file contents or copy direction |
| EDR / file auditing (if configured) | Process-level file operations with timestamps | Coverage and event semantics vary; check actual evidence |
| Acquired external-device image | Matching paths/files/hashes and volume context | Requires obtaining that separate Evidence item lawfully and validating original/extraction |

**If you can acquire the submitted external drive**, a validated file hash match with an on-host file supports identical bytes of the compared items. It does **not** alone determine copying direction, who performed it, or whether two files originated from a common third source.

## 6. A worked hypothesis test — fictitious

**Authorized question:** Was an external storage device present near an alleged report transfer?

| Source | Observed artifact | Meaning and uncertainty |
| --- | --- | --- |
| SYSTEM USBSTOR | Device instance LABSERIAL001 | One storage-enumeration reference; verify serial stability |
| SetupAPI | First-driver-install section within investigation week | Installation event, not proof of that day's reconnection |
| MountedDevices | E: mapping associated with volume | Historical letter/volume association; E: may have been reassigned |
| Profile A MountPoints2 | Related volume GUID entry | Profile-context lead, not attribution to a physical person |
| LNK file | Shortcut pointing to E:\Reports\example.pdf | Context for file interaction, not direct proof of a copy operation |
| External drive image | **Not collected** | Cannot verify actual destination file or compare content |

**Hypothesis A:** The drive was connected and used for report transfer.  
**Hypothesis B:** The drive was installed/known earlier and the report wasn't copied.  
**Hypothesis C:** A different drive later received letter E:, or file artifacts came from another context.

**Supported finding:** “The examined system contains multiple references to a removable storage device and a file shortcut naming a removable-drive path. Without corroborating device connection records for the precise window or an acquired destination device, the examination does not establish that the alleged file transfer occurred.”

**Do not write:** “User A stole example.pdf on USB serial LABSERIAL001.” The collected artifacts don't establish that.

## 7. Examiner handoff / report worksheet

```text
Evidence item, image ID and verified source/export SHA-256:
Legal scope and alleged action to investigate:
Windows edition/build, device clock/timezone:
Active ControlSet decision and relevant hives + transaction logs:
USBSTOR / USB / SCSI device instance IDs:
MountedDevices volume / drive-letter mapping with decoding method:
Device-reported serial and uniqueness limitations:
setupapi.dev.log original text/time, UTC conversion method:
Relevant EVTX channel, event IDs, coverage and original records:
User hive, profile path and SID-to-account mapping:
MountPoints2 raw key and LastWrite interpretation:
LNK/Jump List/file-activity paths and sources:
Available external drive image and comparison hashes, if any:
Each artifact's corroboration, alternative explanation and gaps:
Hypothesis supported / contradicted / unresolved:
Final finding, reviewer and saved derivative results:
```

## Published source ledger

- [SWGDE 18-F-001-2.0, *Best Practices for Computer Forensic Examinations* (final July 28, 2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) — controlled examination and interpretation, documentation, scope and contradictory information.
- [Microsoft Incident Response — Windows Internals for Forensic Investigation](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/IR-Guidebook-Final.pdf) — official Microsoft interpretation cautions for registry, user-activity and file/shortcut artifacts (consult relevant pages).
- [Eric Zimmerman RECmd/Registry tooling](https://github.com/EricZimmerman/RECmd) — offline hive and batch-based parsing; verify tool/plugin build actually used.
- [Hashimoire live USB inventory snippet](../../snippets/powershell/usb-storage-history.md) — live/current PnP checks; **not a substitute for offline full-artifact analysis**.

**Technical limitations:** USB device properties, driver log formats, Windows event channels and mount behavior change across OS/builds. Run the workflow on a known test image with the installed parser versions before case use. No field/VM output was captured or validated during creation of this article.

[Windows Examiner](README.md) · [Registry fundamentals](registry.md) · [Execution correlation](execution.md) · [Windows timeline](timelines.md) · [Evidence/artifact philosophy](../../planning/TERMINOLOGY.md)
