class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #You cannot buy twice at one day, not sell twice at one day
        #http://bangbingsyb.blogspot.com/2014/11/leetcode-best-time-to-buy-and-sell.html
        max_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]
        return max_profit