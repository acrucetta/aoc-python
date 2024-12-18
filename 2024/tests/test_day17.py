import logging
import pytest
from ..day17 import Program


class TestProgram:
    def test_case_1(self):
        program = Program(reg_a=0, reg_b=0, reg_c=9, ops=[2, 6])
        program.run_pt1(2, 6)
        assert program.b == 1

    def test_case_2(self, caplog):
        program = Program(reg_a=10, reg_b=0, reg_c=0, ops=[5, 0, 5, 1, 5, 4])
        with caplog.at_level(logging.INFO):
            program.run_pt1(5, 0)
            program.run_pt1(5, 1)
            program.run_pt1(5, 4)
        assert caplog.text == "0\n1\n2\n"

    def test_case_3(self, caplog):
        program = Program(reg_a=2024, reg_b=0, reg_c=0, ops=[0, 1, 5, 4, 3, 0])
        with caplog.at_level(logging.INFO):
            program.run_pt1(0, 1)
            program.run_pt1(5, 4)
            program.run_pt1(3, 0)
        assert caplog.text == "4\n2\n5\n6\n7\n7\n7\n7\n3\n1\n0\n"
        assert program.a == 0

    def test_case_4(self):
        program = Program(reg_a=0, reg_b=29, reg_c=0, ops=[1, 7])
        program.run_pt1(1, 7)
        assert program.b == 26

    def test_case_5(self):
        program = Program(reg_a=0, reg_b=2024, reg_c=43690, ops=[4, 0])
        program.run_pt1(4, 0)
        assert program.b == 44354
