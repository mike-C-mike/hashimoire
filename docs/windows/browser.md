# Browser Artifacts — Visits, Downloads & Source Correlation

**Audience:** authorized digital forensic examiners and DFIR analysts  
**Question:** *Does the acquired Windows profile support a browser visit or download, and what happened to the referenced file afterward?*  
**Evidence:** acquired browser profiles, associated SQLite files and journals, download folders, Windows user-activity artifacts  
**Risk:** caution — privacy, incomplete profiles, synchronization, deleted records and timestamp interpretation  
**Published guidance reviewed:** October 29, 2026

> **Examiner-only, on a verified working copy.** A browser History entry is an **artifact**, not proof that the account holder personally read a webpage. A Downloads record is not by itself proof that the file exists now or was ever opened. Respect scope and data minimization. Follow [SWGDE 18-F-001-2.0 (final July 28, 2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/).

## Start with distinct investigative questions

| Question | Candidate artifact | What it can support | What it does not establish by itself |
| --- | --- | --- | --- |
| Did a browser record a URL visit? | Chromium `History`: `urls`, `visits`; Firefox `places.sqlite` | Browser-profile history of a visit/transition | A human read the page or initiated it intentionally |
| Was a download initiated? | Chromium `downloads` / `downloads_url_chains`; Firefox download metadata | Download-manager entry, origin, target and status where available | File was completed, retained, opened or malicious |
| Did a file reach the endpoint? | Filesystem entry, acquired file hash, alternate data streams, endpoint telemetry | A file existed within examined scope | That its creation came from this browser visit |
| Did an application interact with it? | LNK, Jump Lists, Recent, Prefetch, process/EDR events | Application/document relationship | That someone edited, copied or exfiltrated content |
| Was it transferred off-host? | External-device image, source/destination file hashes, file audit, USB/volume records | Potentially independent support for matching data and device context | Direction, actor or actual copy from USB history alone |

**Our convention:** the collected computer is **Evidence**; browser database records are **artifacts**. Together with other observations, those artifacts can provide **evidence** for or against a narrow hypothesis. This is editorial terminology, not a rule of admissibility. [Terminology guide](../../planning/TERMINOLOGY.md).

## 1. Prepare the browser-profile acquisition

Identify Windows account/profile, browser product, **all relevant browser profiles**, version/build and whether browser sync or other devices might affect records. Do not assume the machine's default profile was used.

Common example locations (actual paths vary by version, install mode, profile and roaming setup):

```text
Windows / Chromium family
C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\History
C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Profile 1\History
C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\Default\History

Windows / Firefox
C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\places.sqlite
C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\favicons.sqlite
```

**Do not collect only one database file blindly.** SQLite connections may have outstanding `-wal` and `-shm` companions; acquire the related consistent file set from the same point in time when present, along with metadata needed for validation. Depending on forensic method, copying a live SQLite database without its WAL may omit recent committed activity. Document any recovery/reconciliation and preserve untouched original acquisition.

The browser profile can contain **cookies, credentials, authentication tokens, saved form data and private browsing context**. Capture only within legal authority, isolate and restrict case exports, and do not open a subject's synced browser account or replay session tokens to obtain extra data without separate authorization.

**Critical acquisition detail:** The `sqlite3` commands below apply to **lab working copies only**. Opening a SQLite database may perform journaling or checkpoint-related work depending on mode and companion files. Preserve the original acquired files and hashes; use validated read-only forensic tooling, or work on a disposable derivative that can be altered. Never point SQLite at the original Evidence image.

## 2. Chromium / Edge: inspect real schemas before using a query

Chromium and Microsoft Edge share Chromium-derived storage concepts, but **schema, retention, browser profiles and private-browsing behavior vary**. This is a bounded educational query on a working copy using the SQLite command-line tool; confirm `sqlite3 -version` and the actual schema.

```powershell
# Paths refer ONLY to staged copies in the examination lab.
$History = 'D:\CASE-EXAMPLE\working\Browser\Chrome-Default\History'
& sqlite3.exe -readonly $History "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
& sqlite3.exe -readonly $History "PRAGMA table_info(visits);"
& sqlite3.exe -readonly $History "PRAGMA table_info(urls);"
```

If your `History` has no `visits` table or cannot be opened consistently, **don't force the query**. Review the browser build, collection completeness and associated WAL, then use a tested artifact parser.

### History: join visited URLs to visit records

```powershell
$History = 'D:\CASE-EXAMPLE\working\Browser\Chrome-Default\History'
$query = @'
SELECT
  v.id AS visit_id,
  u.url,
  u.title,
  v.visit_time AS raw_chromium_time,
  datetime((v.visit_time / 1000000) - 11644473600, 'unixepoch') AS interpreted_utc
FROM visits AS v
JOIN urls AS u ON u.id = v.url
ORDER BY v.visit_time DESC
LIMIT 50;
'@
& sqlite3.exe -readonly -header -csv $History $query
```

**Clock explanation:** Chromium's commonly used `visit_time` represents **microseconds since 1601-01-01 UTC**. Divide by 1,000,000 and subtract 11,644,473,600 seconds to display Unix-based UTC. Preserve **raw integers and converted time**; review zero/invalid timestamps, format changes, source clock error and timezone assumptions.

**Synthetic output (simplified, not an actual case):**

```text
visit_id,url,title,raw_chromium_time,interpreted_utc
324,https://example.org/reports,"Reports",13405705000000000,2025-10-15 12:16:40
```

These figures are **fictional and illustrative**; do not use their exact numbers to validate a parser. A database URL/visit row alone does not establish whether the page was read, background-refreshed, synced, opened from an app, or navigated by the human whose Windows profile contains it. Inspect transition/source flags and corroborating artifacts where needed.

### Download: check status, filename and URL-chain context separately

Use a schema check first:

```powershell
& sqlite3.exe -readonly $History "PRAGMA table_info(downloads);"
& sqlite3.exe -readonly $History "SELECT name FROM sqlite_master WHERE name='downloads_url_chains';"
```

On Chromium versions with these columns:

```powershell
$query = @'
SELECT id, target_path, start_time, state, received_bytes, total_bytes, opened
FROM downloads ORDER BY start_time DESC LIMIT 25;
'@
& sqlite3.exe -readonly -header -csv $History $query
```

**Do not interpret `state` numeric codes without checking the exact browser version.** Chromium's maintained source shows a downloads table with fields for target path, start/end time, received/total bytes, state, interrupted reason, hash and whether the browser considers an item opened. It separately holds a `downloads_url_chains` table for redirects/origin history. A reported `opened` flag is application metadata, **not independently verified human action**.

Source: [Chromium download database implementation](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/history/core/browser/download_database.cc) and [Chromium history database](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/history/core/browser/history_database.cc). These are **product-source technical references, not forensic standards**.

**Questions to test:** Does the acquired file still exist? Does its SHA-256 match a subsequent LNK target or independently acquired media? Was it incomplete/interrupted? Did Edge/Chrome sync introduce data from other profiles? Are there external download logs or browser policy controls?

## 3. Firefox: places.sqlite needs its own time basis

Mozilla identifies `places.sqlite` as storing bookmarks, download references and browsing history, and identifies related profile files such as `favicons.sqlite`. [Mozilla profile file reference](https://support.mozilla.org/en-US/kb/about-your-important-data-and-their-files) (updated July 2026).

On a **verified lab copy** inspect schema first:

```powershell
$Places = 'D:\CASE-EXAMPLE\working\Browser\Firefox-ProfileA\places.sqlite'
& sqlite3.exe -readonly $Places "PRAGMA table_info(moz_places);"
& sqlite3.exe -readonly $Places "PRAGMA table_info(moz_historyvisits);"
```

Common Firefox releases store `moz_historyvisits.visit_date` as **microseconds since 1970-01-01 UTC**, *not* the Chromium 1601 epoch:

```powershell
$query = @'
SELECT
  v.id AS visit_id, p.url, p.title, v.visit_date AS raw_firefox_time,
  datetime(v.visit_date / 1000000, 'unixepoch') AS interpreted_utc
FROM moz_historyvisits AS v
JOIN moz_places AS p ON p.id = v.place_id
ORDER BY v.visit_date DESC
LIMIT 50;
'@
& sqlite3.exe -readonly -header -csv $Places $query
```

Browser history records may reflect navigation rules, redirects, bookmarks, internal/synced behavior or deletion. **Never apply Chromium's 1601 offset to Firefox visits**. Download information storage has changed over Firefox versions; use tested parsing and corroborate the actual acquired file rather than assuming a historic annotations table exists today.

## 4. Test the “visited → downloaded → opened” story

**Fictional investigation:** An allegation suggests a PDF was downloaded from a web portal and opened by an employee shortly before a USB drive was attached. The examiner must test this, not merely find items that fit it.

| Artifact | Observed | Alternative / limitation |
| --- | --- | --- |
| Chromium `visits` | URL visit within broad window | Browser/background activity; not personal intent or reading |
| Browser `downloads` | Filename and destination, state must be decoded | May be incomplete, synchronized, renamed or deleted |
| NTFS file data | PDF exists in acquired `Downloads` directory | Could have been placed there by another method |
| LNK / Jump List | Application references an apparent PDF path | Can be recent-app metadata, not proof user read the contents |
| USB registry | Storage device enumerated | May have been installed long before; file copy not established |
| Acquired USB device | **Unavailable** | No destination file or independent content comparison |

**Competing hypotheses:** A browser download was followed by document opening; an automated process created the file; the file was acquired by another application; USB enumeration is unrelated. Check exact times, file hash, source profile, installed software, EDR and negative-source coverage.

**Possible finding:** “The acquired browser profile records a visit and a download entry for the referenced document. The available Windows artifacts are consistent with later application interaction, but the collected records do not establish which person initiated the activity or that the file was transferred to external media.”

**Not supported:** “The employee browsed to the portal, intentionally stole the PDF, and copied it to the USB.” Each added assertion needs independent support.

## 5. Documentation checklist

- [ ] Authority, scope, incident time window, Evidence item, image and relevant dataset SHA-256 documented.
- [ ] Browser product/build, Windows user profile, browser profile names and sync considerations identified.
- [ ] SQLite main database **and appropriate -wal/-shm companions** preserved from consistent collection.
- [ ] Raw source values and exact schema fields recorded with tool/parser version, exported CSV location and any errors.
- [ ] Chromium 1601 versus Firefox 1970 timestamp calculations documented; time uncertainty and timezone preserved.
- [ ] Visit, download manager state, file existence, application interaction and transfer claims **separated**.
- [ ] Missing/deleted history or absent logs treated as **coverage limitations**, not negative proof of no activity.
- [ ] Alternative hypotheses, conflicting artifacts and exculpatory observations captured.

### Examiner note worksheet

```text
Evidence item / profile / case authorization:
Acquisition scope and hash verification:
Browser name, version, profile directory and sync status:
History/places SQLite file and matched WAL/SHM:
Schema inspected and SQL/parser build:
Raw visit/download values and UTC conversion:
Download state, target path, origin/redirect chain, status:
Target file present? source hash and validation:
LNK/Jump List or OS execution/user-activity corroboration:
Contradictions, missing sources and independent data:
Hypotheses supported / weakened / unresolved:
Final bounded finding:
```

## Published source ledger

| Publisher | Publication or reference | What it supports |
| --- | --- | --- |
| [SWGDE](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) | **18-F-001-2.0, Best Practices for Computer Forensic Examinations, final July 28, 2025** | Authority, scoped examination, copy protection, integrity, interpretation and reporting; *not* browser-schema specification |
| [Chromium project](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/history/core/browser/history_database.cc) | Maintained source code, reviewed Oct 29, 2026 | The presence of `urls` / `visits` relationships in current Chromium history implementation; version-sensitive |
| [Chromium project](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/history/core/browser/download_database.cc) | Maintained source code, reviewed Oct 29, 2026 | Downloads schema, status/path/byte fields and redirect chains; **not a guarantee for old versions** |
| [Mozilla Support](https://support.mozilla.org/en-US/kb/about-your-important-data-and-their-files) | *About your important data and their files*, updated July 18, 2026 | `places.sqlite` history/download profile inventory and companion files |
| [Hashimoire user-activity workflow](user-activity.md) | Project article | LNK, Jump Lists, ShellBags and independent OS-level corroboration |

**Practice limit:** Queries shown are based on published schemas, **not run against a validated forensic Windows image during this authoring pass**. Reproduce with known test data, current browser builds and an approved forensic process before case use.

[Windows Examiner](README.md) · [Windows user-activity artifacts](user-activity.md) · [USB examination](usb-device-history.md) · [Execution findings](execution.md)
