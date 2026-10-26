# Damaged & Hazardous Digital Devices — First-Responder Preservation

**Audience:** authorized field collectors | patrol officers | investigators | evidence technicians  
**Use case:** initial safety assessment | damage documentation | specialist escalation | safe handoff  
**Environment:** smartphones | tablets | laptops | HDD/SSD | USB/SD media  
**Risk:** **HIGH — battery, electric shock, chemical, fire, contamination and evidence-loss hazards**  
**Sources reviewed:** October 26, 2026

> **STOP: personnel safety and incident command take precedence over digital evidence.** If a battery is **smoking, hissing, swelling, leaking, emitting an unusual odor, very hot, punctured, or burning**, do **not** charge, power on, touch, move, bag or transport it as routine evidence. Keep people away, follow scene/emergency procedures and request a qualified fire/hazmat/battery responder. A phone's unlocked state does **not** justify exposing anyone to a battery hazard. [USFA battery safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/batteries/) · [OSHA battery-response controls](https://www.osha.gov/lithium-ion-battery-safety/control)

> **WHO THIS IS FOR:** Authorized first responders or collectors encountering *damaged* evidence, including an officer at a department without a specialized collection capability, or an officer securing a changing scene until qualified personnel arrive. **Not a repair, drying, data recovery, or battery-disassembly guide.** Apply agency SOP, lawful authority and relevant safety/transport requirements.

## First 60 seconds — observe, protect, notify

- [ ] **Make the area safe first.** Address people, fire, chemical exposure, traffic, electricity and scene access. Do not risk injury to keep a device unlocked.
- [ ] From a safe position **photograph the item as found** and its surroundings; if CSU is available and the scene is stable, preserve it for CSU rather than performing unnecessary scene processing. See [interim scene guidance](scene-documentation.md).
- [ ] Record **what happened** (drop, water, fire, crushing, chemical exposure, unknown), **when**, **who reported it**, and what you personally observed. Don't convert a witness theory into a confirmed cause.
- [ ] Observe **smoke/odor/heat/swelling/leakage/cracks/exposed circuitry/contaminants**. Do not bring your face close to investigate smells or heat.
- [ ] **Do not plug in, charge, restart, connect to a computer, perform a “quick check,” shake, dry with heat, open housings or run disk repair.**
- [ ] Record whether it was **already powered on or off**, and any screen/indicator visible *without touching it*.
- [ ] Contact the proper **safety responder** if active hazard is possible and the **digital examiner/data-recovery specialist** for evidence decisions. Tell the receiving lab about damage **before** delivery.
- [ ] Follow an **approved packaging, transport and custody plan** suited to the actual damage; ordinary evidence bags may be unsafe.

## Decision table — different damage, different response

| What you encounter | Collector priority | What you must **not** improvise |
| --- | --- | --- |
| **Smoke, hissing, swelling, puncture, unusual odor or intense heat** | **Safety STOP.** Restrict access; alert fire/hazmat and supervisor; specialist determines response and movement. | Charging, cooling in an improvised way, touching/removing battery, sealing a hot device in evidence packaging, taking it in an ordinary patrol vehicle. |
| **Wet or previously submerged phone/tablet** | Note liquid **type**, source, depth/duration if known, observed power state; contact mobile-forensics specialist **immediately** for safe recovery/transport instructions. | Charging, booting, connecting data cable, rice, hair dryer, opening sealed phone, guessing that ordinary mobile power-preservation rules still apply. |
| **Wet HDD, SSD, NVMe, USB or SD media** | Do not energize or connect. Photograph, record liquid and time; contact a **damaged-media recovery specialist** before packaging/transport. | Powering on, imaging a failing drive, using a normal USB dock to test, assuming the mobile-device wet transport procedure applies. |
| **Dropped/crushed HDD or failing spinning disk** | Record fall/impact, noises already heard, power-on attempts already made, missing fragments; get recovery specialist direction. | Repeated boots, `chkdsk`, spinning it up for reassurance, opening its sealed chassis. |
| **Cracked, crushed, or fragmented phone / drive** | Preserve visible identifiers, original location, detached parts and nearby accessories **without causing further breakage**; coordinate examination order for prints/DNA. | Prying screens, bending boards, soldering, transferring memory chips or handling sharp/contaminated fragments without PPE/training. |
| **Fire, smoke, suppression chemical or extreme heat exposure** | Confirm scene released as safe by responsible personnel; document thermal and chemical exposure; notify examiner of water/foam/powder use. | Powering a device that looks intact, scraping soot off, washing contamination away or performing makeshift “cleaning.” |
| **Blood/biohazard or unknown chemicals** | Follow exposure-control/hazmat procedures; notify evidence custodian and qualified lab of contaminant before shipment. | Barehanded contact, wiping/sterilizing evidence to make it convenient to handle, mixing contaminated evidence with ordinary equipment. |

**Important nuance:** A cracked screen is not automatically a failing battery. Conversely, a device may have dangerous **internal** damage despite an intact exterior. Use observed hazard indicators and qualified assessment, not guesses.

## 1. Powered on when damaged — whose priority wins?

**Two preservation principles can conflict:**

- SWGDE **18-F-003-2.0 (Aug 21, 2025)** discusses preserving a powered-on phone's forensic access, since reboot or power loss can reduce available data.
- SWGDE **14-F-004-1.1 (Feb 8, 2016)** warns that **applying power to a damaged mobile device can increase damage**; handling may also expose collectors to electric shock or other hazards.

**Collector decision:** **Do not attempt to “save” an unlocked hazardous device by charging it.** Prioritize the safety response. If a damaged device is still powered on but **has no apparent active hazard**, obtain rapid examiner direction on power and access decisions **before any intervention**. When a decision is made, document safety reason, authority, actions, original and final state, timestamps and witnesses. The collector does not make a blanket rule that all damaged devices must stay on or all must be shut down.

## 2. Water exposure: why there is no universal packaging trick

You need to identify **what kind of device was wet**, **what the liquid was**, whether there may be an active battery or chemical hazard, and **who is qualified to receive it**.

- **SWGDE 14-F-004-1.1 (2016)** addresses **mobile devices** and describes specialized handling of submerged devices, including prompt lab delivery; its recommendations depend on device construction and hazard conditions.
- **SWGDE 14-F-002-2.0 (Mar 4, 2025)** separately addresses **hard disks, SSDs, NVMe, and NAND-based USB/SD storage**; it warns not to power liquid-damaged media and describes **different specialist-directed transport methods**.
- **These are not interchangeable.** Do not put a laptop, battery-powered phone and loose HDD into the same transport method, and do not copy a liquid-immersion or vacuum-packaging instruction from one device type to another without qualified direction.
- **No home remedies:** rice, ovens, hair dryers, compressed air, ad hoc solvents, or ordinary charging/power-up attempts can create new risk or alter evidence.

For a phone **found immersed**, document the liquid type and hazards, isolate people from any dangerous substance and **contact the mobile-forensics lab and safety responder for immediate, device-specific collection/transport direction**. Do not start a universal “keep it submerged” procedure yourself; a contaminated liquid and a compromised lithium-ion battery may require specialized treatment.

For **already-removed** wet media, minimize handling and arrange **prompt qualified handoff**, documenting who removed it, when and how it has been stored.

## 3. Dropped, crushed, clicking or “not recognized” storage

SWGDE **14-F-002-2.0 (2025)** specifically warns that conventional imaging on failed/failing storage **can destroy data**. An examiner should determine when specialized recovery is needed.

**Collector actions:**

1. Document if the device was dropped/crushed, who observed it, impact location, original packaging, cables and exact known power-on attempts.
2. Preserve fragments and identifiable boards/labels, protecting them from further damage and mixing; don't pull parts apart to look for a serial.
3. Report noises **already heard** (clicking, scraping, repeated spin-up) as observations—**do not power up to listen again**.
4. Tell the receiving examiner that the unit is **suspected damaged/failing**, so it is not put through an ordinary imaging workflow without review.

**Do not** open a spinning disk's sealed mechanism, swap circuit boards, run surface tests or try a generic “repair disk” wizard.

## 4. Heat, fire, chemical and battery safety

The **U.S. Fire Administration** and **OSHA** emphasize the risk from damaged lithium-ion batteries, including uncontrolled heat and harmful emissions. A device that has been in a fire may remain dangerous even if it is no longer visibly burning.

- **Escalate** swelling, smoke, hissing, heat, punctures, leaks and abnormal odor rather than experimenting with the device.
- **Do not** place a suspected unstable battery in a tight sealed evidence bag or near combustibles, evidence shelves or personnel.
- **Do not** apply a generic “put it in water / sand / saltwater / freezer” action. Emergency responders use hazard-specific protocols and equipment.
- **Do not** assume a typical evidentiary transport box is a compliant hazardous-material shipment.
- A **damaged, defective or recalled lithium battery** presenting a heat/fire/short-circuit risk can trigger special U.S. transport requirements (49 CFR 173.185(f)); have your agency's hazmat/transport authority determine the correct packaging, mode and documentation. This page is **not shipping instruction**. [PHMSA interpretation #24-0050](https://www.phmsa.dot.gov/regulations/title49/interp/24-0050)

**Transport is a separate decision from collection.** First determine it is safe to approach, then get an approved plan for movement and handoff. If the qualified plan requires specialist equipment, keep personnel away until that equipment arrives.

## 5. Protect physical as well as digital evidence

Surface damage does not prove data is unrecoverable, and cleaning can harm fingerprints, DNA, trace or digital components. Under **SWGDE 14-F-004-1.1** and **14-F-002-2.0**, coordinate traditional forensic needs with the investigator and lab **before** cleaning or disassembly.

- Photograph exterior damage, labels and the original location from safe positions (and follow the CSU-limited scene-photography rules if applicable).
- Don't peel tape, lift glass, remove broken components, wash soot, detach a swollen battery or open water-damaged housing.
- Preserve fragments as **distinctly identifiable associated items** if safe, including memory cards, printed labels, chargers and cables.
- For possible chemical/biological contamination, get PPE, packaging and handling instructions from trained personnel; protect the receiving lab from an unannounced exposure.

## 6. Examiner handoff — say what happened, not what you think failed

```text
Item / original scene location:
Authority / collecting unit:
Device type and externally visible identifiers:
Original powered-on / off / unknown state; visible screen if any:
Observed damage (exact location, smell/heat/leakage from safe distance):
Reported cause, source of report and whether corroborated:
Liquid/chemical name if known; time in liquid or heat if known:
Fire suppression agents or emergency treatment used:
Photos / scene log / fragments and associated accessories:
Prior attempts by anyone: boot, charging, connection, repair, drying, cleaning:
Responder/supervisor/lab consulted, time and instructions:
Known changes to condition; who made them and why:
Approved packaging and transport plan / qualified responder:
Custody transfers and receiving hazard notification:
Unresolved hazards or examination restrictions:
```

### Example — fictional, not a real incident

> “Item 03, tablet recovered beside a sink at 10:14 CDT. Water visible around the charging connector; device screen dark (power state **not determined**). No charging, unlocking or cleaning attempted. Exterior photographed before handling. Mobile-forensics examiner and evidence supervisor notified at 10:18; packaging followed the direction recorded in the agency evidence system. Receiver advised of water exposure.”

Notice what this **doesn't** say: “The tablet was off,” “the battery was safe,” or “data was destroyed.” Those claims were not established.

## Seven avoidable errors

1. Charging or restarting a damaged phone to learn whether it works.
2. Keeping a smoking or swollen battery powered to preserve an unlocked state.
3. Transporting submerged **mobile devices and bare storage drives** under one generic rule.
4. Putting an overheating battery in an ordinary sealed property bag or patrol vehicle.
5. Running imaging, `chkdsk`, a recovery wizard, or repeated boots on a failing drive.
6. Cleaning chemical/biological residue or discarding fragments without coordinating evidence disciplines.
7. Delivering hazardous or damaged evidence without advance notice of its condition and interventions.

## Source ledger — published guidance actually used

| Guidance | Published edition | Applied to |
| --- | --- | --- |
| [SWGDE Best Practices for Collection of Damaged Mobile Devices](https://www.swgde.org/documents/published-complete-listing/14-f-004-swgde-best-practices-for-collection-of-damaged-mobile-devices/) | **14-F-004-1.1**, Feb 8, 2016 | Wet, fractured, thermally damaged **mobile devices**; no routine energizing, prompt specialist transfer, document hazards. Older specialized guidance; don't treat it as universal lithium-battery safety policy. |
| [SWGDE Best Practices for Handling Damaged Digital Storage Devices](https://www.swgde.org/documents/published-complete-listing/14-f-002-best-practices-for-handling-damaged-digital-storage-devices/) | **14-F-002-2.0**, Mar 4, 2025 | HDD/SSD/NVMe/USB/SD handling, avoiding power or routine imaging of failed media, reporting prior recovery attempts, trained recovery. **Not a mobile-device standard.** |
| [SWGDE Best Practices for Mobile Device Evidence Collection & Preservation Handling and Acquisition](https://www.swgde.org/documents/published-complete-listing/18-f-003-2/) | **18-F-003-2.0**, Aug 21, 2025 | Power/lock states, encryption and damage condition in mobile preservation, examiner notification. |
| [SWGDE Best Practices for Digital Evidence Collection](https://www.swgde.org/documents/published-complete-listing/18-f-002-best-practices-for-digital-evidence-collection/) | **18-F-002-2.0**, 2025 | Scope, scene documentation, safe collection, live/off state and custody. |
| [U.S. Fire Administration — Battery Fire Safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/batteries/) | Current online guidance, reviewed Oct 26, 2026 | Smoke, odor, heat and shape changes: stop using and seek appropriate response. |
| [OSHA — Lithium-ion Battery Safety: Control](https://www.osha.gov/lithium-ion-battery-safety/control) | Current online guidance, reviewed Oct 26, 2026 | Hazard assessment, personnel training, PPE and emergency plans. |
| [PHMSA Interpretation #24-0050](https://www.phmsa.dot.gov/regulations/title49/interp/24-0050) | Jul 2, 2024 | Escalation of damaged/defective lithium battery **transport** requirements. |

**Scope of this page:** Field preservation and qualified transfer, not instructions for emergency firefighting, hazardous-material shipping, battery disassembly, chip-off, board repair, forensic data recovery or unsafe scene processing. Verify current standards and agency SOP on every substantive revision.

[← Field Collector](README.md) · [Mobile preservation](mobile-device-collection.md) · [Removable storage](removable-media.md) · [Evidence handoff](evidence-handoff.md)
