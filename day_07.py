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
import attr
from intcode import Intcode
from pathlib import Path
from itertools import permutations


# %%
class TestDay7_part1(unittest.TestCase):
    """Tests for day 7, part 1."""
    
    def test_example1(self):
        series = Series(
            path=r'./data/day_07/example1.txt',
            phases=[4, 3, 2, 1, 0]
        )
        self.assertEqual(series.output, 43210)
        
    def test_example2(self):
        series = Series(
            path=r'./data/day_07/example2.txt',
            phases=[0, 1, 2, 3, 4]
        )
        self.assertEqual(series.output, 54321)
        
    def test_example3(self):
        series = Series(
            path=r'./data/day_07/example3.txt',
            phases=[1, 0, 4, 3, 2]
        )
        self.assertEqual(series.output, 65210)
        
    def test_reset(self):
        series = Series(
            path=r'./data/day_07/example3.txt',
            phases=[1, 0, 4, 3, 2]
        )
        self.assertEqual(series.output, series.output)


# %%
@attr.s(auto_attribs=True)
class Series:
    path: Path = attr.ib(converter=Path)
    phases: list
    input_value: int = attr.ib(default=0)
        
    def __getitem__(self, item):
        if item < len(self.phases):
            phase = self.phases[item]
            if item == 0:
                user_input = [phase, self.input_value]
            else:
                user_input = [phase, self[item - 1]]
            amplifier = Intcode.from_file(
                self.path,
                user_input=user_input
            )
            return amplifier.execute()[0]
        else:
            raise IndexError('Series index out of range.')
            
    @property
    def output(self):
        return self[len(self.phases) - 1]


# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%
phases = [0, 1, 2, 3, 4]

# %%
max_thrust = 0
best_permutation = []
for permutation in permutations(phases):
    series = Series(
        path=r'./data/day_07/input.txt',
        phases=permutation
    )
    if series.output > max_thrust:
        max_thrust = series.output
        best_permutation = permutation

# %%
max_thrust
