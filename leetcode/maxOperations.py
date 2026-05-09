from typing import List


class Solution:
    @staticmethod
    def maxOperations(nums: List[int], k: int) -> int:

        if not nums or not k:
            return 0

        if not isinstance(nums, (list, tuple)):
            raise TypeError(f"{nums=} should be list or tuple")

        if not isinstance(k, int):
            raise TypeError(f"{k=} should be int")

        if k < 0:
            raise ValueError(f"{k=} should not be less than 0")

        # Heavy check, leetcode ensures incoming values
        # for elem in nums:
        #     if not isinstance(elem, int):
        #         raise TypeError(f"{k=} should be int")

        max_ops = 0

        used = []
        for k1, v1 in enumerate(nums):
            for k2, v2 in enumerate(nums[1:], start=1):
                if k2 in used or k1 in used or k1 == k2:
                    continue
                if v1 + v2 == k:
                    max_ops += 1
                    used.extend([k1, k2])

        return max_ops

    @staticmethod
    def maxOperations2(nums: List[int], k: int) -> int:

        if not nums or not k:
            return 0

        nums = sorted(nums)
        left, right = 0, len(nums)-1
        max_ops = 0

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == k:
                max_ops += 1
                left += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:  # curr_sum > k
                right -= 1

        return max_ops


class TestSolution:
    @staticmethod
    def test_arr_with_2_ops():
        nums = [1, 2, 3, 4]
        k = 5
        expected = 2

        got = Solution().maxOperations2(nums, k)

        assert got == expected, "Should be 2"

    @staticmethod
    def test_arr_with_1_ops():
        nums = [3, 1, 3, 4, 3]
        k = 6
        expected = 1

        got = Solution().maxOperations2(nums, k)

        assert got == expected, "Should be 1"
