# Add the parent directory to the Python path so `common` can be found
from enum import Enum
import re
import math
import os
import sys
import functools
import itertools
from typing import Dict, List, Optional, Tuple

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

import common.util as util

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DAY = 15
MAIN_PATH = f"2023/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2023/data/day{DAY:02d}-sample.txt"

"""
Day 15: Lens Library

Part 1 
~~~~~~~
We have a hash algorithm to build. We want to turn any string of characters into a single number ranging from 0 to 255. To run it on a string we start with 0. Then for each character in the string we:
- Get ASCII code for the current char
- Increase the curr value by the ASII code
- Set curr value to itself x 17
- Set curr value to remainder of itself / 256

Our sample input is:
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7

When running the algorithm we get a value for each; resulting in 1320 total.

Part 2
~~~~~~
We have lenses organized by focal length ranging from through 9.
We now have a HASHMAP algorithm.

We find the box by applying the HASH algorithm to a label. The 
label is followed by a character that indicates an operation. Either
an equal (=) or a dash (-)

(-) Operation
Go to the relevant box and remove the lens with the 
given label if it is present in the box. Then, 
move any remaining lenses as far forward in the 
box as they can go without changing their order.
Fill any space made by removing the indicated lens.

(=) Operation
It will be followed by a number indicating the 
focal length of the lens that needs to go into 
the relevant box; be sure to use the label maker to 
mark the lens with the label given in the beginning 
of the step so you can find it later.

    If there's already a lens in the box with the same label
    replace the old lens with the new lens; remove the old lens
    and put the new lens in its place

    If there's not, add the lens to the box immediately. Don't
    move any other lens

Label = Focal Length
Label 

"""


class Operation(Enum):
    REMOVE = "-"
    ADD = "="


def hash(word: str) -> int:
    curr = 0
    for char in word:
        curr += ord(char)
        curr = curr * 17
        curr = curr % 256
    return curr


def part1(input: str) -> int:
    words = input.split(",")
    return sum([hash(word) for word in words])


def parse_step(step: str) -> Tuple[str, Operation, Optional[int]]:
    if "=" in step:
        equal_step = step.split("=")
        return equal_step[0], Operation.ADD, int(equal_step[1])
    if "-" in step:
        minus_step = step.split("-")
        return minus_step[0], Operation.REMOVE, None
    else:
        raise ValueError("Step is not valid")


def update_boxes(
    boxes: Dict[int, List[Tuple[str, int]]], step: str
) -> Dict[int, List[Tuple[str, int]]]:
    """Apply a single step to the boxes and return a new boxes state."""
    label, operation, length = parse_step(step)

    box_hash = hash(label)
    current_box = boxes.get(box_hash, [])

    match operation:
        case Operation.ADD:
            assert length is not None, "Length should not be None"
            updated_box = add_or_replace_lens(current_box, label, length)
        case Operation.REMOVE:
            updated_box = remove_lens(current_box, label)

    # Return a new boxes dictionary with the updated box
    return {**boxes, box_hash: updated_box}


def add_or_replace_lens(
    box: List[Tuple[str, int]], label: str, length: int
) -> List[Tuple[str, int]]:
    labels = [pair[0] for pair in box]
    if label in labels:
        # Replace the label with the new length
        # in its place
        box[labels.index(label)] = (label, length)
        return box
    # Add to the box
    box.append((label, length))
    return box


def remove_lens(box: List[Tuple[str, int]], label: str) -> List[Tuple[str, int]]:
    labels = [pair[0] for pair in box]
    if label in labels:
        # Remove the label from the box
        box.pop(labels.index(label))
    return box


def calculate_focusing_power(boxes: Dict[int, List[Tuple[str, int]]]) -> int:
    """Calculate the focusing power of the given boxes."""
    focus_power = 0
    for box, lenses in boxes.items():
        for pos, (_, length) in enumerate(lenses):
            focus_power += (box + 1) * (pos + 1) * length
    return focus_power


def part2(input: str) -> int:
    sequence = input.split(",")
    boxes: Dict[int, List[Tuple[str, int]]] = {}
    for step in sequence:
        boxes = update_boxes(boxes, step)
        print(f"Step: {step}, Boxes: {boxes}")
    return calculate_focusing_power(boxes)


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH)[0]
    sample = util.read_strs(SAMPLE_PATH)[0]

    # print("PART 1")
    # print(part1(input))
    # print(part1(sample))

    print("PART 2")
    print(part2(input))
    print(part2(sample))
