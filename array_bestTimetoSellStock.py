__author__ = 'yusizhang'
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #i: day to buy
        #j: day to sell
        # max_profit = 0
        # for i in range(0, len(prices) - 1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > 0:
        #             max_profit = max(prices[j]-prices[i], max_profit)

        # return max_profit

        currentMinPrice = prices[0] if len(prices) > 0 else 0
        maxProfit = 0
        for price in prices:
            currentMinPrice = min(currentMinPrice, price)
            maxProfit = max(maxProfit, price - currentMinPrice)
        return maxProfit
