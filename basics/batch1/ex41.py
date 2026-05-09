import re

PATTERN = re.compile(r"(.)\1+")

INPUT = """
attraction
buzzzz
"""

REF = """
atraction
buz
"""


def amend_mult_rep(text: str) -> str:
    """
    Replace multiple repetitions for single letter.
    Args:
        text (str): Text that may contain letters' reps.
    Returns:
        (str): Text that does not contain any letters' reps.
    Example:
        >>> amend_mult_rep("Hello world!")
        'Helo world!'
        >>> amend_mult_rep("Whatt is uppp!!")
        'What is up!'
    """
    res = []
    for line in text.strip().splitlines():
        upd_line = []
        for word in line.split():
            upd_word = PATTERN.sub(r'\1', word)
            upd_line.append(upd_word)
        res.append(" ".join(upd_line))

    return "\n".join(res)


def test_output():
    """Test output of 'amend_mult_rep' func"""
    result = amend_mult_rep(INPUT)
    expected = REF.strip()
    assert result == expected, f"Expected:\n{expected}\n\nGot:\n{result}"


if __name__ == "__main__":
    print("Input:")
    print(INPUT)
    print("Output:")
    print(amend_mult_rep(INPUT))
    print("\nRunning tests...")
    test_output()
    print("All tests passed!")