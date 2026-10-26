# Hashimoire — Depth-First Content Roadmap

**Planning baseline:** October 2026  
**Method:** Stable navigation + one high-quality section per development pass. No publication for empty categories.

## Strategic direction

**First priority: mobile devices and Windows.** The site should become particularly useful for an officer holding an actual phone at a scene and an examiner opening a Windows laptop in the lab. Mac, Linux, cloud and niche devices follow once those primary workflows are deep enough to be reliable.

Every pass should produce **operationally coherent coverage**—not merely ten more one-paragraph pages. Each published page must help answer: *what to do, what output to expect, why it matters, and what to document*.

## Pass 0 — Architecture and quality controls (established)

- [x] Role selection: Field Collector / Forensic Examiner.
- [x] Expandable left-hand navigation.
- [x] Windows forensic snippet foundation and example outputs.
- [x] Establish top-level categories and hidden future-section registry.
- [x] Validate sidebar generator and link checks in pull requests.
- [x] Establish the content quality/promotion checklist.
- [ ] Establish last-reviewed metadata conventions without burdensome boilerplate.

**Exit:** Navigation structure decided; new sections can be planned invisibly and promoted safely.

## Maintenance gate — repair existing content before expanding (completed structurally)

- [x] Identify the empty OSINT index and malformed published workflows.
- [x] Rebuild existing OSINT domain, username, metadata, exposure and safety references rather than adding categories.
- [x] Repair truncated hashing and Volatility Markdown and refresh tool-install guidance.
- [x] Run and clear automated published-content audit across the existing repository (55 Markdown pages, 0 structural errors/warnings in the prior repair pass).
- [ ] Review live Docsify rendering and OSINT route navigation on mobile and desktop.
- [x] Resume Collector depth work after the existing published pages passed the automated structural checks.

**Scope decision:** offline support is intentionally deferred; a phone home-screen shortcut is sufficient for the current release.

## Pass 1 — Field Collector: scene preservation depth (active)

**Published work (October 2026):**

- [x] A full [smartphone/tablet](../collector/mobile-device-collection.md) power-state guide: off, locked, unlocked, uncertain, damaged, isolation and transfer.
- [x] Deepened [computer/laptop](../collector/computer-collection.md) live-state, encryption and connected-storage decisions.
- [x] Created [USB/SD/removable media](../collector/removable-media.md) field preservation guidance for loose versus live-attached storage.
- [x] Created [CCTV/DVR/cloud-video](../collector/video-preservation.md) preservation guidance focused on retention urgency, clock discrepancies, native export and verification.
- [x] Expanded [evidence packaging/handoff](../collector/evidence-handoff.md) with custody, safety, synthetic examples and examiner-ready reports.
- [x] Reworked the [Collector hub](../collector/README.md) as a eight-situation, one-click decision index.
- [x] Added [Interim Scene Triage & Photography](../collector/scene-documentation.md) **only** for departments without CSU or urgent documentation ahead of delayed CSU. Covers safety/perimeter, entry control, outside-in overall/midrange/close-up, original unmarked views, later visible ID markers and properly aligned scales, image integrity and specialist handoff.
- [x] Added [Damaged & Hazardous Digital Devices](../collector/damaged-devices.md), grounded in SWGDE 14-F-004-1.1 (2016 mobile), 14-F-002-2.0 (2025 storage), 18-F-003-2.0 (2025), USFA/OSHA battery safety and PHMSA transport; clear stop conditions, wet-device scope distinctions and specialist handoff.
- [x] Built [Cloud & Account Evidence Preservation](../collector/cloud-preservation.md): immediate account/item identifiers, expiring evidence, provider vs. enterprise custodian, 18 U.S.C. §2703(f) preservation vs. production and renewal, emergency legal escalation, internal referral worksheet and examiner verification; references SWGDE 23-F-004-1.1 (2025) and 18-F-002-2.0 (2025).

**Next potential refinements—not automatically new pages:**

- [ ] Field test guide readability with officers on common mobile screen sizes and ask where uncertainty remains.
- [ ] Verify live-site Docsify rendering, preservation checklists, and external references after deployment.
- [ ] Have CSU/scene-trained personnel review the interim-photography guide against local SOP, scene safety and marker/scale contamination controls.
- [ ] Review vendor-specific CCTV/cloud workflows **only** with current source documentation; leave uncertain capabilities out.
- [ ] Agency counsel/investigator review of the cloud provider preservation/production distinctions and internal referral protocol; verify current provider contact channels when used.
- [ ] Periodically recheck mobile OS behavior, agency SOP fit and SWGDE guidance.
- [ ] Have fire/hazmat and damaged-media recovery personnel review the hazardous-device handling article and local evidence-transport SOP.
- [x] Add a **mandatory current published best-practice source ledger** and scope-conflict check to the [architecture quality gate](ARCHITECTURE.md).

**Exit:** Eight common collector situations lead directly to actionable field guidance, without empty clicks. New public articles require user value, current references and review.

## Pass 2 — Windows Examiner: field-to-lab evidence (active)

**First depth pass — October 26, 2026:**

- [x] Published a complete [Windows Examiner execution-evidence hub](../docs/windows/README.md), linked to already-published collection and command references.
- [x] Published [execution evidence: Prefetch, Amcache, Security 4688 and Sysmon](../docs/windows/execution.md) with maintainer-documented parser options, synthetic outputs, source coverage, provenance, and **what each artifact cannot prove**.
- [x] Published a [worked PID-to-network intrusion timeline](../docs/windows/timelines.md), including hexadecimal PID conversion, XML-by-name field parsing, ProcessGuid event correlation, UTC normalization and constrained report wording.
- [x] Exposed **Windows Artifacts & Timelines** in the sidebar only with these **three genuinely useful pages**. Registry, browser and filesystem topics stay **unpublished and hidden**.
- [x] Linked deeper examiner pages from existing Windows snippets, Examiner hub and homepage.

**Still to develop in this workstream:**

- [ ] Windows registry and artifact examination beyond Amcache/ShimCache (UserAssist, USB, BAM, services, logon context).
- [ ] Browser artifacts and user-activity correlation; validation of examiner tools on current Windows builds.
- [ ] Filesystem/$MFT, USN and Volume Shadow Copy contextual timelines.
- [ ] RAM acquisition/Volatility deeper examples; BitLocker/field-to-lab encryption continuity.
- [ ] Field/lab reproduction on validated Windows images and peer review of exact parser outputs and timestamp semantics.

**Publishing standard:** One investigated question, collection scope, tool commands, **synthetic output**, interpretations, limitations and relevant SWGDE/official references **before** the page appears publicly. Never publish empty registry/browser/MFT pages simply to fill the submenu.

## Pass 3 — Mobile Examiner: iOS and Android

- Evidence intake, initial power/lock/encryption state and scope.
- Acquisition types and capabilities/limits, with current platform/tool compatibility noted.
- iOS and Android system/app artifacts; handling backups, exports and timestamps.
- Artifact verification against original extraction and reporting limitations.
- Clear separation between what a collector does and examiner-only actions.

**Exit:** A coherent mobile examination handbook and artifact references. Then expose the **Mobile Device Forensics** section.

## Pass 4 — Case quality, video evidence and repeatable reporting

- Chain-of-custody, collection logs, validation checklists and hashes.
- Court-ready report structure, tool transparency, negative findings and limitations.
- CCTV export integrity/retention, playback, timestamps and evidence package handling.
- Document templates and synthetic worked case for training.

**Exit:** Evidence-to-report workflow, reviewed against relevant professional guidance. Promote reporting and video sections **only when each has a usable hub**.

## Pass 5 — macOS and Linux foundations

- macOS: disk encryption/APFS, safe acquisition, logs, user activity, validation.
- Linux: safe live triage, storage, journald/system logs, user context, filesystem evidence.
- Each OS gets a tested baseline workflow, artifact examples, and a note on tool/OS compatibility.

**Exit:** Two self-contained introductory reference sections, published individually when ready. Do not rush for symmetry with Windows.

## Pass 6 — Broaden based on real use

- Cloud, identity and SaaS records.
- Network/email/log analysis and detections.
- External/removable storage and niche devices.
- Authorized OSINT, tool validation labs and training examples.
- Feedback-driven topic selection from frequent forensic tasks.

## Small-passes operating rhythm

For **each** topic:

1. Define scope, target user, incident question and authoritative references.
2. Write one complete core page and linked quick-reference material.
3. Add synthetic output, explain fields, caveats and cross-artifact verification.
4. Run command/OS/tool compatibility checks using a test machine or vetted sources.
5. Verify mobile readability, links, safety and navigability.
6. Mark complete pages `published`, regenerate sidebar, merge and review on the live site.
7. Move to the next page in that topic—not the next operating system—until coverage is useful.

## Work intake and prioritization

Pick the next topic based on **field frequency × risk of evidence loss × investigative value × validation readiness**. A BitLocker recovery guide or phone preservation flow outranks a fashionable but low-use feature.

Keep actual case data and sensitive operational details out of the repository, even when pages are omitted from navigation.

[Architecture and navigation contract](ARCHITECTURE.md) · [Navigation registry](../site/navigation.json)
