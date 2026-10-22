# Computer & Laptop — Field Collection

**Use case:** collection | preservation | handoff  
**Environment:** windows | macos | linux  
**Risk:** caution

> **Field quick guide.** A running or encrypted system can lose important evidence and access after shutdown. **Do not run tools or alter power/network state unless trained, authorized, and following the designated response plan.**

## 60-second priority check

- [ ] Photograph the device **before touching it**: screen, cables, attached drives, ports, and surrounding area.
- [ ] Record make/model, serial/asset identifiers, case reference, location, and collection time.
- [ ] Record whether it appears **powered off, on, asleep, locked, or unlocked**. A blank screen may mean sleep, not shutdown.
- [ ] Note visible applications, sessions, external devices, power connection, and any obvious on-screen warnings.
- [ ] **If off, leave it off** until the examiner or SOP directs otherwise.
- [ ] **If on**, contact the digital forensic examiner or incident commander before shutdown, reboot, or unplugging; volatile data and encryption access may be lost.
- [ ] Follow the approved response plan for suspected remote activity, destruction, network connections, and operational disruption.
- [ ] Record every interaction and custody transfer.

## Why live systems need special consideration

A live computer may hold RAM, active connections, logged-in sessions, mounted volumes, decrypted data, and encryption access that cannot be recreated from a powered-off disk. Full memory capture and live acquisition are **examiner tasks**, not routine collector actions.

## Do not

- Turn on an off computer to inspect its contents.
- Restart, log out, click around, search files, or run unapproved commands.
- Remove media from a live system without documenting connections and consulting the response plan.
- Assume disconnecting a network, removing a battery, or forcing shutdown is risk-free.
- Plug found storage devices into an ordinary workstation to “see what's on them.”

## Escalate when

- A volume appears encrypted or is currently unlocked.
- The screen shows a logged-in account or a remote-control session.
- Malware destruction, remote wipe, or a safety-critical system is suspected.
- Enterprise servers, virtual machines, network storage, or RAID configurations are involved.

## Handoff

Record original system state, changes performed, external media, final power state, handling decisions, and where the device was transferred. Attach photographs and the custody record.

[Evidence handoff checklist](evidence-handoff.md) · [Collector home](README.md) · [Examiner: rapid collection](../playbooks/acquisition/0-rapid-evidence-collection.md)

## Reference

[SWGDE — Best Practices for Digital Evidence Collection](https://www.swgde.org/documents/published-complete-listing/18-f-002-2-0/)
