# Cloud & Account Evidence — First-Responder Preservation

**Audience:** sworn officers | investigators | authorized evidence personnel  
**Use case:** identify cloud evidence | prevent loss | request preservation through agency channels | examiner handoff  
**Environment:** messaging | social media | cloud storage | email | enterprise accounts | cloud video  
**Risk:** caution — rapidly changing content, legal process and sensitive personal data  
**Guidance reviewed:** October 26, 2026

> **START HERE:** This is a **first-responder identification and preservation-referral guide**, not authorization for an officer to sign in to someone's account, download private cloud data, issue legal process without authorization, or promise that content has been preserved. **Preserving records is different from obtaining or reviewing them.** Follow your agency's designated investigative/legal process, applicable law, policies and case-specific authority. [SWGDE 23-F-004-1.1](https://www.swgde.org/documents/published-complete-listing/23-f-004-best-practices-for-digital-evidence-acquisition-preservation-and-analysis-from-cloud-service-providers/), §§6–11.

## First 60 seconds — what can disappear?

- [ ] **Identify the service and evidence** without accessing restricted content: account handle, exact profile/post/file URL, service name, visible post/message/clip ID and related date/time if already lawfully available.
- [ ] **Record the relevant time window**, including timezone, event time versus observation time, and any known expiration/auto-delete setting. An app's displayed "yesterday" is not a defensible absolute timestamp.
- [ ] **Record how you learned about it:** witness report, already-visible screen, public page, business custodian or lawfully available agency records. Distinguish first-hand observation from an allegation.
- [ ] **Decide what is urgent:** disappearing post, expiring story/message, account-deletion risk, rolling security logs, temporary share link or short cloud-video retention.
- [ ] **Notify the assigned investigator / agency-authorized preservation requester immediately**; include the exact identifiers and relevant scope so they can contact the provider or lawful custodian using approved channels.
- [ ] **Do not browse a seized person's cloud account**, attempt a password reset, use recovered credentials/tokens, impersonate the account owner, or ask a witness to forward credentials to a personal account.
- [ ] Log **who received the request, when, what was requested, acknowledgment/confirmation, and next responsible owner**. A request being *sent* is **not** evidence that the provider accepted it.

**If a person faces imminent death or serious physical injury:** follow emergency dispatch/command procedures and your agency's designated emergency legal liaison immediately. U.S. law has limited **provider-discretion** emergency disclosure provisions, but an ordinary preservation request does not substitute for that pathway. [18 U.S.C. § 2702(b)(8), (c)(4)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2702&num=0&edition=prelim).

## Choose the actual situation

| What you encounter | Immediate field value | Route for preservation |
| --- | --- | --- |
| **Public social post / profile / livestream / story** | Record exact public URL/handle, observed time, public context and expiry concern; use authorized public capture SOP if available. | Agency preservation liaison for the provider; a screenshot is a supplementary observation, not a provider record. |
| **Private chat / disappearing message** | Record what a lawful witness or visible device shows *without navigating an account beyond your authority*. Identify sender/recipient accounts, platform and time range as available. | Qualified investigator/legal liaison evaluates a targeted provider preservation request; consider endpoint evidence separately. |
| **Cloud photo, file or shared link** | Identify platform, file/share link, owner/tenant when known, permissions/expiration, observed title and time. | Provider and/or lawful data custodian; link alone may expire or fail to give access to original metadata. |
| **Organization account** (Microsoft 365, Google Workspace, school/business) | Identify **tenant**, responsible administrator/records custodian, exact account and retention urgency. | Coordinate with authorized organization custodian, counsel and technical staff; **do not unilaterally change tenant policies**. |
| **Cloud camera, DVR or doorbell clip** | Identify camera ID, location, incident time/timezone, retention window, clip ID, custodian and urgent overwrite risk. | Start the [CCTV/cloud-video preservation workflow](video-preservation.md); refer provider/enterprise-specific retention and legal needs. |
| **Possible account compromise** | Capture what was lawfully reported: account name, alleged activity, time, suspicious notices and who has control. | Notify digital examiner and cyber-response lead; preservation, containment and acquisition are separate decisions. |

**Do not promise scope that is not available.** A provider may not have a particular message, encryption key, expired story, deleted object, login-log period or metadata field. The fact that a user saw content at one moment doesn't establish it remains on the service.

## 1. Identify the correct account and actual data holder

**Similar names are not enough to identify an account.** Collect precise identifiers *as lawfully available*:

- **Platform/service and product**: e.g., a messaging service versus a cloud-drive feature of the same company.
- **Account locator**: exact username/handle with capitalization, profile URL, numeric user/channel/post identifier if directly visible, account email or business tenant ID if properly known.
- **Item locator**: exact post URL, file ID, message/thread ID, shared-link URL, camera ID or folder reference, where supported.
- **Date/time and timezone**: timestamps as displayed, plus **independent observed time** and any known device clock discrepancy.
- **Provenance**: who provided the identifier, from what source, and when; retain only what is justified in the approved case record.

A screenshot of `@examplehandle` is **not proof of account ownership**; one person can rename an account, and two services can use the same handle. Similarly, a custom domain name is not necessarily the organization that holds the underlying account data.

### Consumer provider versus organization custodian

For enterprise accounts, data may be controlled by a **lawful organizational custodian** (employer, school, government agency) using a third-party cloud vendor. SWGDE 23-F-004-1.1 §§4, 6–9 distinguishes providers, lawful custodians and enterprises. Identifying **who can place an authorized hold** is part of preservation.

- Ask the investigator to identify the lawful custodian and whether contacting them could jeopardize the investigation.
- A public-facing service name alone does not tell you who can preserve the exact data, or who may be notified about legal process.
- Requests involving employee/student/health information can have **additional privacy and access constraints**. Route through legal and the custodian's approved processes; this article grants no cross-department access.
- Do **not** ask a school or enterprise administrator to quietly browse an employee/student mailbox or export account contents outside their authorized policy/legal scope.

Microsoft notes that enterprise requests may be redirected to enterprise customers and that customers often receive notice. [Microsoft Government Requests for Customer Data](https://www.microsoft.com/en-us/corporate-responsibility/reports/government-requests/customer-data).

## 2. Preservation is not production

| Event | What it means | What it **does not** mean |
| --- | --- | --- |
| **Officer identifies the target** | Case has names/IDs and time range for preservation referral. | No data has been frozen, obtained or authenticated. |
| **Agency transmits a preservation request** | A request was sent via an approved mechanism. | The provider has necessarily received, accepted or executed it. |
| **Provider confirms preservation** | Provider indicates it set aside applicable existing data within acknowledged scope. | All requested data exists, will be disclosed, includes future messages or lasts indefinitely. |
| **Legal process / qualifying consent established** | Authorized path for obtaining defined information may proceed. | Every category is obtainable under one process or from one party. |
| **Production/export received** | Files/records have been delivered or acquired. | The contents are complete, in-scope, intact and usable without verification. |

### U.S. federal preservation rule — qualified overview

Under **18 U.S.C. § 2703(f)**, a qualifying provider of electronic communication/remote computing services must preserve records/evidence already **in its possession** upon a **governmental entity's request** pending lawful process. The statutory retention period is **90 days**, extendable by **an additional 90 days** on a renewed government request. [U.S. House Office of the Law Revision Counsel, §2703(f)](https://uscode.house.gov/us/usc/119-118/t18/s2703/).

**Four traps:**

1. **Preservation does not authorize disclosure.** Obtaining content/non-content information requires its own valid legal basis and process, determined with counsel.
2. **Not prospective monitoring.** A preservation request doesn't generally compel the provider to retain information **created after** the request; Google's published policy says the same. [Google Requests for User Information FAQ](https://support.google.com/transparencyreport/answer/9713961?hl=en).
3. **Not every party or data set is covered the same way.** Agency counsel must determine whether §2703(f), another legal mechanism or an authorized internal records hold applies.
4. **Not an automatic 180-day guarantee.** Record provider confirmation, **actual covered records and dates**, and arrange renewal **before** expiry. A renewal may extend the period another 90 days; don't rely on the mere passage of time as proof of preservation.

This is a **U.S. federal legal reference**, not advice that every officer may independently direct preservation, and not a substitute for state law, counsel or agency SOP. Provider processes and notification policies can change.

## 3. What to send to your agency preservation liaison

Fill in only data **lawfully established** and necessary to target the request. This is an **internal referral worksheet**, **not** a provider-ready §2703(f) letter or search warrant:

```text
INTERNAL PRESERVATION REFERRAL — FICTIONAL TEMPLATE
Case / agency contact:
Officer / unit / supervisor:
Basis for requesting preservation / authorized purpose:
Provider AND exact product/service:
Individual account identifiers and source of each:
Specific content identifiers (URL, file ID, post ID, channel/camera ID):
Relevant start/end timestamps WITH timezone:
Urgency (auto-delete, story expiry, short retention, link deadline):
Source of observation: directly observed / witness / custodian:
Existing endpoint/physical-device association (if lawfully known):
Enterprise tenant / lawful custodian and contact (if applicable):
Potential sensitivity (juvenile, employee, student, medical, etc.):
Known risk of tipping off subject by contacting custodian:
Requested scope: existing relevant records only; no future monitoring:
Appropriate legal/process reviewer and approval status:
Time referred and receiving investigator/liaison:
Acknowledgment / provider ticket reference, if received:
Requested expiry / renewal follow-up owner:
Known unavailable data / assumptions requiring verification:
```

**Do not paste actual identifiers, records or case details into Hashimoire, GitHub, chat assistants or personal accounts.** Store the worksheet in approved investigative systems.

### Example — expiring social story (fictional)

> At 21:14 CDT an officer receives a witness's report of a public story on `@exampleaccount` that may disappear overnight. The witness provides the exact visible URL and a screenshot, whose collection/source is logged. The officer documents **what the witness claims**, records independent time/timezone, and refers the exact account/URL plus incident window to the agency's authorized preservation liaison. The officer does not attempt to log in as the account owner or promise the screenshot represents the provider's retained original.

### Example — school-managed cloud file (fictional)

> The investigator identifies a relevant cloud-drive link under an educational tenant. Rather than using ordinary administrator privileges to investigate a student's or employee's files, the officer identifies the custodian and contacts agency counsel/authorized records personnel. The preservation route and legal access are separately determined, with any concern about notification recorded. Neither a shared link nor an employee's access permission establishes authority to perform a criminal evidence search.

## 4. Emergency requests, notice and sensitive cases

Some providers have emergency disclosure processes for imminent threats of death or serious injury under **18 U.S.C. §2702(b)(8) and (c)(4)**; those exceptions are **discretionary/provider-evaluated** and legally distinct from ordinary preservation. Route a true emergency through dispatch, incident command, designated agency personnel and provider-approved emergency pathways. Preserve objective supporting facts, precise urgency and legal-review decisions. [Official §2702](https://uscode.house.gov/us/usc/119-118/t18/s2702/).

Providers may notify account holders or enterprise custodians when receiving legal process. If notice could compromise safety or a valid investigation, **consult counsel about lawful restrictions** before contacting a provider or custodian; do not promise secrecy or personally instruct them to conceal a request. [SWGDE 23-F-004-1.1 §8](https://www.swgde.org/documents/published-complete-listing/23-f-004-best-practices-for-digital-evidence-acquisition-preservation-and-analysis-from-cloud-service-providers/).

## 5. Don't lose the provider's response

A preservation acknowledgment is **not** the evidence package. A production is **not** automatically authentic or complete.

When provider records are delivered, the **qualified evidence custodian/examiner**, following process and authority, should:

1. Preserve the original response, cover letter, scope, date/time, account identifiers, service/ticket number and any signed manifest or provided hashes.
2. Secure time-limited download links **promptly** through approved systems. Record link expiration/restrictions and delivery method; a view-only portal may not provide a durable evidence copy.
3. Verify receipt, file counts, categories, time range and relevant available metadata against the process. **If material appears outside legal scope, stop review and seek legal direction.**
4. Hash acquired data at the appropriate scope; compare provider hashes/signatures where available, retain the baseline and create controlled working copies.
5. Record the provider's time standard and distinguish source-service creation/modification times from **download/export times**.
6. Document absent records, gaps, format limitations, inaccessible proprietary formats and any custody or transfer discrepancies.

These post-production steps are **examiner/custodian work**, not justification for a field officer to log in or download account data without specific authority. [SWGDE 23-F-004-1.1 §§10–12](https://www.swgde.org/documents/published-complete-listing/23-f-004-best-practices-for-digital-evidence-acquisition-preservation-and-analysis-from-cloud-service-providers/) and [SWGDE 18-F-002-2.0 §§11–12](https://www.swgde.org/documents/published-complete-listing/18-f-002-2-0/).

## Six common mistakes

1. Treating a preservation email sent as proof the provider accepted or performed the hold.
2. Recording only a display name, without a verifiable account URL/ID and source.
3. Assuming a screenshot, forwarded clip or shared link equals the provider's original record.
4. Assuming an ordinary preservation request covers **future** messages or indefinitely protects existing records.
5. Asking someone to sign in or using an officer's/administrator's unrelated access to "check the cloud" before confirming legal scope.
6. Waiting until the provider's preservation/renewal or temporary download deadline has elapsed without assigning an owner.

## Final handoff — did we answer these?

- [ ] **What** specific platform/account/item is involved and how was it identified?
- [ ] **When** was it relevant, observed and referred, with timezone?
- [ ] **Why urgent** (deleted/expiring content, log rotation, video retention, account closure)?
- [ ] **Who owns next action** (agency liaison, legal reviewer, enterprise custodian, examiner)?
- [ ] **What is the state**: not yet referred / referred / acknowledged / provider-confirmed preservation / produced / verified?
- [ ] **When does the action expire** and who will track renewal, service response and court process?
- [ ] **What wasn't established** (identity, provider, original availability, authority, scope or interpretation)?

See [evidence packaging and examiner handoff](evidence-handoff.md) for the broader custody record and [CCTV/cloud-video preservation](video-preservation.md) for cameras with short retention.

## Published source ledger

| Source | Document / edition | Scope and how used |
| --- | --- | --- |
| [SWGDE — Best Practices for Digital Evidence Acquisition, Preservation, and Analysis from Cloud Service Providers](https://www.swgde.org/documents/published-complete-listing/23-f-004-best-practices-for-digital-evidence-acquisition-preservation-and-analysis-from-cloud-service-providers/) | **23-F-004-1.1**, Jan 13, 2025 | Cloud providers versus lawful custodians; legal authority, preservation, specific identifiers, limited/expiring links, provider production integrity, timestamps. Technical guidance, not legal authority. |
| [SWGDE — Best Practices for Digital Evidence Collection](https://www.swgde.org/documents/published-complete-listing/18-f-002-2-0/) | **18-F-002-2.0**, Nov 20, 2025 | Third-party collection, acquisition changes, preservation of original production, hash and custody documentation. |
| [18 U.S.C. §2703(f), U.S. House Office of Law Revision Counsel](https://uscode.house.gov/us/usc/119-118/t18/s2703/) | Federal statute, consulted Oct 26, 2026 | Government request to qualifying provider; existing evidence retention **90 days + 90 on renewal**; **not** a production order. |
| [18 U.S.C. §2702(b)(8), (c)(4)](https://uscode.house.gov/us/usc/119-118/t18/s2702/) | Federal statute, consulted Oct 26, 2026 | **Discretionary** emergency disclosure for danger of death or serious injury; a separate process from preservation. |
| [Google — Requests for User Information FAQ](https://support.google.com/transparencyreport/answer/9713961?hl=en) | Provider-published online guidance, reviewed Oct 26, 2026 | Preservation covers **information already held**, not prospective data; verified government request systems and legal process. |
| [Microsoft — Government Requests for Customer Data](https://www.microsoft.com/en-us/corporate-responsibility/reports/government-requests/customer-data) | Provider-published online guidance, reviewed Oct 26, 2026 | Enterprise data may be directed to organizational customer; notice and disclosure processes differ from ordinary consumer accounts. |

**Limits:** This article is written for **U.S. law-enforcement first responders** and general evidentiary hygiene. No account, provider, location, consent, court order, user identity or retention schedule is implied. Verify provider processes and statutory editions with agency counsel before sending a formal request.

[← Field Collector](README.md) · [CCTV/cloud video](video-preservation.md) · [Evidence handoff](evidence-handoff.md)
