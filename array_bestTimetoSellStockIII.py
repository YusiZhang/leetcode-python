# coding=utf-8
__author__ = 'yusizhang'


class Solution(object):
    """
    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. You may complete at most two transactions.
    Note:
    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # http://blog.unieagle.net/2012/12/05/leetcode%E9%A2%98%E7%9B%AE%EF%BC%9Abest-time-to-buy-and-sell-stock-iii%EF%BC%8C%E4%B8%80%E7%BB%B4%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/
        # http://bangbingsyb.blogspot.com/2014/11/leetcode-best-time-to-buy-and-sell.html
        n = len(prices)
        if n <= 1:
            return 0
        max_profit_left = [0] * n
        max_profit_right = [0] * n
        # 从左往右扫描找最小价格，是因为越前面的价格是买入价。
        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            max_profit_left[i] = max(max_profit_left[i - 1], prices[i] - minPrice)  # max profit [0...i]
        # 从右往左扫描找最大价格，是因为越后面的价格是卖出价。
        maxPrice = prices[-1]
        for i in range(n - 2, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            max_profit_right[i] = max(max_profit_right[i + 1], maxPrice - prices[i])  # max profit [i...n]

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_profit_left[i] + max_profit_right[i])
        return max_profit
