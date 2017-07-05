import unittest
from random import randint

from math_utils import is_even, fib, fib_rec, is_between

fib_scenarios = {-10: -55, -9: 34, -8: -21, -7: 13, -6: -8, -5: 5, -4: -3, -3: 2, -2: -1, -1: 1, 0: 0, 1: 1, 2: 1, 3: 2,
                 4: 3, 5: 5,
                 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}


class MathUtilsTest(unittest.TestCase):
    def test_is_even(self):
        random_int = randint(5, 400)
        scenarios = {1: False,
                     2: True,
                     3: False,
                     4: True,
                     random_int: random_int % 2 == 0}

        for key in scenarios:
            with self.subTest(i=key):
                self.assertEquals(is_even(key), scenarios[key])

    def test_is_in_range(self):
        first = 0
        second = 10
        scenarios = {-5: False,
                     0: True,
                     5: True,
                     10: True,
                     15: False}

        for number in scenarios:
            with self.subTest(i=number):
                self.assertEquals(is_between(first, second, number), scenarios[number])

    def test_fib_rec(self):
        for key in fib_scenarios:
            with self.subTest(i=key):
                self.assertEquals(fib_rec(key), fib_scenarios[key])

    def test_fib(self):
        for key in fib_scenarios:
            with self.subTest(i=key):
                self.assertEquals(fib(key), fib_scenarios[key])
