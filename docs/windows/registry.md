# Windows Registry Forensics — Users, Execution & Context

**Audience:** authorized Windows forensic examiners and DFIR analysts  
**Questions:** Which user profile was involved? What application activity is recorded? What can registry artifacts corroborate or contradict?  
**Environment:** verified Windows forensic image or scoped hive collection, examined on an isolated lab workstation  
**Risk:** caution — sensitive user data, OS-version effects, incomplete registry transactions  
**Published references reviewed:** October 26, 2026

> **Do not examine the original Evidence item by loading its hives read/write into Windows.** Acquire with a documented method, verify source and output integrity, and analyze a controlled working copy with a validated offline parser. Follow [SWGDE 18-F-001-2.0, *Best Practices for Computer Forensic Examinations* (final July 28, 2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/). This is an examiner reference, **not** a first-responder instruction to search the live system.

## Begin with an investigative question

Imagine an investigator asks whether an unknown utility was used on a submitted laptop and whether that activity relates to a removable drive. **Don't assume the allegation is true.** Identify potentially relevant traces, test their interpretations and look for both supporting and contradictory observations.

**Our editorial vocabulary:** the acquired computer is the **Evidence** item; recovered registry entries are **artifacts**; the support they collectively provide *for or against a specific proposition* is **evidence** (lowercase e). This is a writing convention, not a legal rule: an artifact can itself qualify as digital evidence. See [terminology and hypothesis testing](../../planning/TERMINOLOGY.md).

## Registry questions at a glance

| Investigative question | Primary artifact | Possible observation | What it **cannot** establish alone |
| --- | --- | --- | --- |
| Which profiles exist? | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`, plus SAM and NTUSER.DAT | SID-to-profile-path association | Who physically used an account at an exact time |
| Did a user interact with a GUI program? | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | GUI activity traces, ROT13 names, last-run/focus data | A precise number of runs, sole human actor, or necessarily actual execution |
| Is there recent executable activity tied to a SID? | `SYSTEM\ControlSet00x\Services\bam\State\UserSettings\<SID>` | Executable path and timestamp in some builds | Complete activity history, unique operator identity or malicious intent |
| Was a file/application present? | `Amcache.hve` / `SOFTWARE` inventory | Software/path/metadata association | Program execution simply from inventory |
| Is a path recorded by compatibility caching? | `SYSTEM\ControlSet00x\Control\Session Manager\AppCompatCache` | Path and format-specific timestamps | Execution proof on modern Windows |
| Did an external storage device appear? | `SYSTEM\ControlSet00x\Enum\USBSTOR` / `SCSI` / `USB` | Device identity and enumeration traces | A particular file was copied to or from it |
| Did a profile see a mounted volume? | `NTUSER.DAT\...\Explorer\MountPoints2` | Per-profile mount-related artifacts | Every connect/disconnect event or direct proof of copying |
| Was persistence configured? | `SOFTWARE` and `NTUSER.DAT` Run/RunOnce, services and related sources | Startup registration | That the program executed, or that the registration was malicious |

**Registry LastWrite is a key modification timestamp**, not automatically the time a file opened, a USB connected, or a program ran. Many relevant records have **their own embedded timestamps**, and the precise semantics vary by artifact and Windows build.

## 1. Acquire and identify the right hives

A verified forensic image or appropriately scoped offline collection typically includes:

```text
Windows\System32\config\SYSTEM        and SYSTEM.LOG1 / SYSTEM.LOG2
Windows\System32\config\SOFTWARE      and SOFTWARE.LOG1 / SOFTWARE.LOG2
Windows\System32\config\SAM           and SAM.LOG1 / SAM.LOG2
Windows\System32\config\SECURITY      and SECURITY.LOG1 / SECURITY.LOG2
Users\<profile>\NTUSER.DAT             and NTUSER.DAT.LOG1 / LOG2
Users\<profile>\AppData\Local\Microsoft\Windows\UsrClass.dat (+ logs)
Windows\AppCompat\Programs\Amcache.hve (+ transaction/companion files)
Windows\INF\setupapi.dev.log
Windows\System32\winevt\Logs\*.evtx   (if within authority/scope)
```

These files may contain private user information and secrets; acquire/store according to legal scope and case policy. A missing hive or transaction log is a **collection/coverage limitation**, not proof the activity did not occur.

### The ControlSet trap

In a **running** Windows Registry, `CurrentControlSet` is a convenient alias. In an **offline SYSTEM hive**, examine actual `ControlSet001`, `ControlSet002`, etc., and the `SYSTEM\Select` values to identify which set was current/selected. **Do not assume ControlSet001 is always the active set.** Explain differences if the image holds multiple sets.

### Transaction-log caveat

Registry hive modifications can exist in `.LOG1`/`.LOG2` before being incorporated into the base hive. Some parsers automatically replay these logs; some require separate handling. Work **only on copies**, preserve original hive/log hashes, record whether recovery was applied, and don't apply the same logs twice. The maintained [RECmd/rla documentation](https://github.com/EricZimmerman/RECmd) explains transaction-log replay and directory options.

## 2. Offline inspection with Registry Explorer and RECmd

**Tools:** [Registry Explorer](https://ericzimmerman.github.io/#!index.md) provides interactive bookmarks and a hive viewer; [RECmd](https://github.com/EricZimmerman/RECmd) offers command-line inspection and predefined batches. Validate the exact release, compatibility and included batch-file name on your analysis machine.

**Illustrative lab folders, not live system paths:**

```text
D:\CASE-EXAMPLE\working\Registry\
   SYSTEM, SYSTEM.LOG1, SYSTEM.LOG2, SOFTWARE, ...
   Users\UserA\NTUSER.DAT, NTUSER.DAT.LOG1, NTUSER.DAT.LOG2
D:\CASE-EXAMPLE\results\Registry\
```

For a focused offline UserAssist review:

```powershell
# Run in the directory containing the validated RECmd.exe and its BatchExamples.
# Confirm this specific batch is present in your installed release.
.\RECmd.exe -f "D:\CASE-EXAMPLE\working\Registry\Users\UserA\NTUSER.DAT" --bn ".\BatchExamples\BatchExampleUserAssist.reb" --csv "D:\CASE-EXAMPLE\results\Registry"
```

The [tool author's published examples](https://github.com/EricZimmerman/RECmd) document `-f`, `--bn` and `--csv`, and the author's [published command poster](https://assets.contentstack.io/v3/assets/blt36c2e63521272fdc/blt83d26bfaab457108/EZ_Tools_Poster.pdf) includes a UserAssist batch example. If your release doesn't ship that example file, **use its provided documented batch or Registry Explorer bookmarks**, don't fabricate a file name.

For a SYSTEM-based compatibility-cache check on the acquired copy:

```powershell
.\AppCompatCacheParser.exe -f "D:\CASE-EXAMPLE\working\Registry\SYSTEM" --csv "D:\CASE-EXAMPLE\results\Registry"
```

[AppCompatCacheParser](https://github.com/EricZimmerman/AppCompatCacheParser) documents `-f` for an offline SYSTEM hive and `--csv` for results. Its output can assist with **path/context** review; do not label its entries as proven executions on current Windows merely because the parser emits a row.

### What should be recorded?

- Evidence item identifier, image/export hashes and whether each hive/log is complete.
- Profile SID, matching `ProfileList` path and relevant logon history; beware renamed or deleted accounts.
- Windows build, active ControlSet determination, mounted volume/device path mapping.
- Parser name/build, plugin/batch version, exact arguments, warnings, transaction-log recovery.
- Original key path, value name/type, raw value, embedded timestamp, key LastWrite and interpreted UTC time.
- Independent corroboration, contradictions, alternative explanations and source limitations.

## 3. UserAssist: distinguish GUI traces from verified execution

**Source:** `Users\<profile>\NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count`. UserAssist names are ROT13-encoded; specialized parsers decode fields, counts, last-run data and focus metrics.

**Critical published caveat:** Microsoft's Incident Response Team demonstrates that on Windows 10 and later **right-clicking a Start-menu application and choosing “Open file location” can update UserAssist's run count and last-executed field even without executing the binary**. Focus-time behavior offers additional context but is not a universal guarantee. See [Microsoft Incident Response's Windows Internals Forensics Guidebook — UserAssist](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/IR-Guidebook-Final.pdf), p. 11.

### Example parsed observations — completely synthetic

```text
Profile SID     : S-1-5-21-...-1001  (fictional)
Decoded item    : C:\Windows\System32\notepad.exe
Last recorded   : 2026-10-21T15:02:14Z
Run count       : 4
Focus time      : 12000 ms
Raw artifact    : NTUSER.DAT / Explorer\UserAssist\...\Count
```

**What it suggests:** GUI-user activity related to a named application in one user's profile. The data merits comparison with process-start telemetry and the real Windows build.

**What it does not prove:** Four confirmed executions, physical presence of the profile owner, successful file access, or any unlawful activity. **Avoid treating the LastWrite of the whole Count key as a timestamp for each child entry.**

If the application appears in UserAssist but there is **no** corresponding Event 4688, consider audit-policy coverage, retention, alternate execution, or a UserAssist interaction that did not launch the binary. Record these as hypotheses, not excuses for a predetermined story.

## 4. BAM/DAM: recent path/SID indications, not human attribution

On some Windows 10/11 builds, Background Activity Moderator (BAM) values appear under a path like:

```text
SYSTEM\ControlSet00x\Services\bam\State\UserSettings\<SID>
```

Older builds may use a different subtree; DAM behavior and availability differ by hardware/configuration. The embedded timestamp and program path can be useful for **recent executable activity**, but collection time, pruning, app type and OS build affect presence. A SID associates a registry location with a Windows account; it **does not identify who operated the keyboard**.

**Synthetic interpretation:**

```text
SID: S-1-5-21-...-1001
Path: \Device\HarddiskVolume4\Program Files\Example\helper.exe
Time interpreted: 2026-10-21T15:03:02Z
Observation: BAM record for this executable path under that SID
```

This can **support a time-bounded activity lead**, particularly when corroborated by an event record, but may be absent for console, network or removable-media executions. Don't treat a missing BAM value as proof a binary never ran. Device paths need mapping to the actual acquired disk/partition; `HarddiskVolume4` is not universally drive `C:\`.

## 5. Amcache and ShimCache: inventory is not a process event

- **Amcache:** See the [execution evidence guide](execution.md) for current `Amcache.hve` and possible `Inventory*.db` companion artifacts. Microsoft warns that **file presence/metadata cannot by itself prove execution**, and Amcache SHA-1 fields may reflect only a partial file hash for sufficiently large files.
- **ShimCache/AppCompatCache:** Read from the applicable SYSTEM ControlSet with a validated parser. Interpretation changes by Windows build; a cache entry or key LastWrite is not automatically a launch time.
- **Registry autoruns:** Run keys and service registrations are **configuration/persistence possibilities**. Combine with task logs, actual process creation, files and authorized system administration records before concluding that software ran or was malicious.

### Counterevidence is part of the workflow

If Registry and event records disagree, record the discrepancy. Possible causes include wrong profile, stale ControlSet, parser incompatibility, clock error, incomplete capture, missing transaction files or an actual false hypothesis. **Do not discard contradictions to preserve the theory.**

## 6. A hypothetical case note

**Question:** Was `helper.exe` run by the person associated with Profile A?

| Artifact / source | Observation | Limits and what to check next |
| --- | --- | --- |
| UserAssist, Profile A | GUI-related reference to `helper.exe` | Start menu interaction could update fields without execution; inspect focus and source context |
| BAM, SID 1001 | Executable path/time recorded | SID-to-profile mapping, retention and program-type gaps; not actual operator |
| Security 4688 | No related entry in acquired range | Was process creation auditing enabled and was the right time window retained? |
| Amcache | Same file path inventoried | Presence may corroborate a file, not confirm a launch |
| External IT record | Authorized helper installed by support team | Alternative legitimate explanation; verify task and timestamp |

**Defensible finding:** “Several registry artifacts refer to a utility under a profile/SID and indicate possible application activity. No collected process-creation event independently establishes a launch in the reviewed interval. The available artifacts do not determine which person used the system or establish malicious activity.”

**What to do next:** request legitimately available EDR or application logs, inspect Prefetch and other execution traces, verify clock normalization, and assess alternative benign use. Stop at an *unresolved* finding if that's what the artifacts support.

**Profile-related corroboration:** [ShellBags from NTUSER.DAT/UsrClass.dat](user-activity.md) can record folder-view state while [browser profiles](browser.md) record visited URLs and downloads. The two artifact categories do not automatically identify a human actor or prove file opening/copying. Check other profiles and conflicting sources.

## 7. Reporting checklist

- [ ] Evidence Item and forensic acquisition scope/hash documented.
- [ ] Offline hive and associated transaction-log/companion files preserved.
- [ ] Correct actual ControlSet and account profile/SID verified.
- [ ] Registry artifact path + exact raw field recorded (not only parser summary).
- [ ] Parser/OS versions and whether transaction replay occurred documented.
- [ ] UTC versus local times and key LastWrite versus embedded event times distinguished.
- [ ] Corroboration checked at independent **source** level—not merely two parsers of one hive.
- [ ] Contrary findings and alternative explanations retained.
- [ ] Conclusion limited to what the collected records support, including negative-source coverage.

## Published source ledger

| Publisher and publication | Version/date | Specific support |
| --- | --- | --- |
| [SWGDE, *Best Practices for Computer Forensic Examinations*](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) | **18-F-001-2.0, final July 28, 2025** | Scope, validated forensic tools, protecting original Evidence, reporting exculpatory/contrary information |
| [Microsoft Incident Response, *Leveraging Windows Internals for Forensic Investigation*](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/IR-Guidebook-Final.pdf) | Microsoft published guide, reviewed Oct 2026, pp. 3, 11 | Amcache presence vs execution; UserAssist last-run/run-count and focus pitfalls |
| [Eric Zimmerman, RECmd and rla](https://github.com/EricZimmerman/RECmd) | Maintainer CLI documentation, reviewed Oct 2026 | Offline hive inspection, batch parsing and transaction recovery |
| [Eric Zimmerman, AppCompatCacheParser](https://github.com/EricZimmerman/AppCompatCacheParser) | Maintainer CLI documentation, reviewed Oct 2026 | Offline SYSTEM-hive parsing and supported CSV options |
| [Eric Zimmerman Tools changelog](https://ericzimmerman.github.io/changelog/) | Maintainer changelog, checked Oct 2026 | Registry parser builds evolve; record actual installed release |
| [Hashimoire terminology](../../planning/TERMINOLOGY.md) | Project editorial standard | Evidence/submitted item versus artifact observations versus analytical evidence; hypothesis testing |

**Limit:** SWGDE provides overarching examination best practices. The artifact mechanics come from Microsoft and forensic tool research, and must be revalidated against the **specific Windows build** and tool version. No commands on this page were executed against a real Windows Evidence image during authoring.

[Windows Examiner](README.md) · [Removable-device correlation](usb-device-history.md) · [Execution artifacts](execution.md) · [Process timeline](timelines.md) · [Registry preservation snippet](../../snippets/powershell/registry-hive-preservation.md)
