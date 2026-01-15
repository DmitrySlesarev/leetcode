"""Pytest simple example"""
import pytest


def factorial(num: int) -> int:
    """
    Return number with num-sequence in factorial row
    Args:
        num (int): Sequence of a number in factorial row
    Returns:
        int: Factorial value
    Raises:
        TypeError: If num is non-integer
        ValueError: If num is less than zero
    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(3)
        6
    """
    if not isinstance(num, int):
        raise TypeError(f"{num=} should be integer")
    if num < 0:
        raise ValueError(f"{num=} should not be less than zero")

    if num in [0, 1]:
        return 1
    return num * factorial(num - 1)


def test_factorial_return_one_if_number_eq_zero() -> None:
    expected = 1

    got = factorial(0)

    assert expected == got


def test_factorial_return_one_if_number_eq_one() -> None:
    expected = 1

    got = factorial(1)

    assert expected == got


def test_factorial_with_six() -> None:
    expected = 720

    got = factorial(6)

    assert expected == got


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, 1),
        (1, 1),
        (5, 120),
    ],
)
def test_factorial(number: int, expected: int) -> None:
    got = factorial(number)

    assert expected == got


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(0, 1, id="return one if number equal zero"),
        (1, 1),
        (5, 120),
    ],
)
def test_factorial(number: int, expected: int) -> None:
    got = factorial(number)

    assert got == expected


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
