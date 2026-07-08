class RecentCounter:
    INTERVAL = 3000

    def __init__(self):
        self.interval = self.INTERVAL
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - self.interval:
            self.requests.pop(0)
        return len(self.requests)


class TestRecentCounter:
    def test_ping(self):
        input = [[], [1], [100], [3001], [3002]]
        expected = [None, 1, 2, 3, 3]

        obj = RecentCounter()
        test_cases = [
            (1, 1),
            (100, 2),
            (3001, 3),
            (3002, 3),
        ]

        for t, expected in test_cases:
            got = obj.ping(t)
            assert got == expected

if __name__ == "__main__":
    test = TestRecentCounter()
    test.test_ping()