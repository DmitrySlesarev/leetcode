import re


WORD_PATTERN = re.compile(r".*\bcat\b.*")

TEXT = """cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?
"""

REF = """cat
catapult and cat
"cat"
!cat?
"""

def find_pattern(text: str) -> str:
    """
    Looks for 'cat' word in text and returns string containing it.
    Args:
        text: That may content the 'cat' word.
    Returns:
        str: Lines containing 'cat' word.
    """
    res = [line.strip() for line in text.splitlines() if WORD_PATTERN.search(line)]
    return "\n".join(res)


def test_func_out():
    assert REF.strip() == find_pattern(TEXT)


if __name__ == "__main__":
    print(find_pattern(TEXT))