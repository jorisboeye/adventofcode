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
import numpy as np
import pandas as pd

# %%
example1 = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
example2 = [
    'R75,D30,R83,U83,L12,D49,R71,U7,L72',
    'U62,R66,U55,R34,D71,R55,D58,R83'
]
example3 = [
    'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
    'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
]
class TestsDay3(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(distance(*example1), 6)
    
    def test_example2(self):
        self.assertEqual(distance(*example2), 159)
    
    def test_example3(self):
        self.assertEqual(distance(*example3), 135)
        
    def test_example4(self):
        self.assertEqual(steps(*example1), 30)
    
    def test_example5(self):
        self.assertEqual(steps(*example2), 610)
    
    def test_example6(self):
        self.assertEqual(steps(*example3), 410)
    


# %%
def next_step(wire, orientation):
    step = wire[-1]
    if orientation == 'U':
        step = (wire[-1][0] + 1, wire[-1][1])
    elif orientation == 'D':
        step = (wire[-1][0] - 1, wire[-1][1])
    elif orientation == 'R':
        step = (wire[-1][0], wire[-1][1] + 1)
    else:
        step = (wire[-1][0], wire[-1][1] - 1)
    return step


# %%
def add_section(wire, section):
    for step in range(int(section[1:])):
        wire.append(next_step(wire, orientation=section[0]))


# %%
def make_wire(wire_text):
    sections = wire_text.split(',')
    wire = [(0, 0)]
    for section in sections:
        add_section(wire, section)
    return wire


# %%
def get_intersections(*wires):
    wire_sets = [set(wire) for wire in wires]
    return set.intersection(*wire_sets) - {(0, 0)}


# %%
def manhattan(point):
    return abs(point[0]) + abs(point[1])


# %%
def distance(*args):
    wires = [make_wire(wire_text) for wire_text in args]
    intersections = get_intersections(*wires) 
    distances = [manhattan(i) for i in intersections]
    return min(distances)


# %%
def count_steps(wires, point):
    return sum([wire.index(point) for wire in wires])


# %%
def steps(*args):
    wires = [make_wire(wire_text) for wire_text in args]
    intersections = get_intersections(*wires)
    steps = [count_steps(wires, p) for p in intersections]
    return min(steps)


# %%
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# %% [markdown]
# # Solutions

# %%
with open("data/day_03/input.txt", 'r') as file:
    text = file.readlines()

# %%
distance(*[t.strip() for t in text])

# %%
steps(*[t.strip() for t in text])
