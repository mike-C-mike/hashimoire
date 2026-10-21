# Rapid Evidence Collection Prep and Deployment

**Use case:** readiness | field deployment | forensic intake support  
**Environment:** windows | macos | linux | mixed endpoint environments  
**Risk:** caution | high-impact  

> **Caution:** Preparation directly affects evidence quality. A responder who arrives without the right tools, storage, power, adapters, and documentation materials may unintentionally alter or lose important evidence before collection even begins.

---

## Purpose

This document outlines the preparation, equipment, software, storage, documentation practices, and deployment considerations that should be in place before performing a rapid evidence collection.

It is intended to support the Rapid Evidence Collection Playbook by focusing on readiness and practical field execution rather than artifact analysis. The goal is to ensure collectors arrive prepared to document system state, preserve volatile data, capture targeted artifacts, and transition evidence safely to lab or follow-on examination.

---

## When to use

Use this document when:

- Building or maintaining a rapid evidence collection kit
- Preparing a response bag or deployment case
- Standardizing field collection procedures
- Training responders on what must be ready before deployment
- Reviewing whether collection tools and media are current and functional
- Preparing for live endpoint acquisition in administrative, civil, or criminal contexts

---

## Collection readiness philosophy

A rapid evidence collection should not begin with improvisation.

Preparation should assume that:

- The first few minutes matter
- Volatile evidence may disappear quickly
- Investigators may only get one clean chance to document the initial state
- The device may be encrypted
- The endpoint may be offline, damaged, locked, or unstable
- The environment may be operationally sensitive
- The responder may need to collect, package, label, and transport evidence without returning to the office first

Readiness is part of the evidence process, not an afterthought.

---

## Pre-deployment goals

Before deployment, the responder or team should ensure they can:

- Document the machine’s condition before interacting with it
- Collect volatile data from a live system
- Save collected artifacts to known-good storage
- Preserve integrity through documentation and hashing
- Capture relevant identifiers such as hostname, serial number, user, and timestamps
- Handle basic power, cable, and adapter issues in the field
- Preserve items that may later support deeper lab examination, including encryption information and volatile context
- Package and transfer the collected evidence in a structured way

---

## Core field kit components

# 1. Documentation and scene capture items

These items help preserve the initial state of the system before investigators begin interacting with it.

Recommended items:

- Dedicated camera or approved mobile camera device
- Extra battery pack or charging cable for camera device
- Notebook or field notes pad
- Permanent marker
- Evidence labels
- Tamper-evident bags if used by policy
- Asset or evidence tags
- Printed quick checklist or field worksheet
- Time-synced watch or approved time reference

### Why this matters

Initial photographs and notes may capture:

- the screen state before user interaction
- open windows or applications
- visible chats, documents, or browser tabs
- error messages
- evidence of remote sessions
- attached USB devices
- visible usernames
- lock state or active session state
- whether the system appears powered on, asleep, or unlocked

This documentation can become extremely important later, especially if the screen contents change once the collector starts touching the keyboard or mouse.

---

# 2. Primary collection media

Collectors should have a dedicated, known-good method for storing acquired artifacts.

Recommended items:

- External SSD or other approved high-speed storage media
- Clearly labeled destination media for active collection
- Separate evidence storage media if policy requires staging versus final storage
- Write-protected or read-only media where appropriate for tool distribution
- Spare storage media in case collection size exceeds expectations

### Preparation considerations

Before deployment:

- Ensure sufficient free space exists
- Label storage clearly
- Verify the file system supports expected file sizes
- Confirm the media is readable and writable on expected systems
- Confirm the media has been scanned, checked, and prepared according to policy
- Use predictable folder structures for field collections

### Why this matters

Collected data may include:

- memory captures
- exported logs
- browser artifacts
- targeted file collections
- screenshots or photographs
- collected encryption materials
- hash files
- chain-of-custody notes

Running out of space in the middle of a memory capture is a terrible way to discover your “prepared” drive was mostly optimism.

---

# 3. Tool delivery media

Collectors should have a consistent and controlled way to bring approved tools into the field.

Recommended items:

- Dedicated USB drive containing approved live-response tools
- Backup USB drive with the same tool set
- Version-controlled tool package where possible
- Read-only or write-protected option when available
- Clear folder structure by function

Example organization:

- `/docs`
- `/memory`
- `/system-info`
- `/network`
- `/logging`
- `/hashing`
- `/browser`
- `/packaging`

### Preparation considerations

Before deployment:

- Verify tools still launch correctly
- Confirm licensing requirements where applicable
- Record tool versions
- Remove outdated or duplicate tools
- Keep instructions with the tools where needed
- Ensure naming conventions are consistent

The field is not the place to discover your RAM tool is expired, missing a dependency, or sitting in a folder named `new_final_v2_real`.

---

# 4. Memory acquisition capability

If memory capture is part of your approved workflow, the responder should be ready to perform it without improvising.

Examples of preparation may include:

- Approved RAM capture utility on a dedicated USB drive
- Sufficient destination storage for the memory image
- Documentation on expected runtime and output location
- Hashing capability for the resulting image
- Notes on any platform limitations or compatibility requirements

### Why memory collection may matter

Memory can contain:

- fileless malware artifacts
- active process state
- injected code
- decrypted content
- active sessions or tokens
- chat fragments or temporary data
- network artifacts
- remnants of executed payloads
- volatile context that will disappear after shutdown

### Additional consideration

If a device is encrypted, a live session may also present an opportunity to capture information needed later for examination, such as:

- proof that the device is in an unlocked state
- recovery information if it is displayed or legitimately accessible
- documentation needed to preserve access to encrypted storage during later lab work

This does not mean indiscriminate hunting. It means the responder should understand that once power is lost, some access conditions may disappear with it.

---

# 5. Power, adapter, and connectivity support

Field collections often fail for boring reasons rather than forensic reasons.

Recommended items:

- Power adapter bank for common device types
- USB-A to USB-C adapters
- USB-C hubs
- Ethernet adapter if needed
- Spare charging cables
- Extension cord or compact power strip if appropriate
- Portable battery pack for documentation device
- Known-good mouse, when permitted and useful
- Video adapters if external monitor viewing is necessary and policy allows it

### Why this matters

A collector may need to:

- power a failing device long enough to complete volatile collection
- connect modern storage to older machines or older storage to modern machines
- deal with limited ports on laptops
- support photography and note-taking devices during extended collection

The enemy is not always malware. Sometimes it is a laptop with one USB-C port and a battery at 3 percent.

---

# 6. Hashing and integrity tools

Collectors should be able to validate what they acquired.

Recommended capabilities:

- approved hashing utility
- method to generate and store hash outputs
- note template for recording source, destination, timestamps, and hash values
- known location for storing integrity records with the collection set

### Why this matters

Hashing supports:

- integrity verification
- repeatability
- later comparison
- evidentiary defensibility
- transfer validation between field and lab

---

# 7. Packaging and custody materials

Recommended items:

- evidence bags or approved packaging
- tamper-evident seals if required
- labels
- custody forms
- field collection worksheet
- prebuilt folder and naming templates
- protective sleeves for loose USB drives or media cards

### Why this matters

A technically sound collection can still become a mess if:

- media is unlabeled
- collected files are mixed together
- the storage device is not associated clearly with the case
- no one can explain who handled what and when

---

## Software and tool preparation checklist

Before deployment, verify:

- tools are approved for use
- tools are current and functional
- storage media is empty or staged appropriately
- destination path structure is ready
- hashes can be generated
- memory capture tool is present if authorized
- documentation forms are available
- the camera or photo device works
- charging equipment is packed
- adapters needed for likely device types are packed
- collector notes include tool versions and collection kit contents

A prepared kit should be boringly reliable.

---

## Example field-ready kit layout

A practical field kit may include:

### Documentation pouch
- camera or approved phone
- notebook
- pens and marker
- labels
- printed checklist

### Tool media pouch
- primary USB tool drive
- backup USB tool drive
- write-protected reference media if used

### Storage pouch
- primary external SSD
- backup external SSD
- protective cases

### Power and adapter pouch
- charging cables
- USB adapters
- hub
- power brick
- extension cable if needed

### Evidence handling pouch
- bags
- seals
- forms
- tags

This kind of layout makes deployment faster and reduces the chance of leaving one critical item behind.

---

## Deployment in practice

# 1. Before arrival

Before going on scene:

- confirm scope and authority
- confirm what type of system is involved
- estimate whether memory collection may be appropriate
- verify storage space
- verify the collection kit is complete
- know where collected data will be staged
- know who will receive the evidence afterward

---

# 2. At first contact with the machine

Before clicking around:

- observe the device state
- photograph the screen if permitted
- note whether the machine is on, off, locked, or unlocked
- note visible user context
- note external devices attached
- note network connectivity indicators
- note power state

The first few moments should focus on documentation, not curiosity.

---

# 3. Initial deployment sequence

A practical deployment sequence often looks like this:

1. Document the current state
2. Connect approved destination storage if needed
3. Connect approved tool media
4. Capture system time and baseline details
5. Perform volatile collection first
6. Save outputs to the prepared destination path
7. Record what was collected and where it was saved
8. Hash collected outputs where appropriate
9. Transition to targeted artifact collection
10. Make a documented decision about shutdown, seizure, or leaving the system live

---

# 4. Collection output handling

During the collection, ensure:

- outputs go to the correct case folder
- files are named consistently
- notes record the exact artifact collected
- large items such as memory images are monitored for completion
- collection errors are documented
- potentially important supporting items are preserved

Examples of supporting items may include:

- visible encryption recovery information if properly accessible and in scope
- logs that may later support review of outbound transfers or exfiltration activity
- records of connected external media
- timestamps needed to align later review across systems

This stage is not about deep analysis. It is about preserving useful material for the people doing analysis later.

---

# 5. Transition to packaging and handoff

After collection:

- hash final collected items where appropriate
- export or save notes
- package media
- label everything clearly
- document who collected it
- document who received it
- note whether the source system remained live or was powered down
- note whether a fuller dead-box examination is expected later

A field collection should land in the lab or evidence room in a way that makes sense without the original collector standing there to explain it.

---

## What may be preserved by area

This document does not address analysis, but responders should understand why different collection areas matter.

### Documentation and photos may preserve
- initial screen state
- unlocked condition
- visible user activity
- device and accessory relationships

### Memory capture may preserve
- fileless malware artifacts
- active sessions or tokens
- decrypted context
- transient execution evidence

### System and network data may preserve
- running process context
- active connections
- signs of command-and-control or remote access
- indicators useful for broader scoping

### Logs and targeted artifacts may preserve
- evidence of account use
- evidence of data movement
- possible exfiltration timing
- execution history
- user activity context

### Encryption-related documentation may preserve
- the fact that the device was unlocked at collection time
- information needed to support later decryption workflows in the lab when legitimately available and in scope

---

## Validation / expected output

A prepared and successfully deployed collection process should result in:

- documented initial machine state
- organized evidence storage
- volatile collection capability that was ready before arrival
- collected artifacts saved to known-good media
- integrity records for collected items
- notes linking the collection to the case or incident
- a clear handoff path to deeper examination or retention

---

## Notes for field use

A good rapid collection setup is not built around having every possible tool. It is built around having the right tools, in the right place, in a known state, with enough storage, power, and documentation discipline to use them effectively.

In practice, preparation is what allows the responder to act calmly and predictably when the machine in front of them is not calm or predictable.
