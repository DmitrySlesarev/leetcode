class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if not nums:
            return -1

        total = sum(nums)
        left_sum = 0

        for ind in range(len(nums)):
            if left_sum == total - left_sum - nums[ind]:
                return ind
            left_sum += nums[ind]

        return -1


class TestSolution:
    def test_pI_eq_3(self):
        nums = [1, 7, 3, 6, 5, 6]
        expected = 3

        got = Solution().pivotIndex(nums)

        assert got == expected

    def test_no_pI_in_arr(self):
        nums = [2, 1, -1]
        expected = -1

        got = Solution().pivotIndex(nums)

        assert got == expected
