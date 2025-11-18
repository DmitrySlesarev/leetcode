import re

UIN = """-2.4 -5.82 -2.73 10 24.3 180 -3.14"""

REF = """-5.82 -2.73 -3.14"""

patt = re.compile(r"-\d+.\d{2}")


def check_digits(text: str) -> str:
    res = []
    for line in text.splitlines():
        if m := patt.findall(line):
            res += m
    return " ".join(res)


def test_out():
    assert check_digits(UIN).strip() == REF.strip()


if __name__ == "__main__":
    print(check_digits(UIN))
