def gnome_sort(lst: list):
    i = 1
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i = i + 1
        else:
            buf = lst[i - 1]
            lst[i - 1] = lst[i]
            lst[i] = buf
            i = i - 1
            if i == 0:
                i = 1
    return lst
