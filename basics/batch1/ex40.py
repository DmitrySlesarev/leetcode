import re

# Pattern to match any character repeated 2 or more times
PATTERN = re.compile(r"(.)\1+")


INPUT = """attraction
buzzzz
"""
REF = """atraction
buz
"""

def amend_repetitions(text: str) -> str:
    """Replace repetitive symbols in words by single one.

    Args:
        text(str): A text that may contain repetitive symbols in words

    Returns:
        str: Text that does not contain repetitive symbols in words

    Examples:
        >>> amend_repetitions("Hello!!! How are you???")
        'Helo! How are you?'
        >>> amend_repetitions("Woow, this is coool")
        'Wow, this is col'
    """
    res = []
    for line in text.splitlines():
        upd_line = []
        for word in line.split():
            upd_word = PATTERN.sub(r'\1', word)
            upd_line.append(upd_word)
        res.append(" ".join(upd_line))

    return "\n".join(res)


def test_res():
    assert amend_repetitions(INPUT).strip() == REF.strip()


# if __name__ == "__main__":
#     print(amend_repetitions(INPUT))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=True))