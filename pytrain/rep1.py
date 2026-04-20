import sys

import pytest


def factorial(n: int) -> int:
    """ Return factorial num by sequence """
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)


def test_factorial_return_one_if_n_eq_zero() -> None:
    expected = 1
    got = factorial(0)
    assert expected == got


def test_factorial_return_one_if_n_eq_one() -> None:
    expected = 1
    got = factorial(1)
    assert expected == got


def test_factorial_with_five() -> None:
    expected = 120
    got = factorial(5)
    assert expected == got


@pytest.mark.parametrize(
    ("num", "expected"), [
        [0, 1],
        [1, 1],
        [5, 120]
    ]
)
def test_factorial_parametrized(num: int, expected: int) -> None:  # Changed name
    got = factorial(num)
    assert expected == got


@pytest.mark.parametrize(
    ["num", "expected"],
    [  # Added missing outer container
        [0, 1],
        [1, 1],
        pytest.param(10, 3628800, marks=pytest.mark.skip(reason="Slow test")),
    ]
)
def test_factorial_with_skip(num: int, expected: int) -> None:  # Changed name
    got = factorial(num)
    assert expected == got


@pytest.mark.parametrize(
    ["number1", "number2", "number3"],
    [
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9)
    ],
)
def test_sum_from_builtins(number1: int, number2: int, number3: int) -> None:
    got = sum([number1, number2, number3])
    assert got == number1 + number2 + number3


@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Test is not supported on Windows"
)
def test_unix_specific_function() -> None:
    def unix_specific_function():
        return True

    expected_result = True

    assert unix_specific_function() == expected_result


@pytest.fixture()
def five() -> int:
    return 5


def test_first(five: int) -> None:
    got = 5

    assert got == five


@pytest.fixture(scope="function")
def param() -> str:
    return 'Dmitry'


def say_hello(name) -> str:
    return f"Hello, {name}"


def test_say_hello(param):
    expected = "Hello, Dmitry"

    got = say_hello(param)

    assert got == expected


@pytest.fixture()
def a() -> None:
    ...


@pytest.fixture()
def b(a: None) -> None:
    ...


@pytest.fixture()
def c(b: None, fixture_from_another_file: None) -> None:
    ...


@pytest.fixture(scope="function", autouse=True)
def clear_test_db() -> None:
    ...


class MyTester:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def sum(self) -> int:
        return self._x + self._y


@pytest.fixture()
def tester(request) -> MyTester:
    x, y = request.param
    return MyTester(x, y)


class TestIt:
    @pytest.mark.parametrize('tester', [[1, 2], [3, 0]], indirect=True)
    def test_tc1(self, tester) -> None:
        expected = 3
        assert expected == tester.sum()
