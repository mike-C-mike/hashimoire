# Windows — Running Processes and Services

**Use case:** triage | response  
**Environment:** windows  
**Risk:** safe

## When to use
While the endpoint is still live, after confirming scope and deciding whether memory acquisition is warranted. This snapshot is not a RAM image.

## PowerShell (read-only)

```powershell
Get-CimInstance Win32_Process |
  Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine, CreationDate |
  Sort-Object ProcessId

Get-CimInstance Win32_Service |
  Select-Object Name, DisplayName, State, StartMode, ProcessId, PathName |
  Sort-Object Name
```

## Expected output
Running process identifiers and parent identifiers; execution paths and command lines when accessible; service status/start behavior and binary paths.

## Example output — synthetic lab scenario

The following sample illustrates the **kind** of output you may encounter. These are invented values, not evidence from a real investigation:

```text
ProcessId ParentProcessId Name           CreationDate
--------- --------------- -------------- -------------------
2540      1180            explorer.exe   2026-10-21 09:11:04
4024      2540            WINWORD.EXE    2026-10-21 10:02:14
6128      4024            powershell.exe 2026-10-21 10:03:02
```

Reconstructed as a **parent-child process tree**, based on the reported IDs:

```text
explorer.exe (PID 2540)
└── WINWORD.EXE (PID 4024, PPID 2540)
    └── powershell.exe (PID 6128, PPID 4024)
```

### What are PID and PPID?

- **PID (Process ID)** is a temporary identifier assigned by Windows to a running process. Here, PowerShell has **PID 6128**.
- **PPID (Parent Process ID)** is the identifier recorded for the process reported as its parent. PowerShell reports **PPID 4024**, pointing to the Word process in this snapshot.
- **CreationDate** lets you correlate process start time with logons, document access, and network events.
- **CommandLine** and **ExecutablePath**, when accessible, can provide more context about how the process launched, but can also expose sensitive data.

A tree makes the relationships easier to read, but **the operating system does not give you a complete historical process tree from this live query**. Parent processes can exit, IDs are reused, relationships can be manipulated, and protected processes may omit fields.

### Example: connecting process and network evidence

Suppose an intrusion investigation begins with an alert about a suspicious outbound connection. Your [network-state snapshot](network-state.md) shows its **OwningProcess** is **6128**. Matching that number to this snapshot points to the PowerShell process, which reports Word as its parent.

That creates an investigative lead: **Did a document launch PowerShell around the time of the connection?** Check the document's origin, command line, process-creation telemetry (for example Security event 4688 if enabled), EDR records, memory evidence, and timestamps. This combination **does not by itself prove compromise**, and a PID match is only meaningful when the records cover the same time window. Do not confuse a matching PID on two different days with the same process.

## Useful focused follow-up (read-only)

```powershell
# Substitute the PID found during triage; this shows the current process, if still alive.
Get-CimInstance Win32_Process -Filter 'ProcessId = 6128' |
  Select-Object ProcessId, ParentProcessId, Name, CreationDate, ExecutablePath, CommandLine
```

## Collection cautions
Command lines can contain credentials, tokens, and personal information—restrict output access. Missing fields can reflect privileges, protected processes, or provider limitations. Queries may cause minor live-state changes. Note whether PowerShell was elevated and use the same collection window as related network/session snapshots.
