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
# # Advent of code day 8

# %%
import unittest
import numpy as np


# %%
class TestDay8_part1(unittest.TestCase):
    """Tests for day 6, part 1."""
    def test_shape(self):
        image = Image('./data/day8/test1.txt', width=3, height=2)
        self.assertEqual(image.data.shape, (2, 2, 3))


# %%
class Image:
    def __init__(self, path, width, height):
        self.data = (
            np.genfromtxt(path, delimiter=1, dtype=int)
            .reshape(-1, height, width)
        )
    
    @staticmethod
    def count_array_occurence(arr, digit):
        return np.where(arr == digit, 1, 0).sum()
    
    @classmethod
    def count_occurences(cls, digit):
        return lambda x: cls.count_array_occurence(x, digit)
    
    @property
    def min_0_layer(self):
        return (
            np.apply_along_axis(
                self.count_occurences(0),
                1,
                self.data.reshape(self.data.shape[0], -1)
            )
            .argmin()
        )
    
    @property
    def validate(self):
        layer = self.data[self.min_0_layer]
        return (
            Image.count_array_occurence(layer, 1)
            * Image.count_array_occurence(layer, 2)
        )


# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%
solution = Image('./data/day8/input.txt', width=25, height=6)

# %%
solution.validate
