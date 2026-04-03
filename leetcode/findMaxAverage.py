class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if not nums:
            raise ValueError(f"{nums=} cannot be empty")

        if k > len(nums):
            raise ValueError(f"{k=} should be greater than or equal to {len(nums)=}")

        if k <= 0:
            raise ValueError(f"{k=} should be greater than 0")

        if k == len(nums):
            return sum(nums) / k

        max_avg = float('-inf')
        mods = len(nums) - k + 1

        for i in range(mods):
            sub = nums[i:i + k]
            avg = sum(sub) / k
            if avg > max_avg:
                max_avg = avg

        return max_avg

    def findMaxAverage2(self, nums: list[int], k: int) -> float:
        if not nums:
            raise ValueError(f"{nums=} cannot be empty")

        if k > len(nums):
            raise ValueError(f"{k=} should be greater than or equal to {len(nums)=}")

        if k <= 0:
            raise ValueError(f"{k=} should be greater than 0")

        if k == len(nums):
            return sum(nums) / k

        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum / k


class TestSolution:
    def test_max_avg_from_four_elem(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75

        got = Solution().findMaxAverage(nums=nums, k=k)

        assert expected == got

    def test_max_avg_for_single_elem(self):
        nums = [5]
        k = 1
        expected = 5.0

        got = Solution().findMaxAverage(nums=nums, k=k)

        assert expected == got
