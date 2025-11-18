import re

NUM_PATTERN = re.compile(r"-\d+\.\d{2}")

INPUT = "-2.4 -5.82 -2.73 10 24.3 180 -3.14"
REF = """-5.82 -2.73 -3.14"""


def get_nums(text: str) -> str:
    """
    Get negative real numbers with 2 digits after point
    Args:
        Text that may contain required nums
    Returns:
        Text that contain required nums
    """
    res = []
    for line in text.splitlines():
        for word in line.split():
            if num := NUM_PATTERN.search(word):
                res.append(num.group())
    return " ".join(res)


def test_out():
    assert get_nums(INPUT).strip() == REF.strip()


if __name__ == "__main__":
    print(get_nums(INPUT))
