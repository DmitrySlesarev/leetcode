class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res1 = set(nums2) - set(nums1) if nums1 else set(nums2)
        res2 = set(nums1) - set(nums2) if nums2 else set(nums1)
        return [list(res2), list(res1)]

class TestSolution:
    def test_two_lists_with_diff_vals(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        expected = [[1, 3], [4, 6]]

        got = Solution().findDifference(nums1, nums2)

        assert got == expected

    def test_two_almost_identical_lists(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        expected = [[3], []]

        got = Solution().findDifference(nums1, nums2)

        assert got == expected
