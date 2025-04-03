"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Time Complexity: O(n*m) where m is the length of needle
Space Complexity: O(m)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        i = 0
        while i < len(haystack):
            if haystack[i : i + len(needle)] == needle:
                return i

            i += 1

        return -1
