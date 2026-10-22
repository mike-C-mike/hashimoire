# Hashimoire — Depth-First Content Roadmap

**Planning baseline:** October 2026  
**Method:** Stable navigation + one high-quality section per development pass. No publication for empty categories.

## Strategic direction

**First priority: mobile devices and Windows.** The site should become particularly useful for an officer holding an actual phone at a scene and an examiner opening a Windows laptop in the lab. Mac, Linux, cloud and niche devices follow once those primary workflows are deep enough to be reliable.

Every pass should produce **operationally coherent coverage**—not merely ten more one-paragraph pages. Each published page must help answer: *what to do, what output to expect, why it matters, and what to document*.

## Pass 0 — Architecture and quality controls (current)

- [x] Role selection: Field Collector / Forensic Examiner.
- [x] Expandable left-hand navigation.
- [x] Windows forensic snippet foundation and example outputs.
- [ ] Freeze top-level categories and hidden future-section registry after review.
- [ ] Validate sidebar generator and link checks in pull requests.
- [ ] Establish the content quality/promotion checklist.
- [ ] Establish last-reviewed metadata conventions without burdensome boilerplate.

**Exit:** Navigation structure decided; new sections can be planned invisibly and promoted safely.

## Pass 1 — Field Collector: mobile evidence (first content depth pass)

- On/off, locked/unlocked and visible state: first-contact decisions.
- Photographs and scene documentation; what *not* to touch.
- Network isolation and RF containment options, failure modes and battery tradeoffs.
- Handling unlocked devices, risks of reboot/power-down and escalation.
- Charging, damage, overheating, moisture and transport safety.
- Packaging, power/isolation state, custody and prompt examiner handoff.
- Short phone-friendly decision tree and 60-second checklist; reviewed against official mobile evidence guidance.

**Exit:** Field collector can make a defensible initial-preservation decision and get the device to an examiner without needing examiner-level instructions. Publish the first new collector subpages only after review.

## Pass 2 — Windows Examiner: field-to-lab evidence

- Live collection and order of volatility with a documented stop/shutdown decision.
- BitLocker state, recovery protector handling, approved escrow and lab access checks.
- Memory acquisition and Volatility 3 lab interpretation.
- Disk layouts, image formats, hashing, write-blocker scope and handoff.
- Registry, USB, PowerShell, event log, execution and browser artifacts.
- Timelines and correlation: PID/PPID, creation events, network connections, user context.
- Worked **synthetic investigation** demonstrating alternative explanations and confidence limits.

**Exit:** One end-to-end Windows workflow, with meaningful collection and analysis links and validated example outputs. Then expose the **Windows Artifacts & Timelines** section.

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
