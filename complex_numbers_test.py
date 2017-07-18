import unittest

from complex_numbers_class import ComplexNumber

first_1 = ComplexNumber(2, 3)
first_2 = ComplexNumber(0, 0)
first_3 = ComplexNumber(-3, 5)
second_1 = ComplexNumber(1, 6)
second_2 = ComplexNumber(1, 3)
second_3 = ComplexNumber(3, -6)


class ComplexNumberTest(unittest.TestCase):
    def test_complex_plus(self):
        scenarios = [
            (first_1, second_1, ComplexNumber(3, 9)),
            (first_2, second_2, ComplexNumber(1, 3)),
            (first_3, second_3, ComplexNumber(0, -1))
        ]

        for current_scenario in scenarios:
            first = current_scenario[0]
            second = current_scenario[1]
            with self.subTest(i=second):
                self.assertEquals(first.plus(second), current_scenario[2])

    def test_complex_minus(self):
        scenarios = [
            (first_1, second_1, ComplexNumber(1, -3)),
            (first_2, second_2, ComplexNumber(-1, -3)),
            (first_3, second_3, ComplexNumber(-6, 11))
        ]

        for current_scenario in scenarios:
            first = current_scenario[0]
            second = current_scenario[1]
            with self.subTest(i=second):
                self.assertEquals(first.minus(second), current_scenario[2])

    def test_complex_adj(self):
        scenarios = [
            (first_1, ComplexNumber(2, -3)),
            (first_2, ComplexNumber(0, 0)),
            (first_3, ComplexNumber(-3, -5))
        ]

        for current_scenario in scenarios:
            first = current_scenario[0]
            with self.subTest(i=first):
                self.assertEquals(first.adj(), current_scenario[1])

    def test_complex_module(self):
        scenarios = [
            (first_1, 13),
            (first_2, 0),
            (first_3, 34)
        ]

        for current_scenario in scenarios:
            first = current_scenario[0]
            with self.subTest(i=first):
                self.assertEquals(first.module2(), current_scenario[1])

    def test_complex_multi(self):
        scenarios = [
            (first_1, second_1, ComplexNumber(-16, 15)),
            (first_2, second_2, ComplexNumber(0, 0)),
            (first_3, second_3, ComplexNumber(21, 33))
        ]

        for current_scenario in scenarios:
            first = current_scenario[0]
            second = current_scenario[1]
            with self.subTest(i=second):
                self.assertEquals(first.multi(second), current_scenario[2])

    def test_complex_div(self):
        scenarios = [
            (first_1, second_1, ComplexNumber(20 / 37, -9 / 37)),
            (first_2, second_2, ComplexNumber(0, 0)),
            (first_3, second_3, ComplexNumber(-39 / 45, -3 / 45))
        ]

        for current_scenario in scenarios:
            first = current_scenario[0]
            second = current_scenario[1]
            with self.subTest(i=first):
                self.assertAlmostEquals(first.division(second), current_scenario[2])
