# Add the parent directory to the Python path so `common` can be found
from typing import List, Optional
import util as util
import unittest

"""
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0

We have a 3-bit computer, with a program as a list 
of 3-bit number. (0 through 7) like 0,1,2,3 
We also have 3 registers: A,  b and C. Can hold any int.

The PC knows 8 instructions. Each inst reads the 3-bit number
after it as an input; this is called an operand.

So, the program 0,1,2,3 would run the instruction whose opcode is 0 and pass 
it the operand 1,
then run the instruction having opcode 2 and pass it the operand 3, then halts

Operands have values associated with them: 0-3 literal, 4-6 A-C, 7 is reserved.

Instructions:
- 0 adv - division
- 1 bxl - bitwise xor
- 2 bst - calculates value of its combo operand modulo 8 then writes to B registers
- 3 jnz - does nothing if A is 0, if not 0 then jumps by setting the instruction
  pointer to the value of its literal; the pointer is not increased by 2 after this
- 4 bxc - calculates bitwise xor of register B and C, sores in register B
- 5 out - calculates value of its combo operand modulo 8, and outputs that
- 6 bdv - like adv except the result is stored in B register (numerator read from A) 
- 7 cdv - like adv, except stores in C register (num from A)

Part 2:

The last two numbers are 3,0 which means that we will divide the ouput 
by 8.

The output will come from the last 3 digits of the bit.
Whenever we call out i.e., 5, we will need to have 
bits that match whatever last instruction we're processing.

"""

DAY = 17
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"


class Program:
    def __init__(self, reg_a: int, reg_b: int, reg_c: int, ops: List[int]):
        self.a = reg_a
        self.b = reg_b
        self.c = reg_c
        self.initial_ops = "".join(list(map(str, ops)))
        self.ops = ops
        self.ptr = 0
        self.output = ""

    def run_pt1(self):
        while True:
            print(
                f"\nRegisters:\nA:{bin(self.a)[2:]}\nB:{bin(self.b)[2:]}\nC:{bin(self.c)[2:]}"
            )
            print(f"Output: {self.output}\n")
            if self.ptr < len(self.ops):
                op1, op2 = self.ops[self.ptr], self.ops[self.ptr + 1]
                self.compute(op1, op2)
            else:
                # Halt the program
                break

    def run_pt2(self):
        self.a = 0
        while True:
            print(f"Current register A: {self.a}")
            while True:
                if self.ptr < len(self.ops):
                    op1, op2 = self.ops[self.ptr], self.ops[self.ptr + 1]
                    self.compute(op1, op2)
                else:
                    # Halt the program
                    break
            if self.initial_ops == self.output:
                return
            self.a += 1

    def _combo(self, op: int) -> int:
        match op:
            case 0 | 1 | 2 | 3:
                return op
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                raise ValueError("Op not valid")

    def compute(self, opcode: int, operand: int) -> None:
        match opcode:
            case 0:
                print(f"DIV: A = {self.a} / 2**{self._combo(operand)}")
                self.a = int(self.a / (2 ** self._combo(operand)))
            case 1:
                print(f"XOR: B = {self.b} ^ {operand}")
                self.b = self.b ^ operand
            case 2:
                print(f"MOD: B = {self._combo(operand)} % 8")
                self.b = self._combo(operand) % 8
            case 3:
                print(f"JNZ: if A != 0, jump to {operand}")
                if self.a != 0:
                    self.ptr = operand
                    return None
            case 4:
                print(f"XOR: B = {self.b} ^ C")
                self.b = self.b ^ self.c
            case 5:
                res = self._combo(operand) % 8
                print(f"OUT: output {res}")
                self.output += str(res)
                # print(res, end=",")
            case 6:
                print(f"BDV: B = {self.a} / 2^{self._combo(operand)}")
                self.b = int(self.a / (2 ** self._combo(operand)))
            case 7:
                print(f"CDV: C = {self.a} / 2^{self._combo(operand)}")
                self.c = int(self.a / (2 ** self._combo(operand)))
        self.ptr += 2


def part1(input: str) -> int:
    regs = list(map(int, map(lambda x: x.split(":")[1], input[0].split("\n"))))
    program = list(map(int, input[1].split("Program:")[1].split(",")))
    prog = Program(117440, regs[1], regs[2], program)
    prog.run_pt1()
    return 0


def part2(input: str) -> int:
    regs = list(map(int, map(lambda x: x.split(":")[1], input[0].split("\n"))))
    program = list(map(int, input[1].split("Program:")[1].split(",")))
    prog = Program(regs[0], regs[1], regs[2], program)
    prog.run_pt2()


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, "\n\n")
    sample = util.read_strs(SAMPLE_PATH, "\n\n")

    print("PART 1")
    # util.call_and_print(part1, input)
    util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    # util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
