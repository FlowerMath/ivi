import unittest

from brackets import BracketMatcher


class MathUtilsTest(unittest.TestCase):
    def test_brackets(self):
        scenarios = {'()fgh()[(){()}]': True,
                     '': True,
                     'ss(ffff)]': False,
                     '[()': False,
                     '{}[]()f': True}

        for key in scenarios:
            with self.subTest(i=key):
                self.assertEquals(BracketMatcher.are_brackets_correct(key), scenarios[key])
