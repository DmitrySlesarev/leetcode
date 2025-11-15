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

    # Make sure there is at least one non-empty string
    max_len = 0
    for word in strs:
        if len(word) > max_len:
            max_len = len(word)
    if max_len == 0:  # Changed from assert to return
        return ""

    freq = dict.fromkeys(list(ascii_lowercase), 0)

    # a. Check early if there is no common prefixes
    # Prepare dict of frequencies
    for word in strs:
        if word:  # Check if word is not empty
            starting_letter = word[0].lower()
            freq[starting_letter] += 1

    # Remove words with single prefix
    double = freq.copy()
    for f in freq:
        if freq[f] < 2:
            double.pop(f)
    freq = double
    # If there is no common prefixes, return empty string
    if not freq:
        return ""

    # b. Get the longest prefix - SIMPLIFIED approach
    min_len = min(len(s) for s in strs if s)  # Get minimum length of non-empty strings

    # Compare character by character
    for i in range(min_len):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return strs[0][:i]

    # Return the prefix up to the shortest string length
    return strs[0][:min_len]


def test_out_1():
    assert longestCommonPrefix(INPUT1).strip() == REF1.strip()


def test_out_2():
    assert longestCommonPrefix(INPUT2).strip() == REF2.strip()


def test_out_3():
    assert longestCommonPrefix(INPUT3).strip() == REF3.strip()


if __name__ == "__main__":
    print(longestCommonPrefix(INPUT1))