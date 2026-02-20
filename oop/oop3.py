class Clock:
    __DAY = 60 * 60 * 24  # sec * sec * h

    @classmethod
    def add_formatting(cls, var):
        return str(var).rjust(2, "0")

    def __init__(self, seconds: int):
        if seconds > self.__DAY:
            seconds = seconds % self.__DAY
        self.__seconds = seconds

    @property
    def get_raw(self):
        return self.__seconds

    @property
    def get_time(self):
        s = self.__seconds % 60
        m = self.__seconds // 60 % 60
        h = self.__seconds // 60 // 60 % 24
        return (f"{self.add_formatting(h)}:"
                f"{self.add_formatting(m)}:"
                f"{self.add_formatting(s)}")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(f"Should be instance of 'int' or {self.__class__.__name__}")
        seconds = other
        if isinstance(other, Clock):
            seconds = other.get_raw
        return Clock(self.__seconds + seconds)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(f"Should be instance of 'int' or {self.__class__.__name__}")
        sc = other
        if isinstance(other, Clock):
            sc = other.get_raw
        self.__seconds += sc
        return self



def test_clock_3600sec_eq_1hour():
    expected = "01:00:00"

    got = Clock(3600).get_time

    assert got == expected


if __name__ == "__main__":
    c1 = Clock(1000)
    print(f"{c1.get_time=}")
    c2 = Clock(2000)
    # c3 = c1 + c2
    # print(c3.get_raw)
    # print(c3.get_time)
    # c4 = c3 + 1000
    # print(c4.get_time)
    # c5 = c1 + c2 + c3 + c4
    # print(c5.get_time)
    c3 = 100 + c1
    print(f"{c3.get_time=}")
    c3 += 100
    print(f"{c3.get_time=}")

