#!/usr/bin/env python3
"""Draft a multi-year proposal budget from a small JSON file.

Usage:
    budget-calc.py budget.json            # Markdown tables to stdout
    budget-calc.py --example > budget.json

Every rate is an input. Nothing here knows IU's F&A rate, its fringe rates,
or the sponsor's salary cap; the budgeting-a-proposal skill says where to get
each one. The output is a planning draft for a conversation with the
department's pre-award contact, never the budget that is submitted.

What it computes, per year:
  - salary requested per person, from base salary, appointment months, and
    person months, with an optional annual salary cap applied to the
    annualized base salary;
  - fringe on the requested salary, by fringe class;
  - other direct costs by category, with an optional annual escalation;
  - the modified total direct cost (MTDC) base, excluding the categories
    listed in "mtdc_exclusions" and each subaward's amount above
    "subaward_mtdc_cap" over the life of the award. A subaward's "amounts"
    are its total costs, its own F&A included; "fa_amounts" names that F&A
    so the NIH checks can leave it out;
  - F&A at "fa_rate" on that base;
  - NIH checks: whether direct costs less consortium F&A fit a modular
    budget (at most 250,000 per year), and whether any year reaches 500,000.
    NIH dropped its prior-contact rule for such budgets in NOT-OD-26-019;
    the flag is a prompt to talk to the program officer.

Standard library only.
"""

import json
import math
import sys

EXAMPLE = {
    "title": "Example R01, 5 years",
    "years": 5,
    "escalation": 0.03,
    "salary_cap": None,
    "fa_rate": 0.0,
    "subaward_mtdc_cap": 25000,
    "mtdc_exclusions": [
        "equipment", "patient_care", "tuition", "participant_support",
        "rental", "scholarships",
    ],
    "fringe": {"faculty": 0.0, "staff": 0.0, "student": 0.0},
    "personnel": [
        {"role": "PI", "base_salary": 150000, "appointment_months": 12,
         "person_months": [1.8, 1.8, 1.8, 1.8, 1.8], "fringe_class": "faculty"},
        {"role": "Data analyst", "base_salary": 70000, "appointment_months": 12,
         "person_months": [6, 6, 6, 6, 6], "fringe_class": "staff"},
    ],
    "other": [
        {"item": "Core facility services", "category": "core_services",
         "amounts": [20000, 20000, 15000, 10000, 5000], "escalate": False},
        {"item": "Conference travel", "category": "travel",
         "amounts": [3000, 3000, 3000, 3000, 3000], "escalate": False},
        {"item": "Subaward to a partner site", "category": "subaward",
         "amounts": [60000, 60000, 60000, 60000, 60000],
         "fa_amounts": [20000, 20000, 20000, 20000, 20000], "escalate": False},
    ],
}


def money(x):
    return f"{x:,.0f}"


def salary_requested(person, year, escalation, cap):
    base = person["base_salary"] * (1 + escalation) ** year
    months = person["appointment_months"]
    annualized = base * 12 / months
    capped = annualized if cap is None else min(annualized, cap)
    pm = person["person_months"][year]
    return capped * pm / 12, annualized, capped < annualized


def build(spec):
    years = spec["years"]
    esc = spec.get("escalation", 0.0)
    cap = spec.get("salary_cap")
    rows = []
    sub_used = {}
    notes = []
    for y in range(years):
        r = {"salary": 0.0, "fringe": 0.0, "by_cat": {}, "people": []}
        for p in spec["personnel"]:
            sal, annual, was_capped = salary_requested(p, y, esc, cap)
            fr = sal * spec["fringe"].get(p["fringe_class"], 0.0)
            r["salary"] += sal
            r["fringe"] += fr
            r["people"].append((p["role"], p["person_months"][y], sal, fr))
            if was_capped and y == 0:
                notes.append(f"{p['role']}: annualized base {money(annual)} is above the cap; "
                             "the difference is not charged to the award.")
        for o in spec.get("other", []):
            amt = o["amounts"][y]
            if o.get("escalate"):
                amt *= (1 + esc) ** y
            r["by_cat"].setdefault(o["category"], 0.0)
            r["by_cat"][o["category"]] += amt
        direct = r["salary"] + r["fringe"] + sum(r["by_cat"].values())
        excluded = sum(v for k, v in r["by_cat"].items() if k in spec["mtdc_exclusions"])
        # Each subaward's first `subaward_mtdc_cap` over the award is in the base.
        sub_in_base = 0.0
        for o in spec.get("other", []):
            if o["category"] != "subaward":
                continue
            used = sub_used.get(o["item"], 0.0)
            room = max(0.0, spec["subaward_mtdc_cap"] - used)
            amt = o["amounts"][y]
            take = min(room, amt)
            sub_used[o["item"]] = used + amt
            sub_in_base += take
        excluded += r["by_cat"].get("subaward", 0.0) - sub_in_base
        mtdc = direct - excluded
        fa = mtdc * spec["fa_rate"]
        consortium_fa = sum(o.get("fa_amounts", [0.0] * years)[y]
                            for o in spec.get("other", []) if o["category"] == "subaward")
        r.update(direct=direct, mtdc=mtdc, fa=fa, total=direct + fa,
                 nih_direct=direct - consortium_fa)
        rows.append(r)
    return rows, notes


def report(spec, rows, notes):
    years = spec["years"]
    head = "| Line | " + " | ".join(f"Year {i + 1}" for i in range(years)) + " | Total |"
    sep = "| --- |" + " ---: |" * (years + 1)
    out = [f"# Budget draft: {spec.get('title', 'untitled')}", "",
           "Planning draft only. Confirm every rate with your pre-award contact.", "",
           "## Personnel", "", head, sep]
    for i, p in enumerate(spec["personnel"]):
        vals = [rows[y]["people"][i][2] for y in range(years)]
        pms = [rows[y]["people"][i][1] for y in range(years)]
        out.append(f"| {p['role']} salary ({', '.join(str(m) for m in pms)} PM) | "
                   + " | ".join(money(v) for v in vals) + f" | {money(sum(vals))} |")
    for key, label in (("salary", "Salary subtotal"), ("fringe", "Fringe")):
        vals = [r[key] for r in rows]
        out.append(f"| {label} | " + " | ".join(money(v) for v in vals) + f" | {money(sum(vals))} |")
    cats = sorted({c for r in rows for c in r["by_cat"]})
    out += ["", "## Totals", "", head, sep]
    for c in cats:
        vals = [r["by_cat"].get(c, 0.0) for r in rows]
        out.append(f"| {c} | " + " | ".join(money(v) for v in vals) + f" | {money(sum(vals))} |")
    for key, label in (("direct", "Total direct costs"), ("mtdc", "MTDC base"),
                       ("fa", f"F&A at {spec['fa_rate']:.1%}"), ("total", "Total costs"),
                       ("nih_direct", "Direct costs less consortium F&A")):
        vals = [r[key] for r in rows]
        out.append(f"| {label} | " + " | ".join(money(v) for v in vals) + f" | {money(sum(vals))} |")
    out += ["", "## Checks", ""]
    peak = max(r["nih_direct"] for r in rows)
    if peak <= 250000:
        modules = [math.ceil(r["nih_direct"] / 25000) for r in rows]
        out.append(f"- NIH modular: fits; modules of 25,000 per year would be {modules}.")
    else:
        out.append(f"- NIH modular: does not fit; peak year is {money(peak)}. Use a detailed budget.")
    if peak >= 500000:
        out.append("- NIH: a year reaches 500,000 direct costs less consortium F&A. "
                   "NIH no longer requires prior contact (NOT-OD-26-019); "
                   "still discuss the budget with the program officer.")
    if spec["fa_rate"] == 0:
        out.append("- F&A rate is 0. Enter the rate your pre-award contact confirms.")
    if spec.get("salary_cap") is None:
        out.append("- No salary cap entered. NIH and some other sponsors cap salary.")
    out += [f"- {n}" for n in notes]
    return "\n".join(out)


def main(argv):
    if "--example" in argv:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    with open(argv[0]) as f:
        spec = json.load(f)
    for p in spec["personnel"]:
        if len(p["person_months"]) != spec["years"]:
            sys.exit(f"{p['role']}: person_months needs {spec['years']} values")
    for o in spec.get("other", []):
        if len(o["amounts"]) != spec["years"]:
            sys.exit(f"{o['item']}: amounts needs {spec['years']} values")
    rows, notes = build(spec)
    print(report(spec, rows, notes))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
