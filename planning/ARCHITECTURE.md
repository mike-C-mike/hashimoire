# Hashimoire Information Architecture — v1

**Status:** Proposed structural baseline · October 2026  
**Audience:** Repository maintainers  
**Primary readers:** Field collectors (mobile-first) and trained forensic examiners (depth-first)

> **Goal:** Keep the structure predictable while building depth one subject at a time. Stable categories; incremental pages; no empty navigation destinations.

## Two entrances, one library

1. **Field Collector:** First contact, preservation, minimal interaction, scene documentation, packaging, custody and escalation. Concise checklists that fit a phone screen.
2. **Forensic Examiner:** Acquisition, validation, artifact interpretation, analysis, timelines, reporting, technical snippets and tool use.

The role hubs are *views into shared documentation*, not duplicate repositories. A collector guide can point to a deeper examiner page and back.

## Navigation principles

- **Home → choose role → choose subject → task.**
- **No placeholders in public navigation.** A header or link appears only when marked `published` and its destination exists.
- **Proposed subjects are already reserved** in [site/navigation.json](../site/navigation.json) with status `planned`. Those entries are hidden from the GitHub Pages sidebar.
- A subject moving to `drafting` or `ready` **stays hidden**. Only `published` appears.
- `_sidebar.md` is generated output. Do not hand-edit; regenerate after changing the registry:
  ```shell
  python scripts/generate_sidebar.py
  python scripts/generate_sidebar.py --check
  ```
- Published categories remain independently collapsible; expand only what you are working on. Keep meaningful landing/index pages for large topics.
- Future links have reserved *intended paths*. If reality demands a different path, adjust the registry **before publication**. Never silently break published URLs.

### What "hidden" means

**Hidden from the navigation is not private.** The repository and GitHub Pages are public; any file committed to `main` can be found through GitHub or opened directly, even without a menu link. For unfinished text or proprietary case material, use a development branch or private storage instead. Never publish real case data, credentials, recovered BitLocker passwords, or CJI.

## Category architecture (stable top-level groups)

| Group | Intended coverage | Initial visibility |
| --- | --- | --- |
| Start Here | Role selection, installation on phone, orientation | Published |
| Field Collector | Mobile, computers, peripherals, multimedia, handoff | Published |
| Forensic Examiner | Examiner entry point and cross-discipline procedures | Published |
| Windows Forensic Commands | Fast read-only queries and intentional exports | Published |
| Tool Reference | Installation, readiness, tool-to-artifact mapping | Published |
| OSINT & Exposure | Authorized public-source identification and defensive exposure review | Published |
| About | Project scope, attribution, safety and visual language | Published |
| Mobile Device Forensics | iOS, Android, state, acquisition, app artifacts and validation | Planned |
| Windows Artifacts & Timelines | Registry, execution, filesystems, browser and timelines | Planned |
| macOS Forensics | APFS, unified logs, system artifacts and imaging | Planned |
| Linux Forensics | Live response, logs, persistence and filesystems | Planned |
| Memory Forensics | Acquisition by OS, Volatility and evidence interpretation | Planned |
| Storage & Removable Media | Imaging, write blockers, NTFS/exFAT, encryption, USB | Planned |
| Cloud, Accounts & Identity | Microsoft 365, Entra, Google Workspace, escrow and authentication | Planned |
| Network, Email & Logs | PCAP, DNS, proxy, VPN, email and log sources | Planned |
| Video & Multimedia Evidence | CCTV exports, video/audio/images and integrity | Planned |
| Specialized Devices | Vehicles, wearables, IoT and niche collections | Planned |
| Detections & Incident Response | SIEM, threat hunting, containment and response | Planned |
| Evidence, Reporting & Templates | Chain of custody, artifact validation, prosecutor-ready reports | Planned |
| Training & Validation Labs | Synthetic datasets, exercises and tool validation | Planned |

### Content types, not extra navigational silos

Content *format* can differ within a subject:
- **Collector guide:** simple decision flow + action/avoid/escalate + handoff.
- **Examiner playbook:** authority, scope, sequence, exact collection steps, validation, handoff.
- **Command snippet:** what/when, exact command, example **synthetic** output, explanation of fields, limitations, cross-correlation and official references.
- **Artifact reference:** where found, data meaning, timestamps, acquisition, parser, confidence limits.
- **Tool guide:** official source, tested build/dependencies, acquisition output, lab-side analysis and issues.
- **Template:** ready-to-use worksheet, chain-of-custody or report structure with no real case data.

Avoid separate navigation categories for each format. Keep crosslinks to the relevant tool/snippet/playbook from the subject hub.

## Editorial terminology and investigative mindset

[**Hashimoire terminology and artifact-to-finding guidance**](TERMINOLOGY.md) is the house writing standard for examiner material:

- **Evidence** (capital E): the formally collected/submitted item or dataset (specify physical original, forensic acquisition and derivatives).
- **artifacts**: the specific recovered traces, records and metadata identified through examination.
- **evidence** (lowercase e): the support **for or against** a narrowly stated proposition that emerges from those artifacts and other appropriately evaluated sources.
- **finding/conclusion**: the examiner's supported, qualified determination after evaluating alternatives and limitations.

**Mindset:** Start with the authorized investigative question, not a preconceived answer. Observed artifacts inform hypotheses; explicitly test alternative explanations, seek contradictions/exculpatory information, and be prepared to weaken or reject an initial theory. Avoid confirmation bias and unsupported statements of guilt, intent or attribution.

This capitalization is **editorial shorthand, not a legal definition**: artifacts can themselves constitute legally probative digital evidence. Agency documentation and court terminology take precedence.

## Publish quality gate

A page can be marked `published` in the registry only after:

- [ ] Clear intended reader (collector or examiner) and task.
- [ ] Authority, safety, scope and risk notes appropriate to the procedure.
- [ ] Commands or procedures reviewed for **actual support** on applicable OS/tool version.
- [ ] Invented examples plainly labeled, with explanations of fields and investigative significance.
- [ ] Explicit limits: what the artifact/result does *not* establish; relevant clock issues.
- [ ] **Terminology and bias check:** follow [Evidence/artifact/evidence distinctions](TERMINOLOGY.md), document hypotheses and reasonable competing explanations, and include contrary or exculpatory observations instead of only artifacts supporting a preferred story.
- [ ] Evidence integrity, handling or custody instructions where applicable.
- [ ] **Published best-practice baseline:** for operational recommendations, consult relevant current published professional/standards-body or government guidance (e.g., SWGDE, ANSI/ASB, NIST, NIJ, USFA/OSHA/PHMSA where safety or transport matters). Attribute technical claims accurately; don't invent citations or imply a best practice is law.
- [ ] **Source ledger on substantive field procedures:** include document title, **ID/version/date**, publisher, applicable device/task and link to the publisher. State any scope/edition limits and verify whether a newer edition supersedes it.
- [ ] **Safety hierarchy and conflicts:** record when sources apply to **different device types** or their recommendations differ. Never silently transpose phone wet-handling guidance onto drives, or prioritize forensic access over active safety risks.
- [ ] Official links/reference material and no case, credential, or protected data.
- [ ] Internal links and Docsify/mobile display checked.
- [ ] A meaningful landing page exists before publishing a new **top-level** section.
- [ ] Any reviewer feedback addressed; version/update date recorded for fast-changing guidance.

**Reference-review protocol:** Before writing, identify the actual current version via the issuing body's website. Use direct, stable publisher links (not PDF files redistributed into this repo); cite sections when material. Include date last checked, whether publication is an approved standard/recommendation rather than a law, and any training/specialist boundary. If source support cannot be verified, keep the item as a question for examiner review rather than a directive.

**Publication protocol:** Draft on feature branch → validate → merge documentation → set status `published` → regenerate sidebar → check → deploy. This is a publishing convention, not an access-control mechanism.

## URL and naming policy

- Retain existing public paths and links wherever possible; redirect or update on deliberate moves.
- Folder and file names: descriptive `lower-kebab-case.md`; one subject/one responsibility.
- Avoid dates in permanent page URLs; include last validated date *within content* where needed.
- Keep main navigation limited to mature categories; use deep pages and index links beneath them.

## What is intentionally *not* locked down

Exact future leaf-page names, tool choices, and procedure details will evolve with technology and examiner feedback. The **taxonomy and publication gates** are the stable foundation, not a freeze on forensic practice.

[Roadmap and section-by-section passes](ROADMAP.md)
