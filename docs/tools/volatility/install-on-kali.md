# Install Volatility 3 on Kali / Debian

**Use case:** lab-side memory analysis | installation and verification  
**Environment:** Kali, Debian and compatible Linux  
**Risk:** caution  
**Reviewed:** October 2026

> **Current default: Volatility 3.** Volatility 2 depends on end-of-life Python 2 and is treated here as a **legacy, isolated lab-only** compatibility option, not the general install path.

## Preconditions

Use a lab workstation or disposable VM, not the evidence source. Have an appropriate supported Python 3 environment, network access for package installation, enough disk space for symbol downloads/cache, and a separate read-only master memory image with hashed working copy.

## 1. Install Volatility 3 in a virtual environment

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip

python3 -m venv ~/venvs/volatility3
source ~/venvs/volatility3/bin/activate
python -m pip install --upgrade pip
python -m pip install volatility3
```

The version available through PyPI changes; pin and record the **tested release** for case work. The environment stays separate from Kali's system Python.

## 2. Confirm the executable and dependencies

```bash
vol -h
python -m pip show volatility3
```

If `vol` is not found, confirm the virtual environment is activated and the installation completed. Do not mix a virtual-environment install with system-wide `sudo pip` upgrades.

## 3. Test with a **synthetic or approved** Windows memory sample

```bash
vol -f /path/to/approved-sample.raw windows.info
vol -f /path/to/approved-sample.raw windows.pslist
vol -f /path/to/approved-sample.raw windows.pstree
```

`windows.info` confirms that the framework can interpret key details of the Windows sample, not that every plugin will work. `pslist` enumerates linked process objects and `pstree` organizes parent relationships. For forensic interpretation, cross-check findings with disk and event-log artifacts.

## 4. Symbols and network constraints

Windows symbol data may be downloaded and cached as required. Linux and macOS image examination needs appropriate matching symbols and additional setup; do not assume that working Windows analysis means automatic support for every other OS.

If the lab is isolated from the internet, obtain validated symbol packs and dependencies **ahead of time** using the project's documented procedure, and record the versions/files used.

## 5. Record a validation result

```text
Tool: Volatility 3
Python and OS version:
Installation source/version:
Lab test image ID and original SHA-256:
Command run and completion time:
Result or error:
Symbol source/cache:
Validated by:
```

## Legacy Volatility 2 (only when required)

Volatility 2 is historically useful for particular old plugins and images, but Python 2.7 and its dependencies are unsupported and unsafe to install into a normal analysis environment. Use a specifically isolated legacy VM with frozen dependencies and documented, prevalidated tools; avoid copying old unverified setup commands or reaching unknown mirrors.

For legacy CLI syntax see [the archived Volatility 2 help output](vol2-help.md). For modern work prefer the commands in [Volatility 3 high-value workflow](useful-commands.md).

## References

- [Volatility 3 official repository and current installation instructions](https://github.com/volatilityfoundation/volatility3)
- [Volatility 3 PyPI package](https://pypi.org/project/volatility3/)
- [Volatility 3 documentation](https://volatility3.readthedocs.io/)

[Tool index](../README.md) · [Volatility commands](useful-commands.md)
