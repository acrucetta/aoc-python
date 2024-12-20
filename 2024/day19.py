import util as util
from typing import List, Dict

DAY = 19
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
Challenge:
- We have a set of patterns: r, wr, b, g, bwu, rb, gb, br
- We want to match them with a set of lines:
brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb

Some will match all the lines, some won't. We want to return
the number of designs possible. In this sample case there
are 6.

Approach:
- We will want to check if each of the patterns will match
if it does, we try adding the next pattern, if not we backtrack
and go to the next one. If none of the patterns match, we backtrack
all the way back until we hit one that does and do it all over again.

E.g.,

brwrr
- try r, wr, b
- b matches
- try b + r
- r matches
- try b + r + (r, wr)
- wr matches
- try b + r + wr + + r match!

Caching:
- Which patterns work for which set of patterns.

We have a set of patterns of different lengths. 
Ideally, we have a cache that has a list of the patterns
that are available. We try to use the longest patterns
first, then we go to the smallest ones. 

dict
    pos -> next_pos
"""


def is_design_possible(design: str, patterns: List[str], pos=0, cache=None) -> bool:
    if cache is None:
        cache = {}
    if pos >= len(design):
        # We went through all positions and found matches
        return True
    if (pos) in cache:
        # Move to the next position that we know is available
        return is_design_possible(design, patterns, cache[pos], cache)
    for pattern in patterns:
        if pos + len(pattern) <= len(design):
            # Check if they match
            patterns_match = pattern == design[pos : pos + len(pattern)]
            if patterns_match:
                cache[pos] = pos + len(pattern)
                return is_design_possible(design, patterns, pos + len(pattern), cache)
    return False


def get_possible_designs(
    design: str,
    patterns: List[str],
    pos=0,
    curr_matches: List[str] = [],
    all_matches: List[List[str]] = [],
) -> List[List[str]]:
    # TODO: Figure out recursion here.
    if pos >= len(design):
        # We went through all positions and found matches
        if curr_matches not in all_matches:
            all_matches.append(curr_matches)
        return get_possible_designs(
            design,
            patterns,
            0,
            [],
            all_matches,
        )
    for pattern in patterns:
        if pos + len(pattern) <= len(design):
            patterns_match = pattern == design[pos : pos + len(pattern)]
            if patterns_match:
                return get_possible_designs(
                    design,
                    patterns,
                    pos + len(pattern),
                    curr_matches + [pattern],
                    all_matches,
                )
    return all_matches


def part1(input: str) -> int:
    patterns = list(map(lambda x: x.strip(), input[0].split(",")))
    designs = input[1].split("\n")
    res = 0
    for design in designs:
        if is_design_possible(design, patterns):
            res += 1
    return res


def part2(input: str) -> int:
    patterns = list(map(lambda x: x.strip(), input[0].split(",")))
    designs = input[1].split("\n")
    res = []
    for design in designs:
        res.append(get_possible_designs(design, patterns))
    return 0


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, "\n\n")
    sample = util.read_strs(SAMPLE_PATH, "\n\n")

    print("PART 1")
    # util.call_and_print(part1, sample)
    # util.call_and_print(part1, input)

    print("PART 2")
    util.call_and_print(part2, sample)
    # util.call_and_print(part2, input)
