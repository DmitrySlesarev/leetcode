import re
from string import ascii_lowercase

WORD_PATTERN = re.compile(rf"([{ascii_lowercase}])\1+", flags=re.IGNORECASE)

USER_INPUT = """attraction
buzzzz
"""

REF_OUTPUT = """atraction
buz
"""


def find_rep_letters(text: str) -> str:
    """
    Deletes consecutive duplicate letters in words while preserving case.

    Args:
        text: Input text containing words with possible consecutive duplicates.

    Returns:
        Text with processed words where consecutive duplicates are replaced by a single letter.
    """

    def replace_rep_letters(match: re.Match) -> str:
        """Returns the first character of a match of consecutive duplicate letters."""
        return match.group(1)  # Group 1 is the first captured letter

    # Process each line separately and join with newlines
    return "\n".join(
        WORD_PATTERN.sub(replace_rep_letters, line)
        for line in text.strip().splitlines()
    )


if __name__ == "__main__":
    result = find_rep_letters(USER_INPUT)
    print(result)
    assert result == REF_OUTPUT, f"Expected:\n{REF_OUTPUT}\nGot:\n{result}"