import util as util
from typing import List, Dict, Tuple, Set, Optional, Union
from collections import OrderedDict

DAY = 19
MAIN_PATH = f"2023/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2023/data/day{DAY:02d}-sample.txt"

"""
Day 19: Aplenty

Each part is organized in four categories:
- x: cool looking
- m: musical
- a: aerodynamic
- s: shiny

Each part will be sent through workflows that will accept or reject it. Each workflow has a name and contains a list of rules.

E.g.,

px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}

Rules:
1. Rule "x>10:one" - if the part's x is more than 10; send the part to the workflow named oen
2. Rule "m<20:two" - if m is < 20; send to workflow named two
3. Rule "a>30:R" - if a is > 30 the part is rejected
4. Rule "A": otherwise, no more rules, the part is accepted

If a part is sent to another workflow. It switches to the start and never returns. If a part is A or R it stops.

Approach:
- Store all the procedures as well as their rules into a data structure we can use
- Store all the instructions into a list; have each one be a dictionary with the key as string and number as value

"""


def parse_rules(input: str) -> Dict[str, List[str]]:
    """
    Parses each rule and returns a dictionary of the type:
    {'path': {
    OrderedDict( 'part' : {"< or >":value, "then": next path} )
    }
    """
    rule_set = input.split("\n")
    all_rules = {}
    for rules in rule_set:
        workflow, rules_str = rules.split("{")
        workflow = workflow.strip()
        rules_str = rules_str.strip("}")
        rules = rules_str.split(",")
        conditions = OrderedDict()
        for rule in rules:
            if "<" in rule:
                part, rest = rule.split("<")
                comp_value, to_workflow = rest.split(":")
                conditions[part] = {"<": int(comp_value), "then": to_workflow}
            elif ">" in rule:
                part, rest = rule.split(">")
                comp_value, to_workflow = rest.split(":")
                conditions[part] = {">": int(comp_value), "then": to_workflow}
            else:
                conditions[rule] = {"finally": rule}
        all_rules[workflow] = conditions
    return all_rules


def parse_parts(input: str) -> List[Dict[str, int]]:
    # {x=787,m=2655,a=1222,s=2876
    all_parts = []
    parts = input.split("\n")
    for part in parts:
        part = part.strip("{}")
        part = part.split(",")
        parts_dict = {}
        for p in part:
            key, value = p.split("=")
            parts_dict[key] = int(value)
        all_parts.append(parts_dict)
    return all_parts


def process_part(
    parts: Dict[str, int], workflows: Dict[str, Dict[str, List[str]]]
) -> str:
    """
    We will take each part through the workflows and determine if it ends
    up being "A" accepted or "R" rejected.
    """
    init_workflow = workflows["in"]

    def process_workflow(parts, workflow) -> str:
        """
        Takes a part and a workflow and returns the next workflow to process
        """
        to_workflow = ""
        print(f"Processing workflow: {workflow}")
        for part, conditions in workflow.items():
            rating = int(parts.get(part, None))
            if "<" in conditions:
                if rating < conditions["<"]:
                    to_workflow = workflows[conditions["then"]]
                break
            elif ">" in conditions:
                if rating > conditions[">"]:
                    to_workflow = workflows[conditions["then"]]
            else:
                to_workflow = workflows[conditions["finally"]]
                break
        return to_workflow

    while True:
        next_workflow = process_workflow(parts, init_workflow)
        if next_workflow == "A":
            return "A"
        elif next_workflow == "R":
            return "R"
        else:
            next_workflow = workflows[next_workflow]


def part1(input: List[str]) -> int:
    print(input)
    workflows = parse_rules(input[0])
    parts = parse_parts(input[1])
    result = process_part(parts[0], workflows)
    return result


def part2(input: str) -> int:
    return 0


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, sep="\n\n")
    sample = util.read_strs(SAMPLE_PATH, sep="\n\n")

    print("PART 1")
    util.call_and_print(part1, sample)
