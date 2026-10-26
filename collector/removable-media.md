# USB Drives, SD Cards & Removable Storage — Field Collection

**Audience:** patrol officers | investigators | evidence technicians  
**Use case:** collection | preservation | transport | handoff  
**Risk:** caution  
**Guidance reviewed:** 2026-10-23

> **Field collector rule:** A drive that looks harmless may contain relevant data, malware, encryption or fragile hardware. **Do not insert found media into a computer to identify its contents.** Document what you see, protect the item's condition and hand it to an examiner. This guide supplements legal authority, training and agency SOP.

> **KNOWN-DAMAGED STORAGE:** SWGDE **14-F-002-2.0 (Mar 4, 2025)** warns that routine imaging or energizing failed/failing media may destroy evidence. Before testing a dropped, wet, fire-exposed or malfunctioning drive, follow the [damaged-media preservation guide](damaged-devices.md) and consult qualified recovery personnel.

## First 60 seconds

- [ ] Confirm the item's authorized collection scope and physical safety. Photograph **in place** before moving it.
- [ ] Record where it was found and whether it was **connected to a powered-on device**, unplugged, loose, damaged or exposed to liquid.
- [ ] If connected to a live computer, **do not unplug it yet**: document the connections and call the examiner before changing the system's state.
- [ ] If disconnected, **leave disconnected**. Do not test it, browse files, power it up or try a password.
- [ ] Photograph both sides and any printed make/model, capacity, serial or distinctive features without opening the device.
- [ ] Keep matching adapters, card readers, cables and cases associated with the item; record each separately.
- [ ] Package securely using an agency-approved method suited to its size and condition; begin or maintain custody records.

## Choose the situation

| What you found | First collector action | Avoid |
| --- | --- | --- |
| **Loose USB flash drive, SD or microSD** | Photograph, identify without opening/connecting, protect contacts, package and log custody. | Inserting into a workstation or phone to see what's on it. |
| **External USB HDD or SSD, unplugged** | Record enclosure, labels, attached cable and physical condition. Keep it unpowered. | Connecting power or opening the enclosure to identify the drive. |
| **Storage connected to a running computer** | Photograph the full setup and note visible applications; contact examiner for live/volatile evidence plan. | Pulling cable, unmounting/ejecting, shutting down, or browsing contents. |
| **Encrypted or password-protected media** | Preserve media, label and any *lawfully supplied* recovery information using protected case storage. | Guessing passwords or attempting repair, initialization or formatting. |
| **Damaged, wet or overheating media** | Prioritize safety and contamination/trace-evidence coordination; escalate. | Drying with heat, powering it, cleaning contacts or opening housing. |
| **Multiple similar cards/drives** | Assign distinct item identifiers; photograph each original location and relative placement. | Mixing devices or placing them loose in one bag. |

### Why a connected drive is different

A computer may be writing to an attached drive, have a mounted encrypted volume, or hold open files, process artifacts and credentials that are lost when power or connections change. Whether to disconnect it is part of a **live-system collection decision**. Use the [computer collection guide](computer-collection.md) and contact an examiner rather than improvise.

### Why an unused SD lock tab is not a write blocker

The physical switch on many full-size SD cards is a **write-protect request** interpreted by the reader, not a universal guarantee that the media cannot be written. MicroSD cards typically lack that tab. Likewise, choosing a file explorer's “read only” mode does not provide validated forensic write protection. **Qualified examiners** should select and validate appropriate write-blocking/acquisition methods for the interface and device.

## Before packaging

1. **Scene context:** photograph the item near relevant computers, recorders, phones, adapters or written notes. Do not access files just to build context.
2. **Identify from exterior:** note USB-A/USB-C, full-size SD/microSD, external SSD/HDD, card reader, unusual connector, visible capacity and labels. Do not infer actual storage size from printing alone.
3. **Trace evidence:** where prints, DNA or other physical evidence may matter, coordinate examination order with the relevant specialist **before** destructive or contaminating handling.
4. **Preserve accessories:** include linked charger, power adapter, dock, original cable or case **when relevant**, documenting which item was connected to which port.
5. **Protect against damage:** use appropriate anti-static or protective packaging when the device/media warrants it; protect exposed contacts and avoid bending cards or crushing connectors. Follow evidence-room rules for seals.
6. **Special cases:** swollen batteries, wet devices, unknown hazardous electronics or active overheating require trained handling, not routine sealed-bag storage.

## Examiner handoff — information worth collecting

| Field | Example of a useful note |
| --- | --- |
| Item and location | “Item 004, black USB-A flash drive, left desk drawer, photograph 12.” |
| Found state | “Disconnected, no indicator illuminated; no power applied by collector.” |
| Association | “Located next to laptop Item 003; no connection observed.” |
| Exterior identity | “Example brand, printed 64 GB, partial serial visible, connector photographed.” |
| Changes made | “Moved with clean gloves to approved protective holder; no computer connection.” |
| Custody | Collector, seal/item label, date/time with timezone, each transfer. |
| Potential complications | Possible encryption, damaged housing, contamination or specialized connector. |

**Fictional example only:** “At 09:42 CDT, Item 004 (microSD card) was photographed inside an unconnected adapter. No device accessed its contents. The adapter and card were labeled as associated components; transferred to evidence at 10:15 CDT.” Do not use sample case data as real documentation.

## Five expensive mistakes

1. Connecting unknown media to an ordinary computer and triggering writes, synchronization, malware or an automated repair prompt.
2. Disconnecting live-attached storage before consulting the examiner, potentially losing access to an unlocked volume.
3. Formatting, initializing, running `chkdsk`, or using a recovery wizard on the original.
4. Treating an SD card's plastic lock tab or ordinary USB hub as verified forensic write blocking.
5. Losing an item's original location, interface/cable association, label or chain-of-custody information.

## What happens in the laboratory?

An examiner may document the device's physical/firmware identifiers, select compatible **validated write blocking**, image the in-scope source, verify acquired data with hashes, and examine a forensic working copy. The collector's job is to preserve the **source and its context**, not perform a quick file check.

## Related guidance and sources

- [Damaged media and hazardous devices](damaged-devices.md).
- [Computer and laptop collection](computer-collection.md) — live systems and connected drives.
- [Evidence packaging and handoff](evidence-handoff.md).
- [SWGDE 18-F-002-2.0 — Best Practices for Digital Evidence Collection](https://www.swgde.org/documents/published-complete-listing/18-f-002-2-0/).
- [NIST OSAC Lexicon — Write Blocker](https://www.nist.gov/glossary-term/41206).

[← Field Collector hub](README.md)
