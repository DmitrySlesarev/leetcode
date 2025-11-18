import re


DPATTERN = re.compile(r"-\d+.\d{2}\b")

INPUT = """-2.4 -5.82 -2.73 10 24.3 180 -3.14"""

REF = """-5.82 -2.73 -3.14"""


def filter_nums(line: str) -> str:
    """
    Get negative float numbers with 2 digits after "."
    Args:
        line: That may content negative nums
    Returns:
         String of negative numbers
    """
    return " ".join(DPATTERN.findall(line))


def test_with_ref():
    assert filter_nums(INPUT) == REF.strip()


def test_wrong_answer():
    assert "-2.4" not in filter_nums(INPUT)


if __name__ == "__main__":
    # print(filter_nums(INPUT))
    print(filter_nums(INPUT))