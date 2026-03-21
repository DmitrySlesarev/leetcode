class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        res = []
        for i in range(len(nums)):
            tmp = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                tmp *= nums[j]
            res.append(tmp)
        return res

    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for j in range(n - 1, -1, -1):
            result[j] *= suffix
            suffix *= nums[j]

        return result



def test_product_eq_desired_values():
    expected = [24, 12, 8, 6]

    got = Solution().productExceptSelf([1, 2, 3, 4])

    assert expected == got


def test_product_eq_desired_values2():
    expected = [24, 12, 8, 6]

    got = Solution().productExceptSelf2([1, 2, 3, 4])

    assert expected == got


if __name__ == "__main__":
    ...
