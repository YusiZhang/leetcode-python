class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
        	return 0
        # this is the unlimited buy and sell cases(stockII), since k is larger than the half of amount prices
        if k >= len(prices) / 2:
        	profit = 0
        	for i in range(1, len(prices)):
        		if prices[i] > prices[i-1]:
        			profit += prices[i] - prices[i-1]
        	return profit

        n = len(prices)
        # state
        # mustSell[i][j] 表示前i天，至多进行j次交易，第i天必须sell的最大获益
        mustsell  = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # globalbest[i][j] 表示前i天，至多进行j次交易，第i天可以不sell的最大获益
        globalbest = [[0 for _ in range(n+1)] for _ in range(n+1)]

        # init
        mustsell[0][0] = globalbest[0][0] = 0

        # func
        for i in range(1, n):
        	diff = prices[i] - prices[i-1]
        	for j in range(1, k+1):
        		mustsell[i][j]   = max(globalbest[i-1][j-1] + diff, mustsell[i-1][j] + diff)
        		globalbest[i][j] = max(globalbest[i-1][j], mustsell[i][j])

        return globalbest[n-1][k]