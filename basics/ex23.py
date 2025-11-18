import re

PATTERN = re.compile(r'.*z\w{3}z.*')

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
        text(str): Which may contain relevant words.
    Returns:
        Text that contains relevant words.
    """
    ret = []
    for line in text.splitlines():
        if m := PATTERN.findall(line):
            ret += m
    return "\n".join(ret)


def test_ret():
    assert REF.strip() == find_word(TEST_BATCH).strip()


if __name__ == "__main__":
    print(find_word(TEST_BATCH))
