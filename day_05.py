# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3 (adventofcode)
#     language: python
#     name: adventofcode
# ---

# %%
import unittest
from intcode import Intcode


# %%
class TestDay5_part1(unittest.TestCase):
    """Tests for day 5, part 1."""
    def test_opcode(self):
        program = Intcode([1002])
        self.assertEqual(program.opcode, 2)
    
    def test_modes1(self):
        program = Intcode([1002])
        self.assertEqual(program.modes, (0, 1, 0))
    
    def test_modes2(self):
        program = Intcode([10102])
        self.assertEqual(program.modes, (1, 0, 1))
    
    def test_instruction1(self):
        program = Intcode([1101, 100, -1, 4, 0])
        self.assertEqual(program.instruction, [1101, 100, -1, 4])

    def test_instruction2(self):
        program = Intcode([4, 100, 99])
        self.assertEqual(program.instruction, [4, 100])
    
    def test_example1(self):
        program = Intcode([3, 0, 4, 0, 99], user_input=[7, ])
        output = program.execute()
        self.assertEqual(output, [7])
    
    def test_example2(self):
        program = Intcode([1101, 100, -1, 4, 0])
        output = program.execute()
        self.assertEqual(program.opcodes, [1101, 100, -1, 4, 99])
    
    def test_example3(self):
        program = Intcode([3,9,8,9,10,9,4,9,99,-1,8], user_input=[8, ])
        output = program.execute()
        self.assertEqual(output, [1])
    
    def test_example4(self):
        program = Intcode([3,9,7,9,10,9,4,9,99,-1,8], user_input=[9, ])
        output = program.execute()
        self.assertEqual(output, [0])
    
    def test_example5(self):
        program = Intcode([3,3,1108,-1,8,3,4,3,99], user_input=[9, ])
        output = program.execute()
        self.assertEqual(output, [0])
    
    def test_example6(self):
        program = Intcode([3,3,1107,-1,8,3,4,3,99], user_input=[5, ])
        output = program.execute()
        self.assertEqual(output, [0])
    
    def test_jump_if_true(self):
        program = Intcode([5, 10, 6, 0, 0, 0, 99])
        output = program.execute()
        self.assert_equal(program.instruction_pointer, 6)
    
    def test_jump_pos(self):
        program = Intcode(
            [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],
            user_input=[0, ]
        )
        output = program.execute()
        self.assertEqual(output, [0])
    
    def test_jump_imm(self):
        program = Intcode(
            [3,3,1105,-1,9,1101,0,0,12,4,12,99,1],
            user_input=[100, ]
        )
        output = program.execute()
        self.assertEqual(output, [1])
    
    def test_larger_example_1(self):
        program = Intcode.from_file(
            "./data/day_05/larger_example.txt",
            user_input=[4, ]
        )
        output = program.execute()
        self.assertEqual(output, [999])
    
    def test_larger_example_2(self):
        program = Intcode.from_file(
            "./data/day_05/larger_example.txt",
            user_input=[8, ]
        )
        output = program.execute()
        self.assertEqual(output, [1000])
    
    def test_larger_example_3(self):
        program = Intcode.from_file(
            "./data/day_05/larger_example.txt",
            user_input=[10, ]
        )
        output = program.execute()
        self.assertEqual(output, [1001])



# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%
solution = Intcode.from_file("data/day_05/input.txt", user_input=[1])

# %%
result = solution.execute()

# %%
result

# %%
part2 = Intcode.from_file("data/day_05/input.txt", user_input=[5])

# %%
part2.execute()

# %%
