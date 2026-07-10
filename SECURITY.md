
---

# `SECURITY.md`

```markdown
# Security Policy

Hashimoire is a public DFIR and defensive security reference. Because this repository deals with digital forensics, security, evidence workflows, OSINT, detections, and tooling notes, security and scope boundaries matter.

## Scope

This repository is intended for authorized, legal, ethical, defensive use.

Appropriate topics include:

- defensive security notes
- digital forensics workflows
- evidence documentation habits
- tool installation notes
- artifact references
- hashing and integrity checks
- detection and hunting logic
- defensive OSINT and exposure checks
- templates and checklists
- small helper scripts for authorized work

Inappropriate topics include:

- exploit development
- credential theft
- stealth or evasion guidance
- persistence guidance
- unauthorized access techniques
- instructions designed to bypass security controls
- malware deployment
- destructive actions
- case-specific sensitive information
- confidential system details
- protected personal information

## Reporting Security Issues

If you find a security concern in this repository, please open a GitHub issue if the concern can be discussed publicly without exposing sensitive details.

Examples of public issues:

- incorrect command syntax
- misleading forensic guidance
- unsafe assumptions
- broken links
- outdated tool references
- unclear risk warnings
- accidental inclusion of non-sensitive test data

Do **not** open a public issue if the report includes:

- credentials
- private keys
- real case information
- protected personal information
- confidential system details
- exploit instructions
- sensitive internal data
- anything that could create harm if published

For sensitive concerns, contact me through ForensicsByte:

https://forensicsbyte.com/contact/

Please describe the issue in general terms first. Do not send sensitive evidence, passwords, confidential case details, protected personal information, or internal system data through an open form or public issue.

## Responsible Disclosure Expectations

When reporting a concern:

- Provide a clear summary of the issue.
- Identify the affected file, note, script, or workflow.
- Explain why it may be unsafe, misleading, or inappropriate.
- Avoid including sensitive data.
- Avoid including step-by-step abuse instructions.
- Keep the report focused on defensive correction.

## Repository Safety Rules

Hashimoire should not contain:

- real case data
- client data
- agency-sensitive data
- credentials
- tokens
- API keys
- private keys
- protected personal information
- non-public system details
- offensive exploit chains
- stealth, persistence, or evasion instructions

If any of that appears in the repo by mistake, it should be removed immediately.

## Defensive Framing

Some security topics can be dual-use. When included, they should be framed around:

- detection
- validation
- hardening
- authorized triage
- evidence preservation
- incident response
- documentation
- risk reduction

If a note primarily helps unauthorized activity, it does not belong here.

## Disclaimer

Hashimoire is provided as a public reference for authorized defensive work.

You are responsible for verifying scope, authority, permissions, and legal requirements before using any command, workflow, script, or template.