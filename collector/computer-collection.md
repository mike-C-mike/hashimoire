# Computers & Laptops — Field Preservation

**Audience:** field collectors | patrol officers | investigators  
**Use case:** live/off decision | connection documentation | preservation | handoff  
**Environment:** Windows | macOS | Linux | workstations  
**Risk:** caution  
**Guidance reviewed:** 2026-10-23

> **A powered-on computer is not the same as a powered-off computer.** Shutting it down may destroy volatile evidence and access to unlocked encryption; touching a live system may also alter evidence. If it is powered on, asleep, or its state is uncertain, **document what you see and consult the examiner/incident lead before changing power or network connections**. Follow legal authority, agency policy and safety priorities.

> **DAMAGE OVERRIDE:** Battery swelling, smoke, unusual heat/odor, leaking fluid or other hazards **override** ordinary live-system power preservation. Do not charge, bag or transport an unsafe device as routine evidence. Follow the [damaged-device response guide](damaged-devices.md) and specialist/safety direction.

## First 60 seconds

- [ ] Establish authority to collect or preserve the specific machine and related media.
- [ ] Photograph **the full setup as found**: display, open applications, laptop lid, cables, drives, docks, network connections, nearby phones and accessories.
- [ ] Record independent **date/time/timezone**; photograph visible computer clock if already on screen, without unlocking or navigating.
- [ ] Record what is **visibly** known: on and logged in, on and locked, apparently asleep, off, or uncertain. A black screen is not proof of shutdown.
- [ ] Identify hazards and operational impacts (overheating, damage, production server, medical/safety systems, school services).
- [ ] **Do not** restart, shut down, log off, close a laptop lid, detach an attached drive, unplug power or execute commands just to “check” the machine.
- [ ] Request examiner/incident-lead direction for any live system; arrange controlled custody and transport.

## Choose the actual state

| What you observe | Collector's immediate priority | Avoid |
| --- | --- | --- |
| **OFF, confirmed** | Leave off. Photograph connectors and power state, package and transfer under SOP. | Booting it to identify user/OS or test whether files exist. |
| **ON and logged in / unlocked** | Urgently notify examiner. Preserve the current state pending a controlled live evidence plan. | Locking, logout, reboot, casual browsing or closing a laptop lid. |
| **ON and locked** | Document the lock screen and visible indicators; escalate power, encryption and network decisions. | Guessing passwords, changing settings or force-shutdown. |
| **Screen dark / possibly asleep** | Treat state as **unknown** until trained personnel assess. Photograph power LEDs and connected peripherals. | Pressing keys or removing power merely to identify state. |
| **Connected external USB/drive** | Document cable, port, and connected device IDs; keep association; call examiner. | Ejecting/removing before assessing running system and mounted encryption. |
| **Shared / enterprise / server** | Notify responsible operator and incident lead; preserve service and network dependencies. | Unplanned shutdown, disconnecting shared storage or isolating a critical production host. |
| **Damaged or hazardous** | Prioritize safety/other forensic disciplines and specialist handling. | Applying power or packing unsafe batteries/contaminated devices as ordinary evidence. |

### Why does “leave on / leave off” matter?

A live machine may contain volatile **RAM**, running processes, network connections, open or mounted encrypted volumes, authentication context and temporary data. Rebooting or powering down may make those irretrievable. On the other hand, allowing continued activity can also change data or permit remote interference. There is **no universal one-button choice**. The examiner and authorized response lead weigh these factors, legal scope, preservation urgency and safety.

If the device was truly off when found, the routine collector approach is to **leave it off** rather than start it for identification.

## Computers with encryption

Encryption products include BitLocker, FileVault, LUKS and third-party full-disk solutions. A disk that is accessible while a computer is running may be locked after shutdown.

**Collector responsibilities:**

1. Report whether the device was on, logged in, locked and connected to power.
2. Avoid a needless restart before the examiner can decide on live acquisition and protected recovery material.
3. Do not search for recovery keys, disable encryption, change protectors, or move secrets into ordinary notes.
4. If recovery information is voluntarily/lawfully provided, route it through **approved protected evidence or credential handling**, with associated authority and custody records.

Examiners can consult [BitLocker recovery readiness](../snippets/powershell/bitlocker-recovery-readiness.md). That technical procedure is **not a collector field task**.

## Connection and network decisions

Before touching cables, photograph the backs/sides of the device, the exact ports and attached peripherals. A removable drive could contain critical evidence; a network link could be used for remote wiping or could support necessary business operations.

- **Do not assume pulling Ethernet or disabling Wi-Fi is harmless.** It may disrupt services, alter running processes or interfere with approved live collection.
- **Do not leave a suspected active attacker situation unreported.** Notify the qualified response lead immediately about destructive activity or credible remote interference.
- **Document the initial connected state** and who ordered any subsequent isolation, when it happened, and what changed.
- **Avoid plugging in a found USB** or attaching an unvalidated acquisition kit without training and authorization.

## Physical evidence and accessories

- Preserve the physical relationship between laptop, dock, charger, external drives, cards, wireless receivers and devices found beside the computer.
- Identify installed and connected peripherals from the **outside**. Opening housings or removing drives is an examiner/evidence-lab decision.
- If fingerprints, biological evidence or toolmarks matter, coordinate examination order before cleaning or disassembling.
- Label separate items distinctly, keeping the association documented.
- For a powered-on device being transported, seek an examiner-approved power, cooling, isolation and packaging plan before movement.

## Handoff example (fictional)

```text
Item: 002 — laptop and charger (separate associated item 002A)
Found: office desk, screen showing unlocked Windows desktop
Observed at: 2026-10-23 09:16 CDT (-05:00)
Visible: desktop clock reads 09:13; no typing or file exploration
Connections: wall power, HDMI display, USB external drive Item 003
Photos: scene 07–13, ports and attachment close-ups
Changes: none; examiner notified 09:19, live response directed 09:22
Disposition: awaiting trained examiner; not rebooted or disconnected
```

This sample shows what the **collector saw and did**, not what was found on the computer. Do not use fictional case references as real evidence records.

## Mistakes that are hard to undo

1. Shutting down an **unlocked encrypted** computer before collecting volatile evidence or assessing access.
2. Booting an off computer just to see which user owns it.
3. Treating an apparently sleeping laptop as powered down and removing its battery/power.
4. Unplugging external media from a live system without recording whether it was mounted.
5. Providing a computer to the examiner with no photographs of ports, peripherals, state or changes made.

## Questions to answer before transfer

- What was the power, lock, screen and connection state when first seen?
- Who had authority over any isolation, reboot, shutdown or live-collection choice?
- What drive, card, docking station, charger or other accessory was attached?
- Were there safety/operational, remote-wipe, encryption or cloud-storage concerns?
- What was changed and what remained unexamined?

## Related guidance and references

- [Damaged and hazardous digital devices](damaged-devices.md).
- [Removable media collection](removable-media.md).
- [Evidence packaging and handoff](evidence-handoff.md).
- [Examiner: rapid evidence collection](../playbooks/acquisition/0-rapid-evidence-collection.md).
- [SWGDE 18-F-002-2.0 — Best Practices for Digital Evidence Collection](https://www.swgde.org/documents/published-complete-listing/18-f-002-2-0/).

[← Field Collector hub](README.md)
