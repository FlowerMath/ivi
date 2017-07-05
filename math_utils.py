def is_even(number: int) -> bool:
    return number % 2 == 0


def is_between(first, second, number) -> bool:
    return min(first, second) <= number <= max(first, second)


def calc_prefix(n):
    return (-1) ** (n + 1)


def fib_rec(n: int) -> int:
    if n < 0:
        return calc_prefix(n) * fib_rec((-1) * n)
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib(n: int) -> int:
    if n < 0:
        return calc_prefix(n) * fib(-1 * n)
    if n == 0 or n == 1:
        return n
    else:
        previous = 0
        current = 1
        for i in range(2, n + 1):
            temp = current
            current = current + previous
            previous = temp
        return current
