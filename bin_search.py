def max_index(a: list, index: int) -> int:
    elem = a[index]
    while index < len(a) - 1 and elem == a[index + 1]:
        index = index + 1
    return index + 1


def min_index(a: list, index: int) -> int:
    elem = a[index]
    while index > 0 and elem == a[index - 1]:
        index = index - 1
    return index


def bin_search(a: list, elem: int) -> range:
    if len(a) == 0:
        return range(-1, -1)
    last = len(a)
    first = 0
    if elem == a[0]:
        return range(min_index(a, 0), max_index(a, 0))
    while last - first > 1:
        half = first + (last - first) // 2
        if a[half] > elem:
            last = half
        elif a[half] < elem:
            first = half
        else:
            return range(min_index(a, half), max_index(a, half))


l = [1, 1, 1, 1, 3, 7, 10, 10, 10, 10, 10, 10]
print(bin_search(l, 10))  # 5-10
print(bin_search(l, 3))  # 0-3
