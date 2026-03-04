class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds should be integer")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):

        if not isinstance(other, (int, Clock)):
            raise TypeError("Right operand should be int or Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        return self.seconds == self.__verify_data(other)

    def __lt__(self, other):
        return self.seconds < self.__verify_data(other)

    def __gt__(self, other):
        return self.seconds > self.__verify_data(other)

    def __le__(self, other):
        return self.seconds <= self.__verify_data(other)


c1 = Clock(1000)
c2 = Clock(2000)
print(c2 <= c1)
