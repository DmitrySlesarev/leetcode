class Solution:
    @staticmethod
    def longestOnes(nums: list[int], k: int) -> int:
        if not (1 in nums):
            return 0

        if sum(nums) == len(nums):
            return len(nums)

        if k == 0:
            return sum(nums)

        max_seq = 0
        local_max_seq = 0

        def count_conseq_ones(local_nums, max_seq, local_max_seq, k):
            for i in range(len(local_nums)):
                if local_nums[i] == 1:
                    local_max_seq += 1
                    max_seq = max(local_max_seq, max_seq)
                elif local_nums[i] == 0:
                    if k:
                        local_max_seq += 1
                        k -= 1
                        try:
                            local_nums = local_nums[i + 1::]
                            local_max_seq = count_conseq_ones(local_nums, max_seq, local_max_seq, k)
                            max_seq = max(max_seq, local_max_seq)
                        except IndexError:
                            return max(max_seq, local_max_seq)
                    else:
                        local_max_seq = 0
                else:
                    raise ValueError("Only '1' or '0' are allowed")
            return max_seq

        return count_conseq_ones(nums, max_seq, local_max_seq, k)

    @staticmethod
    def longestOnes2(nums: list[int], k: int) -> int:
        '''With ChatGPT assistance'''
        max_len = 0
        left = 0
        zeros = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:

                if nums[left] == 0:
                    zeros -= 1

                left += 1

            window_size = right - left + 1

            max_len = max(max_len, window_size)

        return max_len


class TestSolution:
    def test_longest_eq_six(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        expected = 6

        got = Solution.longestOnes2(nums, k)

        assert got == expected
