""" TBU """
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not isinstance(flowerbed, (List, list)):
            raise TypeError(f"{flowerbed=} should be list!")

        if not flowerbed:
            raise ValueError(f"{flowerbed=} should not be empty!")

        values_check = [isinstance(val, int) and (val == 1 or val == 0) for val in flowerbed]
        if not all(values_check):
            raise TypeError(f"All values of {flowerbed=} should be int!")

        if not isinstance(n, int):
            raise TypeError(f"{n=} should be int!")

        if n < 0:
            raise ValueError(f"{n=} should be greater than zero!")
        if n == 0:
            return True

        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i+1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n


def test_func_input_eq_true():
    _input = [1, 0, 0, 0, 1]
    expected = True

    got = Solution().canPlaceFlowers(_input, 1)

    assert expected == got


def test_func_input_eq_false():
    _input = [1, 0, 0, 0, 1]
    expected = False

    got = Solution().canPlaceFlowers(_input, 2)

    assert expected == got


if __name__ == "__main__":
    ...
