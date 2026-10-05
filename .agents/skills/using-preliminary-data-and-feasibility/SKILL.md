---
name: using-preliminary-data-and-feasibility
description: Turn evidence a researcher already has into preliminary data and a feasibility case for a proposal. Covers what NIH reviewers mean by feasibility under the Rigor and Feasibility factor, which mechanisms expect preliminary data, cohort and recruitment counts from biobanks, EHR feasibility queries, and registries, small-cell suppression and data-use limits on counts, sample size and power justification from the smallest analyzable group, documenting analytic decisions for rigor, and using a prior-work search for significance. Use when someone has pilot results, cohort counts, a feasibility query, or an exploratory analysis and wants to present it in a proposal, or asks whether they need preliminary data.
---

# Using preliminary data and feasibility evidence

Verified 2026-10-04 against NIH Grants and Funding pages and IU data
guidance. Sources are listed at the end.

Preliminary data answer one reviewer question: can this team do this work,
and is the hypothesis worth testing? Present only what supports that. The
data are the researcher's. An agent organizes and checks them, and never
invents, rounds up, or extrapolates a result.

## Where preliminary data go

- **Required.** For NIH research grants, preliminary studies go in the
  Research Strategy, usually in the Approach, per the NIH Application Guide.
  There is no separate section unless the NOFO creates one.
- **Required.** Do not use the Appendix to get around page limits. NIH
  allows only the narrow list of appendix items in its Appendix policy
  (NOT-OD-17-098). Preliminary figures go in the page-limited Research
  Strategy.
- **Required.** For a renewal, a Progress Report replaces or adds to
  preliminary data, per the Application Guide.

## Which mechanisms expect them

| Mechanism | Expectation | Source |
| --- | --- | --- |
| NIH R01 | Not formally required by the parent NOFO, but reviewers expect evidence of feasibility | Parent R01 NOFO; **Practice** for reviewer expectations |
| NIH R21 | Not required, per the parent R21 NOFO; reviewers may still weigh feasibility | Parent R21 NOFO |
| NIH R03 | Usually not required; check the NOFO | The NOFO |
| NIH K awards | Feasibility of the research plan and the candidate's readiness | The NOFO |
| NSF | Results from Prior NSF Support are required for PIs with NSF funding in the past five years; pilot data are optional | NSF PAPPG |
| Foundations | Varies by call | The call |

**Recommended.** Read the review criteria in the specific NOFO. They state
what reviewers will judge, and they override general advice.

## Kinds of feasibility evidence

| Evidence | Shows | Care needed |
| --- | --- | --- |
| Pilot experiment results | The method works in your hands | Show the actual data, with n and variability |
| Cohort or patient counts from a biobank, EHR query, or registry | Enough eligible people exist | Counts are not participants; see attrition below |
| Recruitment history from a prior study | You can enroll at the needed rate | Give the rate, not just the total |
| Access commitments | You can get the data or samples | A letter from the data holder; see `assembling-required-documents` |
| Published work by the team | The team has done similar work | Cite it; the biosketch carries it too |
| Exploratory aggregate analyses | The signal is worth testing | Present as hypothesis-generating, not as a finding |
| Code, pipelines, and computing access | The analysis can run at scale | research-technologies [`planning-research-computing-work`](https://github.com/IUSCA/research-technologies/tree/main/.agents/skills/planning-research-computing-work) |

## Counts from data you do not own

Biobanks, health systems, and registries give feasibility counts under terms.
Those terms follow the counts into the proposal.

- **Required.** Follow the data holder's terms for any count used outside
  its system. Data use agreements and portal terms of use often limit where
  aggregate counts may appear. Ask the data holder before putting a count in
  a proposal.
- **Required.** Respect small-cell suppression. If the source suppressed a
  count, never print it, and never print a total with its other cells so a
  reader can subtract. Suppression thresholds are set by the data holder's
  agreement or policy, such as the cell-size rules in CMS and HCUP data use
  agreements.
- **Recommended.** Name the data version and date of every count, such as
  the release or query date. Counts change with each data release.
- **Recommended.** Report the fewest counts that make the case. Each extra
  count from the same population raises the risk that suppressed values can
  be recovered by differencing.
- **Recommended.** Say who ran the query and on what definitions. A count is
  only as good as its phenotype definition.

For IU health data sources, see the research-data [`accessing-health-and-clinical-data`](https://github.com/IUSCA/research-data/tree/main/.agents/skills/accessing-health-and-clinical-data)
skill. Regenstrief Data Services provides feasibility counts at no cost to
Regenstrief and Indiana CTSI member investigators, per that skill.

## From a count to a sample size

Reviewers check that the sample size can answer each aim. A feasibility count
is the start of that argument, not the end.

1. **Start from the smallest group that matters.** Power the smallest
   stratum or comparison arm in the planned analysis, not the whole cohort.
2. **Walk the attrition.** Write each step from eligible to analyzable:
   meets criteria, has the exposure and outcome recorded, consents or is
   approved for access, has a sample, passes quality control. Give a number
   or a rate for each step, with its source.
3. **State the power calculation.** Name the test, alpha, power, effect
   size, and its source. **Recommended.** Take the effect size from published
   work or pilot data, not from what makes the sample look sufficient.
4. **Show the minimum detectable effect.** When the sample is fixed by what
   exists, give the smallest effect the study can detect, and say why it
   matters.
5. **Get a statistician.** **Recommended.** Ask a biostatistician to check
   the calculation and to be named on the proposal when they do substantive
   work. `getting-help-with-proposals` names IU sources of biostatistics help.

An agent may run the arithmetic with the researcher's inputs, in code it
shows. It must not choose the effect size.

## Making analytic choices visible

Under the Rigor and Feasibility factor, reviewers judge whether the design is
rigorous and transparent. Exploratory work done before the proposal raises a
question: were the planned analyses chosen after seeing the data?

**Recommended.** Keep a dated decision log while exploring: each choice, the
options, what was chosen, why, and whether results had been seen yet. Then:

- Present choices made before results as the pre-specified plan.
- Present choices made after results with their reason, and treat their
  tests as confirmatory only in new data.
- List alternatives tried and dropped under pitfalls and alternative
  approaches. They show the team knows the risks.

`writing-the-research-strategy` covers where these go.

## From a literature search to significance

A structured prior-work search supports the significance and innovation
arguments.

- **Recommended.** Keep the search reproducible: the sources, queries, and
  date. PubMed, Europe PMC, and NIH RePORTER for funded projects are the
  usual starting points.
- **Recommended.** Record for each work one sentence on why it matters to the
  question. The researcher writes that sentence after reading the work.
- **Required.** Cite only works the researcher has read and judged. An agent
  that suggests a paper must give a resolvable identifier, such as a PMID or
  DOI. NIH treats fabricated or misattributed content as research misconduct
  under 42 CFR Part 93.

## Investigation systems

Some research portals keep a structured record of the exploratory work: the
question, cohorts and counts, a decision log, prior work, and findings. Such
a record maps cleanly onto a proposal. Use it as the researcher's own notes,
under the data holder's terms for counts.

## Keep this file current

- Re-read the parent R01 and R21 NOFOs when NIH reissues them.
- Re-read the NIH Appendix policy page each review.
- **Open item.** No single IU policy states a minimum cell size for counts
  used in proposals. Each data holder sets its own. Ask the data holder.

## Sources

Checked 2026-10-04.

- External: NIH, How to Apply – Application Guide, Research Strategy
  instructions,
  https://grants.nih.gov/grants-process/write-application/how-to-apply-application-guide
- External: NOT-OD-17-098, Reminder: NIH Policy on the Appendix,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-17-098.html
- External: NIH parent R21 NOFO, search "PA-25" parent announcements at
  https://grants.nih.gov/funding/explore-nih-opportunities/parent-announcements
- External: NOT-OD-24-010, Simplified Review Framework,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-010.html
- External: 42 CFR Part 93, Public Health Service Policies on Research
  Misconduct, https://www.ecfr.gov/current/title-42/chapter-I/subchapter-H/part-93
- External: NSF PAPPG, Results from Prior NSF Support,
  https://www.nsf.gov/policies/pappg
- External: NIH RePORTER, https://reporter.nih.gov/
- External: HCUP data use agreement (cell-size rule),
  https://hcup-us.ahrq.gov/team/NationwideDUA.jsp
