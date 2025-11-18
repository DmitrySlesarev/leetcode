import re

PATT = re.compile(r"[a-zA-Z0-9-.]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}\b")

UIN = """prettyandsimple@example.com 
very.common@example.com 
other.email-with-dash@example.com
x@example.com 
example-indeed@strange-example.com
admin@mailserver1 
example@localhost 
example@s.solutions 
user@com
user@localserver
Abc.example.com 
john.doe@example..com
"""


def validate_email(text: str) -> str:
    """
    Verify emails
    Args:
        text: That may content valid emails
    Returns:
        (str): That contents valid emails or emp
    """
    res = [line.strip() for line in text.splitlines() if PATT.search(line.strip())]
    return "\n".join(res)


if __name__ == "__main__":
    print(validate_email(UIN))
