"""
https://leetcode.com/problems/is-subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        s_index, t_index = 0, 0
        while s_index < len(s):
            if t_index == len(t):
                return False

            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        return True
