class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        tail = None
        res = list()

        if len(word1) > len(word2):
            i = (len(word1) - len(word2)) * (-1)
            tail = word1[i::]
        if len(word2) > len(word1):
            i = (len(word2) - len(word1)) * (-1)
            tail = word2[i::]

        for w1, w2 in zip(word1, word2):
            res.append(w1)
            res.append(w2)

        if tail:
            res.append(tail)

        return "".join(res)

    def mergeAlternately2(self, word1: str, word2: str) -> str:
        res = list()

        i = (-1) * (
            len(word1) - len(word2)
            if len(word1) >= len(word2)
            else len(word2) - len(word1)
        )
        tail = word1[i::] if len(word1) < len(word2) else word2[i::]

        for l1, l2 in zip(word1, word2):
            res.append(l1)
            res.append(l2)

        if i:
            res.append(tail)

        return "".join(res)

    def mergeAlternately3(self, word1: str, word2: str) -> str:
        """ Deepseek's version, not mine"""
        result = []
        for c1, c2 in zip(word1, word2):
            result.extend([c1, c2])

        # Add remaining characters from the longer string
        result.extend([word1[len(word2):], word2[len(word1):]])

        return "".join(result)