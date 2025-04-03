"""
https://leetcode.com/problems/valid-palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Time Complexity: O(n)
Space Complexity: O(1)
"""

import re


class Solution:
    def isAlphaNumeric(self, char) -> bool:
        return bool(re.match(r"[a-zA-Z0-9]", char))

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while j > i:
            if not self.isAlphaNumeric(s[i]):
                i += 1
            elif not self.isAlphaNumeric(s[j]):
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False

                i += 1
                j -= 1

        return True
