class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(len(nums)):
            i_val = nums[i]
            for j in range(i + 1, len(nums)):
                j_val = nums[j]
                if j_val > i_val:
                    for k in range(j + 1, len(nums)):
                        k_val = nums[k]
                        if k_val > j_val:
                            return True

        return False

    def increasingTriplet2(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                 return True

        return False

def test_increasing_raw_ret_true():
    nums = [1, 2, 3, 4, 5]
    expected = True

    got = Solution().increasingTriplet2(nums)

    assert expected == got


def test_random_raw_ret_false():
    nums = [5, 4, 3, 2, 1]
    expected = False

    got = Solution().increasingTriplet2(nums)

    assert expected == got


def test_increasing_raw2_ret_true():
    nums = [1, 2, 2147483647]
    expected = True

    got = Solution().increasingTriplet2(nums)

    assert expected == got


if __name__ == "__main__":
    ...
