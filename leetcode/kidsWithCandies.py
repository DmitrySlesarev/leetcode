"""Solving LeetCode tasks"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if not isinstance(candies, (list, tuple)):
            raise TypeError("Variable 'Candies' should be 'list' or 'tuple'")
        if not candies:
            raise ValueError("Length of 'Candies' should be greater than zero")

        if not isinstance(extraCandies, int):
            raise TypeError("Variable 'extraCandies' should be 'int'")
        if not extraCandies:
            raise ValueError("Value 'extraCandies' should be greater than zero")

        res = [None] * len(candies)

        for ind, val in enumerate(candies):
            tmp = list(candies)
            val += extraCandies
            tmp[ind] = val
            res[ind] = True if max(tmp) == val else False

        return res

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """DeepSeek version"""
        max_candies = max(candies)

        # For each kid, check if current + extra >= maximum
        return [candy + extraCandies >= max_candies for candy in candies]
