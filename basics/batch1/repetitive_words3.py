import re

# WORD_PATTERN = re.compile(r"^(?:.*cat.*){2,}$")
WORD_PATTERN = re.compile(r"^(?=(.*cat.*){2,}).*$")

INPUT_TXT = """catcat
cat and cat
catac
cat
ccaatt
"""

REF_TXT = """
catcat
cat and cat
"""


def check_cat(text) -> str:
    """
    Picks lines with 'cat' in it

    Args:
        text (str): Text that may contain 'cat'
    Returns:
        Lines with 'cat'(s)
    """
    res = []
    for line in text.strip().splitlines():
        if WORD_PATTERN.search(line):
            res.append(line)
    return "\n".join(res)


def test_catching_cats():
    assert check_cat(INPUT_TXT).strip() == REF_TXT.strip()


def test_type_of_cat():
    assert isinstance(check_cat(INPUT_TXT), str)


if __name__ == "__main__":
    print(check_cat(INPUT_TXT))
