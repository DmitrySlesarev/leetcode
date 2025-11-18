import re

PATTERN = re.compile(r"(\w+)\1")

TEST_INPUT = """
blabla is a tandem repetition
123123 is good too
go go
aaa
"""

REF = """
blabla is a tandem repetition
123123 is good too
"""


def find_reps(text: str) -> str:
    """
    Check if text contents tamdem repetition.
    Args:
        text(str): That may contain repetitive strings.
    Returns:
        Lines with tandem repetitions.
    """
    res = [line for line in text.splitlines() if PATTERN.search(line)]
    return "\n".join(res)


if __name__ == "__main__":
    print(find_reps(TEST_INPUT))
