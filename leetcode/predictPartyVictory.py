class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        if not senate:
            raise ValueError("At least one member should be present!")

        if not ("R" in senate):
            return "Dire"

        if not ("D" in senate):
            return "Radiant"

        flag = 'R' if senate.startswith('R') else 'D'
        t = list(senate)
        while True:
            if flag == 'R':
                t.remove('D')
            else:
                t.remove('R')

            if len(t) == 1:
                break

            flag = 'D' if flag == 'R' else 'R'

        return 'Radiant' if t.pop() == 'R' else 'Dire'

    def predictPartyVictory2(self, senate: str) -> str:
        """ DeepSeek's version """

        radiant = []
        dire = []
        n = len(senate)

        for idx, val in enumerate(senate):
            if val == 'R':
                radiant.append(idx)
            else:
                dire.append(idx)

        while radiant and dire:
            r_idx = radiant.pop(0)
            d_idx = dire.pop(0)

            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)

        return "Radiant" if radiant else "Dire"


class TestSolution:
    def test_two_members_wins_first(self):
        senate = "RD"
        expected = "Radiant"

        got = Solution().predictPartyVictory2(senate=senate)

        assert got == expected

    def test_three_members_majority_wins(self):
        senate = "RDD"
        expected = "Dire"

        got = Solution().predictPartyVictory2(senate=senate)

        assert got == expected

    def test_four(self):
        senate = "DDRRR"
        expected = "Dire"

        got = Solution().predictPartyVictory2(senate=senate)

        assert got == expected
