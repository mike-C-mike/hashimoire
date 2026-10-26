# CCTV, DVR/NVR & Cloud Video — Field Preservation

**Audience:** patrol officers | investigators | evidence technicians  
**Use case:** video identification | urgent preservation | trained export | handoff  
**Risk:** caution  
**Guidance reviewed:** 2026-10-23

> **Time-sensitive:** Many video systems overwrite or purge recordings automatically. The first priority is to **identify the right cameras and time window and initiate preservation immediately**. Do not wait until a later report is finished. Actual export steps depend on authority, training, the recorder/cloud service and agency SOP.

## First 60 seconds: preserve the opportunity

- [ ] Identify **who controls the cameras** (owner, manager, administrator, vendor or authorized custodian) and how to contact them.
- [ ] Record the incident's **best-known time window, date and timezone**; ask for an approved buffer before/after the event.
- [ ] Identify **every likely camera**, including entrances, exits, adjacent angles, hallways, parking areas and cameras showing approach/departure.
- [ ] Ask the custodian **how long footage is retained**, what triggers overwrite/deletion and whether an approved hold or preservation request can be placed immediately.
- [ ] Document the preservation request: person contacted, time (including timezone), requested camera IDs and window, acknowledgement and any limits.
- [ ] If there is imminent deletion, escalate to the assigned investigator/authorized administrator promptly. Preserve through approved systems; avoid changing recorder settings yourself.
- [ ] **Do not assume watching video in a browser preserves a copy.** Viewing is not collection.

## Pick the situation

| Situation | Priority and approach | Important caution |
| --- | --- | --- |
| **Business DVR/NVR** | Identify recorder model, owner and camera IDs; request urgent native export by trained custodian/examiner. | Do not power off, unplug drives, change retention/compression or delete settings without specialist direction. |
| **School / enterprise camera system** | Initiate the organization's approved preservation/hold workflow, with specific camera IDs, times and incident reference. | Viewing permissions and export permissions are different; ask an authorized administrator to handle it. |
| **Cloud-hosted cameras** | Ask account administrator/vendor about immediate hold, export format, expiring share URLs and audit records. | A shared viewing link is not necessarily an enduring evidence copy. |
| **Body-worn / dash camera system** | Follow the program's evidence management/retention and categorization workflow. | Avoid exporting with personal accounts or ad hoc consumer file shares. |
| **Cellphone video or social platform clip** | Preserve source identity, posting context and original file or authorized provider export when possible. | A screen recording, repost or downloaded preview may lose metadata/quality. |

> **Cloud vs. video:** An online viewing link is not the same as preserved records, and a provider preservation request is not legal authority to access account content. For provider-held camera records or organization-owned cloud accounts, cross-check the [cloud and account preservation field guide](cloud-preservation.md) and arrange authorized custodian/legal review.

## 1. Get the *right* footage

**Ask these questions before the export:**

1. Which camera names/IDs cover the incident? Are there alternate perspectives?
2. What date/time range is needed—including reasonable lead-in and departure time?
3. Does the system display local time, UTC, or an unspecified recorder clock?
4. Was the recorder clock correct? Can you compare it to a reliable reference **without changing its settings**?
5. Does the system have an audio track, distinct video streams, or separate associated metadata?
6. When will the earliest requested footage be overwritten, purged or become inaccessible?

### Clock offset example (fictional)

At the scene, a recorder displays **14:17** while a trusted reference is **14:25** in the same stated timezone. The recorder appears **8 minutes slow** at that moment. Record *both observations*, including dates/timezones, how they were obtained, and whether the recorder clock was changed (ideally it was not).

An apparent offset measured later may not apply uniformly to the entire recording; daylight-saving changes, sync failures or timezone configuration can complicate interpretation.

## 2. Preserve immediately, then acquire correctly

- An approved **preservation hold/request** should identify the relevant recorders, camera IDs, start/end range, buffer, time zone, requested audio/metadata and retention urgency.
- When a trained collector exports evidence, **prefer native/proprietary format** with original data and available timestamps/metadata. Obtain the necessary player/codec or vendor documentation to permit later verification.
- If the system offers a second ordinary video format (for example MP4), collect an **additional convenience copy** when authorized and feasible—do not replace the native export solely with a transcoded preview.
- Record export account/operator, method, source system, camera/channel identifiers, requested versus actual time range, filenames and output destination.
- Keep original **sidecar files**, index files, associated audio, export logs and player files together or clearly associated.
- Do not adjust recorder compression, image enhancement, overlay or clock settings to “improve” the earlier recording. Such settings cannot restore lost historic quality.

**Collector boundary:** If you lack training or permission to export, **document and request preservation**; an authorized custodian, technician or forensic video specialist should perform the export.

## 3. Verify before relying on it

For an authorized export, verify on an **approved computer or evidence management system**, using a working copy when appropriate:

- [ ] File(s) exist, with recorded names/sizes and no obvious export error.
- [ ] All intended **camera IDs/channels** and the full required time ranges appear.
- [ ] Playback works with the necessary native viewer or validated player; no unexpected gap in the incident window.
- [ ] Video and audio tracks (if present) are available as expected.
- [ ] The clock display/offset and timezone observations are documented; timestamps have not silently been treated as UTC.
- [ ] Preserve hash values of the exported files/dataset as defined by SOP. Record the hash **scope** (individual file, ZIP, export container or manifest) and tool/version.
- [ ] The exported material and any temporary media are handed to the approved evidence storage process before shared links expire or removable media is reused.

**Verification is not interpretation.** Successful playback and matching hashes do not prove the recorded clock was correct, that every camera existed, or that footage was never edited before export.

## 4. Evidence request & handoff template

```text
Incident / authorization reference:
Requester / organization:
Site and camera-system owner:
System make/model / cloud provider (if known):
Preservation request date/time/timezone:
Contact/acknowledgement:
Requested camera IDs and view descriptions:
Requested event date and start/end times, plus buffer:
Time zone and any observed recorder offset:
Known retention deadline and hold status:
Export operator / account:
Native file format and proprietary player:
Additional convenience export (if any):
Actual camera/time coverage supplied:
Filename(s), byte sizes, hashes and hash scope:
Evidence location, access restrictions and custody:
Missing periods, errors, player issues or limitations:
```

### Worked scenario (fictional)

A store manager says recording retention is approximately **72 hours**. The reported incident occurred at 19:10 local time; the entrance camera and parking lot cameras may show approach and departure. The collector records a request for **18:55–19:30 local time** for the selected cameras, documents the requested hold and manager's acknowledgement, and arranges a trained export. The manager later supplies native video and its proprietary viewer; the receiving examiner checks that every required channel and period plays and notes a separate recorder clock-offset observation.

**Why this matters:** A clip that starts at 19:09 might show the incident but miss the lead-up; a link to footage may expire without warning; and a converted clip may omit original camera metadata.

## Five expensive mistakes

1. Waiting beyond the system's overwrite window because “someone already saw the footage.”
2. Recording only a wall-clock time without timezone, clock source or measured offset.
3. Exporting a short MP4 preview but not the available native/proprietary evidence or viewer.
4. Collecting one camera while adjacent views of approach/departure are overlooked.
5. Treating a view-only link or unverified thumb drive as a preserved evidence package.

## Related guidance and sources

- [Evidence packaging, custody and handoff](evidence-handoff.md).
- [Collector home](README.md).
- [SWGDE 17-V-002-1.4 — Best Practices for Data Acquisition from Digital Video Recorders](https://www.swgde.org/documents/published-complete-listing/17-v-002-1-4/).
- [SWGDE 18-F-002-2.0 — Best Practices for Digital Evidence Collection](https://www.swgde.org/documents/published-complete-listing/18-f-002-2-0/).

**Privacy note:** Never upload protected or investigative video to this public website. Follow legal authority, retention, FERPA/CJI/privacy requirements as applicable, and agency procedures.
