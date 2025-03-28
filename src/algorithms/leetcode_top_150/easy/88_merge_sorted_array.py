"""
https://leetcode.com/problems/merge-sorted-array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums2):
            insertion_index = len(nums1) - n + right
            while left < insertion_index:
                if nums2[right] < nums1[left]:
                    insertion_index = left
                    break
                left += 1

            nums1.insert(insertion_index, nums2[right])
            nums1.pop()
            right += 1

        return nums1
