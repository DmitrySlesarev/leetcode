import re

# Improved regex pattern:
# - More precise special character set (you can adjust [-_+/!$&] as needed)
# - Better readability with verbose flag and comments
VALID_PSW = re.compile(r"""
    ^                   # Start of string
    (?=.*\d)            # At least one digit
    (?=.*[a-z])         # At least one lowercase letter
    (?=.*[A-Z])         # At least one uppercase letter
    (?=.*[-_+/!$&])     # At least one special character
    .{6,}               # At least 6 characters long
    $                   # End of string
""", re.VERBOSE)

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
    """Extracts and returns valid passwords from the given text.

    Scans the input text line by line for strings that meet password validity requirements:
    - At least 6 characters long
    - Contains at least one digit, one lowercase, one uppercase letter, and one special character
    - Returns all valid passwords found, joined by newlines.

    Args:
        text: Input string potentially containing password candidates.
            May contain multiple lines to be evaluated.

    Returns:
        A string containing all valid passwords separated by newlines.
        Returns an empty string if no valid passwords are found.

    Raises:
        ValueError: If the input text is empty or contains only whitespace.

    Examples:
        >>> pick_psw("Secure123!")
        'Secure123!'
        >>> pick_psw("all invalid")
        ''
        >>> pick_psw("120980@aA\\nabc1&23FF")
        '120980@aA\\nabc1&23FF'
    """
    if not text.strip():
        raise ValueError("Input is empty or consists of whitespace only!")

    valid_passwords = [
        line.strip() for line in text.splitlines()
        if VALID_PSW.fullmatch(line.strip())
    ]
    return "\n".join(valid_passwords)


def test_pick_psw():
    """Test function for pick_psw."""
    # Test with the provided batch
    assert pick_psw(BATCH) == REF.strip()

    # Test with empty input
    try:
        pick_psw("")
        assert False, "Expected ValueError for empty input"
    except ValueError:
        pass

    # Test with whitespace only
    try:
        pick_psw("   \n  \t")
        assert False, "Expected ValueError for whitespace only"
    except ValueError:
        pass

    # Test with single valid password
    assert pick_psw("aA1!*!1Aa") == "aA1!*!1Aa"

    # Test with no valid passwords
    assert pick_psw("password\n123456\nqwerty") == ""

    print("All tests passed!")


if __name__ == "__main__":
    test_pick_psw()