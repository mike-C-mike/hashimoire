# Digital Evidence — Packaging, Custody & Examiner Handoff

**Audience:** field collectors | patrol officers | investigators | evidence technicians  
**Use case:** final scene check | packaging | transfer | lab readiness  
**Risk:** caution  
**Guidance reviewed:** 2026-10-23

> **This page is a handoff decision checklist**, not an agency evidence form or authority to collect beyond your case scope. Physical handling, digital preservation, chain of custody and hazardous-device procedures follow your organization's SOP and the examiner's direction.

> **UNSAFE EVIDENCE HANDOFF:** Never treat a leaking, swollen, smoking or overheated battery as an ordinary sealed-bag exhibit. The [damaged-device guide](damaged-devices.md) identifies required specialist escalation and the need for a qualified transport plan. Alert the receiving property room/lab **before arrival**.

## Before you leave the scene — 60-second checklist

- [ ] **Identify every item** uniquely and tie it to its original location, photographs and incident authority.
- [ ] If CSU is absent or delayed and interim scene photographs were authorized, retain the **outside-in unmarked series**, later marker/scale views and photograph log; document why the officer performed this work instead of CSU.
- [ ] Record how it was found: **on/off, locked/unlocked, screen visible, connected/disconnected, attached cables/media**, where applicable.
- [ ] Record **who made every intervention** (power, network, disconnection, packaging, export, charging, settings) and when, with timezone.
- [ ] Note whether physical traces (latent prints, DNA, toolmarks) require coordination **before digital examination**.
- [ ] Preserve device/accessory relationships; avoid mixing unlabeled loose cards or similar USB drives.
- [ ] Confirm any **powered-on or hazardous-device** transport requirements with trained personnel rather than applying ordinary sealed packaging.
- [ ] For CCTV/cloud evidence: confirm the **actual hold/export status**, retention deadline, camera/time scope and whether files were secured—not just viewed.
- [ ] Document custody transfer details and tell the examiner what remains urgent or unresolved.

## Match packaging and transport to the evidence

| Item or condition | Packaging/handoff priority | Stop or escalate if |
| --- | --- | --- |
| **Powered-off phone / computer** | Preserve state and physical condition; protect from accidental power-on and damage as agency SOP permits. | Contaminated, wet, swollen or hot battery. |
| **Powered-on phone / laptop** | Obtain examiner-approved cooling, power, isolation and transport plan; document deviations. | Access state may be lost, remote-wipe risk, unsafe handling. |
| **USB / memory card / external disk** | Protect contacts/connectors, label individually and associate adapters/cables; keep disconnected. | Attached to a live computer, damaged or encrypted/unlocked. |
| **CCTV / cloud export** | Secure original/natively exported files, related player/sidecars and approved dataset hashes; log export origin. | Viewing link expires, incomplete coverage, missing files, retention window imminent. |
| **Multiple devices at one scene** | Separate identifiable evidence items; record what was connected or near each other before movement. | Similar items could be confused or mixed. |

**Anti-static packaging** can be appropriate for some disconnected components. **Radio-frequency isolation** may be necessary for certain mobile devices. These are different controls; no single bag type is appropriate for every situation. Always follow approved handling and hazardous battery rules.

## Chain of custody is a sequence, not one signature

A useful custody record answers: **Who had the item, where was it, when was it transferred, what condition was it in, and what happened to it?**

Record each transfer contemporaneously according to your agency's process, including date, time/timezone, sender, receiver, item ID, seal/condition and any exception. When a digital dataset is exported separately from a physical recorder or phone, record its source, creator, original destination and association with the case.

Do not assume a file hash replaces custody documentation. A hash comparison speaks to the tested bytes; it does not independently establish lawful collection, context or completeness.

## What a receiving examiner actually needs

| Handoff question | Give the specific observation |
| --- | --- |
| **What is this?** | Item ID, make/model or source system, outward identifiers, physical accessories. |
| **Where and how found?** | Original location, photographs, associated devices, power/lock/connected state. |
| **What was changed?** | Every touch, disconnect, shutdown, radio action, charging, export, preservation hold, who authorized it. |
| **What timeline?** | Local time and timezone for scene events, independent reference clock and any device clock discrepancy. |
| **What's urgent?** | Unlocked phone, running encrypted computer, pending remote wipe, unsafe battery, recorder overwrite deadline. |
| **What's available?** | Device(s), photographs, evidence record, native video/export files, viewers/sidecars, hash manifests where applicable. |
| **What is missing?** | No recovery access confirmed, incomplete export, unknown camera, unidentified connected drive, unavailable witness contact. |

### Fictional handoff — physical device

```text
Item: 005 — black USB flash drive, printed 32 GB
Original location: west desk drawer, scene photo 18
Found: disconnected; no file access or power applied
Connections: none observed; no associated computer asserted
Handling: photographed, contacts protected, sealed under agency SOP
Collector: Officer A, 2026-10-23 11:08 CDT (-05:00)
Transferred to: Evidence Technician B, 11:36 CDT
Concerns: housing cracked, no further manipulation attempted
```

### Fictional handoff — digital video export

```text
Item: 006 — business DVR native video export
Source: lobby camera CAM-02, requested 14:00–14:45 local
Time note: recorder displayed 4 min slow vs independent reference
Hold: custodian confirmed at 15:10 local; known overwrite not yet reached
Native export: .vendor bundle, companion viewer and index files
Files transferred: evidence-storage location recorded in agency system
Hash: per-file SHA-256 manifest created by authorized export operator
Limits: other camera CAM-03 unavailable; follow-up requested
```

**These examples are invented.** Preserve actual case details only in approved systems—not Hashimoire, GitHub issues or a public form.

## Useful examiner notification script

> “I've collected Item 003, a laptop found running and unlocked. I photographed the screen and all attachments without navigating. There is an attached external drive. No power or network changes have been made. Please advise whether live collection is needed before we disconnect anything.”

This is deliberately a **state report**, not an unsupported assessment of file contents.

## Don't let these details disappear

1. **Found-state versus received-state:** clearly separate what the initial collector saw from what a later examiner observed.
2. **Original versus copy:** distinguish a physical device, forensic image, native video export, converted video preview and cloud-viewing link.
3. **Time standards:** document timezone, any daylight-saving context and measured device-clock discrepancies instead of silently “correcting” device times.
4. **Exceptions:** incomplete export, damaged item, unavailable accessories, emergency safety intervention or missed photograph should be documented, not concealed.
5. **Urgent follow-ups:** a pending overwrite deadline or inaccessible encryption key is part of the handoff, not a detail to discover days later.

## Related field guides

- [Interim scene triage and outside-in photography — no CSU or delayed CSU only](scene-documentation.md)

- [Damaged-device response and specialist handoff](damaged-devices.md)
- [Smartphone and tablet preservation](mobile-device-collection.md)
- [Computer and laptop preservation](computer-collection.md)
- [USB, SD card and removable storage collection](removable-media.md)
- [CCTV and cloud video preservation](video-preservation.md)
- [SWGDE 18-F-002-2.0 — Best Practices for Digital Evidence Collection](https://www.swgde.org/documents/published-complete-listing/18-f-002-2-0/)

[← Field Collector hub](README.md)
