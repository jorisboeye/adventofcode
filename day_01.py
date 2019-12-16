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
#     display_name: Python 3 (adventofcode)
#     language: python
#     name: adventofcode
# ---

# %% [markdown]
# # Day 1

# %%
import attr
import numpy as np
import unittest


# %%
class TestDay1_part1(unittest.TestCase):
    """Tests for day 1, part 1."""
    
    def test_example1(self):
        self.assertEqual(Module(mass=12).base_fuel, 2)
    
    def test_example2(self):
        self.assertEqual(Module(mass=14).base_fuel, 2)
    
    def test_example3(self):
        self.assertEqual(Module(mass=1969).base_fuel, 654)
    
    def test_example4(self):
        self.assertEqual(Module(mass=100756).base_fuel, 33583)


# %%
class TestDay1_part2(unittest.TestCase):
    """Tests for day 1, part 2."""
    
    def test_example1(self):
        self.assertEqual(Module(mass=14).fuel, 2)
    
    def test_example2(self):
        self.assertEqual(Module(mass=1969).fuel, 966)
    
    def test_example3(self):
        self.assertEqual(Module(mass=100756).fuel, 50346)


# %%
@attr.s(auto_attribs=True)
class Module:
    mass: int
    
    @staticmethod
    def fuel_for_mass(mass):
        return (np.floor(mass / 3) - 2).astype(int)
    
    @property
    def base_fuel(self):
        return self.fuel_for_mass(self.mass)
    
    @property
    def fuel_generator(self):
        fuel = self.base_fuel
        while fuel > 0:
            yield fuel
            fuel = self.fuel_for_mass(fuel)  
    
    @property
    def fuel(self):
        return sum(list(self.fuel_generator))


# %%
@attr.s(auto_attribs=True)
class SpaceCraft:
    modules: list
    
    @classmethod
    def from_file(cls, path):
        return cls(modules=[Module(m) for m in np.loadtxt(path, dtype=int)])
    
    @property
    def base_fuel(self):
        return sum([m.base_fuel for m in self.modules])  
    
    @property
    def fuel(self):
        return sum([m.fuel for m in self.modules])


# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%
spacecraft = SpaceCraft.from_file("data/day_01/input.txt")

# %%
spacecraft.base_fuel

# %%
spacecraft.fuel
