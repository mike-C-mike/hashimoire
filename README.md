# Hashimoire

**Hashimoire** is a practical DFIR and defensive security field reference for tool notes, playbooks, artifact paths, snippets, detections, templates, scripts, and repeatable workflows.

It is not meant to be a polished textbook or a copy of tool `--help` output. It is a working knowledge base for the commands, procedures, reminders, and documentation habits that are useful when time matters.

The name is intentionally a little weird.

A grimoire is a book of collected knowledge, formulas, instructions, and working notes. Hashimoire applies that idea to digital forensics and defensive security: hashes, artifacts, commands, triage notes, tool references, detections, templates, and field-tested reminders.

## The Live Reference

**Website:** [Hashimoire on GitHub Pages](https://mike-C-mike.github.io/hashimoire/)

Hashimoire has two useful starting points backed by the same Markdown repository:

- **[Field Collector](collector/README.md):** mobile-first preservation, scene documentation and clean handoff. The [Smartphone & Tablet Field Preservation Guide](collector/mobile-device-collection.md) gives an immediate power-state decision path for officers without asking them to learn examiner tooling.
- **[Forensic Examiner](examiner/README.md):** acquisition, Windows forensic snippets, expected command outputs, evidence integrity and lab examination.

### Current content focus — Windows examiner execution evidence (October 26, 2026)

The **Field Collector foundation remains complete** with eight useful scenario guides. This pass deepens forensic examination rather than adding more collector categories. [Windows Examiner — Execution & Intrusion Timeline](docs/windows/README.md) now provides a question-driven path from a verified acquired Windows image to defensible process/network findings.

**New reviewed pages:** [Prefetch, Amcache and process-creation interpretation](docs/windows/execution.md) and [worked Security 4688 / Sysmon ProcessGuid timeline](docs/windows/timelines.md). These demonstrate **real supported tool commands** with labeled synthetic outputs; show how hexadecimal PIDs, timestamps and log coverage affect conclusions; and distinguish historical execution artifacts from proof of actor identity, malicious intent or exfiltration. The primary professional baseline is [SWGDE 18-F-001-2.0 (Feb 28, 2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/).

Only the completed Windows workflow is published in the **Windows Artifacts & Timelines** category. Registry, browser and filesystem pages remain hidden until substantive, source-reviewed material exists. Continue to test commands and tool versions on actual lab images before case use.

### Completed Field Collector foundation — cloud and account preservation (October 26, 2026)

**Field Collector remains first.** The role hub now leads directly to eight complete field situations rather than multiple placeholder stops:

| Collector situation | Complete field reference |
| --- | --- |
| A device is smoking, swollen, wet, crushed, or storage has failed | [Damaged and hazardous digital devices](collector/damaged-devices.md) |
| A phone is off, locked, unlocked or damaged | [Smartphone and tablet preservation](collector/mobile-device-collection.md) |
| A computer is on, off, asleep or connected to external storage | [Computer and laptop preservation](collector/computer-collection.md) |
| A found USB drive, SD card or external disk | [Removable media collection](collector/removable-media.md) |
| CCTV/DVR or cloud video is at risk of retention overwrite | [Video preservation and export handoff](collector/video-preservation.md) |
| A social post, cloud file, message or account record may disappear | [Cloud and account first-response preservation](collector/cloud-preservation.md) |
| Evidence is being packaged or transferred | [Packaging, chain of custody and examiner handoff](collector/evidence-handoff.md) |
| CSU unavailable or delayed and the scene risks changing | [Interim scene triage and outside-in photography](collector/scene-documentation.md) |

The Collector reference now also includes a **CSU-limited** interim scene photography guide: perimeter control first, then original-condition overall/midrange/close-up views from outside in, followed by identification markers and appropriately placed scale photographs **only after unmarked images**. This does not replace a specialist CSU examination; it applies to agencies without a CSU or urgent documentation while one is delayed. The storage, video, computer and handoff guides remain available.

**Evidence-first, safety-first exception:** Different SWGDE publications govern wet/damaged **mobile devices** and failed/damaged **storage media**; lithium battery danger overrides normal powered-on evidence preservation. This latest guide includes a dated source ledger and direct publisher references.

**Cloud-evidence distinction:** The new Collector article explicitly distinguishes identifying a record, requesting preservation, provider confirmation, legal production and forensic validation. Based on **SWGDE 23-F-004-1.1 (Jan 2025)** and **SWGDE 18-F-002-2.0 (Nov 2025)**, it explains the limited U.S. **18 U.S.C. §2703(f)** preservation period and renewal, avoids unauthorized account access, and directs formal requests to authorized legal/investigative personnel. It includes a source ledger, scope/identity requirements and internal referral worksheet—not a provider-ready legal demand.

### Publishing and maintenance checks

The previous repair sprint rebuilt the empty OSINT index and corrected malformed hashing and tool pages. Before any new pages are linked publicly, run:

```bash
python3 scripts/generate_sidebar.py --check
python3 scripts/audit_published_docs.py
```

The first validates publication status and navigation targets. The second checks existing Markdown for empty pages, malformed code fences, missing titles and unresolved local links. GitHub Actions runs both on relevant changes. These are **structural checks**, not a substitute for testing procedures, reviewing official guidance or confirming the live site renders correctly.

**Product constraint:** A one-tap phone home-screen shortcut is sufficient for now; offline access is not a current development priority.

### Publishing standard: immediate value, not empty pages

**Source rule:** Operational field articles must be based on verified, published best-practice guidance from the appropriate professional body or government agency, with a title, standard/document number and version/date where applicable, direct publisher link, last-reviewed date, and clear notes about scope or conflicting recommendations. Do not present general recommendations as binding law; agency SOP, safety and case authority still apply.

A new page or navigation section is published only when it supports a real decision or task and has enough validated substance to be used. At minimum, it should provide **action, rationale, risks/limitations, documentation and a clear next step**, with official references where relevant.

The future navigation taxonomy is recorded in [site/navigation.json](site/navigation.json) and intentionally hides unpublished areas. Read the [architecture](planning/ARCHITECTURE.md) and [roadmap](planning/ROADMAP.md) before restructuring sections.

**Maintenance rule:** Every substantive content pass also reviews and updates this README's **current focus**, related links, and roadmap progress. Don't let the README describe a repository that no longer exists.

### Phone home-screen icon

The site provides a dedicated **emerald-and-gold Hashimoire icon** with iOS touch icon and Android web-app manifest variants. See [Save Hashimoire to a phone home screen](docs/mobile-home-screen.md). A shortcut still needs an internet connection; this is **not yet an offline PWA**.

## What This Is

Hashimoire is a living reference for authorized defensive work, including:

- DFIR triage notes
- Evidence handling habits
- Tool installation and usage notes
- Common command patterns
- Hashing references
- Windows, Linux, and macOS notes
- Detection and hunting queries
- SIEM-focused tuning notes
- Defensive OSINT and exposure checks
- Templates and checklists
- Repeatable workflows
- Scripts and small helpers

The goal is to build something practical enough to use, not something that only looks impressive in a README.

## What This Is Not

Hashimoire is not a hacking tutorial.

It is not:

- exploit development
- credential theft
- stealth guidance
- evasion guidance
- persistence guidance
- unauthorized access guidance
- “how to break in” material
- case-specific or sensitive content

This repo does not contain client data, internal system details, confidential case information, protected personal information, or anything that would be inappropriate to publish.

The working rule is simple:

> If a note would primarily help someone harm people, bypass authorization, misuse access, or evade accountability, it does not belong here.

This project is for authorized, legal, ethical, defensive work.

## Core Principles

Hashimoire follows a few simple rules:

- Practical beats exhaustive.
- Notes should explain why a step matters, not just what to type.
- Commands should include context, assumptions, and expected output where possible.
- Evidence-related workflows should include documentation considerations.
- Dangerous techniques are framed defensively or excluded.
- Templates should make work more consistent, not create paperwork theater.
- If a workflow affects evidence, the documentation path matters as much as the tool output.

## How to Use This Repo

Use the repo by task type:

- Start with **snippets** for quick command refreshers.
- Use **playbooks** for repeatable workflows under time pressure.
- Use **docs** for deeper notes, install steps, gotchas, and artifact references.
- Use **detections** for hunting logic, SIEM queries, and tuning notes.
- Use **templates** for repeatable documentation and review checklists.
- Use **scripts** for small helpers that reduce repetitive work.

## Repository Structure: Today and Tomorrow

Hashimoire uses **two audience entry points** backed by a shared, evolving reference library.

```text
hashimoire/
├─ home.md                       # Site entry point: choose a role
├─ collector/                    # Fast field preservation and handoff
├─ examiner/                     # Examiner start page
├─ playbooks/                    # Repeatable procedures and decision flows
│  ├─ acquisition/
│  └─ suspicious-email/
├─ snippets/powershell/          # Windows forensic commands and sample output
├─ docs/                         # Tool notes, hashing and deeper explanations
├─ osint/                        # Defensive OSINT and exposure checks
├─ site/navigation.json          # Published + planned/hideable menu registry
├─ scripts/generate_sidebar.py   # Sidebar publisher with link validation
├─ planning/                     # Architecture, content gates, phased roadmap
└─ _sidebar.md                   # Generated, published-only Docsify navigation
```

Future sections (including **mobile examiner, Windows artifact deep dives, macOS, Linux, memory, cloud, networks, video, reporting and training**) are reserved in the [navigation registry](site/navigation.json) but intentionally **hidden until a useful body of reviewed content is ready**.

See the [Information Architecture v1](planning/ARCHITECTURE.md) and [depth-first roadmap](planning/ROADMAP.md) for the planned headings, writing standards and release order.

To publish a finished page, update its status in `site/navigation.json`, then regenerate `_sidebar.md` with:

```bash
python scripts/generate_sidebar.py
python scripts/generate_sidebar.py --check
```

The published website never shows empty future categories. **Hidden from navigation does not mean private** in a public repository.

## Start here: acquisition and live-response reference

- [Acquisition playbooks](playbooks/acquisition/README.md) — collection sequence, field bag, software readiness and lab follow-on.
- [Windows collection snippets](snippets/powershell/README.md) — small, reusable PowerShell command references, with scope and output cautions.
