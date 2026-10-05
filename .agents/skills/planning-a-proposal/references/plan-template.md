# Proposal plan template

Verified 2026-10-04. Read the main `SKILL.md` first. Copy this template, fill
every field, and write "unknown" rather than guess. Each rule names the skill
or source behind it.

Save the filled plan with the proposal, such as in the proposal's folder or
repository. Never save it in a shared skill. It names people, salaries, and
unpublished ideas.

```markdown
# Proposal plan: <short working title>

Date: <YYYY-MM-DD>. Re-check the funding opportunity and IU deadlines if this
plan is older than a month.

## The opportunity

| Question | Answer |
| --- | --- |
| Sponsor and program | <e.g. NIH, NIA; or NSF, a directorate and program> |
| Funding opportunity number and URL | <NOFO, solicitation, or call; read it end to end> |
| Activity code or mechanism | <e.g. R01, R21, K23, NSF standard grant> |
| Clinical trial allowed? | <required / optional / not allowed / n.a.> |
| Sponsor deadline, time, and time zone | <date, 5:00 PM local time of the applicant organization for NIH> |
| New, resubmission, or renewal | <A0 / A1 / renewal / NSF new> |
| Limited submission? | <yes: IU internal competition date / no> |
| Budget ceiling and project period | <from the opportunity> |
| Program officer contacted? | <date and gist, or not yet> |
| Study section or panel (likely) | <from NIH RePORTER or the CSR roster; see `finding-funding-opportunities`> |

## Fit and go/no-go

- Why this opportunity fits the question: <one or two sentences, the researcher's own>
- Eligibility checked (PI status at IU, career stage, citizenship if required): <yes / question for pre-award>
- Overlap with current or pending support: <none / describe; see `assembling-required-documents`>
- Decision: <go / wait for next cycle / different opportunity>, on <date>

## Team

| Person | Role on the proposal | Institution | Effort (person months) | Biosketch | Other Support |
| --- | --- | --- | --- | --- | --- |
| <name> | PD/PI | IU | <PM> | <started / certified> | <started / certified> |
| <name> | Key personnel / Other significant contributor / consultant | <inst> | <PM or n.a.> | ... | ... |

Multiple PI? <yes: leadership plan needed / no>
Subawards? <list sites; each needs its own documents from its sponsored-programs office>

## Science (the researcher's own words)

- Question and central hypothesis: <researcher writes>
- Aims, one line each: <researcher writes>
- Preliminary data in hand: <list; see `using-preliminary-data-and-feasibility`>
- Preliminary data still needed, and by when: <list>

## Data, subjects, and compliance

| Question | Answer | Skill |
| --- | --- | --- |
| Human subjects? Exempt or non-exempt? | <answer> | `assembling-required-documents` |
| Clinical trial by NIH's definition? | <answer from the four questions> | `assembling-required-documents` |
| IRB status | <not yet / submitted / approved, protocol on file> | `assembling-required-documents` |
| Vertebrate animals? | <yes / no> | `assembling-required-documents` |
| Data generated, and where it will be shared | <for the DMS plan> | research-data `planning-data-management-and-sharing` |
| Data obtained under an agreement (DUA, biobank, registry) | <names and limits> | research-data `accessing-health-and-clinical-data` |
| Data classification and computing | <classification; systems> | research-technologies `planning-research-computing-work` |
| Foreign components, export control, conflicts of interest | <answer> | `routing-and-submitting-at-iu` |

## Budget sketch

- Direct costs per year (rough): <amount>; modular or detailed: <which>
- $500,000 or more direct costs in any year? <yes: discussed with the program officer on <date> / no>
- Core facility and service costs: <list, with quotes requested>
- Cost sharing: <none / mandatory per the opportunity / voluntary, needs approval>
- Pre-award contact building the budget: <name or "to be assigned">

See `budgeting-a-proposal`.

## Documents

| Document | Owner | Due to me | Status |
| --- | --- | --- | --- |
| Specific Aims | PI | <date> | |
| Research Strategy | PI | <date> | |
| Biosketches (Common Form via SciENcv) | each key person | <date> | |
| Current and Pending (Other) Support | each key person | <date> | |
| Facilities and Other Resources | PI with department | <date> | |
| Equipment | PI | <date> | |
| Data Management and Sharing Plan | PI | <date> | |
| Human subjects and clinical trial information | PI | <date> | |
| Letters of support | each letter writer | <date> | |
| Budget and justification | PI with pre-award | <date> | |
| Subaward documents | each site's office | <date> | |
| Other attachments the opportunity requires | | | |

See `assembling-required-documents` for what each one needs.

## Timeline

Paste the output of `scripts/backward-timeline.py` here, then adjust.

## Reviews before submission

- Internal reviewers for Aims: <names, date>
- Internal reviewers for full draft: <names, date>
- Mock study section or school review program: <yes, date / no>

## After submission

- Where to watch status: eRA Commons (NIH) or Research.gov (NSF)
- Expected review and council dates: <from the NIH standard due dates page>
- Just-in-Time items likely needed: <IRB approval, Other Support updates>
- Resubmission plan if not funded: see `responding-to-reviews-and-resubmitting`
```

Notes on filling it in:

- The opportunity table comes from the funding opportunity, not memory.
  `finding-funding-opportunities` explains how to read one.
- The IU internal deadline and routing steps come from
  `routing-and-submitting-at-iu`.
- Person months are effort times appointment months. `budgeting-a-proposal`
  shows the arithmetic.
- Leave the Science section to the researcher. An agent may restate it, but
  never supply it.
