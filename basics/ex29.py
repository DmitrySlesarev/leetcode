import re

PATTERN = re.compile(r"([a]+)", flags=re.IGNORECASE)

TEST_BATCH = """
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
"""

REF = """
There’ll be no more "argh"
argh AaAaAaA
"""


def replace_letters(text: str) -> str:
    """TBU"""
    res = []
    for line in text.splitlines():
        line = PATTERN.sub("argh", line, count=1)
        res.append(line)
    return "\n".join(res)


def test_res():
    assert replace_letters(TEST_BATCH).strip() == REF.strip()


if __name__ == "__main__":
    print(replace_letters(TEST_BATCH))
