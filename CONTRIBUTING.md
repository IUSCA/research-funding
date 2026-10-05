# Verifying and updating a skill

A skill is only as good as its last check. Sponsor rules change several
times a year, and a proposal built on last year's rule can be returned
without review. Update a skill whenever an agent finds a claim that no longer
matches the sponsor's page, the funding opportunity, or IU's own guidance.
[MAINTAINING.md](MAINTAINING.md) is the runbook for reviewing the whole set.

## Know which source wins

Proposal rules come in layers. When two layers disagree, the narrower,
newer, binding one wins.

1. **The funding opportunity itself.** An NIH Notice of Funding Opportunity
   (NOFO), an NSF solicitation, or a foundation's call. Its instructions
   override the general guide for that one opportunity.
2. **Sponsor notices and guides.** NIH Guide notices (`NOT-OD-...`), the NIH
   How to Apply – Application Guide, the NIH Grants Policy Statement, and the
   NSF Proposal and Award Policies and Procedures Guide (PAPPG). A newer
   notice overrides an older guide until the guide catches up.
3. **Federal regulation.** The Uniform Guidance, 2 CFR 200, and the Common
   Rule, 45 CFR 46.
4. **IU policy and IU guidance.** IU policies at `policies.iu.edu`, and the
   IU Research and Office for Research Administration (ORA) pages that explain
   how IU applies them.
5. **Practice.** What experienced applicants and reviewers know and no
   source states.

A skill states layers 1 to 4 with a citation. It never presents layer 5 as
a rule. It always tells the agent to read the actual funding opportunity,
because no skill can know what one opportunity says.

## Mark every claim

Every claim carries one of these markers, or cites its source inline:

| Marker | Meaning | Must cite |
| --- | --- | --- |
| **Required** | A binding rule: a sponsor notice, guide, or policy, a regulation, or an IU policy | The notice number, guide section, regulation, or policy |
| **Recommended** | Advice this repository gives where no rule applies | The reason, and any guidance it follows |
| **Observed** | Read from a live system, such as NIH RePORTER or a sponsor's due-date page | The date and the URL or command |
| **External** | From a non-sponsor, non-IU source, such as a published grant-writing guide | The source |
| **Practice** | A lesson from experience that no source states | How to check it, where possible |
| **Open item** | No source answers it, or sources conflict | The sources that disagree |

`tools/check-skills.py` fails a **Required** statement that names no binding
source. It cannot tell a good citation from a bad one. A reviewer must.

## Fetch the page, not a memory of it

An agent's memory of NIH and NSF rules is out of date by construction. Before
writing or changing a claim, fetch the source page and read the current
text. Record what you read in the skill's Sources list.

- Cite NIH Guide notices by number, such as NOT-OD-21-013, with the notice
  URL under `grants.nih.gov/grants/guide/notice-files/`.
- Cite the NIH Application Guide and Grants Policy Statement by section, and
  the NSF PAPPG by its document number and chapter.
- Cite IU pages by URL. Note the page's own "last updated" date when it shows
  one.
- Quote short phrases for anything a reader might dispute: a page limit, a
  date, a dollar figure, or a definition.

When a page will not load in a script, read it in a browser and say so in
Sources. Several federal sites block scripted requests.

## Write a lesson as Practice

A Practice lesson saves the next applicant a mistake. Write it so anyone at
IU can use it:

- State the lesson and the reason.
- Give a check where one exists, such as "search NIH RePORTER for the
  study section's recent awards."
- Leave out the incident: no names, no proposal numbers, no scores, and no
  reviewer comments from a real summary statement.
- Prefer a sponsor or IU citation when one backs the lesson. Then it is not
  Practice.

## Record what is unknown

Write an open item when no source answers a question, or when sources
disagree. Name the pages that disagree and quote the words that differ. Do
not resolve a contradiction by picking the more plausible value. Add it to
[docs/open-items.md](docs/open-items.md) under the office that can answer it.

## Update the verified date

Each skill carries a `Verified <date>` line near the top. Change it only after
re-reading every source in that skill's Sources list. A partial re-read names
what it covered, in this form: `Verified 2026-12-01 (NIH page limits and
NOT-OD-26-046 only). Other sources were verified 2026-10-04.`
`tools/check-skills.py` prints `STALE` when a Verified date is older than
120 days, the `stale_after_days` setting in `tools/check-skills.toml`.

## Keep the science with the researcher

These skills guide structure, review criteria, rules, and checks. They do not
write a researcher's science.

- A skill may show the shape of a section, list what reviewers look for, and
  check a draft against the rules and the funding opportunity.
- A skill must not tell an agent to invent aims, hypotheses, preliminary
  results, citations, or letters.
- An agent may draft connective text from the researcher's own notes when
  asked. It marks such text as drafted, and the researcher rewrites it.
- **Required.** NIH does not consider applications "substantially developed
  by AI" to be the applicant's original ideas; see
  `planning-a-proposal` for the notice. Keep that rule in every skill that
  touches drafting.

## Format and style

- Follow the [Agent Skills specification](https://agentskills.io/specification).
  Keep `name` equal to the directory name, in kebab-case. Keep `description`
  under 1024 characters. Say what the skill does, then "Use when".
- Use only `name` and `description` in frontmatter unless a spec field is
  needed.
- Keep `SKILL.md` under 500 lines. Move templates and detail to
  `references/`.
- Put runnable helpers in `scripts/`. Use Bash or the Python standard
  library. A script takes rates and dates as inputs. It never hard-codes a
  rate that changes, such as an F&A rate or a salary cap.
- Keep skills harness-neutral. Do not name a harness's tools.
- Refer to another skill by its name in backticks. Refer to a skill in a
  companion repository by its name and the repository's name. Do not link
  across skill directories, because a skill may be installed alone.
- One idea per sentence, under 25 words, with the serial comma.
- Lead each section with its claim, then support it.
- End every skill with a "Keep this file current" section, then Sources.
- Nothing specific to one person, lab, or proposal: no names, award
  numbers, scores, salaries, or internal hostnames. A researcher's own
  proposal plan lives with that proposal, not here.
- Name office addresses, not people. Add a new one to `allowed_emails` in
  `tools/check-skills.toml` after checking it on an official page. The
  checker fails any other address, and any internal hostname.
- Date every **Observed** statement. The checker fails one without a date.

Run `tools/check-skills.py` before committing. It must exit cleanly.

`tools/check-skills.py` is the same file in every repository of this
family. Do not edit it here. Change this repository's settings in
`tools/check-skills.toml`: allowed emails, the Required-source pattern,
the STALE age, link skip lists, and the weekly checks. The first line it
prints carries its version and hash, so copies can be compared.

## Commits

Make one focused commit per skill change. Say in the message which notices
and pages were re-read.
