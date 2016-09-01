class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            # dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
            dp.append(min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1)
        return dp[n]

if __name__ == '__main__':
    dp = [1,2,3]
    dp2 = [4,5]
    var = 5
    dp += var,
    dp.append(dp2)
    print dp