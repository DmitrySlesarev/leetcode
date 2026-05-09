"""" Python practical sheet """

import re

PATTERN = re.compile(r".*(cat+).*\1")

UIN = """catcat
cat and cat
catac
cat
ccaatt
"""

REF = """
catcat
cat and cat
"""


def catch_cat(uin: str) -> str:
    """
    Gets lines where 'cat' is present at least 2 times.
    Args:
        uin(str): Text that may contain 'cat' word
    Returns:
        Text that contain 'cat' at least twice
    Examples:
        >>> catch_cat('cat and cat')
        'cat and cat'
        >>> catch_cat('just a simple line')
        ''
        >>> catch_cat('cat\\ncat and cat')
        'cat and cat'
    """
    if not isinstance(uin, str):
        raise TypeError("Should be of str type!")
    res = []
    for line in uin.splitlines():
        # Count occurrences of 'cat' as a whole word
        if line.count('cat') >= 2:
            res.append(line)
    return "\n".join(res)


# Use this pattern to match exactly "cat" twice
PATTERN = re.compile(r".*(cat).*\1")
# Or better yet, to match "cat" appearing at least twice:
PATTERN = re.compile(r"(.*cat.*){2,}")