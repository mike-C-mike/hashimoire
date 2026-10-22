# Document & Image Metadata Review

**Use case:** publication checks | authorized disclosure review | forensic triage  
**Risk:** caution · **Environment:** Windows/macOS/Linux workstation, approved lab copy

> **Do not change original evidence.** Hash and preserve the source if it is evidence. Review a working copy. Metadata removal is only for a **separate, authorized publication copy**, never the evidence original.

## What metadata can tell you

| Format | Possible fields | Important limitation |
| --- | --- | --- |
| JPEG/HEIC/TIFF | Camera, EXIF time, GPS, software, orientation | GPS and times can be absent, edited or wrong; uploading often strips EXIF. |
| DOCX/XLSX/PPTX | Author, last modified by, company, creation/modification, comments | App properties may reflect templates or editing software, not actual authorship. |
| PDF | Creator, producer, dates, metadata fields | Printed/exported PDFs may discard prior author/revision history. |
| ZIP / archives | Entry names and archive timestamps | Archive timestamps may be normalized or influenced by extraction/creation. |
| CSV/text | Usually little built-in metadata | File system timestamps are *not* embedded document metadata. |

## 1. Prepare a review copy

Record source filename/path, custody/source information if relevant, file size and current SHA-256. Use approved external evidence storage rather than uploading potentially sensitive documents to online metadata viewers.

**Windows:**

```powershell
Get-FileHash -LiteralPath 'D:\Review\submitted-photo.jpg' -Algorithm SHA256
```

**Linux/macOS:**

```bash
sha256sum submitted-photo.jpg       # Linux
shasum -a 256 submitted-photo.jpg  # macOS
```

## 2. Read metadata offline

[ExifTool](https://exiftool.org/) is a widely used metadata reader. Validate the downloaded utility and its version before use.

```bash
exiftool -G1 -s submitted-photo.jpg
exiftool -time:all -G1 -s submitted-photo.jpg
exiftool -GPS:all -G1 -s submitted-photo.jpg
exiftool -G1 -s submitted-document.pdf
```

These commands **read** metadata. For archive/Office formats, some relevant details can also reside within the package contents or application-specific history; no single command extracts everything.

## Example output (fictional)

```text
[EXIF] DateTimeOriginal : 2026:10:20 13:42:11
[EXIF] Make             : Example Camera
[GPS]  GPSLatitude      : 29 deg 45' 0.00" N
[GPS]  GPSLongitude     : 95 deg 22' 0.00" W
```

**Interpretation:** the file contains tags representing a capture time and coordinates, but these values are **claims stored in metadata**, not independent proof of where or when a photo was created. Correlate with acquisition source, device clock, context and other evidence. The GPS values shown are synthetic.

## 3. Decide what belongs in a public release

- **Keep original:** preserve the submitted original and hash under evidence policy.
- **Create publication copy:** strip or redact only after approval, with documented tools/settings.
- **Recheck release copy:** inspect it again to ensure author, GPS, comments, tracked changes, thumbnails and embedded objects do not remain.
- **Document differences:** the released copy has a new hash and is **not byte-identical** to the original.

## Review notes template

```text
File / item ID:
Original SHA-256:
Working copy location:
Tool / version:
Fields observed:
Sensitive fields present?:
Timestamp/timezone caveats:
Disclosure recommendation:
Publication copy hash (if created):
Approver / reviewer / date:
```

## Cautions

- Do not upload protected, confidential or case-related files to unknown web services.
- A blank GPS field does **not** prove the image was never geotagged.
- File creation/modification timestamps alone do not establish provenance.
- Retain the complete original when preserving evidentiary value; redaction is a distinct disclosure process.

[OSINT home](../README.md) · [Metadata category](README.md) · [Hashing basics](../../docs/hashing/README.md)
