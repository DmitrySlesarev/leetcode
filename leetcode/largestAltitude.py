class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        if not gain:
            return 0

        calc_altitudes = [0]
        for ind in range(len(gain)):
            prev_pos = calc_altitudes[-1]
            curr_pos = prev_pos + gain[ind]
            calc_altitudes.append(curr_pos)

        return max(calc_altitudes)


class TestSolution:
    def test_lA_eq_1(self):
        gain = [-5, 1, 5, 0, -7]
        altitudes = [0, -5, -4, 1, 1, -6]
        expected = 1

        got = Solution().largestAltitude(gain)

        assert expected == got

    def test_lA_eq_zero(self):
        gain = [-4, -3, -2, -1, 4, 3, 2]
        expected = 0

        got = Solution().largestAltitude(gain)

        assert expected == got
