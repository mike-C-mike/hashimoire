# Defensive OSINT — Field Reference

**Use case:** public-source verification | exposure reduction | documentation  
**Audience:** authorized investigators, defenders, individuals reviewing their own footprint  
**Risk:** caution · **Review scope before collection**

> **Start here:** OSINT can reveal public information, but it is not permission to access private data, deceive a subject, target minors, or circumvent a site's controls. Collect only what the authorized question requires. Never enter evidence, credentials, or personal case data into this public website.

## Choose the question, not the tool

| I need to… | Start with | Expected result |
| --- | --- | --- |
| Review a domain's public footprint | [Domain exposure review](domain-checks/domain-exposure-review.md) | DNS/mail-authentication inventory, observations, and remediation notes |
| Reduce my own or an organization's public exposure | [Personal exposure review](exposure-checks/personal-exposure-review.md) | Risk-prioritized cleanup actions, without building unnecessary dossiers |
| Check whether a handle is reused or impersonated | [Username review](username-checks/username-review-workflow.md) | Documented public-account candidates with confidence labels |
| Inspect documents/images for unwanted metadata | [Document and image metadata review](metadata-checks/document-image-metadata-review.md) | File metadata inventory and safe publication recommendation |
| Decide whether a method is appropriate | [OSINT safety boundaries](safety-notes/osint-safety-boundaries.md) | Clear stop/escalation criteria |

## First five minutes — any OSINT review

1. **Record the objective:** exactly what is the question? Who authorized it? Which domain, account or organization is in scope?
2. **Specify allowed methods:** public web pages, search engines, ordinary DNS resolution, authorized submitted files, and passive sources as applicable. No login probing, credential tests or access-control bypass.
3. **Set a collection limit:** collect the minimum links, screenshots or metadata required to support findings.
4. **Record the time:** use a date, time and timezone (prefer UTC in a formal record); volatile online pages can change.
5. **Separate observations from conclusions:** the same username or a similar domain is not enough to identify an account owner or prove impersonation.

## General documentation template

```text
Review identifier:
Purpose / authorized by:
Scope and exclusions:
Reviewer and date/time/timezone:
Sources visited and access dates:
Finding:
What was directly observed:
What is inferred (and confidence):
Alternative explanations:
Recommended action:
What was retained / retention period:
Limitations / unverified items:
```

## Boundaries

Do not publicly publish collected personal details. Avoid bulk scraping, collecting data about unrelated people, interacting with suspected scammers, or seeking access to nonpublic material. If you discover evidence of a crime, preservation and reporting should follow the authorized organization's procedures.

**OSINT is most useful when it produces a defensible answer and a practical decision, not when it produces the largest spreadsheet.**

[Domain](domain-checks/README.md) · [Exposure](exposure-checks/README.md) · [Username](username-checks/README.md) · [Metadata](metadata-checks/README.md) · [Safety](safety-notes/README.md)
