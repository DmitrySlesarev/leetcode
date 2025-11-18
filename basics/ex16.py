import re

VALID_PSW = re.compile(r"^(?=.*\d.*)(?=.*[a-zA-Z])(?=.*[-_+/!$&]).{6,}$")

BATCH = """123456789aB
120980@aA
absghk4D
abc1&23FF
123ABCac
rtG3FG!Tr^e
aA1!*!1Aa
oF^a1D@y5e6
enroi#$rkdeR#$092u
aA1@
aa1@#bbcc
пароль
password
qwerty
lOngPa$$W0Rd
"""


REF = """120980@aA
abc1&23FF
rtG3FG!Tr^e
aA1!*!1Aa
oF^a1D@y5e6
enroi#$rkdeR#$092u
lOngPa$$W0Rd
"""


def pick_psw(text: str) -> str:
    """Extracts and returns valid passwords from the given text

    Scans the input text for strings that meet password validity requirements
    (such as minimum length, character variety, etc.) and returns the first
    valid password found.

    Args:
        text: Input string potentially containing password candidates.
            May contain multiple words or patterns to be evaluated.

    Returns:
        All the valid passwords in the input text. If no valid password is found,
        returns an empty string.

    Raises:
        ValueError: If the input text is empty or contains only whitespaces.

    Example:
        >>> pick_psw("Secure123!")
        'Secure123!'
        >>> pick_psw("all invalid")
        ''
    """
    if text.strip() == "":
        raise ValueError("Input is empty string/consists of whitespaces only!")
    res = [line.strip() for line in text.splitlines() if VALID_PSW.search(line)]
    return "\n".join(res)


def test_out():
    assert pick_psw(BATCH) == REF.strip()


if __name__ == "__main__":
    print(pick_psw(BATCH))
