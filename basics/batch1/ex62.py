import re

PATTERN = re.compile(r"[-a-z0-9.]+@[-a-z0-9]+\.[a-z]{2,3}\b")

INPUT = """prettyandsimple@example.com 
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


def validate_emails(text: str) -> list:
    """
    Validate correct email in text
    Args:
        text(str): Text that may contain correct emails
    Returns:
        (list): List of emails or empty list
    Examples:
        >>> validate_emails("very.common@example.com")
        ['very.common@example.com']
        >>> validate_emails("user@com")
        []
    """
    res = []
    for line in text.splitlines():
        if PATTERN.search(line):
            res.append(line.strip())
    return res


if __name__ == "__main__":
    print(validate_emails(INPUT))
