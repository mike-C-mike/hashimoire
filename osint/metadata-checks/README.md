
```markdown
<!-- osint/metadata-checks/README.md -->

# Metadata Checks

This folder contains defensive notes for reviewing metadata in documents, images, exports, and other files.

Metadata can reveal useful context, but it can also expose information that was not intended for publication.

## Purpose

Metadata checks help answer:

- Does this file contain hidden author information?
- Does this image include GPS coordinates?
- Does this document reveal usernames or internal paths?
- Does this spreadsheet contain hidden sheets?
- Does this PDF include comments or revision history?
- Does this file expose software, device, or organization details?
- Should metadata be removed before publication or sharing?

## Appropriate Use Cases

Appropriate uses include:

- reviewing your own files before publishing
- checking organization documents before public release
- reviewing images before posting online
- checking exported reports before handoff
- reviewing shared templates
- identifying avoidable exposure in public files

## Evidence Warning

Metadata may be evidence.

Do not casually strip metadata from original evidence, forensic images, exports, or working copies.

Sanitization is appropriate for public release or controlled sharing when authorized. Original evidence should be preserved according to policy.

## Folder Contents

- `document-image-metadata-review.md`  
  A detailed workflow for reviewing metadata in documents, images, PDFs, spreadsheets, archives, and forensic/security exports.