class Solution:
    def moveZeros(self, nums: list[int]) -> None:
        if not nums:
            return

        non_zeros = list(filter(lambda x: x != 0, nums))
        zeros = len(nums) - len(non_zeros)

        nums.clear()
        nums.extend(non_zeros)
        nums.extend([0] * zeros)

    def moveZeros2(self, nums: list[int]) -> None:
        if not nums:
            return

        if 0 not in nums:
            return

        i = 0
        while nums.count(0):
            i += 1
            nums.remove(0)

        nums.extend([0] * i)


def test_ex_is_sorted():
    nums = [0, 1, 0, 3, 12]
    expected = [1,3,12,0,0]

    Solution().moveZeros(nums)
    got = nums

    assert expected == got

def test_ex_is_sorted2():
    nums = [0, 1, 0, 3, 12]
    expected = [1,3,12,0,0]

    Solution().moveZeros2(nums)
    got = nums

    assert expected == got