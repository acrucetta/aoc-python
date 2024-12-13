from typing import List, Tuple
import util as util
from typing import List, Tuple

DAY = 9
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
We have (file_id, size, empties)
We want to build a list with: [[size],[empties]] for each one.
Then append them to the big list. Once done, we will
try to fill up the empties.
"""


def build_list(input: List[str]) -> List[List[str | int]]:
    result = []
    file_id = 0
    for i in range(0, len(input), 2):
        # If we're at the last value, and we don't have a pair
        # input the sizes array only
        if i == len(input) - 1:
            size = int(input[i])
            result.append([file_id for _ in range(size)])
            break
        size = int(input[i])
        empties = int(input[i + 1])
        if size > 0:
            result.append([file_id for _ in range(size)])
        if empties > 0:
            result.append(["." for _ in range(empties)])
        file_id += 1
    return result


def part2(input: List[str]) -> int:
    util.log(f"Input: {input}")
    lst = build_list(input)
    flat_lst = [x for xs in lst for x in xs]
    queue = list(filter(lambda x: "." not in x, lst))[::-1]

    for block in queue:
        needed_slots = len(block)
        file_id = block[0]
        for i, block_id in enumerate(flat_lst):
            if block_id == ".":
                available_slots = 0
                for j in range(i, len(flat_lst)):
                    if flat_lst[j] == ".":
                        available_slots += 1
                        continue
                    else:
                        break
                if needed_slots <= available_slots:
                    flat_lst[i:i+needed_slots] = [file_id] * needed_slots
                    for k in range(j, len(flat_lst)):
                        if flat_lst[k] == file_id:
                            flat_lst[k] = "."
                    queue.pop(0)
                    break
    print(lst)
    return 2


if __name__ == "__main__":
    util.set_debug(True)
    input = util.read_strs(MAIN_PATH, sep="\n")[0]
    sample = util.read_strs(SAMPLE_PATH, sep="\n")[0]

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    # util.call_and_print(part2, input)
    util.call_and_print(part2, sample)
