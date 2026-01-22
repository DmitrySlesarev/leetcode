import pytest
import sys


@pytest.mark.parametrize("number1", [1,2,3])
@pytest.mark.parametrize("number2", [4,5,6])
@pytest.mark.parametrize("number3", [7,8,9])
def test_sum_from_builtins(number1: int, number2: int, number3: int) -> None:
    got = sum([number1, number2, number3])

    assert got == number1 + number2 + number3


@pytest.mark.skip(
    reason="Known error in ver 1.2.3, bugfix is pending"
)
def test_some_function() -> None:
    assert some_function() == expected_result

@pytest.mark.skipif(
    sys.platform == "linux",
    reason = "Linux is not supported"
)
def test_win_specifix_func() -> None:

    win_specific_func = lambda: print("hello world")

    expected_result = None

    assert win_specific_func == expected_result

@pytest.mark.xfail(
    reason="Expected to fail test"
)
def test_scenario_return_expected_fail() -> None:
    assert True == False