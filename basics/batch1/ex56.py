"""" Python practical sheet """

import re

PATTERN = re.compile(r".*(cat).*\1")

UIN = """catcat
cat and cat
catac
cat
ccaatt
"""

REF = """
catcat
cat and cat
"""


def catch_cat(uin: str) -> str:
    """
    Gets lines where 'cat' is present at least 2 times.
    Args:
        uin(str): Text that may contain 'cat' word
    Returns:
        Text that contain 'cat' at least twice
    Examples:
        >>> catch_cat('cat and cat\\n nothing is here')
        'cat and cat'
        >>> catch_cat('just a simple line')
        ''
    """
    if not isinstance(uin, str):
        raise TypeError("Should be of str type!")
    res = []
    for line in uin.splitlines():
        if PATTERN.search(line):
            res.append(line)
    return "\n".join(res)


def test_res():
    assert catch_cat(UIN).strip() == REF.strip()


if __name__ == "__main__":
    print(catch_cat(UIN))
