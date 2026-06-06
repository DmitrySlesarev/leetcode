class Solution:
    @staticmethod
    def longestSubarray(nums: list[int]) -> int:
        """ Note: with DeepSeek's assistance """
        if not nums:
            return 0

        if sum(nums) == len(nums):
            return len(nums) - 1

        if sum(nums) == 0:
            return 0

        max_len = 0
        left = 0
        zeros_count = False

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1

            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            curr_len = right - left + 1
            max_len = max(max_len, curr_len)

        return max_len - 1


class TestSolution:
    def test_maxlen_eq_three(self):
        nums = [1, 1, 0, 1]
        expected = 3

        got = Solution().longestSubarray(nums)

        assert got == expected

    def test_maxlen_eq_five(self):
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        expected = 5

        got = Solution().longestSubarray(nums)

        assert got == expected

    def test_maxlen_eq_two(self):
        nums = [1, 1, 1]
        expected = 2

        got = Solution().longestSubarray(nums)

        assert got == expected
