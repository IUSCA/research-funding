#!/usr/bin/env python3
"""Plan a proposal backward from the sponsor deadline.

Usage:
    backward-timeline.py 2027-02-05
    backward-timeline.py 2027-02-05 --internal-days 5 --holiday 2027-01-18
    backward-timeline.py 2027-02-05 --large-budget --from 2026-10-04
    backward-timeline.py 2027-02-05 --milestones my-milestones.tsv

Prints a Markdown table of milestones with dates, newest last. Weekends and
any --holiday date are skipped. With --from, it also says how many working
days remain and flags milestones already past.

--internal-days is the number of business days before the sponsor deadline
that the institution's pre-award office needs the final proposal. The
default, 4, is IU's published expectation as of 2026-10-04: received at ORA
by 9 a.m. four business days before. The routing-and-submitting-at-iu skill
cites it and notes a policy that sets other days for some components.

The default milestones are planning advice, not rules, except the ones
marked Required. A milestones file has one milestone per line:
    <weeks before sponsor deadline><TAB><marker><TAB><text>

Standard library only.
"""

import argparse
import datetime as dt
import sys

DEFAULT_INTERNAL_DAYS = 4  # IU routing page, read 2026-10-04: 9 a.m., four business days before

# (weeks before the sponsor deadline, marker, text)
DEFAULT_MILESTONES = [
    (16, "Recommended", "Decide to apply: opportunity, mechanism, and institute chosen; read the NOFO end to end"),
    (14, "Recommended", "Tell your department pre-award contact; ask about internal deadlines and limited submissions"),
    (12, "Recommended", "Contact the program officer with a one-page aims draft"),
    (10, "Recommended", "Specific Aims draft shared with mentors or colleagues for critique"),
    (8, "Recommended", "Request letters of support and collaboration, with a draft and a date"),
    (8, "Recommended", "Ask core facilities and collaborators for quotes and subaward documents"),
    (6, "Recommended", "Budget and budget justification draft to pre-award"),
    (6, "Recommended", "Biosketches and Other Support started in SciENcv for every key person"),
    (5, "Recommended", "Full Research Strategy draft out for internal review"),
    (3, "Recommended", "Data Management and Sharing Plan, human subjects, and other attachments final"),
    (2, "Recommended", "Research Strategy final; all letters received"),
]
LARGE_BUDGET = (8, "Recommended", "Large budget: discuss it with the program officer (NIH dropped its prior-contact rule in NOT-OD-26-019)")


def parse_date(text):
    return dt.date.fromisoformat(text)


def is_workday(day, holidays):
    return day.weekday() < 5 and day not in holidays


def back_business_days(day, n, holidays):
    while n > 0:
        day -= dt.timedelta(days=1)
        if is_workday(day, holidays):
            n -= 1
    return day


def previous_workday(day, holidays):
    while not is_workday(day, holidays):
        day -= dt.timedelta(days=1)
    return day


def next_workday(day, holidays):
    while not is_workday(day, holidays):
        day += dt.timedelta(days=1)
    return day


def workdays_between(a, b, holidays):
    n, day = 0, a
    while day < b:
        if is_workday(day, holidays):
            n += 1
        day += dt.timedelta(days=1)
    return n


def load_milestones(path):
    out = []
    with open(path) as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            weeks, marker, text = line.rstrip("\n").split("\t", 2)
            out.append((float(weeks), marker, text))
    return out


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deadline", type=parse_date, help="sponsor deadline, YYYY-MM-DD")
    ap.add_argument("--internal-days", type=int, default=DEFAULT_INTERNAL_DAYS,
                    help="business days before the deadline the pre-award office needs the final proposal")
    ap.add_argument("--holiday", type=parse_date, action="append", default=[],
                    help="a date to skip; repeat for each holiday or closure")
    ap.add_argument("--large-budget", action="store_true",
                    help="add a program-officer step for a budget of $500,000 or more direct costs in a year")
    ap.add_argument("--rolls-forward", action="store_true",
                    help="the sponsor moves a weekend or holiday deadline to the next business day, as NIH does")
    ap.add_argument("--from", dest="start", type=parse_date,
                    help="today's date, to count the working days left")
    ap.add_argument("--milestones", help="a tab-separated milestones file to use instead of the defaults")
    args = ap.parse_args(argv)

    holidays = set(args.holiday)
    deadline = args.deadline
    if args.rolls_forward:
        deadline = next_workday(deadline, holidays)
    internal = back_business_days(deadline, args.internal_days, holidays)

    milestones = load_milestones(args.milestones) if args.milestones else list(DEFAULT_MILESTONES)
    if args.large_budget:
        milestones.append(LARGE_BUDGET)

    rows = []
    for weeks, marker, text in milestones:
        day = previous_workday(deadline - dt.timedelta(days=round(weeks * 7)), holidays)
        rows.append((day, marker, text))
    rows.append((internal, "Required", f"Final proposal routed and received by the pre-award office, 9 a.m. ({args.internal_days} business days before)"))
    rows.append((deadline, "Required", "Sponsor deadline"))
    rows.sort(key=lambda r: r[0])

    print(f"# Proposal timeline: sponsor deadline {deadline:%a %Y-%m-%d}")
    print()
    if deadline != args.deadline:
        print(f"The sponsor moves {args.deadline} to the next business day, {deadline}.")
        print()
    print("| Date | Day | Marker | Milestone | Status |")
    print("| --- | --- | --- | --- | --- |")
    for day, marker, text in rows:
        status = ""
        if args.start:
            status = "past" if day < args.start else f"{workdays_between(args.start, day, holidays)} working days"
        print(f"| {day} | {day:%a} | {marker} | {text} | {status} |")
    if args.start:
        left = workdays_between(args.start, internal, holidays)
        print()
        print(f"{left} working days remain before the internal deadline.")
        if left < 30:
            print("That is under six working weeks. Talk to pre-award and consider the next cycle.")
    print()
    print("Recommended milestones are planning advice. Confirm the internal deadline with pre-award.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
