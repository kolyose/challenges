"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        i = 1
        while i < len(prices):
            if prices[i] < buy:
                buy = prices[i]
            elif i == len(prices) - 1 or prices[i + 1] < prices[i]:
                profit += prices[i] - buy
                buy = prices[i]

            i += 1

        return profit
