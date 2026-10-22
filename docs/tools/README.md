# Forensic Tools — Collection to Analysis

**Use case:** equipment readiness | forensic examination | lab verification

A tool belongs here only if its page explains **what to prepare, how to use it, what output it produces, and what can examine that output afterward**. A download link alone does not make a useful tool reference.

## Start with the task

| Need | Working reference | What it covers |
| --- | --- | --- |
| Portable Windows imaging | [FTK Imager from USB](ftk/ftk-imager-usb-runtime.md) | Preparation, testing and acquisition considerations |
| Current memory analysis on Kali/Debian | [Volatility installation](volatility/install-on-kali.md) | Python environment, stable installation and validation |
| Investigate a RAM image | [Volatility high-value commands](volatility/useful-commands.md) | Image identity, process tree, network, command lines and caveats |
| Reproduce a legacy investigation | [Volatility 2.6.1 help reference](volatility/vol2-help.md) | Archived CLI reference for legacy environments |
| Decide which field tool pairs with a lab parser | [Field-to-lab matrix](../../playbooks/acquisition/4-field-to-lab-tool-matrix.md) | RAM, disk, browser, logs, PCAP and collection validation |
| Check whether evidence changed | [Hashing](../hashing/README.md) | SHA-256, verification and reporting |

## Field kit → laboratory sanity check

1. Confirm **tool provenance and licensing**, supported OS/version, hardware and architecture.
2. Test the **collector** on a synthetic system or representative lab image; document changes the tool makes.
3. Record the produced **image or artifact format**, destination and hashing method.
4. Verify an independent **lab tool** can open or parse that output, not simply that it exists.
5. Record testing date, versions, driver/elevation requirements, incompatibilities and remediation.

For example, a successful RAM image is only the start. Verify the image can be read in [Volatility 3](volatility/useful-commands.md) on a lab machine, and keep a test record of that result.

## Evidence considerations

Tool execution on a live source can leave artifacts. A program advertised as portable is not necessarily forensically noninvasive, fully offline, or supported across OS builds. Use separate approved acquisition storage; record versions, options, errors and output hashes.

**Before deploying in a criminal or administrative case, validate against your organization's SOP and required tool validation process.**

[Examiner toolkit](../../examiner/README.md) · [Software checklist](../../playbooks/acquisition/3-collection-software-checklist.md)
