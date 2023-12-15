import pytest
from days import day12

TEST_INPUT = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

def test_part1():
    result = day12.part1(TEST_INPUT)
    expected_result = 21
    assert result == expected_result

def test_part2():
    result = day12.part2(TEST_INPUT)
    expected_result = 21
    assert result == expected_result

