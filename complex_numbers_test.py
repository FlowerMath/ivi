import unittest

from complex_numbers_class import ComplexNumber


class BubbleSortTest(unittest.TestCase):
    def test_complex_plus(self):
        scenarios = [
            (ComplexNumber(), ComplexNumber(), ComplexNumber()),
            (ComplexNumber(), ComplexNumber(), ComplexNumber()),
            (ComplexNumber(), ComplexNumber(), ComplexNumber())
        ]

        for current_scenario in scenarios:
            unsorted_array = current_scenario[0]
            with self.subTest(i=unsorted_array):
                self.assertEquals(bubble_sort(unsorted_array), current_scenario[1])
