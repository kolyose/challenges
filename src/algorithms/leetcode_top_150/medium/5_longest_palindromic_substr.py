"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Time Complexity: O(n*n)
Space Complexity: O(n)
"""


class Solution:
    def lookup_palindrome(self, s: str, i: int, j: int):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i + 1 : j]

    def get_longest_string(self, s1: str, s2: str) -> str:
        return s1 if len(s1) > len(s2) else s2

    def longest_palindrome(self, s: str) -> str:
        palindrome: str = ""
        for i in range(len(s)):
            p = self.lookup_palindrome(s, i, i)
            palindrome = self.get_longest_string(p, palindrome)

            p = self.lookup_palindrome(s, i, i + 1)
            palindrome = self.get_longest_string(p, palindrome)

        return palindrome
