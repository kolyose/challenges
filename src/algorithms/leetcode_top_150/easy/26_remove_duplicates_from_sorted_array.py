"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums. Return k.


Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, i = 0, 1
        while i < len(nums):
            if nums[i] == nums[k]:
                i += 1
            else:
                nums[k + 1] = nums[
                    i
                ]  # it's faster to re-assign an array item than to delete it
                k += 1

        return k + 1
