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
    {
        "px": {
            "a<2006": "qkq",
            "m>2090": "A",
            "rfg": "R"
        },
        "pv": {
            "a>1716": "R",
            "A": "A"
        }
    }

    Args:
        input (str): The input string of rules

    Returns:
        Dict[str, List[str]]: A dictionary of rules
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
    """
    Convers a string list of parts into a list of
    dictionaries where each item has the part
    and its rating

    E.g.,{x=787,m=2655,a=1222,s=2876}

    Args:
        input (str): The input string of parts

    Returns:
        List[Dict[str, int]]: A list of parts
    """
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


def process_workflow(parts, workflow_rules) -> str | None:
    """
    Takes a part and a workflow and returns the next workflow to process
    """
    for part, condition in workflow_rules.items():
        if "finally" in condition:
            return condition["finally"]
        # "<" or ">"n.keys())[0] # "<" or ">"
        operator = list(condition.keys())[0]
        threshold = int(condition.get("<") or condition.get(">"))
        part_value = parts.get(part)

        if (operator == "<" and part_value < threshold) or (
            operator == ">" and part_value > threshold
        ):
            return condition["then"]
    return None


def process_part(
    parts: Dict[str, int], workflows: Dict[str, Dict[str, List[str]]]
) -> str:
    """
    We will take each part through the workflows and determine if it ends
    up being "A" accepted or "R" rejected.
    """
    current_workflow = "in"
    visited = set()
    while current_workflow not in ("A", "R"):
        if current_workflow in visited:
            raise Exception("Infinite loop")
        visited.add(current_workflow)
        workflow_rules = workflows[current_workflow]
        next_workflow = process_workflow(parts, workflow_rules)
        if next_workflow is None:
            raise Exception("No next workflow")
        current_workflow = next_workflow
    return current_workflow


def part1(input: List[str]) -> int:
    print(input)
    workflows = parse_rules(input[0])
    parts = parse_parts(input[1])
    accepted_parts = [part for part in parts if process_part(part, workflows) == "A"] in parts if process_part(part, workflows) == "A"]
    total_rating= sum(sum(part.values()) for part in accepted_parts)
    return total_rating


def part2(input: str) -> int:
    return 0


if __name__ == "__main__":
    util.set_debug(False)
    input= util.read_strs(MAIN_PATH, sep="\n\n")
    sample= util.read_strs(SAMPLE_PATH, sep="\n\n")

    print("PART 1")
    # util.call_and_print(part1, sample)
    util.call_and_print(part1, input)
