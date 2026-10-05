---
name: planning-a-proposal
description: Start and plan a grant proposal at Indiana University, from idea to submission. Collects the funding opportunity, mechanism, deadline, team, compliance questions, and budget shape, then builds a timeline backward from the sponsor deadline through IU's internal deadline (9 a.m., four business days before) with a script, and fills in a proposal plan template. Covers NIH due dates, the late window, the end of continuous submission, the six-application limit, NIH's rule on AI-developed applications, and when to involve pre-award, program officers, and reviewers. Points to the other proposal skills for each part. Use when someone says they want to apply for a grant, names a deadline, asks what to do and when, or starts any new proposal. Start here.
---

# Planning a proposal

Verified 2026-10-04 against NIH Grants and Funding pages, the NSF PAPPG, and
IU Research pages. Sources are listed at the end.

This skill ties the other proposal skills together. It decides what has to
happen, in what order, and by when. The other skills say how to do each
part.

Settle the opportunity and the deadline before anything else. A strong
proposal sent to the wrong opportunity, or a day late, is not reviewed.

## Keep the science with the researcher

The researcher owns the question, the aims, the hypotheses, and the results.
An agent using these skills plans, explains rules, computes, and checks. It
does not write the science.

**Required.** "NIH will not consider applications that are either
substantially developed by AI, or contain sections substantially developed by
AI, to be original ideas of applicants," per NOT-OD-25-132. NIH adds that AI
"may be appropriate to assist in application preparation for limited aspects."
Detected misuse after award may be referred to the Office of Research
Integrity.

**External.** NSF encourages proposers "to indicate in the project
description the extent to which, if any, generative AI technology was used,"
per its December 2023 notice.

**Required.** Do not paste proposal text into a generative AI service that
IU has not approved for that data. Per KB0025830, providing "grant
proposals" to such services "is the same as posting the information on a
public website." It lists "sharing grant proposals still under review" as an
unacceptable use. KB0026817 covers AI tools with research data.

## Collect the facts

Ask for what the request leaves out. Do not guess a deadline or a mechanism.

| Ask | Why it matters | Skill |
| --- | --- | --- |
| Which sponsor and funding opportunity? Its number and URL? | The opportunity sets every rule | `finding-funding-opportunities` |
| New, resubmission, or renewal? | Changes due dates and required sections | `responding-to-reviews-and-resubmitting` |
| Sponsor deadline, time, and time zone? | Drives the timeline | This skill |
| Is it a limited submission? | IU's internal competition comes first, often months earlier | `finding-funding-opportunities` |
| Who is PI, and is anyone a multiple PI? | Eligibility, application limits, leadership plan | `routing-and-submitting-at-iu` |
| Who else is on the team, and where? | Biosketches, Other Support, subawards, letters | `assembling-required-documents` |
| Human subjects, clinical trial, animals, foreign components? | Extra forms, approvals, and lead time | `assembling-required-documents` |
| Rough budget and years? | Modular or detailed, cores, subawards | `budgeting-a-proposal` |
| What preliminary data exist? | Feasibility, and whether this cycle is realistic | `using-preliminary-data-and-feasibility` |
| What data will be used or generated? | DMS plan, data agreements, computing | research-data and research-technologies skills |
| Who is the unit's grant administrator? | Builds the budget and routes in KC | `getting-help-with-proposals` |

## Deadlines

### NIH standard due dates

**Required.** Unless a NOFO sets its own dates, NIH uses standard due dates,
per the NIH standard due dates page:

| Activity | New | Renewal, resubmission, revision |
| --- | --- | --- |
| R01 and similar | February 5, June 5, October 5 | March 5, July 5, November 5 |
| R03, R21, R33, R34 | February 16, June 16, October 16 | March 16, July 16, November 16 |
| K career awards | February 12, June 12, October 12 | March 12, July 12, November 12 |
| Individual F fellowships | April 8, August 8, December 8 | Same |

**Required.** NIH no longer has separate AIDS due dates, per the standard due
dates page and NOT-OD-26-029.

**Required.** Applications are due by 5:00 PM local time of the applicant
organization. If a due date falls on a weekend or federal holiday, it moves
to the next business day, per the NIH standard due dates page. The timeline
script's `--rolls-forward` flag applies this.

### Late applications and continuous submission

**Required.** For due dates on or after May 25, 2026, NIH accepts late
applications "within two calendar weeks of the original due date," with a
cover letter explaining the delay, per NOT-OD-26-064. Only the PD/PI's own
extenuating circumstances count. Late submission is not allowed for
fellowships, small business applications, international collaboration
applications (PF5, UF5), and any NOFO that says so.

**Required.** NIH ended its Continuous Submission policy, per NOT-OD-26-064.

**Recommended.** Plan for the real deadline. The late window is for
emergencies, and IU's internal deadline still applies to a late application.

### IU's internal deadline

**Required.** The KC Proposal Development Document must be "received at ORA
by 9 a.m. four (4) business days before the funding sponsor's deadline," per
the IU Research routing page. `routing-and-submitting-at-iu` explains the
policy behind it and an open item about it.

## Application limits

**Required.** NIH accepts no more than "six new, renewal, resubmission, or
revision applications" per PD/PI per calendar year, counting multiple-PI
roles, per NOT-OD-25-132. T awards and R13 are exempt. Check the count
before planning a cycle.

**Required.** NSF returns concurrent duplicate or substantially similar
proposals to more than one program, per PAPPG Chapter I. Many NSF
solicitations also limit proposals per PI. Read the solicitation.

## Build the timeline

[scripts/backward-timeline.py](scripts/backward-timeline.py) builds a
milestone table backward from the sponsor deadline. It skips weekends and
any holiday you pass. It places IU's internal deadline four business days
before the sponsor's.

```bash
t=.agents/skills/planning-a-proposal/scripts/backward-timeline.py
$t 2027-02-05 --rolls-forward --from "$(date +%F)"
$t 2027-06-05 --rolls-forward --holiday 2027-05-31 --large-budget
```

Pass IU holidays and closures with `--holiday`. IU's calendar is not built
in.

The default milestones are **Recommended**, drawn from IU's own lead times
where it publishes them:

- RDS Pre-Award Services asks for requests "at least 4 weeks before the due
  date."
- The Research Data Commons asks for three weeks before the routing deadline
  for a data management plan consultation.
- **Practice.** Aims ready for critique about ten weeks out, letters
  requested eight weeks out, and a full draft out for review five weeks out.

**Practice.** Fewer than six working weeks before the internal deadline is
tight for a first R01. Talk to the grant administrator and consider the next
cycle.

## The plan

Fill in [references/plan-template.md](references/plan-template.md). Save the
filled plan with the proposal, such as in its folder or repository. Keep
names, salaries, and unpublished ideas out of shared skills.

## What comes next

| Step | Skill |
| --- | --- |
| Choose and read the opportunity | `finding-funding-opportunities` |
| Draft and critique the aims | `writing-specific-aims` |
| Organize preliminary data and feasibility | `using-preliminary-data-and-feasibility` |
| Draft the Research Strategy | `writing-the-research-strategy` |
| Build the budget | `budgeting-a-proposal` |
| Collect the other documents | `assembling-required-documents` |
| Route through IU and submit | `routing-and-submitting-at-iu` |
| Read the reviews and decide next steps | `responding-to-reviews-and-resubmitting` |
| Find help at any point | `getting-help-with-proposals` |

## After submission

**Observed 2026-10-04 on NIH pages.** NIH's funding decisions changed in
2025 and 2026. Institutes "will not rely on funding paylines" from the
January 2026 councils, per NIH's unified funding strategy. Through January
2027 councils, fewer applications are discussed, per NOT-OD-26-114. Plan the
next cycle with the program officer, not with a payline.

## Keep this file current

- Re-read the NIH standard due dates and late policy pages each review.
- Re-read NOT-OD-25-132 and watch for any change to the six-application
  limit or the AI rule.
- Re-check IU's internal deadline and update the script default if it
  changes.

## Sources

Checked 2026-10-04.

- External: NOT-OD-25-132, Supporting Fairness and Originality in NIH
  Research Applications,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
- External: NIH, Standard Due Dates,
  https://grants.nih.gov/grants-process/submit/submission-policies/standard-due-dates
- External: NOT-OD-26-029, AIDS due dates,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-029.html
- External: NOT-OD-26-064, late applications and continuous submission,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-064.html
- External: NIH, Late Application Policy,
  https://grants.nih.gov/grants-process/submit/submission-policies/late-policy
- External: NOT-OD-26-114, temporary review changes,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-114.html
- External: NIH, Unified NIH funding strategy, Nexus, November 2025,
  https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/implementing-a-unified-nih-funding-strategy-to-guide-consistent-and-clearer-award-decisions
- External: NSF, Notice to the research community on AI, 2023-12-14, now at
  https://www.nsf.gov/policies/ai/merit-review
- External: NSF PAPPG 24-1, Chapter I,
  https://www.nsf.gov/policies/pappg/24-1/ch-1-pre-submission
- IU Research, Routing and Submission:
  https://research.iu.edu/funding-proposals/routing-submission/index.html
- IU Research, Research Development Services:
  https://research.iu.edu/funding-proposals/about/index.html
- Research Data Commons, DMP consultation:
  https://researchdata.iu.edu/resources/dmp-consultation/
- [KB0025830](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0025830)
  Acceptable uses of generative AI services at IU
- [KB0026817](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0026817)
  Acceptable use of AI tools with IU research data
