# ---
# jupyter:
#   jupytext:
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

# %% [markdown]
# # Advent of code day 6

# %%
import unittest
import attr
from typing import Union


# %%
class TestDay6(unittest.TestCase):
    """Tests for day 6."""
    def test_bodies(self):
        system = System('./data/day6/test.txt')
        self.assertEqual(len(system.bodies), 12)
    
    def test_example_1(self):
        system = System('./data/day6/test.txt')
        self.assertEqual(system.orbits('D'), 3)
    
    def test_example_2(self):
        system = System('./data/day6/test.txt')
        self.assertEqual(system.orbits('L'), 7)
    
    def test_example_3(self):
        system = System('./data/day6/test.txt')
        self.assertEqual(system.orbits('COM'), 0)
    
    def test_example_4(self):
        system = System('./data/day6/test.txt')
        self.assertEqual(system.orbits(), 42)


# %%
@attr.s(auto_attribs=True)
class Body:
    name: str
    parent: Union["Body", None] = attr.ib(default=None)
    
    @property
    def orbits(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.orbits


# %%
class System:
    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            input_data = file.read().splitlines() 
        self.bodies = dict()
        for line in input_data:
            data = line.split(')')
            if data[0] not in self.bodies:
                self.add_body(name=data[0], parent=None)
            self.add_body(name=data[1] , parent=self.bodies[data[0]])
    
    def add_body(self, name, parent):
        self.bodies.update({name: Body(name, parent)})
    
    def orbits(self, body=None):
        if body is None:
            return sum([body.orbits for body in self.bodies.values()])
        else:
            return self.bodies[body].orbits


# %%
solution = System("./data/day6/input.txt")

# %%
solution.orbits()

# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%
