class Solution:
    def tribonacci(self, n: int) -> int:

        def gen():
            a, b, c = 0, 1, 1
            while True:
                yield a
                a, b, c = b, c, a + b + c

        generator = gen()
        for i in range(n+1):
            val = next(generator)

        return val


class TestSolution:
    def test_n_eq_4(self):
        n = 4
        expected = 4

        got = Solution().tribonacci(n)

        assert got == expected

    def test_n_eq_25(self):
        n = 25
        expected = 1389537

        got = Solution().tribonacci(n)

        assert got == expected
