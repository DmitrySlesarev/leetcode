import re

PATTERN = re.compile(r"(\w+)\1{2,}", re.IGNORECASE)

INPUT = """
catcat
cat and cat
catac
cat
ccaatt
"""

REF = """
catcat
cat and cat
"""


def find_rep_lines(text: str) -> str:
    """
    Returns lines with repetitive parts
    Arguments:
        text (str): Text that may contain repetitive words
    Returns:
        Lines with repetitive words
    Examples:
        >>> find_rep_lines('something something\n Nothing here\n')
        'something something'
        >>> find_rep_lines("text without repetitve lines")
        ''
    """
    if not isinstance(text, str):
        raise TypeError("Argument should be string!")

    res = []
    for line in text.splitlines():
        if PATTERN.search(line):
            res.append(line.strip())
    return "\n".join(res) if len(res) > 0 else ""


def test_output():
    assert find_rep_lines(INPUT).strip() == REF.strip()


if __name__ == "__main__":
    print(find_rep_lines(INPUT))
