class Solution:
    def compress(self, chars: list[str]) -> int:
        if not chars:
            return 0

        if len(chars) == 1:
            return 1

        write_pos = 0
        read_pos = 0

        while read_pos < len(chars):
            curr_char = chars[read_pos]
            count = 0

            while read_pos < len(chars) and chars[read_pos] == curr_char:
                read_pos += 1
                count += 1

            chars[write_pos] = curr_char
            write_pos += 1

            if count > 1:
                for digit in str(count):
                    chars[write_pos] = digit
                    write_pos += 1

        return write_pos

class TestSolution:
    def test_compress_chars_eq_six(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = 6  # "a2b2c3"

        got = Solution().compress(chars)

        assert expected == got

    def test_compress_single_elem(self):
        chars = ["a"]
        expected = 1

        got = Solution().compress(chars)

        assert expected == got
