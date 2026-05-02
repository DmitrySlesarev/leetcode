class Solution:
    @staticmethod
    def maxArea(height: list[int]) -> int:
        if not isinstance(height, (list, tuple)):
            raise TypeError(f"{type(height)=} should be list or tuple")

        if len(height) < 2:
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class TestSolution:
    def test_many_bars_eq_49(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49

        got = Solution.maxArea(height)

        assert got == expected

    def test_one_bar_eq_one(self):
        height = [1, 1]
        expected = 1

        got = Solution.maxArea(height)

        assert got == expected

    def test_one_two_eq_one(self):
        heigth = [1, 2]
        expected = 1

        got = Solution.maxArea(heigth)

        assert got == expected
