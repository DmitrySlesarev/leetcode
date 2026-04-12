class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in s.strip().split():
            res.append(word)

        return " ".join(reversed(res))
