import random
import unittest

from quick_sort import quick_sort


def random_list() -> list:
    r_list = []
    for i in range(0, random.randint(5, 100)):
        r_list.append(random.randint(-100, 100))
    return r_list


class QuickSortTest(unittest.TestCase):
    def test_quick_sort(self):
        scenarios = [
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([1], [1]),
            ([-9, 1, 0, 10, 4, 7, 2, 4, 2], [-9, 0, 1, 2, 2, 4, 4, 7, 10]),
            ([-3, -3, -3, 0, 9, 5, 3, 6], [-3, -3, -3, 0, 3, 5, 6, 9])
        ]

        self.fill_with_random_scenarios(scenarios)

        for current_scenario in scenarios:
            unsorted_array = current_scenario[0]
            with self.subTest(i=unsorted_array):
                self.assertEquals(quick_sort(unsorted_array), current_scenario[1])

    def fill_with_random_scenarios(self, scenarios):
        for i in range(0, 11):
            unsorted_list = random_list()
            sorted_list = unsorted_list.copy()
            sorted_list.sort()
            scenarios.append((unsorted_list, sorted_list))
