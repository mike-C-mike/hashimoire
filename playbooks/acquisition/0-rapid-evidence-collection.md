# Rapid Evidence Collection — Live to Dead-Box

**Use case:** triage | response | acquisition  
**Environment:** windows | linux | macos  
**Risk:** caution

> **Caution:** Authorized collection only. Every action on a live machine changes some evidence. Order of volatility is a guide, not permission to bypass scope, safety, containment, or encryption concerns.

## Purpose

Preserve the evidence most likely to disappear first, then capture targeted persistent artifacts and document whether the device stays live or transitions to a powered-off (dead-box) examination.

## When to use

- Suspected compromise, unauthorized access, data movement, or employee misuse.
- A powered-on machine that may later be seized or imaged.
- Urgent triage before a full forensic examination.

## Preconditions and authority

- [ ] Record incident/case number, collector, authorizing authority, and scope.
- [ ] Identify safety-critical services or users who could be affected.
- [ ] Decide with incident command whether to isolate the network immediately, defer isolation for volatile collection, or leave it connected under monitoring; document reasons.
- [ ] Check whether full-disk encryption, unlocked volumes, remote-wipe risk, or active sync changes the plan.
- [ ] Verify tools, storage, power, and documentation supplies using the [bag checklist](2-collection-bag-checklist.md) and [software checklist](3-collection-software-checklist.md).

## Collection order: prioritize volatility, not rigidity

| Priority | Preserve | Why now |
| --- | --- | --- |
| 0 | Initial scene/device state, authoritative reference time | Initial state cannot be recreated after interaction. |
| 1 | Memory and live encryption/session state, if authorized and feasible | Lost or changed on shutdown; memory acquisition itself may take time. |
| 2 | Processes, network connections, logged-on users, open files, caches | Live state can change every second. |
| 3 | Temporary data, current user context, mounted shares, recent activity | Can rotate, be cleaned, or be overwritten. |
| 4 | Relevant logs, browser databases, persistence artifacts, selected files | More persistent, but retention/rotation still matters. |
| 5 | Full-disk image or powered-off handling | Follow after a documented live-to-dead-box decision where appropriate. |

**Exception:** Active destruction, exfiltration, or operational risk may make containment more urgent than acquisition. Do not assume memory capture is always possible or always first.

## Field procedure

### 1. Observe before interacting

- Photograph the screen, physical setup, cables, external media, and power indicators with approved equipment.
- Record device location, make/model, serial/asset tag, lock state, visible apps, signed-in user if displayed, and who was present.
- Record the investigator's reference date/time/timezone; compare with system time when safe. Note discrepancies rather than changing the clock.

### 2. Establish baseline

- Record hostname, operating system, user/session context, system time and timezone, uptime, drive mounts, and network interfaces.
- Log the first interaction time and every collection utility launched. Keep results on prepared acquisition media, not scattered across the source drive.

### 3. Acquire volatile material

- If authorized and justified, capture RAM to a separate, adequately sized destination SSD. Note tool, version, command/options, start/end time, failures, and hash.
- Preserve current processes, services, active network connections, route/ARP/neighbor state, sessions, mapped shares, and open files with approved tools.
- Memory may retain fileless execution artifacts, process state, decrypted content, active tokens, and sometimes encryption-related material; **recovery of BitLocker keys is not guaranteed**. Maintain a controlled, separately authorized process for any recovered credentials or keys.

### 4. Capture changing user and disk artifacts

- Preserve in-scope recent files, downloads, browser artifacts, temporary directories, selected logs, relevant scripts, and attached-media context.
- Capture appropriate Windows event logs, EDR exports, firewall/proxy/DNS/VPN records or system journal data before rotation where possible.
- Logs may help reconstruct transfers or possible exfiltration, but a connection or file-access event **alone is not proof** that data left the environment.
- Avoid browsing live files unnecessarily; use tested collection utilities and note unavoidable modifications.

### 5. Validate and package

- Hash evidence containers or acquired files (prefer SHA-256) and produce a manifest. A hash of a logical copy does not undo live-system changes.
- Record source paths, tool versions, timestamps with offsets, errors, excluded items, storage IDs, and custody transfers.
- Keep unredacted logs, memory images, and recovered sensitive material only in approved protected storage.

### 6. Explicit shutdown decision

Choose and document one:

- **Remain live:** maintain power/monitoring as directed; record responsible custodian.
- **Controlled shutdown:** after collection and encryption review, when authorized and operationally appropriate.
- **Forced power-off/disconnect:** only for documented safety, destruction, or containment reasons under applicable procedure.
- **Seizure/handoff:** record whether powered, locked, encrypted, and what remains attached.

On encrypted systems, powering off may remove practical access to an unlocked volume. Where permitted, arrange acquisition or authorized recovery material **before** shutdown. Do not treat an unlocked screen as proof that all volumes are accessible.

### 7. Dead-box handoff

- Tag device and associated media; package according to device/media requirements.
- Record who took custody, time/location, final power state, outstanding risks, and next imaging task.
- Use a hardware write blocker for subsequent **supported offline media acquisition**, where appropriate. A write blocker is not a substitute for safe live collection.

## Validation and expected output

- [ ] Initial state and time baseline documented.
- [ ] Volatile acquisition decision and outcome recorded.
- [ ] Targeted artifacts and errors inventoried.
- [ ] Evidence hashes and collection tool versions recorded.
- [ ] Encryption/containment choices documented.
- [ ] Powered-on/off disposition and custody handoff explicit.

## Companion documents

- [Collection bag checklist](2-collection-bag-checklist.md)
- [Collection software checklist](3-collection-software-checklist.md)
- [Field-to-lab tool matrix](4-field-to-lab-tool-matrix.md)
- [Acquisition prep and deployment notes](1-live-acquisition-playbook.md)

See also: [Visual field reference — collection and handoff diagrams](5-visual-field-reference.md).

## Windows quick-command references

Use these focused snippets alongside the documented order of volatility, not as a substitute for memory capture:

1. [System identity, clock and timezone](../../snippets/powershell/system-identity-time.md)
2. [Process and service snapshot](../../snippets/powershell/processes-services.md)
3. [TCP/UDP connections, route and DNS state](../../snippets/powershell/network-state.md)
4. [Users, logons and mapped shares](../../snippets/powershell/users-sessions.md)
5. [Export Windows event logs](../../snippets/powershell/event-log-export.md)
6. [Generate and verify SHA-256 hashes](../../snippets/powershell/sha256-evidence.md)
