# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python (development)
#     language: python
#     name: development
# ---

# %%
import unittest
from intcode import Intcode


# %%
class TestDay2_part1(unittest.TestCase):
    """Tests for day 2, part 1."""
    def test_example1(self):
        program = Intcode([1,9,10,3,2,3,11,0,99,30,40,50])
        program.execute()
        self.assertEqual(
            program.opcodes,
            [3500,9,10,70,2,3,11,0,99,30,40,50]
        )
        
    def test_example2(self):
        program = Intcode([1,0,0,0,99])
        program.execute()
        self.assertEqual(program.opcodes, [2,0,0,0,99])
        
    def test_example3(self):
        program = Intcode([2,3,0,3,99])
        program.execute()
        self.assertEqual(program.opcodes, [2,3,0,6,99])
        
    def test_example4(self):
        program = Intcode([2,4,4,5,99,0])
        program.execute()
        self.assertEqual(program.opcodes, [2,4,4,5,99,9801])
        
    def test_example5(self):
        program = Intcode([1,1,1,4,99,5,6,0,99])
        program.execute()
        self.assertEqual(program.opcodes, [30,1,1,4,2,5,6,0,99])


# %%
class TestDay2(unittest.TestCase):
    def test_instruction(self):
        program = Intcode([1, 0, 0, 0, 99])
        self.assertEqual(program.instruction, [1, 0, 0, 0])


# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%
solution = Intcode.from_file("data/day_02/input.txt")

# %%
solution.initialize_memory(12, 2)
solution.execute()
solution.opcodes[0]

# %%
for noun in range(99):
    for verb in range(99):
        program = Intcode.from_file("data/day_02/input.txt")
        program.initialize_memory(noun, verb)
        program.execute()
        if program.opcodes[0] == 19690720:
            print(f"{100*noun + verb}")

# %%
