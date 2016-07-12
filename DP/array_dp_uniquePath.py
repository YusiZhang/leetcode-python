"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j] 表示从0，0到i,j有多少种走法，由于到i,j只能通过i-1,j 或者 i,j-1来实现
        # 所以
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        list = [[]]
        if m == 1 and n == 1:
            list = [[1]]
        else:
            list = [[0 for i in range(n)] for i in range(m)]
            for i in range(n):
                list[0][i] = 1
            for j in range(m):
                list[j][0] = 1
            for i in range(1, m):
                for i in range(1, n):
                    list[i][j] = list[i-1][j] + list[i][j-1]

        return list[m-1][n-1]