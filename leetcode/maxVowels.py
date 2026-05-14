class Solution:
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}

        if not s or k == 0:
            return 0

        if k > len(s):
            raise ValueError(f"len({s})={len(s)} should be greater than {k}")

        if k == len(s):
            return sum(char for char in s if char in VOWELS)

        max_num = 0

        for i in range(len(s)):
            subs = s[i:i + k:]
            local_max_num = 0

            for letter in subs:
                if letter in VOWELS:
                    local_max_num += 1

            max_num = max(max_num, local_max_num)

        return max_num

    # by ChatGPT
    @staticmethod
    def maxVowels2(s: str, k: int) -> int:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}

        current = sum(1 for ch in s[:k] if ch in VOWELS)
        maximum = current

        for i in range(k, len(s)):
            if s[i - k] in VOWELS:
                current -= 1

            if s[i] in VOWELS:
                current += 1

            maximum = max(maximum, current)

        return maximum


class TestSolution:
    def test_k_eq_three_vowels(self):
        s = "abciiidef"
        k = 3
        expected = 3

        got = Solution.maxVowels2(s=s, k=k)

        assert got == expected

    def test_k_eq_two_vowels(self):
        s = "aeiou"
        k = 2
        expected = 2

        got = Solution.maxVowels2(s=s, k=k)

        assert got == expected

    def test_k_eq_three_but_two_vowels(self):
        s = "leetcode"
        k = 3
        expected = 2

        got = Solution.maxVowels2(s=s, k=k)

        assert got == expected
