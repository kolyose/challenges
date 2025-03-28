"""
https://leetcode.com/problems/rotate-array/description/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
