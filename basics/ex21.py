import re

PATTERN = re.compile(r"(?=.*\d+)(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[@$!%*#?&])[a-zA-Z@$!%*#?&]{6,}")

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


REF ="""enroi#$rkdeR#$
lOngPa$$W"""



def verify_psw(text: str) -> str:
    """
    Check passwords to comply security policy.
    Args:
        text (str): Text that may content valid passwords.
    Returns:
        Text that contains valid passwords, each from the new line.
    """
    res = []
    for line in text.splitlines():
        if psw := PATTERN.findall(line):
            res += psw
    return "\n".join(res)


def test_passwords():
    assert verify_psw(TEST_BATCH).strip() == REF.strip()


if __name__ == "__main__":
    print(verify_psw(TEST_BATCH))
