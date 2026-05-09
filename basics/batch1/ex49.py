import re

PATTERN = re.compile(r"(\w)\1+", re.IGNORECASE)

INPUT = """
attraction
buzzzz
"""

REF = """atraction
buz
"""

def rem_rep(text: str) -> str:
    """
    Remove consequtive repetitve characters in text
    Arguments:
        text (str): Text that may contain repetitve characters
    Returns:
        (str): Text that does not contain any repetitive charactes
    Examples:
        >>> rem_rep("Hello world!")
        'Helo world!'
        >>> rem_rep("AAAaa")
        'A'
    """
    res = []
    for line in text.splitlines():
        upd = []
        for word in line.strip().split():
            word = PATTERN.sub(r"\1", word)
            upd.append(word)
        res.append(" ".join(upd))
    return "\n".join(res)


def test_output():
    assert rem_rep(INPUT).strip() == REF.strip()


if __name__ == "__main__":
    print(rem_rep(INPUT))
