# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools
from typing import List, Optional, Tuple
import util as util
from sympy import symbols, solve, Eq

DAY = 13
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

What's the minimum number of buttons we can press
to get to 8400 and 5400.

E.g., 
94A+22B=8400
34A+67B=5400

We can solve this by solving the first equation for A
and replacing that on the second one. 
"""


def solve_equation(
    coefficients: Tuple[int, int, int, int], results: Tuple[int, int]
) -> Optional[Tuple[int, int]]:
    e1a, e1b, e2a, e2b = coefficients
    r1, r2 = results
    A, B = symbols("A B")
    eq1 = Eq(e1a * A + e1b * B, r1)
    eq2 = Eq(e2a * A + e2b * B, r2)

    solution = solve((eq1, eq2), (A, B))
    # If the solution doesn't have ints, return None
    if solution[A].is_integer and solution[B].is_integer:
        return (solution[A], solution[B])
    return None


def parse_input(input: str):
    nums = "[X][+]([0-9]{2})|[Y][+]([0-9]{2})"
    res = "[X][=]([0-9]+)|[Y][=]([0-9]+)"
    # Capture group 1 and group 2 in nums
    # Capture group 1 and group 2 in res
    coeff_match = re.findall(nums, input)
    x_coeffs = []
    y_coeffs = []
    for tuple in coeff_match:
        if tuple[0]:
            x_coeffs.append(tuple[0])
        if tuple[1]:
            y_coeffs.append(tuple[1])
    res_match = re.findall(res, input)
    res = []
    for tuple in res_match:
        if tuple[0]:
            res.append(tuple[0])
        if tuple[1]:
            res.append(tuple[1])
    return (x_coeffs, y_coeffs, res)


def part1(input: List[str]) -> int:
    total_pushes = 0
    for button_config in input:
        x_coeff, y_coeff, results = parse_input(button_config)
        coeffs = tuple(map(int, (x_coeff[0], x_coeff[1], y_coeff[0], y_coeff[1])))
        results = tuple(map(int, (results[0], results[1])))
        pushes = solve_equation(coeffs, results)  # type: ignore
        if pushes:
            a_pushes, b_pushes = pushes
            total_pushes += (a_pushes * 3) + (b_pushes * 1)
    return total_pushes


def part2(input: str) -> int:
    total_pushes = 0
    offset = 10000000000000
    for button_config in input:
        x_coeff, y_coeff, results = parse_input(button_config)
        coeffs = tuple(map(int, (x_coeff[0], x_coeff[1], y_coeff[0], y_coeff[1])))
        results = int(results[0]) + offset, int(results[1]) + offset
        pushes = solve_equation(coeffs, results)  # type: ignore
        if pushes:
            print(f"Succeeded with equation: {coeffs}")
            a_pushes, b_pushes = pushes
            total_pushes += (a_pushes * 3) + (b_pushes * 1)
    return total_pushes


def test_solve_equations__with_invalid_coeffs__returns_none():
    # Arrange
    e1a, e1b = 26, 67
    e2a, e2b = 66, 21
    r1, r2 = 12748, 12176

    # Act
    res = solve_equation((e1a, e1b, e2a, e2b), (r1, r2))

    # Assert
    assert res == None, f"Failed, got {res} instead"


def test_solve_equations__with_valid_coeffs__returns_none():
    # Arrange
    e1a, e1b = 94, 22
    e2a, e2b = 34, 67
    r1, r2 = 8400, 5400

    # Act
    res = solve_equation((e1a, e1b, e2a, e2b), (r1, r2))

    # Assert
    assert res == (80, 40), f"Failed, got {res} instead"


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, "\n\n")
    sample = util.read_strs(SAMPLE_PATH, "\n\n")

    # Parse test
    parse_input(sample[0])

    # Tests
    test_solve_equations__with_valid_coeffs__returns_none()
    test_solve_equations__with_invalid_coeffs__returns_none()

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    util.call_and_print(part2, input)
    util.call_and_print(part2, sample)
