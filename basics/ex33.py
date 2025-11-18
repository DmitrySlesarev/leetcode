import re
from string import ascii_letters, digits

PATT = re.compile(r"\b\w{2,}")

TEST_BATCH = """this is a text
"this' !is. ?n1ce,"""

REF = """htis si a etxt
"htis' !si. ?1nce,"""


def change_order(text: str) -> str:
    """Change order of two first letters in words containing >= 2 letters.
    Args:
        text(str): Text that can contain words of two or more letters.
    Returns:
        Text with changed words of 2 and more letters.
    """
    res = []
    for line in text.splitlines():
        upd_line = []
        for word in line.split():
            if m := PATT.search(word):
                m_part = m.group(0)
                upd = m_part[1] + m_part[0] + m_part[2:]
                upd_word = PATT.sub(upd, word)
                upd_line.append(upd_word)
            else:
                upd_line.append(word)
        res.append(" ".join(upd_line))

    return "\n".join(res)


def test_res():
    assert change_order(TEST_BATCH).strip() == REF.strip()


if __name__ == "__main__":
    print(change_order(TEST_BATCH))
