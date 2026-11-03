# Runbook: reviewing and updating the skill set

This runbook keeps the skills true to sponsor rules and IU practice as they
are now. It covers a full review, the checks that drive it, and when to run
it. `CONTRIBUTING.md` covers how to write and verify a single claim.

Proposal rules change faster than most. NIH changed its review criteria, its
biosketch and Other Support forms, its application limits, and its rules on
AI-written applications within about eighteen months. An unreviewed skill is
wrong within a year.

## Who decides what is true

- **The funding opportunity** wins for its own applications. Every skill
  tells the agent to read it.
- **The sponsor** wins for its general rules: NIH Guide notices, the NIH
  Application Guide and Grants Policy Statement, and the NSF PAPPG. A newer
  notice beats an older guide.
- **IU policy and IU Research pages** win for how IU routes, approves, and
  submits a proposal.
- **The owning office** settles what none of these answers: the Office for
  Research Administration (ORA) for routing and budgets, the Human Research
  Protection Program (HRPP) for human subjects, and the sponsor's program
  officer for fit. Record its answer with the date and the email or ticket
  it came from, without personal names.

## When to review

| Trigger | Scope | How you notice |
| --- | --- | --- |
| Monthly | The `freshness` issue, and any notice the weekly reading below found | The `freshness` issue opened on the 1st, and the month's tracking issue on iu-research |
| Any agent finds a wrong claim during real work | That claim, right away, in its own commit | An issue on this repository |
| NIH publishes a notice that changes forms, page limits, review criteria, biosketch, Other Support, or budget rules | Every skill that cites the changed rule | The NIH Guide table of contents; read notices with "OD" in the number |
| NIH announces a new forms version (FORMS-I is current; watch for FORMS-J), usually months before the change | `assembling-required-documents`, `planning-a-proposal`, and the page-limit claims | The NIH Guide table of contents |
| NSF issues a new PAPPG or a supplement, usually effective in January or May | Every NSF claim | NSF news |
| IU changes its routing system, internal deadline, or F&A rate agreement | `routing-and-submitting-at-iu`, `budgeting-a-proposal` | No feed. Re-read the IU Research, ORA, and rate agreement pages at each full review. |
| The federal F&A cap litigation or policy changes | `budgeting-a-proposal` | The NIH Guide table of contents, and NSF news |
| Every quarter (January, April, July, October) | The full review below, after the monthly one | The calendar, and the month's tracking issue |

GitHub Actions runs two checks. On every pull request and push to `main`,
`check-skills.yml` runs `tools/check-skills.py` and fails on any `ERROR`.
On the 1st of each month, `freshness.yml` runs `tools/check-skills.py --freshness`, which
here means the age, KB, and link checks. When it finds `STALE`, `BROKEN`, or
`ERROR` lines, it opens an issue labeled `freshness`, or comments on the one
already open.

**Recommended.** Read the NIH Guide weekly table of contents and NSF news
each week. Read each week's NIH notices with "OD" in the number. Those are
the policy notices. Also check NIH's grants and funding information status
page, which lists burden-reduction changes in one place. No script does
this. The family maintainer assigns someone to each feed, and records who on
the tracking issue each quarter. See the family runbook's "Watching for
events".

## What to re-check, and where

These claims change most often. Re-check each at every full review.

| Claim | Source to re-read | Skill |
| --- | --- | --- |
| Current NIH forms version and its effective due dates | NIH How to Apply – Application Guide, forms page | `assembling-required-documents` |
| NIH page limits | NIH page limits table | `writing-specific-aims`, `writing-the-research-strategy`, `responding-to-reviews-and-resubmitting` |
| Review framework and criteria | NOT-OD-24-010 and later notices; the NOFO's review section | `writing-the-research-strategy` |
| Biosketch and Other Support formats, SciENcv, ORCID | NIH Common Forms pages | `assembling-required-documents` |
| Research security training certification | NIH and NSF research security pages | `assembling-required-documents` |
| Application limits and AI-use rules | NOT-OD-25-132 and later notices | `planning-a-proposal` |
| Standard due dates and late policy | NIH standard due dates page | `planning-a-proposal` |
| Salary cap | NIH salary cap notice for the fiscal year, usually issued in January | `budgeting-a-proposal` |
| F&A rates and the federal cap's legal status | IU rate agreement page; NIH and NSF notices | `budgeting-a-proposal` |
| DMS plan format | NIH DMS pages; research-data `planning-data-management-and-sharing` | `assembling-required-documents` |
| Resubmission rules | NIH resubmission page and NOT-OD-18-197 | `responding-to-reviews-and-resubmitting` |
| NSF PAPPG version | NSF PAPPG page | every skill with NSF notes |
| IU internal deadline, routing system, and contacts | IU Research and ORA pages | `routing-and-submitting-at-iu`, `getting-help-with-proposals` |
| IU limited submissions process | IU Research limited submissions page | `finding-funding-opportunities` |

## Working a freshness issue

Follow the family runbook,
[monthly-review.md](https://github.com/IUSCA/iu-research/blob/main/docs/monthly-review.md).
It has the general steps: how to work each kind of line, the KB snapshot
and Verified-line rules, commits, and the pull request. This section adds
only what is specific to this repository.

- `--freshness` runs the age, KB, and link checks. There is no snapshot
  script, so a run here never prints `CHANGED`.
- Some federal sites refuse scripts. A `BROKEN` line for one of them often
  means the host needs `skip_403_hosts`, not a new address. Test it as the
  runbook's "BROKEN twice" says.
- For a `STALE` line on a notice-based claim, also look for a newer notice
  that supersedes the cited one, as in
  [step 2 of the full review](#2-re-read-the-sources-and-fix-the-claims).
- The monthly item here is what the weekly NIH Guide and NSF news reading
  found. Fix it in the month's review branch, one skill per commit. If no
  one read the feeds this month, say so on the tracking issue.

## Full review

Work on a branch. Commit as the family runbook's "Commits" section says:
one skill per commit, with each KB snapshot in the commit it supports.

### 1. Lint and find stale skills

```bash
tools/check-skills.py --freshness
```

It checks each skill against the Agent Skills specification and the house
rules. It flags any Verified date older than 120 days. It then checks each
cited KB article and fetches every cited URL. Some federal sites refuse
scripts. The checker skips their 403 replies for the hosts and pages listed
in `tools/check-skills.toml`.

- `ERROR` lines must be fixed before merging.
- `STALE` lines are the reading list for step 2.
- Work `INFO` and `BROKEN` lines as the family runbook's step 3 says.
- `WARN` lines usually mean a notice appears in the text but not in
  Sources. A skill without a README row or trigger prompt is an `ERROR`.

### 2. Re-read the sources and fix the claims

For each skill, open every source in its Sources list. Compare each claim
that cites it with the current text. Fix what changed. Then search for newer
notices that supersede the cited ones:

```bash
grep -rhoE "NOT-[A-Z]{2}-[0-9]{2}-[0-9]{3}" .agents/skills | sort -u
```

Open each notice. NIH marks a superseded notice at its top. Update Verified
lines, and record KB articles with `--kb-snapshot`, by the family runbook's
"Rules that trip people up".

### 3. Re-check the scripts

The scripts take rates and dates as inputs, so they rarely go stale. Their
built-in checks do encode NIH facts: the modular budget limit, the $500,000
large-budget flag, and the default internal deadline of four business days.
Re-check each against its source, and run each script once:

```bash
s=.agents/skills/budgeting-a-proposal/scripts/budget-calc.py
$s --example > /tmp/b.json && $s /tmp/b.json
.agents/skills/planning-a-proposal/scripts/backward-timeline.py 2027-02-05 --from "$(date +%F)"
```

### 4. Work the open items

```bash
grep -rn -i "open item" .agents/skills
```

For each item, try in this order:

1. Has the sponsor or IU published an answer? Search again.
2. Otherwise collect the item for its owning office in
   [docs/open-items.md](docs/open-items.md). Send one message per office
   with every question batched.

Close an item only with its source: a notice, a page and date, or a dated
reply from the office.

### 5. Re-check the companion repositories

These skills point to research-data, research-technologies, and research-cores
skills by name. Check that each named skill still exists and still covers
what is claimed.

### 6. Test that agents find the right skill

Start a fresh session in this repository in each harness you support. Try the
prompts in [tests/trigger-prompts.md](tests/trigger-prompts.md). Check that
the expected skill loads and that the answer cites it. Fix a description that
fails to trigger. Note which harness and version you tested in the review
commit.

### 7. Finish

```bash
tools/check-skills.py
```

It must exit cleanly. Open a pull request that lists the sources re-read and
the open items closed or opened.

## Adding a skill

1. Create `.agents/skills/<name>/SKILL.md`. Keep `name` equal to the
   directory name.
2. Follow `CONTRIBUTING.md` for sources, markers, and style.
3. Add a row to the skills table in `README.md`.
4. Add trigger prompts to `tests/trigger-prompts.md`.
5. Run `tools/check-skills.py --links`.

## Retiring a skill

Delete the directory and its README row in one commit. Say why in the
message.
