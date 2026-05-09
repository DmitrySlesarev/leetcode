import re


WORD_PATTERN = re.compile(r"(cat)\1+")


USER_INPUT = """catcat
cat and cat
catac
cat
ccaatt"""


def get_rep_strings(text: str) -> str:
    """
    Display strings with repetitive words
    Args:
        text: may content lines with repetitive words
    Returns:
        lines with repetitive word
    """
    res = []
    for line in text.strip().splitlines():
        if match := WORD_PATTERN.search(line):
            line = match.group()
            res.append(line)

    return "\n".join(res)


if __name__ == "__main__":
    print(get_rep_strings(USER_INPUT))
