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
    flatten_lst = [x for xs in lst for x in xs]
    queue = list(filter(lambda x: "." not in x, lst))[::-1]
    print(queue)
    
    # Iterate over each item in the queue and find a spot for it
    # Iterate over the file system, find a spot that is large enough for 
    # that block to move in that is less than its current position
    # If found, replace that span with the file ID, remove from the queue, replace
    # the spot left by the file with a '.'
    
    # for i in enumerate(flatten_lst):
    #     if "." in arr:
    #         # Check if we can place an item in the queue, if 
    #         # so, replace it
    #         start_e=arr.index(".")
    #         end_e=len(arr)
    #         available_slots = end_e-start_e
    #         for block in queue:
    #             block_id=block[0]
    #             if len(block)<=available_slots:
    #                 lst[i][start_e:start_e+len(block)] = [block_id] * len(block) 
    #                 queue.pop(0)
    #                 available_slots-=len(block)
    #                 if "." in arr:
    #                     start_e=arr.index(".")
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
