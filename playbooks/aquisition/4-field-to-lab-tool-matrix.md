# Field-to-Lab Tool Matrix

**Use case:** readiness | acquisition | validation  
**Environment:** windows | linux | macos  
**Risk:** caution

> **Caution:** Tool availability, licensing, supported OS builds, output formats, and acquisition side effects change. Test tools against representative lab systems *before* an incident. Prefer vendor/project downloads rather than third-party mirrors. All paths below are suggested kit paths, not evidence destinations.

## Minimum tested kit — Windows focus

| Need | Field collection tool (official link) | Where to stage | Lab-side analysis / validation (official link) |
| --- | --- | --- | --- |
| RAM image | [Belkasoft RAM Capturer](https://belkasoft.com/ram-capturer) (primary), [Magnet RAM Capture](https://www.magnetforensics.com/resources/magnet-ram-capture/) (alternate), [WinPmem](https://github.com/Velocidex/WinPmem) (alternate) | `USB/Memory/` | [Volatility 3](https://github.com/volatilityfoundation/volatility3), [MemProcFS](https://github.com/ufrisk/MemProcFS) |
| Targeted Windows artifact collection | [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape), [Velociraptor](https://docs.velociraptor.app/) (approved deployments) | `USB/Artifacts/` | [Eric Zimmerman Tools](https://ericzimmerman.github.io/), [Autopsy](https://www.autopsy.com/) |
| Live host/process/network state | [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite), built-in OS tools | `USB/System/` | Collected text/CSV/log exports; [Timeline Explorer](https://ericzimmerman.github.io/) |
| Disk/logical image | [FTK Imager](https://www.exterro.com/digital-forensics-software/ftk-imager); Linux: [Guymager](https://guymager.sourceforge.io/) | `USB/Imaging/` or validated boot media | [Arsenal Image Mounter](https://arsenalrecon.com/products/arsenal-image-mounter), [Autopsy](https://www.autopsy.com/), [The Sleuth Kit](https://www.sleuthkit.org/sleuthkit/) |
| Logs / event records | OS exports; [KAPE](https://www.kroll.com/en/services/cyber/incident-response-recovery/kroll-artifact-parser-and-extractor-kape) | `USB/Logs/` | [EvtxECmd / EZ Tools](https://ericzimmerman.github.io/), [Hayabusa](https://github.com/Yamato-Security/hayabusa), [Chainsaw](https://github.com/WithSecureLabs/chainsaw) |
| Browser, recent activity, removable-media traces | KAPE targets or targeted copies | `USB/Artifacts/` | [Hindsight](https://github.com/obsidianforensics/hindsight), [Eric Zimmerman Tools](https://ericzimmerman.github.io/), [Autopsy](https://www.autopsy.com/) |
| Network packet capture, if specifically authorized | [Wireshark / dumpcap](https://www.wireshark.org/), [tcpdump](https://www.tcpdump.org/) | `USB/Network/` or preinstalled host tools | [Wireshark](https://www.wireshark.org/), [Zeek](https://zeek.org/) |
| Hashes / manifest | Windows `Get-FileHash` or `certutil -hashfile`; Linux/macOS `sha256sum` or `shasum -a 256` | Built-in / `USB/Hashing/` | Recompute SHA-256; compare to preserved signed or controlled manifest |

## Additional lab capabilities worth staging

- **Memory:** [Volatility 3](https://github.com/volatilityfoundation/volatility3) and [MemProcFS](https://github.com/ufrisk/MemProcFS). Confirm the selected capture format and OS image are actually supported.
- **Windows artifacts:** [Eric Zimmerman Tools](https://ericzimmerman.github.io/) plus [KAPE targets/modules](https://github.com/EricZimmerman/KapeFiles).
- **Registry:** [RECmd](https://ericzimmerman.github.io/) and [RegRipper](https://github.com/keydet89/RegRipper).
- **Timeline:** [Plaso / log2timeline](https://github.com/log2timeline/plaso) and [Timesketch](https://timesketch.org/) (lab service).
- **Disk images:** [Autopsy](https://www.autopsy.com/), [The Sleuth Kit](https://www.sleuthkit.org/sleuthkit/), [Arsenal Image Mounter](https://arsenalrecon.com/products/arsenal-image-mounter).
- **PCAP:** [Wireshark](https://www.wireshark.org/), [Zeek](https://zeek.org/).
- **Commercial (when licensed):** [Magnet AXIOM](https://www.magnetforensics.com/products/magnet-axiom/), [Belkasoft](https://belkasoft.com/), [FTK](https://www.exterro.com/).
- **macOS/Linux:** verify OS-specific acquisition methodology in advance. A Windows memory capturer does not imply modern macOS/Linux RAM capture support.

## Encrypted device readiness

- Record whether the disk/volume is encrypted and mounted/unlocked before changing power state.
- A RAM image **might** contain encryption-related material, but **does not guarantee** a retrievable BitLocker key or successful later decryption.
- When authorized, preserve recovery-key identifiers and use approved escrow/recovery procedures. Store keys separately from general evidence and restrict access.
- Do not experiment with decryption on the only evidence copy. Use validated working copies and document any changes.

## USB staging example

```text
Field-USB/
  Memory/
  Imaging/
  Artifacts/
  System/
  Network/
  Logs/
  Hashing/
  Docs/
  Tool-Manifest.csv
```

**Keep acquisition output on the separate destination SSD**, not on the tool USB or on the target device. Document source and destination identifiers.

## Validate quarterly and after major OS changes

- [ ] Tool binary provenance and SHA-256 recorded; license permits intended use.
- [ ] Launch and elevate on a representative Windows build, including EDR-controlled hosts where authorized.
- [ ] Capture a small test dataset; confirm saved file and SHA-256.
- [ ] Open the resulting image or artifacts with the listed **lab** tools.
- [ ] Check drive space: plan for physical RAM size **plus headroom**; full disk images require significantly more.
- [ ] Ensure output media filesystem supports files larger than 4 GiB (avoid FAT32 for RAM/disk images).
- [ ] Record known failures, drivers, reboots, and security-tool conflicts.
- [ ] Store credentials, licensing secrets, recovery keys, and case data outside this public repository.

## Related

- [Rapid evidence collection workflow](0-rapid-evidence-collection.md)
- [Collection bag checklist](2-collection-bag-checklist.md)
- [Collection software checklist](3-collection-software-checklist.md)
