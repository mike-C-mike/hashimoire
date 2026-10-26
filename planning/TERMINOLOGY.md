# Editorial Terminology — Evidence Items, Artifacts, and Findings

**Audience:** Hashimoire authors, reviewers, and contributors  
**Purpose:** Consistent internal vocabulary across Field Collector, Examiner, snippets, and worked case examples  
**Adopted:** October 26, 2026  
**Status:** Editorial convention, **not** a new legal or forensic-science definition

> **Our working language:** **Evidence** (capital E) refers to the formally collected and submitted items or datasets. **Artifacts** are the traces and records identified through examination. **evidence** (lowercase e) refers in our analytical writing to the *support for or against a proposition* that develops as artifacts are interpreted in context. We do not start with a story and hunt for convenient proof. We let the artifacts shape—and, when necessary, overturn—the working explanation.

**Important qualification:** These capitalization choices are a **Hashimoire house convention**, not legal definitions or mandatory courtroom capitalization. SWGDE defines *digital evidence* broadly as information with probative value in binary form and a computer-forensic *artifact* as device-created information/data reflecting past activity. An artifact **can itself be admissible or probative digital evidence**. In this guide, lowercase **evidence** means the factual support (or counterevidence) we develop from observations; it does **not** mean a claim has been conclusively proven, that a particular person acted, or that conduct was illegal. In court documents or required agency forms, follow the applicable terminology.

## Preferred terms

| Use this term | What we mean within Hashimoire | What we avoid assuming |
| --- | --- | --- |
| **Evidence / Evidence Item** | **Capital E**, by our house convention: the **formally collected or submitted item/source** under custody, such as a phone, laptop, USB drive, forensic image or provider production. Specify *physical item* versus *digital submission* rather than treating them as identical. | That everything in the submission has been examined, is relevant, or supports an allegation. |
| **Acquisition / forensic image / exported dataset** | The collected logical/physical image or provider export, with its own identifier, scope, hash(es), tool/version and custody. This is distinct from the original physical item. | That a verified copy is necessarily complete or that hashing establishes provenance. |
| **Artifact** | A trace or record identified during examination: a Prefetch entry, event log, registry value, browser entry, message database row, or file metadata. It is a **lead/observation**, not a prewritten conclusion. | That its mere presence proves execution, intent, ownership, attribution or a criminal act. |
| **evidence** | **Lowercase e**, in Hashimoire's analytical narrative: the **supporting or challenging basis** for a proposition that develops as artifacts are examined and contextualized. Multiple artifacts may form a stronger account; a single reliable source may support a narrow fact. | That support equals conclusive proof, that a crime occurred, or that conflicting information should be ignored. |
| **Observation** | What a specific artifact **actually contains or reports**, including source path, field, raw value, timestamp and the method used to interpret it. | That the reported field is independently true or that a parser is infallible. |
| **Hypothesis** | A **testable explanation** grounded in observed artifacts and the authorized investigative question. Record competing explanations and look for **disconfirming** as well as corroborating information. Revise or reject it as findings develop. | Choosing a story first and cherry-picking artifacts that fit it. |
| **Corroboration / contrary indication** | Another sufficiently independent source that supports, qualifies or challenges the proposed explanation. | That two tools reading the **same underlying database** constitute two independent corroborating sources. |
| **Finding** | A documented, reproducible determination **supported by identified observations and stated limits**. Some findings can come from one sufficiently reliable artifact; complex claims generally need more. | That every finding proves a crime or identifies a particular human actor. |
| **Opinion / conclusion** | A reasoned assessment permitted by agency policy, the examiner's expertise and the evidentiary support, including uncertainty/alternatives. | Overclaiming intent, identity, causation or definitive absence of activity. |

Use **record**, **trace**, or **artifact** when describing a specific recovered data element. Use **evidence** where it is appropriate under accepted legal/scientific usage; never rewrite quotations from standards or official evidence forms to match our house terminology.

## The reasoning model

```text
Collected / Submitted Evidence (capital E)
    ↓ documented acquisition, scope, custody and integrity
Acquired Data / Working Copy
    ↓ examination and validation
Artifacts → specific Observations
    ↓ notice patterns, gaps and contradictions before settling on a story
Testable Hypothesis A / Alternative B / Alternative C
    ↔ seek further artifacts that SUPPORT or CHALLENGE each
    ↓ evaluate the full record, including contrary observations
evidence (lowercase e): support for / against specific propositions
    ↓ reason only as far as that support allows
Findings / Qualified Conclusions
    ↓ explain both what is established and what remains unresolved
```

**This is iterative, not a one-way conveyor belt.** An investigation normally arrives with a legitimate **question or allegation**; that sets scope, not the desired answer. A preliminary hypothesis can exist, but we should not write the conclusion in advance. An artifact can overturn a working explanation. A single artifact may support a narrow finding while failing to support a larger theory. Document exculpatory, contradictory and ambiguous material as deliberately as corroborating material. **Finding no support is an acceptable outcome.**

### Worked example — fictional Windows intrusion

| Layer | Example | Appropriate wording |
| --- | --- | --- |
| Evidence (capital E) | Agency-submitted laptop, Item 004 | “I examined a verified forensic working copy of Evidence Item 004.” |
| Artifact A | Security.evtx, Event 4688 | “An event records a PowerShell process created at the specified time.” |
| Artifact B | Sysmon Event 1 | “Sysmon records that process and attributes Word as the parent.” |
| Artifact C | Sysmon Event 3 | “Sysmon records a connection associated with that process's ProcessGuid.” |
| Artifact D | Prefetch entry | “The Prefetch artifact contains launch-related information consistent with PowerShell execution.” |
| Hypothesis | Word-initiated activity resulted in a network connection | “These artifacts raise the question whether document-driven execution caused the observed connection.” |
| evidence (lowercase e) | Corroborated observations about process creation and network activity, assessed against missing/conflicting data | “The combined observations support the narrowly stated process-and-connection finding; they do not establish intent.” |
| Disconfirmation / alternative | Legitimate Word automation, unreliable clock, wrong-process correlation, missing network telemetry | “I sought facts that might weaken or refute the initial hypothesis and documented what was not resolved.” |
| Finding | Supported process relationship/connection | “The examined records support that a PowerShell process, with Word reported as its parent, initiated a recorded outbound connection.” |
| Not established | Human identity, malicious purpose, data transferred | “These artifacts alone do not establish the operator, intent or exfiltration.” |

The point isn't that each artifact is meaningless in isolation. **Each artifact has a particular evidentiary reach**, and the examiner's reasoning should stay within that reach.

## Writing and courtroom-language examples

**Preferred (physical item):** “Evidence Item 004, a laptop, was submitted for examination. An acquired working copy was verified against the documented image integrity values.”

**Preferred (discovered artifact):** “During examination of Item 004, I identified a Windows Security event-log artifact. The record reports the creation of a process at the specified timestamp.”

**Preferred (hypothesis):** “That observation raised the hypothesis that the document application initiated the scripting process. I examined available process creation, Prefetch and network records to test it.”

**Preferred (finding):** “The available artifacts, assessed together as evidence for the limited process-and-connection finding, are consistent with the reported process relationship and outbound connection. Source logs, contradictory observations, timestamps and exceptions are recorded.”

**Avoid:** “I knew the suspect stole files, so I searched until I found logs proving it.”

**Avoid:** “I found an artifact that proves the subject ran malware and stole files.”

**Avoid:** “Artifacts are never evidence in court.” This is scientifically and legally too absolute, and conflicts with established broad definitions of digital evidence.

**Avoid:** “Three tools confirmed it” when they all parsed **the same raw event**. Name the underlying sources, not just the tools.

**Avoid:** “No artifacts were found, therefore the activity did not occur.” Absence may reflect coverage, retention, collection scope, privilege, application configuration, parsing or artifact lifecycle.

## A standard artifact-to-finding note

```text
Evidence Item ID / collected source:
Acquisition/working copy ID, method and hash scope:
Question / scope / initial hypothesis:
Artifact name and exact source path / record identifier:
Original observed data (field names, raw values, native timestamp):
Parser or examination method and tool/version:
Interpretation, with OS/app-version and time-zone assumptions:
Other independent sources checked:
Support for each hypothesis (lowercase-e evidence):
Disconfirming findings / competing explanations actively tested:
Supporting artifacts or observations:
Conflicting, missing or unavailable material:
Alternative explanations considered:
Hypothesis supported / weakened / unresolved:
Finding (limited to supported facts):
Confidence and known limitations:
Exhibit/output IDs, custody and reviewer:
```

For public examples, all case/item numbers, IDs, account information and outputs must be **synthetic**, explicitly labeled as such.

## Editorial rules for new and revised articles

1. Use **Evidence** (capital E) for a collected/submitted source or item within our prose, preferably **Evidence Item** when identifying it; clarify physical original versus digital submission, image and derivative.
2. Call individual traces **artifacts** and describe their **observed content** before interpreting. Use lowercase **evidence** for the support/contradiction those observations provide for specific propositions—not as shorthand for established guilt.
3. Organize by **investigative question**, not by a shopping list of artifacts. Each artifact page should specify both useful inferences and unsupported claims.
4. **Guard against confirmation bias:** don't select a conclusion and search only for confirming artifacts. Treat an initial allegation as a question. Seek disconfirming data, competing hypotheses, contradictions and missing sources; revise or reject explanations when appropriate.
5. Don't turn a parser field into a courtroom conclusion without addressing source integrity, version, clock, retention, acquisition scope and corroboration.
6. Differentiate **observed**, **consistent with**, **supports**, **cannot determine** and **concluded**; avoid `proves` unless the precise claim and its basis justify it.
7. Acknowledge that **an artifact may itself be digital evidence** under established scientific/legal usage. Upper/lowercase distinctions clarify analysis and custody; they **do not** redefine admissibility or legal standards of proof.
8. Follow agency procedures, current SWGDE best practices and court/jurisdiction terminology where those requirements differ. Do not rewrite statutory terms or standard quotations.

## Published references

- [SWGDE Digital & Multimedia Evidence Glossary, 05-F-001, version 3.0 (June 23, 2016)](https://www.swgde.org/documents/published-complete-listing/05-f-001-swgde-digital-multimedia-evidence-glossary/) — published broad definitions of *artifact* and *digital evidence*; these definitions do **not** establish our capitalization convention.
- [SWGDE Best Practices for Computer Forensic Examinations, 18-F-001-2.0 (2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) — data analysis, interpretation of recovered material, reproducible/defensible methods, and conclusions supported by the data.
- [SWGDE Requirements for Report Writing in Digital and Multimedia Forensics, 18-Q-002-1.0 (2018)](https://www.swgde.org/documents/published-complete-listing/18-q-002-swgde-requirements-for-report-writing-in-digital-and-multimedia-forensics/) — clear results, source/item identification, documentation, and bases for included opinions/conclusions.

**Source review date:** October 26, 2026. These sources support disciplined terminology and reporting; the particular **Evidence Item / Artifact** separation in this guide is **Hashimoire's chosen editorial convention**, not a rule SWGDE requires of every examiner.

[Architecture and publication standards](ARCHITECTURE.md) · [Windows investigation example](../docs/windows/timelines.md) · [Examiner Toolkit](../examiner/README.md)
