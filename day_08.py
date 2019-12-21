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
import re


# %%
class TestDay8_part1(unittest.TestCase):
    """Tests for day 6, part 1."""
    def test_shape1(self):
        image = Image.from_file('./data/day_08/test1.txt', width=3, height=2)
        self.assertEqual(image.data.shape, (2, 2, 3))
        
    def test_shape2(self):
        image = Image.from_file('./data/day_08/test2.txt', width=2, height=2)
        self.assertEqual(image.data.shape, (4, 2, 2))


# %%
class Image:
    def __init__(self, data, width, height):
        self.data = data.reshape(-1, height, width)
    
    @classmethod
    def from_file(cls, path, *args, **kwargs):
        return cls(
            data=np.genfromtxt(path, delimiter=1, dtype=int), *args, **kwargs
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
    
    @staticmethod
    def evaluate_pixel(arr):
        return arr[arr!=2][0]
    
    @property
    def evaluated_pixels(self):
        return (
            np.apply_along_axis(
                self.evaluate_pixel, 0, self.data.reshape((self.data.shape[0], -1))
            ).reshape(self.data.shape[1:])
        )
    
    def __repr__(self):
        return (
            re.sub('[\[\] ]', '', np.array_str(self.evaluated_pixels))
            .replace('1', ' ').replace('0', '\u2588')
        )
    
    

# %%
unittest.main(argv=['ignored', '-v'], exit=False)

# %%
solution = Image.from_file('./data/day_08/input.txt', width=25, height=6)

# %%
solution.validate

# %%
solution
