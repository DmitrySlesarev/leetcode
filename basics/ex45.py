def fibonacci_recursive(n):
    if not isinstance(n, int):
        raise TypeError("Should be integer!")

    if n < 0:
        raise ValueError("Should be greater than zero!")

    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_generator(n):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # print(fibonacci_recursive(5))
    f = fibonacci_generator(5)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
