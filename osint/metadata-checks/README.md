# Metadata Checks — Documents & Images

**Purpose:** Determine what document and image metadata is present and whether any of it should be redacted **on an authorized publication copy**, without changing the original evidence.

**[Open the Document & Image Metadata Review →](document-image-metadata-review.md)**

## Typical questions

- Does a JPEG or HEIC image claim GPS coordinates or capture time?
- Does a PDF contain author/producer metadata?
- Does an Office document reveal unnecessary staff names or template-origin information?
- Do metadata timestamps conflict with a known device clock?

## Quick local inspection

```bash
exiftool -G1 -s submitted-photo.jpg
```

**Interpretation:** Metadata values are stored claims, not independent proof of authorship or location. Review a copy and document the tool version, observed fields and limitations.

**Evidence warning:** Preserve the original. Metadata removal for a public release is a **separate** procedure and changes the file hash.

[OSINT home](../README.md) · [Hashing](../../docs/hashing/README.md)
