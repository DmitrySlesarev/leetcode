class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        if not t:
            return False

        if len(s) > len(t):
            return False

        j = 0
        for i in range(len(t)):
            if j < len(s):
                if s[j] == t[i]:
                    j += 1
                    if j == len(s):
                        return True

        return j == len(s)


class TestSolution:
    def test_s_is_sub_t(self):
        s = "abc"
        t = "ahbgdc"
        expected = True

        got = Solution().isSubsequence(s, t)

        assert got == expected
