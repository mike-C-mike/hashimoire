# Phishing Email Investigation Playbook

**Use case:** triage | response | validation  
**Environment:** cloud | windows | macos  
**Risk:** safe | caution  

> **Caution:** Do not click links, open attachments, reply to the sender, or forward suspicious emails normally unless your process explicitly calls for it. Normal forwarding can change evidence and increase risk.

---

## Purpose

This playbook provides a repeatable workflow for handling suspicious email reports, starting with what an end user should look for, how they should safely report the message, and how the security team should validate, investigate, and respond.

It is designed to reduce accidental interaction with malicious content, preserve useful evidence, and give the security team a clean path to determine whether the message is spam, phishing, malware delivery, business email compromise, or a benign false positive.

---

## When to use

Use this playbook when:

- A user reports a suspicious email
- A suspicious message is found in a shared mailbox
- A message appears to impersonate a trusted sender, vendor, executive, school, or internal department
- An email includes unexpected links, attachments, login prompts, urgency, payment pressure, or requests for credentials
- Multiple users report similar emails, suggesting a wider campaign

---

## Preconditions / permissions

Before proceeding, confirm:

- Users know how to report suspicious emails safely
- The reporting path is documented, such as a SOC mailbox, phishing mailbox, help desk queue, or mail security team
- The security team has approved tooling or process for:
  - reviewing email headers
  - examining links
  - detonating attachments
  - searching the mail environment
  - blocking or removing malicious messages
- Staff handling analysis understand evidence handling requirements for your environment

---

## Inputs needed

### From the reporting user
- The suspicious email itself
- Time received
- Whether the user opened the email
- Whether the user clicked any links
- Whether the user opened any attachments
- Whether the user entered credentials or responded
- Why the message seemed suspicious

### From the environment
- Message headers
- Message ID if available
- Mail trace or mail security platform logs
- Delivery scope, including how many users received it
- Indicators such as sender domain, reply-to, URLs, and attachment names or hashes

---

## Step-by-step workflow

# 1. End user recognition and safe response

## What a user should look for

Users should pause and review the message for common warning signs, including:

- Sender name does not match the actual email address
- Strange reply-to address
- Unexpected invoice, file share, voicemail, fax, password expiration, or document request
- Pressure to act quickly
- Threats, urgency, or secrecy
- Links that do not match the company or service they claim to represent
- Unexpected attachment types
- Requests for login credentials, MFA codes, gift cards, wire transfers, or sensitive information
- Typos, awkward wording, or odd branding
- A message that feels slightly off or inconsistent with normal communication

A user does not need to prove an email is malicious. If it is suspicious, that is enough to report it.

## What the user should do

The safest user actions are:

1. Do not click links
2. Do not open attachments
3. Do not reply
4. Do not forward it normally unless instructed by policy
5. Report it using the approved method

Preferred reporting methods:

- Use the organization’s phishing-report button if available
- Forward the email **as an attachment** to the designated security or spam-analysis mailbox
- Contact the help desk or security team and note whether any interaction already happened

## Why forward as an attachment

Forwarding a suspicious email **as an attachment** is preferred because it better preserves the original message in a form closer to what was actually received.

Advantages include:

- Preserves more of the original header information
- Retains routing details useful for analysis
- Reduces the chance of altering the message body in transit
- Makes it easier for analysts to inspect the original email safely in a controlled environment
- Avoids mixing the suspicious content into a new email body as part of a normal forward
- Helps mail security teams import or analyze the original artifact with less loss of context

A normal forward can preserve the user’s concern, but it often strips away pieces of the message analysts actually care about.

## What the user should include in the report

The user should include:

- “Suspicious email received”
- Whether they clicked anything
- Whether they opened any attachment
- Whether they entered credentials
- Whether anyone else mentioned getting the same message

Example user report language:

> I received this email and it looks suspicious. I did not click the link or open the attachment. Forwarding as an attachment for review.

If the user already interacted:

> I clicked the link before realizing it looked suspicious. I did not enter credentials. Forwarding the original as an attachment for review.

If credentials were entered:

> I clicked the link and entered my credentials before realizing it may be phishing. Forwarding the original as an attachment for review.

If credentials were entered, the issue should be treated as a potential account compromise rather than a routine suspicious-email review.

---

# 2. Intake and initial triage by security team

When the security team receives a suspicious email report:

1. Confirm receipt
2. Determine whether the user interacted with the message
3. Preserve the email artifact
4. Extract relevant indicators
5. Decide whether this is:
   - spam
   - phishing
   - credential harvesting
   - malware delivery
   - impersonation / BEC attempt
   - benign but suspicious-looking legitimate email

## Immediate priority questions

Answer these first:

- Did the user click the link
- Did the user open the attachment
- Did the user enter credentials
- Did the attachment execute
- Did other users receive the same email
- Is the sender impersonating an internal person or trusted vendor

If there was user interaction, shift immediately from simple triage to potential incident response.

---

# 3. Analyst review and evidence preservation

## Preserve the original

Security should preserve:

- Original attached email file if provided
- Full headers
- Subject line
- Sender and reply-to
- Message ID
- Timestamps
- URLs
- Attachment names and hashes
- Screenshots if needed for awareness or ticket documentation

## Review headers

Check for:

- Return-Path
- Reply-To
- Received chain
- SPF results
- DKIM results
- DMARC alignment
- Display-name spoofing
- Lookalike or newly registered domains
- Mismatch between visible sender and envelope sender

Headers still matter, but they often provide less direct attribution value than they did in the past. Modern mail providers and secure mail gateways commonly rewrite, mask, or replace infrastructure details during message handling. In many cases, identifiers such as the apparent originating IP address may reflect the sending platform or relay service rather than the original sender system. For example, a message sent through Gmail may show infrastructure that resolves back to Google rather than to the actor who composed the email.

Because of that, headers should be treated as one source of context, not as a standalone truth source for attribution. They are most useful for understanding message path, authentication results, sending platform, domain alignment, and whether the message behavior matches what is expected for that sender.

Do not rely on SPF, DKIM, or DMARC alone. A message can authenticate and still be malicious, especially in cases involving compromised vendors, abused bulk-mail platforms, or business email compromise using legitimate accounts.

## Review links

Check:

- Visible URL text versus actual destination
- Redirectors
- URL shorteners
- Lookalike domains
- Unusual subdomains
- Credential harvesting pages
- Recently registered domains if that intelligence is available through approved tooling

Inspect links in a safe workflow only.

## Review attachments

Check:

- File extension
- Double extensions
- Macro-enabled documents
- Password-protected archives
- Executables or script files
- Embedded lures such as invoices, payroll notices, or voice messages
- File hashes in malware or threat intel tooling

If attachment detonation is available, analyze in an isolated environment.

---

# 4. Scope determination

Determine whether the message was targeted or broadly distributed.

Questions to answer:

- How many recipients got the message
- Was it delivered only externally or also internally
- Did any mailbox rules or security tools already flag it
- Were similar messages delivered earlier or later
- Are there matching subjects, sender patterns, URLs, or attachments in the environment

Useful searches may include:

- subject line matches
- sender domain matches
- URL matches
- attachment hash matches
- message trace by sender or timestamp

This is where a one-user report can quickly become a campaign investigation.

---

# 5. Decision points

## If the message is benign
- Close as false positive
- Notify the user
- Optionally document why it was legitimate so similar reports can be resolved faster later

## If the message is spam but low risk
- Block or tune filtering if appropriate
- Remove copies if necessary
- Document recurring indicators

## If the message is phishing or malicious
- Block sender, domain, URL, or hash as appropriate
- Remove or quarantine matching messages
- Identify affected users
- Reset credentials if harvested
- Review sign-in logs if credentials may have been compromised
- Check for mailbox rule creation or account abuse
- Escalate to incident response if malware execution or account compromise is suspected

## If the message is impersonation / BEC
- Notify relevant stakeholders quickly
- Watch for payment fraud, payroll diversion, or gift card follow-on attempts
- Search for related conversation hijacking or thread takeover
- Review whether the impersonated identity has been abused elsewhere

---

## Commands / actions by platform or function

These will vary by environment, but common analyst actions include:

### Mail platform actions
- Search for similar messages across mailboxes
- Pull message trace
- Remove messages from user mailboxes
- Block sender or domain
- Block URLs or attachments where supported

### Identity / account actions
- Force password reset
- Revoke sessions
- Review MFA status
- Check recent sign-in activity
- Review new inbox rules or forwarding rules

### Endpoint actions

If the user opened an attachment or clicked through:

- Review browser history
- Check downloads
- Check process execution
- Review EDR alerts
- Isolate host if needed
- Collect relevant endpoint artifacts if escalation is warranted

---

## Validation / expected output

At the end of triage, the analyst should be able to state:

- What the email was
- Whether it was malicious, suspicious, or benign
- Whether any user interacted with it
- Whether multiple users received it
- What indicators were identified
- What containment actions were taken
- Whether escalation is required

Example outcomes:

- “Confirmed phishing, credential harvesting page, delivered to multiple users, clicks observed, credential reset completed, messages removed.”
- “Spam advertisement, no malicious payload identified, no user interaction, no further action needed.”
- “Potential BEC lure impersonating finance contact, blocked and escalated for broader review.”

---

## Escalation / containment

Escalate when:

- Credentials were entered
- Attachment executed or likely executed
- Malware was detected
- A privileged account was targeted or compromised
- Multiple users interacted with the campaign
- The message is tied to active threat activity or a broader compromise
- Financial fraud or data exposure risk exists

Containment options may include:

- Mailbox purge
- Domain or sender block
- URL block
- Attachment hash block
- Password reset
- Session revocation
- Host isolation
- User notification campaign
- Executive or finance team alerting in BEC scenarios

---

## Notes for user awareness and training

Keep user guidance simple:

- Stop
- Do not click
- Report it
- Forward as attachment if required by process
- Tell security if you already interacted

Users do not need to be email analysts. They just need to avoid turning a suspicious email into an actual incident.

---

## Example lightweight workflow summary

### User
- Sees suspicious email
- Does not click or open
- Forwards as attachment or uses report button
- Tells security whether any interaction happened

### Security team
- Preserves original email
- Reviews headers, links, and attachments safely
- Searches environment for additional recipients
- Determines maliciousness and scope
- Contains and escalates if necessary
