import re
from re import Match
from string import ascii_lowercase


WORD_PATTERN = re.compile(rf"([{ascii_lowercase}])\1+", flags=re.IGNORECASE)

USER_INPUT = """attraction
buzzzz
"""

REF_OUTPUT = """atraction
buz
"""


def find_rep_letters(uin: str) -> str:
    """
    Deletes repetitive letters in words
    Args:
        uin: text containing words
    Returns:
        text with proccessed words
    """
    def replace_rep_letters(match: Match[str]) -> str:
        word = match.group()
        return word[0]

    res = []
    for line in uin.strip().splitlines():
        processed_line = WORD_PATTERN.sub(replace_rep_letters, line)
        res.append(processed_line)

    return "\n".join(res)


if __name__ == "__main__":
    res = find_rep_letters(USER_INPUT)
    print(res)

    assert res.strip() == REF_OUTPUT.strip(), "Should be equal"
