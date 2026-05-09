import re

def replace_rep_letters(text: str) -> str:
    """
    Func changes repetitive letters for single character
    Args:
        text (str) - Text that may contain repetitive letters
    Returns:
        (str) - Text that does not contain repetitive letters
    Examples:
        >>> replace_rep_letters("hello world")
        'helo world'
        >>> replace_rep_letters("AAAaaa")
        'Aa'
    """
    # Pattern to match consecutive repeated characters (case-sensitive)
    PATTERN = re.compile(r'(.)\1+', re.IGNORECASE)

    ret = []
    for line in text.splitlines():
        upd = []
        for word in line.strip().split():
            # Replace consecutive repeated characters with single character
            new_word = PATTERN.sub(r'\1', word)
            upd.append(new_word)
        ret.append(" ".join(upd))
    return "\n".join(ret)


# Test the function
if __name__ == "__main__":
    print(repr(replace_rep_letters("hello world")))  # 'helo world'
    print(repr(replace_rep_letters("AAAaaa")))  # 'Aa'