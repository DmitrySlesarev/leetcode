import re
from typing import Optional

PATTERN = re.compile(r"-\d+\.\d{2}")

INPUT = '-2.4 -5.82 -2.73 10 24.3 180 -3.14'

REF = "-5.82 -2.73 -3.14"

def get_specific_numbers(line: str) -> Optional[int]:
    """Get fractional numbers with 2 digits in its fractional part
    Args:
        line(str): Text that may contain numbers with 2 digits in fractional part
    Returns:
        Numbers with 2 digits in fractional part
    Examples:
        >>> get_specific_numbers('-2.4 -5.82 -2.73 10 24.3 180 -3.14')
        '-5.82 -2.73 -3.14'
    """
    if line.isalpha():
        raise TypeError("Please, check values in INPUT")
    numbers = line.strip().split()
    res = []
    for num in numbers:
        if PATTERN.search(num):
            res.append(num)
    return " ".join(res)


def test_output():
    assert get_specific_numbers(INPUT) == REF


if __name__ == "__main__":
    # for i in get_specific_numbers(INPUT):
    #     print(i, end=" ")
    print(get_specific_numbers(INPUT))
