import pytest


class MyTester:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def sum(self) -> int:
        return self._x + self._y

@pytest.fixture()
def tester(request) -> MyTester:
    return MyTester(request.param[0], request.param[1])

class TestIt:
    @pytest.mark.parametrize('tester', [[1,2],[3,0]], indirect=True)
    def test_tc1(self, tester) -> None:
        assert 3 == tester.sum()
