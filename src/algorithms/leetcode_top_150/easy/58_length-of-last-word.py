"""
https://leetcode.com/problems/length-of-last-word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_start = 0
        word_end = 0
        for i in range(1, len(s)):
            if s[i] != " ":
                word_end = i
                if s[i - 1] == " ":
                    word_start = i

        return word_end - word_start + 1
