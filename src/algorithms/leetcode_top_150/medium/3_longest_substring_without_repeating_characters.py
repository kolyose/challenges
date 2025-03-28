"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string s, find the length of the longest substring without duplicate characters.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def calculate_max_length(self, unique_chars: dict, max_length: int):
        length: int = len(unique_chars.values())
        return max(length, max_length)

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length: int = 0
        unique_chars: dict = {}
        index = 0

        while index < len(s):
            char = s[index]
            if unique_chars.get(char) is None:
                unique_chars[char] = index
                max_length = self.calculate_max_length(unique_chars, max_length)
            else:
                duplicate_index = unique_chars[char]
                unique_chars = {
                    key: value
                    for key, value in unique_chars.items()
                    if value > duplicate_index
                }
                unique_chars[char] = index

            index = index + 1

        return max_length
