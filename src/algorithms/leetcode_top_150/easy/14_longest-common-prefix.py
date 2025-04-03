"""
https://leetcode.com/problems/longest-common-prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Time Complexity: O(s) where S is the sum of characters in all the words
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            if len(prefix) == 0:
                break

            word = strs[i]
            word_length = len(word)
            if len(prefix) > word_length:
                prefix = prefix[0:word_length]

            for j in range(len(prefix)):
                if prefix[j] != word[j]:
                    prefix = prefix[0:j]
                    break

        return prefix
