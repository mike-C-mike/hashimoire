# Windows User-Activity Artifacts — LNK, Jump Lists & ShellBags

**Audience:** authorized forensic examiners and DFIR analysts  
**Question:** *Which document or folder paths were referenced, which applications were associated with them, and do separate artifacts support actual file access or transfer?*  
**Evidence:** acquired Windows user profiles, Recent items, Jump Lists, NTUSER.DAT / UsrClass.dat, volume/USB traces, file and program activity  
**Risk:** caution — user attribution, shell behavior, stale paths, timestamp and parser limitations  
**Published sources reviewed:** October 29, 2026

> **Don't equate a recent-item artifact with someone deliberately opening, modifying or copying a file.** These records can be valuable but are often created by application and Shell behavior, file dialogs, pinned items or historic volume associations. Analyze verified **lab working copies**, not the submitted physical **Evidence** item. [SWGDE 18-F-001-2.0, final July 28, 2025](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/).

## The five separate claims

| Claim to test | Potential artifact | Typical support | Important limitation |
| --- | --- | --- | --- |
| A path or file was known to Windows | LNK or Jump List entry | Target path, item metadata, app identity, volume clues | The file may no longer exist, have moved, or have never been manually opened by the alleged user |
| An application referenced a file | Jump Lists and app-specific MRUs | App-associated file reference | MRU ordering or interaction may be auto-populated; no proof of human intent |
| Explorer displayed or retained folder-view state | ShellBags in NTUSER.DAT / UsrClass.dat | Folder path/view metadata | **Not** a complete list of browsed folders or a certain “folder opened at” timestamp |
| A volume/profile relation existed | MountPoints2, MountedDevices, device registry | Mounted-volume or device association | Not copying, file content or physical operator identity |
| A document was actually transferred | File system on destination, logs and independent acquisition | File presence/byte identity and context | Hash matches don't establish actor, direction or original source |

**Evidence / artifact convention:** the acquired laptop or removable disk is **Evidence**; a shortcut or ShellBag key is an **artifact**. Their corroboration may develop **evidence** for or against a *specific* hypothesis, not a preselected conclusion. An artifact can still itself be legally probative. [Editorial guide](../../planning/TERMINOLOGY.md).

## 1. Preserve all relevant source context

On the **verified working copy**, consider the following under the authorized scope:

```text
C:\Users\<profile>\AppData\Roaming\Microsoft\Windows\Recent\*.lnk
C:\Users\<profile>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\*.automaticDestinations-ms
C:\Users\<profile>\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\*.customDestinations-ms

C:\Users\<profile>\NTUSER.DAT       (+ NTUSER.DAT.LOG1 / .LOG2)
C:\Users\<profile>\AppData\Local\Microsoft\Windows\UsrClass.dat (+ transaction logs)
C:\Windows\System32\config\SYSTEM  (+ transaction logs)
C:\Windows\INF\setupapi.dev.log
```

The same path may appear in several profiles; always record which profile and associated SID it came from. Capture original timestamps, original filename, source hash, tool version, file and hive transaction logs. Different versions of Windows and applications create different records.

**Source hygiene:** Do not double-click or execute the LNK on the host or parse against the original read/write. LNKs may refer to networks, deleted files, other volumes or missing targets. Don't “repair” a missing link by opening it on the analysis workstation.

## 2. LNK shortcuts: path and volume clues, not an opening receipt

A `.lnk` file may include a target path, arguments, local/UNC/relative path, link creation/modified/accessed metadata, target file timestamps as recorded by the Shell, volume label/serial, drive type and machine/network details **when populated**. Missing fields or inconsistencies require scrutiny; parser versions may differ.

### Parse copied shortcuts with LECmd

The [LECmd maintainer README](https://github.com/EricZimmerman/LECmd) documents `-d` for a directory, `-f` for one file, `--csv` for result directory and `--csvf` for output filename.

```powershell
# Run in a validated Windows forensic lab, using staged working copies only.
.\LECmd.exe -d "D:\CASE-EXAMPLE\working\UserA\Recent" --csv "D:\CASE-EXAMPLE\results\LNK" --csvf "UserA-shortcuts.csv"
.\LECmd.exe -f "D:\CASE-EXAMPLE\working\UserA\Recent\example.lnk"
```

**Synthetic parsed result (NOT a literal LECmd CSV schema):**

```text
LNK file        : C:\Users\UserA\AppData\Roaming\Microsoft\Windows\Recent\review.pdf.lnk
Stored target   : E:\Reports\review.pdf
Stored volume ID: A1B2-C3D4
Target times    : recorded metadata, source and timezone to verify
Created by      : Windows Shell / app context not independently established
```

**Interpretation:** The acquired profile holds a shortcut referring to a path and volume information. That could be relevant to a previously attached device or file interaction. **It does not prove** who clicked the file, that `E:` still refers to the same drive, or that `review.pdf` was transferred from the Windows computer to USB.

**Corroboration:** target-file evidence if obtained, acquired volume mapping, USB enumeration/install context, Jump Lists, browser download target, filesystem journals, and independent EDR/file-audit records if available.

## 3. Jump Lists: application context with independent limits

Many Windows applications create **AutomaticDestinations** / **CustomDestinations** records associated with recently accessed or pinned items. These can contain embedded LNK structures, application ID information, paths and timestamps. Some apps store list items differently or don't produce them.

### Parse acquired files with JLECmd

The [JLECmd maintained repository](https://github.com/EricZimmerman/JLECmd) documents directory input, CSV output and optional deeper LNK details. Validate the build and confirm the expected file set is actually present:

```powershell
.\JLECmd.exe -d "D:\CASE-EXAMPLE\working\UserA\Recent\AutomaticDestinations" --csv "D:\CASE-EXAMPLE\results\JumpLists"
.\JLECmd.exe -d "D:\CASE-EXAMPLE\working\UserA\Recent\CustomDestinations" --csv "D:\CASE-EXAMPLE\results\JumpLists"
```

**Example (invented, not a tool-produced row):**

```text
App identity : PDF reader (association subject to validation)
Target path  : E:\Reports\review.pdf
Entry count  : app-specific; verify parser and data fields
Observation  : Jump List contains a reference to review.pdf
```

**Interpretation limit:** A Jump List reference does **not** inherently prove file contents were read, modified, copied or intentionally selected by a particular person. Pinning, automatic application behavior, MRU updates and reused application IDs must be considered. Check the actual metadata and correlate with independent sources.

**Don't count LECmd and JLECmd output from the same embedded LNK as two independent confirmations.** They are different parsers or representations of overlapping underlying data.

## 4. ShellBags: folder-view traces, not a timestamped travel log

Modern Windows commonly stores per-user folder view/shell-bag structures in:

```text
NTUSER.DAT: Software\Microsoft\Windows\Shell\BagMRU / Bags
UsrClass.dat: Local Settings\Software\Microsoft\Windows\Shell\BagMRU / Bags
```

The exact branch, storage and parsing vary by Windows version and roaming/profile history. Some ShellBag records can persist when directories are no longer available; they are particularly useful for **possible folder-view path context**, including some removable/network locations.

**Crucial nuance:** A reconstructed folder path in ShellBags is not guaranteed proof the person browsed to that folder. Key LastWrite can reflect changes to Shell view state rather than the first/last time a human opened it. An artifact may reflect automated or inherited application behavior. Do not use ShellBag “first visited” or “last visited” language unless the specific metadata and validation genuinely support it.

### Offline parser and review

Use an appropriately validated ShellBags parser (for example [ShellBags Explorer and SBECmd](https://ericzimmerman.github.io/)). The command-line utility's tested file formats/flags may change between releases; **check `SBECmd.exe --help` on your installed version**. Its directory-mode processing and CSV options are documented in a [maintainer-reported example](https://github.com/EricZimmerman/Issues/issues/160):

```powershell
# Stage copies of NTUSER.DAT / UsrClass.dat with transaction logs and profile mapping.
.\SBECmd.exe -d "D:\CASE-EXAMPLE\working\Registry\UserA" --csv "D:\CASE-EXAMPLE\results\ShellBags"
```

If parser says the hive is dirty or that logs are missing, **document the warning**; consider recovering transactions on a duplicate according to the tool's validated process. Record reconstruction assumptions, SID, source hive, key path, embedded data and any untrusted time interpretation.

**Synthetic observation:** `UsrClass.dat` of Profile A includes a parsed folder path `E:\Reports`. This can lead to a hypothesis that the Windows Shell had view information for that directory. **It does not prove** the folder was displayed by Profile A at the alleged offense time or that any file was copied.

## 5. Relationship to browser and removable-media artifacts

The [browser history and download guide](browser.md) examines visit timestamps and download-manager records. The [USB examination guide](usb-device-history.md) explains USBSTOR/UASP, SetupAPI, volume IDs and MountPoints2. Combine them **only after** aligning:

1. Evidence item, host, Windows and browser profile.
2. Source time representation, UTC conversion, device clock, and retention/collection window.
3. File paths, actual volume identifiers and whether drive letters changed.
4. Whether an actual file exists on **both** a verified origin and acquired destination, with independently recorded hashes.
5. Alternative explanations that fit the data just as well or better.

### Worked fictional investigation: did an employee copy a PDF?

| Artifact | Observation | Does it prove the alleged copy? |
| --- | --- | --- |
| Browser History | Portal visit and download entry near 10:00 | **No**: visit/download metadata, actual file/path needs validation |
| Target file | PDF present in local Downloads within acquired scope | **No**: origin/activity not uniquely established |
| LNK | Shortcut references `E:\Reports\review.pdf` | **No**: path may be stale, copied from another source, or drive mapping may differ |
| Jump List | PDF reader references the target path | **No**: app-context metadata is not proof of copying |
| ShellBags | `E:\Reports` folder view trace | **No**: cannot establish access at exact time or physical user |
| USBSTOR/SetupAPI | A USB device was recognized or installed at some time | **No**: not a file-transfer log |
| External drive image | **Not available** | Can't independently compare destination content |

**Hypothesis A:** a user downloaded the file and transferred it to USB.  
**Hypothesis B:** the file was downloaded and opened locally; the removable-device traces are unrelated.  
**Hypothesis C:** the target drive was associated with that machine previously, or files were copied in the opposite direction.

**Supported finding:** “The examined browser and Windows user-activity artifacts contain references to a PDF and a removable-volume path. They do not independently establish that the file was copied to an external device, the direction of any transfer, or who performed it.”

**Don't say:** “The owner of Profile A stole review.pdf.” This jumps from profile-associated traces to a human actor and criminal intent without sufficient support.

## 6. Artifact-to-finding worksheet

```text
Evidence item and authorized question:
Image/source and per-artifact hashes:
Windows build, profile SID and user-path mapping:
Relevant browser profile/SQLite acquisition + WAL completeness:
LNK source path, parser version, raw target/volume fields:
Jump List source, AppID, target and parser version:
ShellBag hive (NTUSER/UsrClass), logs, raw branch and interpretation:
USB volume mapping and SetupAPI evidence:
Native source times, timezone and normalized UTC calculation:
Independent filesystem/EDR/auditing evidence:
What supports Hypothesis A:
What challenges Hypothesis A:
Alternative hypotheses and missing sources:
Supported observations / limits / final finding:
Derived exports, examiner and peer reviewer:
```

## Common mistakes

1. Treating a LNK's stored target timestamps as the time someone opened a document.
2. Treating a Jump List item as definitive proof of execution, file editing or copying.
3. Treating ShellBags as an exact log of every folder opened by a particular person.
4. Assuming drive `E:` always means one removable device.
5. Counting two tools parsing one artifact as two independent sources.
6. Ignoring automatic/sync behavior, missing transaction files or profile ID uncertainty.
7. Writing a preferred theft/malware narrative before looking for contradictory artifacts.

## Published source ledger

| Issuer | Reference | Use and limitation |
| --- | --- | --- |
| [SWGDE](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) | **18-F-001-2.0, Best Practices for Computer Forensic Examinations, final July 28, 2025** | Authority, scope, integrity, validation, interpretation and documentation; **not** proof of exact LNK/Jump List/ShellBag behavior |
| [Eric Zimmerman, LECmd](https://github.com/EricZimmerman/LECmd) | Maintainer CLI documentation, reviewed Oct 29, 2026 | LNK extraction options and supported result formats |
| [Eric Zimmerman, JLECmd](https://github.com/EricZimmerman/JLECmd) | Maintainer CLI documentation, reviewed Oct 29, 2026 | Automatic/Custom Jump List parsing, CSV, source/format limitations |
| [Eric Zimmerman ShellBags resources](https://ericzimmerman.github.io/) | Maintained tool resources, reviewed Oct 29, 2026 | SBECmd/ShellBags Explorer; validate release and operation against the test source |
| [Microsoft Explorer folder settings](https://learn.microsoft.com/en-us/answers/questions/2426288/how-to-adjust-the-default-column-displays-in-windo) | Microsoft public support discussion, historical background only | BagMRU/Bags as Shell view data; **not a forensic standard or definitive interpretation validation** |

**Validation boundary:** Published commands were checked against current maintainer references; **no commands or parser outputs were reproduced on a forensic Windows test image in this pass**. Before use on Evidence, validate versions and independently compare samples with known activity.

[Windows Examiner](README.md) · [Browser acquisition and interpretation](browser.md) · [USB forensic examination](usb-device-history.md) · [Registry examination](registry.md) · [Source-based terminology](../../planning/TERMINOLOGY.md)
