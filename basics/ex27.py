import re

PATTERN = re.compile(r'\b(\w+)\1\b')

TEXT = """
blabla is a tandem repetition
123123 is good too
go go
aaa
"""

REF = """
blabla is a tandem repetition
123123 is good too
"""


def find_tandem_rep(text: str) -> str:
    """Find tandem repetition in text
    Args:
        text(str): Text that may content words with tandem repetition.
    Returns:
        Text that contents words with tandem repetition.
    """
    matches = []
    for line in text.strip().splitlines():
        if PATTERN.search(line):
            matches.append(line)
    return "\n".join(matches)


if __name__ == "__main__":
    print(find_tandem_rep(TEXT))
