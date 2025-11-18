import re

PATTERN = re.compile(r'^.*z\w{3}z.*$', re.MULTILINE)

TEST_BATCH = """
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
"""

REF = """
zabcz
zzxzz
"""

def find_word(text: str) -> str:
    """
    Find words where there are exactly 3 symbols between 'z' letters.
    Args:
        text (str): Text which may contain relevant words.
    Returns:
        str: Text containing only the relevant words (one per line).
    """
    matches = PATTERN.findall(text)
    return "\n".join(matches)

def test_ret():
    assert REF.strip() == find_word(TEST_BATCH).strip()

if __name__ == "__main__":
    print(find_word(TEST_BATCH))