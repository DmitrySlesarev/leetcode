from functools import reduce
from time import time


def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial3(n):
    if n in [0, 1]:
        return 1
    numbers = list(range(1, n + 1))
    return reduce(lambda x, y: x * y, numbers)


def count_duration(f):
    def wrapper(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        stop = time()
        print(f"Elapsed time: {stop - start:.6f}")
        return res

    return wrapper


@count_duration
def count_recur(n):
    return factorial(n)


@count_duration
def count_flat(n):
    return factorial2(n)

@count_duration
def count_list(n):
    return factorial3(n)


print(f"Recursion={count_recur(5)} Iterative={count_flat(5)} List={count_list(5)}")
