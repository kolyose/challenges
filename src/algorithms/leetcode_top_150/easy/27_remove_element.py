"""
https://leetcode.com/problems/remove-element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums. Return k.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, i = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[
                    i
                ]  # it's faster to re-assign an array item than to delete it
                k += 1

            i += 1

        return k
