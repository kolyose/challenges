"""
https://leetcode.com/problems/majority-element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int | None:
        lst = {}
        for el in nums:
            lst[el] = lst.get(el, 0) + 1
            if lst[el] > len(nums) / 2:
                return el

    """
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majEl = None

        for el in nums:
            if count == 0:
                majEl = el
                count += 1
            else:
                count += 1 if el == majEl else -1
        
        return majEl
    """
