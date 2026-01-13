"""Implement Tribonacci numbers calculation"""
import doctest


def tribonacci(ind: int) -> int:
    """
    Return number from Tribonacci row by index
    Args:
        ind (int): Index of number in Tribonacci row
    Returns:
        int: Desired Tribonacci number
    Raises:
        TypeError: In case of ind is NOT integer
        ValueError: In case of ind is less than 0
    Examples:
        >>> tribonacci(0)
        0
        >>> tribonacci(1)
        1
        >>> tribonacci(2)
        1
        >>> tribonacci(5)
        7
    """
    if not isinstance(ind, int):
        raise TypeError(f"{ind=} should be integer")
    if ind < 0:
        raise ValueError(f"{ind=} should be greater than or equal to zero")

    if ind < 2:
        return ind

    a, b, c = 0, 1, 1
    for _ in range(3, ind + 1):
        a, b, c = b, c, a + b + c

    return c


def test_tribonacci_returns_zero_if_seq_eq_zero():
    expected = 0

    got = tribonacci(0)

    assert expected == got


def test_tribonacci_returns_one_if_seq_eq_one():
    expected = 1

    got = tribonacci(1)

    assert expected == got


def test_tribonacci_returns_one_if_seq_eq_two():
    expected = 1

    got = tribonacci(2)

    assert expected == got


def test_tribonacci_returns_seven_if_seq_eq_five():
    expected = 7

    got = tribonacci(5)

    assert expected == got


if __name__ == "__main__":
    # print(tribonacci(5))

    doctest.testmod(verbose=True)
