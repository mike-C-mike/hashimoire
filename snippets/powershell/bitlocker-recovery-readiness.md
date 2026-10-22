# Windows — BitLocker Recovery Readiness

**Use case:** acquisition | preservation | validation  
**Environment:** windows  
**Risk:** caution

> **Authorized forensic use only.** A BitLocker recovery password is sensitive key material. Do not add it to general logs, incident tickets, command transcripts, screenshots, or a public repository. Use your organization's protected evidence/key storage.

## Why collect this before shutdown?

An unlocked Windows volume may be readable during live collection but require a recovery credential to access its offline image later. Record the volume's state and protector IDs **before** deciding to power off.

## 1. Identify encrypted and unlocked volumes

Run in elevated Windows PowerShell:

```powershell
Get-BitLockerVolume |
  Select-Object MountPoint, VolumeStatus, ProtectionStatus, LockStatus, EncryptionPercentage
```

Alternative using the built-in executable:

```powershell
manage-bde -status
```

## 2. Inventory protector types and IDs

```powershell
(Get-BitLockerVolume -MountPoint 'C:').KeyProtector |
  Select-Object KeyProtectorType, KeyProtectorId
```

## 3. Display an existing recovery password (restricted)

**Only** in an approved, controlled collection environment where the console is not broadly recorded or shared:

```powershell
(Get-BitLockerVolume -MountPoint 'C:').KeyProtector |
  Where-Object { $_.KeyProtectorType -eq 'RecoveryPassword' } |
  Format-List KeyProtectorId, RecoveryPassword
```

Built-in alternative (may display other protectors too):

```powershell
manage-bde -protectors -get C:
```

The output displays an existing 48-digit recovery password **only if** a matching protector exists and you have sufficient access. It does not create a recovery password or guarantee decryption. A device using TPM protection may have a key escrowed in Microsoft Entra ID or Active Directory instead; correlate the recovery protector ID using your approved escrow workflow.

## Example output — synthetic and redacted

Example `Get-BitLockerVolume` summary:

```text
MountPoint VolumeStatus   ProtectionStatus LockStatus EncryptionPercentage
---------- -------------- ---------------- ---------- --------------------
C:         FullyEncrypted On               Unlocked   100
D:         FullyDecrypted Off              Unlocked   0
```

### What this tells you

- **C:** `FullyEncrypted` means the volume's encryption conversion is complete. `Unlocked` means Windows can currently access it; **it does not guarantee the same offline access after shutdown**.
- **ProtectionStatus:** whether BitLocker protectors are currently enforcing protection. Protection being *Off* can include a suspended state; don't mistake it for a drive being unencrypted.
- **D:** `FullyDecrypted` is a different condition from an encrypted but unlocked volume.

Example protector inventory:

```text
KeyProtectorType KeyProtectorId
---------------- --------------------------------------
Tpm              {11111111-2222-3333-4444-555555555555}
RecoveryPassword {aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee}
```

The **RecoveryPassword protector ID** helps match a recovery record held in approved escrow. The recovery-password command may return a **48-digit numeric secret**; that value is intentionally *not shown in this public example*. An ID alone is **not a decryption key**.

### Field interpretation

The useful decision is not simply "BitLocker enabled?" It is **"Can the forensic laboratory access this volume after we power it down?"** Record state, verify an authorized recovery path with the examiner, and preserve the relevant access material securely.

## 4. Preservation and handoff

- Record case ID, device/volume identity, time with timezone, volume state, tool/command and matching protector ID.
- Put any actual recovered password in an access-controlled key vault or encrypted evidence store, with audit trail and custody reference.
- Confirm use of escrow or a recovery mechanism with authorized lab staff before power-down if an offline forensic image is planned.
- If no recovery-password protector is found, record that fact; do not assume memory acquisition can recover the volume key.
- Do **not** add/remove protectors, suspend encryption, rotate keys, decrypt, or restart without separate approval.

## Official reference

[Microsoft — BitLocker operations guide](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide)  
[Microsoft — manage-bde protectors](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-protectors)

[Back to Windows snippets](README.md)
