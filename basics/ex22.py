import re

PATTERN = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%&])[0-9a-zA-Z@#$%&]{6,}$")

TEST_BATCH = """
123456789aB
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


def verify_psw(text: str) -> str:
    """
    Gets valid passwords from text
    Args:
        text(str): Text that may contain valid passwords.
    Returns:
        Text that contains valid passwords, each from new line, or empty string.
    """
    ret = []
    for line in text.splitlines():
        if m := PATTERN.findall(line):
            ret += m
    return "\n".join(ret)


if __name__ == "__main__":
    print(verify_psw(TEST_BATCH))
