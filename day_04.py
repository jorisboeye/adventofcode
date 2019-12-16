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
# # Advent of code day 4

# %%
import unittest


# %%
class TestDay4_1(unittest.TestCase):
    """Tests for day 4, part 1."""
    def test_example_1(self):
        self.assertTrue(check_password(111111))
        
    def test_example_2(self):
        self.assertFalse(check_password(223450))
        
    def test_example_3(self):
        self.assertFalse(check_password(123789))


# %%
def check_password(password):
    digits = [int(i) for i in str(password)]
    return len(digits) == 6 and len(set(digits)) < 6 and digits == sorted(digits)  


# %%
pw_range = range(125730, 579381 + 1)

# %%
len([pw for pw in pw_range if check_password(pw)])


# %%
class TestDay4_2(unittest.TestCase):
    """Tests for day 4, part 2"""
    def test_example_1(self):
        self.assertTrue(check_password_better(112233))
        
    def test_example_2(self):
        self.assertFalse(check_password_better(123444))
        
    def test_example_3(self):
        self.assertTrue(check_password_better(111122))


# %%
def check_repetitions(password):
    pw_string = str(password)
    repetitions = [str(int(c == p)) for c, p in zip(pw_string, pw_string[1:])]
    return '1' in "".join(repetitions).split('0')
    


# %%
def check_password_better(password):
    return check_password(password) and check_repetitions(password)


# %%
len([pw for pw in pw_range if check_password_better(pw)])

# %%
unittest.main(argv=['ignored', '-v'], exit=False)
