import unittest

from bin_search import bin_search


class BubbleSortTest(unittest.TestCase):
    def test_bin_search(self):
        scenarios = [
            ([1, 2, 3, 4, 5], 5, range(4, 5)),
            ([1, 2, 3, 3, 3, 4, 5, 7], 3, range(2, 5)),
            ([-9, -9, 0, 2, 3, 44, 4, 6, 10], -9, range(0, 2)),
            ([-3, -3, -3, 0, 3, 5, 9, 10, 16], 4, None),
            ([1, 4, 5, 9, 10, 14, 16, 20, 20], 20, range(7, 9))
        ]

        for current_scenario in scenarios:
            sorted_array = current_scenario[0]
            checking_element = current_scenario[1]
            with self.subTest(i=sorted_array):
                self.assertEquals(bin_search(sorted_array, checking_element), current_scenario[2])

