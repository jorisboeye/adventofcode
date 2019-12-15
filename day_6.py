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

# %% [markdown]
# # Advent of code day 6

# %%
import unittest
import attr
import networkx as nx
from typing import Union


# %%
class TestDay6_part1(unittest.TestCase):
    """Tests for day 6, part 1."""
    def test_bodies(self):
        system = System('./data/day6/test1.txt')
        self.assertEqual(len(system), 12)
    
    def test_example_1(self):
        system = System('./data/day6/test1.txt')
        self.assertEqual(system.orbits['D'], 3)
    
    def test_example_2(self):
        system = System('./data/day6/test1.txt')
        self.assertEqual(system.orbits['L'], 7)
    
    def test_example_3(self):
        system = System('./data/day6/test1.txt')
        self.assertEqual(system.orbits['COM'], 0)
    
    def test_example_4(self):
        system = System('./data/day6/test1.txt')
        self.assertEqual(system.checksum, 42)


# %%
class System(nx.DiGraph):
    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            data = file.read().splitlines() 
        super().__init__([line.split(')') for line in data])
    
    @property
    def origin(self):
        origin = [key for key, value in self.pred.items() if not value]
        assert len(origin) == 1
        return origin[0]
    
    @property
    def orbits(self):
        return nx.single_source_shortest_path_length(self, self.origin)
    
    @property
    def checksum(self):
        return sum(self.orbits.values())


# %%
solution = System("./data/day6/input.txt")

# %%
solution.checksum

# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%

# %%
