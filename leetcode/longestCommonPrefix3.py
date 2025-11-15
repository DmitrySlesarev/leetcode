"""Find the longest common prefix string amongst an array of strings"""

from string import ascii_lowercase

INPUT1 = ["flower", "flow", "flight"]
INPUT2 = ["dog", "racecar", "car"]
INPUT3 = ["cheese", "spam", "egg", "egg"]

REF1 = "fl"
REF2 = ""
REF3 = "egg"


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    if len(strs) == 1:
        return strs[0]

    # Find the shortest string length to avoid index errors
    min_len = min(len(s) for s in strs)

    # Compare characters at each position across all strings
    for i in range(min_len):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return strs[0][:i]

    # If we've gone through all characters up to min_len,
    # the common prefix is the prefix of that length
    return strs[0][:min_len]


def test_out_1():
    assert longestCommonPrefix(INPUT1).strip() == REF1.strip()


def test_out_2():
    assert longestCommonPrefix(INPUT2).strip() == REF2.strip()


def test_out_3():
    assert longestCommonPrefix(INPUT3).strip() == REF3.strip()


if __name__ == "__main__":
    print(longestCommonPrefix(INPUT1))