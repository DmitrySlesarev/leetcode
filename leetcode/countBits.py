class Solution:
    @classmethod
    def countBits(cls, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for i in range(n+1):
            bi = bin(i)[2:].count('1')
            ans[i] = bi

        return ans


class TestSolution:
    def test_n2_eq_ans(self):
        n = 2
        expected = [0, 1, 1]

        got = Solution.countBits(n)

        assert got == expected

    def test_n5_eq_ans(self):
        n = 5
        expected = [0, 1, 1, 2, 1, 2]

        got = Solution.countBits(n)

        assert got == expected
