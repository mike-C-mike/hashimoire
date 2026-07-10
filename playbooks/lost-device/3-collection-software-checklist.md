# Collection Software Checklist

**Use case:** tool readiness | field collection capability | lab review support  
**Environment:** windows | macos | linux | mixed forensic workflows  
**Risk:** caution  

> **Caution:** Software readiness includes both collection and follow-on review capability. Capturing an artifact in the field is only half the job. The team should already know how it will validate, mount, parse, and review that artifact back in the lab.

---

## Purpose

This checklist identifies specific software categories, recommended utilities, and practical alternatives that should be staged before conducting rapid evidence collection.

It covers both:

- **Field collection**
- **Lab-side review**

A toolset is incomplete if it can acquire evidence that no one is prepared to examine later.

---

## Readiness philosophy

A good collection stack should answer two questions before deployment:

1. Can we collect the artifact in the field?
2. Can we do something useful with it in the lab?

That means the software kit should be built in pairs whenever possible:

- memory capture + memory analysis
- disk image acquisition + image mounting/review
- artifact collection + artifact parsing
- log export + log review
- browser extraction + browser review

---

## Core software categories

A prepared software stack should usually cover:

1. Documentation and notes
2. Live system information collection
3. Memory acquisition
4. Memory analysis
5. Targeted artifact collection
6. Disk and logical imaging
7. Image mounting and review
8. Browser and user-activity review
9. Hashing and integrity validation
10. Network review
11. Timeline / artifact parsing
12. Full case review in the lab

---

## 1. Documentation and notes

### Recommended capabilities

- Plain text editor for field notes
- Spreadsheet or template-ready note sheet for collection logs
- PDF export capability for final packaging notes
- Screenshot utility when policy allows

### Why this matters

These support:

- initial scene documentation
- collection logs
- artifact inventory
- hash record tracking
- handoff notes

---

## 2. Live system information collection

### Recommended categories

- system info tools
- process listing tools
- service listing tools
- session / logged-in user enumeration
- network connection review
- mounted drive review
- command-history access where appropriate

### Recommended option

- [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape)

### Why this matters

This category supports fast preservation of:

- host context
- user context
- execution context
- targeted forensic artifacts before the machine state changes

---

## 3. Memory acquisition

This is the category where you do not want to be improvising in the field.

### Recommended primary option

- [Belkasoft RAM Capturer](https://belkasoft.com/ram-capturer)

### Recommended alternatives

- [Magnet RAM Capture](https://www.magnetforensics.com/resources/magnet-ram-capture/)
- [WinPmem](https://github.com/Velocidex/WinPmem)

### Why memory capture matters

RAM may preserve:

- fileless malware artifacts
- injected code
- active network state
- decrypted content
- process state
- tokens or active sessions
- volatile evidence that vanishes after shutdown

### Practical recommendation

For a Windows field USB, **Belkasoft RAM Capturer** is a strong default pick, with **Magnet RAM Capture** or **WinPmem** as backup or alternate options.

---

## 4. Memory analysis

Collection without analysis capability is half a toolbox.

### Recommended primary option

- [Volatility 3](https://github.com/volatilityfoundation/volatility3)

### Recommended commercial / integrated options

- [Belkasoft](https://belkasoft.com/)
- [Magnet AXIOM](https://www.magnetforensics.com/products/magnet-axiom/)

### Why this matters

Memory analysis tooling supports review of:

- suspicious processes
- loaded modules / DLLs
- command execution traces
- network artifacts
- injected or hidden code
- evidence that may not exist on disk anymore

### Practical recommendation

For a serious lab baseline, **Volatility 3** should be in the stack even if commercial suites are also available.

---

## 5. Targeted artifact collection

### Recommended primary option

- [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape)

### Strong companion ecosystem

- [Eric Zimmerman Tools](https://ericzimmerman.github.io/)
- [KAPE Documentation](https://ericzimmerman.github.io/KapeDocs/)

### Why this matters

This category helps with:

- recent activity
- evidence of execution
- browser artifacts
- user profile artifacts
- removable media traces
- targeted triage before full imaging

### Practical recommendation

For Windows-heavy rapid collection, **KAPE + Eric Zimmerman tools** is one of the strongest combinations to stage ahead of time.

---

## 6. Disk and logical imaging

### Recommended primary option

- [FTK Imager](https://www.exterro.com/digital-forensics-software/ftk-imager)

### Expanded option

- [FTK Imager Pro](https://www.exterro.com/digital-forensics-software/ftk-imager-pro)

### Why this matters

This category supports:

- logical acquisition
- image creation
- quick preview before deeper processing
- hash-supported acquisition workflows

### Practical recommendation

If you want one imaging utility on the field media by default, **FTK Imager** is still a sensible baseline.

---

## 7. Image mounting and review

### Recommended primary option

- [Arsenal Image Mounter](https://arsenalrecon.com/products/arsenal-image-mounter)

### Why this matters

This category helps you:

- mount and inspect acquired images quickly
- work with BitLocker-protected material
- access Volume Shadow Copies
- validate what was acquired
- move from acquisition into review

### Practical recommendation

If your lab handles Windows images regularly, **Arsenal Image Mounter** is one of the most useful tools to have staged.

---

## 8. Browser and user-activity review

### Lightweight quick-look options

- [BrowsingHistoryView](https://www.nirsoft.net/utils/browsing_history_view.html)
- [ChromeHistoryView](https://www.nirsoft.net/utils/chrome_history_view.html)

### Heavier options

- [Autopsy](https://www.autopsy.com/)
- [The Sleuth Kit / Autopsy](https://www.sleuthkit.org/autopsy/)
- [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape)
- [Eric Zimmerman Tools](https://ericzimmerman.github.io/)

### Why this matters

Browser review helps preserve or analyze:

- access to phishing or staging sites
- downloads
- search activity
- portal logins
- user navigation around an incident window

---

## 9. Hashing and integrity validation

### Required capability

Whatever stack you choose, it should include:

- file hashing
- manifest generation
- integrity validation after transfer

### Why this matters

Hashing supports:

- evidentiary defensibility
- transfer validation
- repeatability
- confidence that the lab is examining what the field actually collected

This category is not optional.

---

## 10. Network review

### Recommended option

- [Wireshark](https://www.wireshark.org/)

### Why this matters

Network tooling supports:

- packet review
- quick pcap validation
- exfil review support
- protocol-level inspection when captures are available

### Practical recommendation

Even if you are not doing full packet forensics every day, **Wireshark** belongs in the lab stack.

---

## 11. Full case review in the lab

### Recommended open-source option

- [Autopsy](https://www.autopsy.com/)
- [Autopsy Documentation](https://sleuthkit.org/autopsy/docs/user-docs/4.22.0/)

### Recommended commercial options

- [Belkasoft](https://belkasoft.com/)
- [Magnet AXIOM](https://www.magnetforensics.com/products/magnet-axiom/)
- [FTK](https://www.exterro.com/ftk-product-downloads/)

### Why this matters

This category is where the team turns acquisitions into:

- reviewable cases
- searchable evidence
- timelines
- exportable findings
- reports suitable for administrative, civil, or criminal matters

---

## Recommended field stack

If you want a practical Windows-centric rapid collection workflow:

### On the field USB

- [Belkasoft RAM Capturer](https://belkasoft.com/ram-capturer)
- [FTK Imager](https://www.exterro.com/digital-forensics-software/ftk-imager)
- [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape)
- selected [Eric Zimmerman tools](https://ericzimmerman.github.io/)
- hashing utility
- collection notes template

### On destination storage / external SSD

- prepared case folder structure
- space for RAM capture
- space for logical collection
- hashes folder
- notes folder

### In the lab

- [Volatility 3](https://github.com/volatilityfoundation/volatility3)
- [Arsenal Image Mounter](https://arsenalrecon.com/products/arsenal-image-mounter)
- [Autopsy](https://www.autopsy.com/)
- [Eric Zimmerman tools](https://ericzimmerman.github.io/)
- [Wireshark](https://www.wireshark.org/)
- commercial suite(s) if available, such as [Belkasoft](https://belkasoft.com/), [Magnet AXIOM](https://www.magnetforensics.com/products/magnet-axiom/), or [FTK](https://www.exterro.com/ftk-product-downloads/)

---

## Expanded options by category

### Memory acquisition

- [Belkasoft RAM Capturer](https://belkasoft.com/ram-capturer)
- [Magnet RAM Capture](https://www.magnetforensics.com/resources/magnet-ram-capture/)
- [WinPmem](https://github.com/Velocidex/WinPmem)

### Memory analysis

- [Volatility 3](https://github.com/volatilityfoundation/volatility3)
- [Belkasoft](https://belkasoft.com/)
- [Magnet AXIOM](https://www.magnetforensics.com/products/magnet-axiom/)

### Artifact triage and parsing

- [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape)
- [Eric Zimmerman Tools](https://ericzimmerman.github.io/)

### Disk / logical imaging

- [FTK Imager](https://www.exterro.com/digital-forensics-software/ftk-imager)
- [FTK Imager Pro](https://www.exterro.com/digital-forensics-software/ftk-imager-pro)

### Image mounting / decrypted access workflows

- [Arsenal Image Mounter](https://arsenalrecon.com/products/arsenal-image-mounter)

### Browser / quick user activity review

- [BrowsingHistoryView](https://www.nirsoft.net/utils/browsing_history_view.html)
- [ChromeHistoryView](https://www.nirsoft.net/utils/chrome_history_view.html)
- [Autopsy](https://www.autopsy.com/)
- [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape)
- [Eric Zimmerman Tools](https://ericzimmerman.github.io/)

### Network review

- [Wireshark](https://www.wireshark.org/)

---

## Preparation checks before deployment

Before relying on the software stack, verify:

- the tool is approved for your environment
- licensing is current where applicable
- the executable actually launches
- dependencies are present
- output format is understood
- destination media has enough space
- the lab has software ready to review the output later
- your team knows where the tool lives and what it is for

A giant folder of utilities is not a toolkit. It is a junk drawer with better branding.

---

## Validation / expected output

A mature software kit should leave you able to say:

- we can capture RAM in the field
- we can analyze that RAM later
- we can collect targeted artifacts quickly
- we can image or preview storage when needed
- we can mount images in the lab
- we can review browser and user artifacts
- we can validate integrity with hashes
- we can move from field collection to lab review without inventing a workflow on the spot

---

## Notes for operational use

If building around real-world usefulness instead of tool hoarding, a strong core stack is:

- [Belkasoft RAM Capturer](https://belkasoft.com/ram-capturer) for field memory acquisition
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) for memory analysis
- [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape) for targeted triage collection
- [Eric Zimmerman Tools](https://ericzimmerman.github.io/) for parsing and artifact work
- [FTK Imager](https://www.exterro.com/digital-forensics-software/ftk-imager) for imaging / preview
- [Arsenal Image Mounter](https://arsenalrecon.com/products/arsenal-image-mounter) for mounted review
- [Wireshark](https://www.wireshark.org/) for packet review
- [Autopsy](https://www.autopsy.com/) as an open-source case-review platform

That stack is not everything on earth, but it covers a lot of practical ground without turning your field USB into a clown car.
