# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools
from typing import List
import util as util

DAY = 11
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"


def apply_rules(stone: int) -> List[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        half = len(str_stone) // 2
        stone1, stone2 = int(str_stone[:half]), int(str_stone[half:])
        return [stone1, stone2]
    return [stone * 2024]


def part1(input: str) -> int:
    # Parsing
    stones = list(map(int, input))

    # Logic
    blinks = 0
    while blinks < 25:
        print(f"Blink: {blinks}, current stones: {stones}")
        new_stones = []
        for stone in stones:
            processed_stones = apply_rules(stone)
            new_stones.extend(processed_stones)
        stones = new_stones
        blinks += 1
    return len(stones)


def part2(input: str) -> int:
    # Parsing
    stones = list(map(int, input))

    # Logic
    blink_cache = {stone: 1 for stone in stones}
    for i in range(75):
        print(f"Blink: {i}, current stones: {blink_cache}\n")
        new_cache={}
        for stone, count in list(blink_cache.items()):
            if count > 0:
                blink_cache[stone] -= 1
                processed_stones = apply_rules(stone)
                for p_stone in processed_stones:
                    new_cache[p_stone] = new_cache.get(p_stone, 0) + count
        # Clean the cache
        blink_cache = new_cache
    return sum(blink_cache.values())


def test_stone_rules():
    # Arrange
    stones = [0, 40, 1000, 3]
    expected = [[1], [4, 0], [10, 0], [2024 * 3]]

    # Apply rules
    for i, stone in enumerate(stones):
        res = apply_rules(stone)
        assert (
            res == expected[i]
        ), f"Result not as expected, got: {res}, expected: {expected[i]}"


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH)
    sample = util.read_strs(SAMPLE_PATH)

    # Tests
    test_stone_rules()

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
