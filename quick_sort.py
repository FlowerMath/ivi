import random


def quick_sort(lst: list):
    if len(lst) > 1:
        rand = random.randint(0, len(lst) - 1)
        privot = lst[rand]
        less = []
        equal = []
        bigger = []
        for i in lst:
            if i < privot:
                less.append(i)
            if i == privot:
                equal.append(i)
            if i > privot:
                bigger.append(i)
        return quick_sort(less) + equal + quick_sort(bigger)
    else:
        return lst
