"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Time Complexity: O(n) - where n is the max list length among l1 & l2
Space Complexity: O(n) - where n is the max list length among l1 & l2
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        v1, n1 = (0, None) if l1 is None else (l1.val, l1.next)
        v2, n2 = (0, None) if l2 is None else (l2.val, l2.next)

        sum = v1 + v2
        overflow = sum // 10

        if overflow:
            if n1 is not None:
                n1.val += overflow
            elif n2 is not None:
                n2.val += overflow
            else:
                n2 = ListNode(overflow)

        current_node = ListNode(sum % 10)
        current_node.next = self.addTwoNumbers(n1, n2)
        return current_node
