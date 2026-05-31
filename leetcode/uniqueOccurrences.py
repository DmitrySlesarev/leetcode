class Solution:
    @staticmethod
    def uniqueOccurrences(arr: list[int]) -> bool:
        """Given an array of integers arr, return true if
        the number of occurrences of each value in the array
        is unique or false otherwise.
        """

        if not arr:
            return False

        if not isinstance(arr, (list, tuple)):
            raise ValueError(f"{arr=} should be 'list' or 'tuple")

        unique_values = {}
        for var in arr:
            if var not in unique_values:
                unique_values[var] = 0
            unique_values[var] += 1

        return len(set(unique_values.values())) == len(unique_values.keys())


class TestSolution:
    def test_simple_ex_returns_true(self):
        arr = [1, 2, 2, 1, 1, 3]
        expected = True

        got = Solution.uniqueOccurrences(arr)

        assert got == expected

    def test_simple_ex_returns_false(self):
        arr = [1, 2]
        expected = False

        got = Solution.uniqueOccurrences(arr)

        assert got == expected

    def test_complex_ex_returns_true(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        expected = True

        got = Solution.uniqueOccurrences(arr)

        assert got == expected
