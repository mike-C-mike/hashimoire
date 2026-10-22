# FTK Imager — Prepare and Validate USB Runtime

**Use case:** Windows evidence preview | logical / physical acquisition  
**Environment:** approved Windows collector or forensic lab  
**Risk:** caution  
**Reviewed:** October 2026

> **Portability is not guaranteed.** Copying an installed program directory to USB may work for some versions/configurations, but that does not prove the application and its dependencies will run correctly on all Windows machines or comply with the software license. Validate on representative systems before relying on it.

## Objective

Prepare an authorized, tested FTK Imager runtime for quick field deployment. Keep the tool USB **separate** from acquisition destination media. Do not turn an untested portable copy into your only imaging method.

## Preparation on a clean setup workstation

1. Download the approved FTK Imager version from the [official Exterro product page](https://www.exterro.com/digital-forensics-software/ftk-imager). Review license/use terms and documentation.
2. Install it on a **lab setup computer**, not the source evidence device.
3. Record the installation version and executable SHA-256.
4. If the vendor/package permits a portable or folder-copy workflow, copy the required program files to a dedicated tool USB, e.g. `X:\Tools\FTKImager\`.
5. **Do not indiscriminately copy Windows system DLL families** from `System32` to a field USB. Runtime libraries must match architecture and versions, and redistributable packages may be subject to licensing. Follow vendor and Microsoft-supported deployment methods.
6. Keep a second validated tool set or a lab-based acquisition alternative available.

## Test on a representative non-evidence computer

- [ ] Confirm the application starts without an installation dialog.
- [ ] Confirm it identifies a known test device or sample data source.
- [ ] Test a small logical/physical acquisition with approved settings.
- [ ] Confirm output directory is correct and **not on the source**.
- [ ] Confirm the acquisition completes with expected size, metadata and hash/verification report.
- [ ] Open the output in a separate forensic viewer or image mounting tool.
- [ ] Record OS build, dependencies, elevation, errors, product build and date tested.

## Field capture considerations

1. Confirm authority, scope and evidence identifiers before starting.
2. Record original state and storage mappings, especially encryption state and mounted volumes.
3. Use the **appropriate write blocker for supported powered-off media**; software launching from USB does not itself block writes to the source.
4. For live acquisition, document unavoidable host changes and what source was accessible/unlocked.
5. Write output to approved dedicated evidence storage; monitor errors, expected data size and verification results.
6. Transfer to lab, validate the image and record custody.

## Expected output and meaning

You may obtain a forensic image (depending on format/settings), acquisition logs, calculated hash values and evidence/item metadata. A successful tool message indicates the software reports completion—**not** that the source was free of prior modification, that all inaccessible data was collected, or that the format is readable by every parser.

## Common failure points

- Architecture/runtime mismatch or missing redistributables.
- Corporate application-control, EDR or admin privilege restrictions.
- Destination media full, wrong file system or a path silently pointing at the evidence source.
- Live encrypted volume whose accessibility changes after reboot.
- Incomplete hash/verification notes.

## References

- [Exterro — FTK Imager](https://www.exterro.com/digital-forensics-software/ftk-imager)
- [Field-to-lab tool matrix](../../../playbooks/acquisition/4-field-to-lab-tool-matrix.md)

[Tool index](../README.md)
