# research-funding

Agent skills for planning and preparing grant proposals at Indiana
University. They help a researcher, or a coding agent working with one, go
from an idea to a submitted proposal. They cover finding a funding
opportunity, Specific Aims, the Research Strategy, preliminary data, the
budget, the required documents, IU routing and deadlines, and resubmission.

The skills center on NIH, where most IU biomedical proposals go. They note
NSF and foundations where the rules differ.

## Companion repositories

Four repositories cover research at IU. Skills name a companion's skill by
its repository and skill name, as in "`sharing-research-data` in
research-data."

- research-technologies covers clusters, storage, data transfer, and
  allocations.
- research-data covers finding, classifying, managing, and sharing research
  data.
- research-funding covers planning and preparing grant proposals.
- research-cores covers core facilities, their instruments, and the data
  they deliver.

This repository covers the proposal as a whole. research-data covers the
data management and sharing plan. research-technologies covers facilities
text for computing and storage. research-cores covers quotes, rates, and
letters from cores.

## Quickstart

1. Clone this repository.
2. Start your agent in the clone. Claude Code, Codex, OpenCode, and pi all
   find the skills there with no install step.
3. Ask: "I want to submit an NIH R01 for the February deadline. Help me
   plan it."

The agent will ask about the opportunity, the team, and the deadline. It
fills in a proposal plan and a backward timeline. Save the plan with your
proposal, not in this repository.

## The researcher owns the science

These skills guide structure, sponsor rules, review criteria, IU process,
and checks. They do not write a researcher's science.

- An agent using them may explain what a section needs, check a draft
  against the rules and the funding opportunity, compute a budget or a
  timeline, and find gaps.
- It must not invent aims, hypotheses, preliminary results, citations, or
  letters. Every result in a proposal is the researcher's own and real.
- NIH does not consider applications "substantially developed by AI" to be
  the applicant's original ideas (NOT-OD-25-132). NSF encourages proposers
  to say how generative AI was used. Each skill that touches drafting
  repeats this.

## What the skills trust

Sponsor rules change several times a year, so an agent must not trust its
own memory of them. Every claim carries one of these markers, or cites its
source inline:

| Marker | Meaning | Must cite |
| --- | --- | --- |
| **Required** | A binding rule: a sponsor notice, guide, or policy, a regulation, or an IU policy | The notice number, guide section, regulation, or policy |
| **Recommended** | Advice this repository gives where no rule applies | The reason, and any guidance it follows |
| **Observed** | Read from a live page or system, such as IU's published rates | The date and the URL |
| **External** | From a non-sponsor, non-IU source | The source |
| **Practice** | A lesson from experience that no source states | How to check it, where possible |
| **Open item** | No source answers it, or sources conflict | The sources that disagree |

Sources rank this way:

1. **The funding opportunity** (NIH NOFO, NSF solicitation, or foundation
   call) wins for its own applications.
2. **Sponsor notices and guides** bind: NIH Guide notices, the NIH
   Application Guide and Grants Policy Statement, and the NSF PAPPG. A newer
   notice beats an older guide.
3. **Federal regulation and IU policy** bind: 2 CFR 200, 45 CFR 46, IU
   policies, and IU's Research Administration Standards.
4. **IU guidance**, from IU Research and its offices, explains how IU
   applies them.

When a skill and a binding source disagree, the binding source wins. When a
source is silent or unclear, the skill says so as an open item.

## What stays out

The skills hold what is true for anyone at IU. What belongs to one proposal
stays with that proposal: the plan, the aims, salaries, budgets, letters,
reviewer comments, and scores. The plan template in `planning-a-proposal`
says where to keep it.

No skill names an individual staff member. Each names an office and its
shared address.

## Skills

| Skill | Use it when |
| --- | --- |
| [planning-a-proposal](.agents/skills/planning-a-proposal/SKILL.md) | Starting a proposal: timeline back from the deadline, IU's internal deadline, application limits, and a plan template. Start here. |
| [finding-funding-opportunities](.agents/skills/finding-funding-opportunities/SKILL.md) | Choosing a sponsor, mechanism, and opportunity, reading a NOFO, or checking for a limited submission. |
| [writing-specific-aims](.agents/skills/writing-specific-aims/SKILL.md) | Drafting or checking a Specific Aims page. |
| [writing-the-research-strategy](.agents/skills/writing-the-research-strategy/SKILL.md) | Drafting or checking Significance, Innovation, and Approach against NIH's review framework, or an NSF Project Description. |
| [using-preliminary-data-and-feasibility](.agents/skills/using-preliminary-data-and-feasibility/SKILL.md) | Presenting pilot data, cohort counts, or a feasibility query, or justifying sample size and power. |
| [budgeting-a-proposal](.agents/skills/budgeting-a-proposal/SKILL.md) | Building a budget and justification: effort, salary cap, fringe, F&A, cores, and subawards. |
| [assembling-required-documents](.agents/skills/assembling-required-documents/SKILL.md) | Preparing biosketches, Other Support, facilities, letters, the DMS plan, human subjects, and other attachments. |
| [routing-and-submitting-at-iu](.agents/skills/routing-and-submitting-at-iu/SKILL.md) | Routing in Kuali Coeus, meeting ORA's deadline, IU approvals, and Just-in-Time. |
| [responding-to-reviews-and-resubmitting](.agents/skills/responding-to-reviews-and-resubmitting/SKILL.md) | Reading a summary statement, deciding whether to resubmit, and writing the Introduction. |
| [getting-help-with-proposals](.agents/skills/getting-help-with-proposals/SKILL.md) | Deciding which IU office or service to ask, and what to send. |

The skills do not depend on any one data platform. A portal that records
exploratory work can map its records onto a proposal, as described in
`using-preliminary-data-and-feasibility`.

## Use the skills

Each skill is a directory in the open
[Agent Skills](https://agentskills.io/specification) format. Scripts use only
Python's standard library, so any harness that can run a shell can use them.

The skills live in `.agents/skills/`. Codex, pi, and OpenCode read that
directory. Claude Code reads only `.claude/skills/`, so `.claude/skills` is a
committed symbolic link to it.

To use the skills in another project, copy the skill directories you need
into that project's `.agents/skills/`. Or use the
[`skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add <this repository> --list
npx skills add <this repository> --skill planning-a-proposal --copy
```

Claude Code users can also run `claude --add-dir ~/repos/research-funding`
for one session.

## Maintaining

- [CONTRIBUTING.md](CONTRIBUTING.md) explains how to verify and write a
  single claim.
- [MAINTAINING.md](MAINTAINING.md) is the runbook for reviewing the whole
  set, and lists what to re-check and when.
- [docs/open-items.md](docs/open-items.md) collects every open question, by
  the office that can answer it.
- `tools/check-skills.py` runs the offline checks: format, markers, sources,
  age, and what stays out. `--kb` and `--links` add the network checks, and
  `--freshness` runs every check this repository's weekly workflow runs.
  `tools/check-skills.toml` holds this repository's settings.
- [tests/trigger-prompts.md](tests/trigger-prompts.md) checks that agents
  load the right skill.

## License

Code, meaning scripts and tools, is under the Educational Community License,
Version 2.0; see [LICENSE](LICENSE). Written content, including every
`SKILL.md` and reference file, is under CC BY 4.0; see
[LICENSE-docs](LICENSE-docs). Copyright the Trustees of Indiana University.
