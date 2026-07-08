class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ret = False

        if not word1 or not word2:
            return ret

        if len(word1) != len(word2):
            return ret

        if set(word1) == set(word2):
            return not ret

        mapping = [True for ch1, ch2 in zip(word1, word2) if ch1 == ch2]
        success_rate = sum(mapping)
        false_indexes = [ind for  ind, val in enumerate(mapping) if val == False]
        for ind, status in enumerate(mapping, start=0):
            if status is True:
                continue

            operation1 = False
            for i in false_indexes:
                w1 = word1
                w2 = word2
                w1[i], w1[ind] = w1[ind], w1[i]
                m = [True for ch1, ch2 in zip(w1, w2) if ch1 == ch2]
                if sum(m) > success_rate:
                    success_rate = sum(m)
                    word1 = w1
                    word2 = w2
                    false_indexes.remove(i)
                    operation1 = True
                    break

            if not operation1:
                for i in false_indexes:
                    w1 = word1
                    w2 = word2
                    w1.replace(w1[ind], w1[i])
                    m = [True for ch1, ch2 in zip(w1, w2) if ch1 == ch2]
                    if sum(m) > success_rate:
                        success_rate = sum(m)
                        word1 = w1
                        word2 = w2
                        false_indexes.remove(i)
                        break

            if success_rate == len(word1):
                return True

        return ret


class TestSolution:
    def test_ret_eq_true(self):
        word1 = "abc"
        word2 = "bca"
        expected = True

        got = Solution().closeStrings(word1, word2)

        assert got == expected

    def test_ret_eq_false(self):
        word1 = "a"
        word2 = "aa"
        expected = False

        got = Solution().closeStrings(word1, word2)

        assert got == expected

    def test_ret_eq_true2(self):
        word1 = "cabbba"
        word2 = "abbccc"
        expected = True

        got = Solution().closeStrings(word1, word2)

        assert got == expected
