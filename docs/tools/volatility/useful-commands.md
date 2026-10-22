# Volatility 3 — Memory Triage Commands and Interpretation

**Use case:** memory analysis | process context | network correlation  
**Environment:** validated lab machine with Volatility 3  
**Risk:** caution  
**Reviewed:** October 2026

> Volatility **analyzes memory images**; it does not acquire memory. Preserve the original image, record SHA-256 and tool versions, and examine a validated working copy.

## First-five-command workflow

The examples assume a memory image named `mem.raw` available to the lab. Run `vol -h` on your installed release to confirm current plugin availability.

```bash
vol -f mem.raw windows.info
vol -f mem.raw windows.pslist
vol -f mem.raw windows.pstree
vol -f mem.raw windows.cmdline
vol -f mem.raw windows.netscan
```

| Plugin | Output to look for | Investigative use | Limitation |
| --- | --- | --- | --- |
| `windows.info` | OS, kernel and layer/symbol information | Sanity-check image identity | Not proof every plugin supports this OS/build |
| `windows.pslist` | PID, PPID, image name, create/exit times | Enumerate process context | Exited/unlinked processes may not appear |
| `windows.pstree` | Parent/child relations | Trace application launch chains | Parent may have exited and PIDs can be reused |
| `windows.cmdline` | Process command-line artifacts | Correlate executed arguments | Some commands missing or overwritten |
| `windows.netscan` | TCP/UDP endpoint artifacts | Correlate PID with network activity | Snapshot/remnant context, not packet content or proof of exfiltration |

## Example process output (fictional)

```text
PID  PPID ImageFileName CreateTime
2540 1180 explorer.exe   2026-10-21 09:11:04
4024 2540 WINWORD.EXE    2026-10-21 10:02:14
6128 4024 powershell.exe 2026-10-21 10:03:02
```

`6128` is an example **Process ID** and `4024` its recorded **Parent Process ID**. If `windows.netscan` reports a socket associated with PID 6128, correlate with creation time, EDR and execution logs. It could represent an intrusion lead; it is **not proof** the traffic was malicious. Compare with the [Windows live process reference](../../../snippets/powershell/processes-services.md).

## Focused follow-up

```bash
# See available options; plugin switches may vary by installed version
vol windows.dlllist -h
vol windows.handles -h
vol windows.registry.hivelist -h

vol -f mem.raw windows.dlllist --pid 6128
vol -f mem.raw windows.handles --pid 6128
vol -f mem.raw windows.registry.hivelist
```

**Why:** DLL listings may help review process modules, handles may show files/registry object references, and registry hive inventory can guide deeper parsing. Missing output is not itself evidence of deliberate hiding.

## Lab output handling

- Record the memory source device, collection time, forensic image format and SHA-256.
- Record exact Volatility 3 release and executed plugin/arguments.
- Save analysis outputs on controlled **lab working storage**, not on the master memory image.
- Parse timestamps into a common reference timezone; monitor tool warnings and symbol failures.
- Preserve result files and note which conclusions require verification against disk or external logs.

## What this does **not** establish

A memory snapshot is not a complete historic process/network log. PID numbers can be reused, network object scanning can show residues, and memory may be incomplete or corrupted. Treat output as a collection-time observation requiring corroboration.

## References

- [Volatility Foundation — Volatility 3](https://github.com/volatilityfoundation/volatility3)
- [Volatility 3 Windows tutorial](https://github.com/volatilityfoundation/volatility3/blob/develop/doc/source/getting-started-windows-tutorial.rst)
- [Current plugin documentation](https://volatility3.readthedocs.io/en/latest/volatility3.plugins.windows.html)

[Install Volatility 3](install-on-kali.md) · [Tool index](../README.md)
