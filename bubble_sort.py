def bubble_sort(a: list):
    for i in range(0, len(a) - 1):
        flag = 0
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                flag = 1
        if flag == 0:
            break
    return a
