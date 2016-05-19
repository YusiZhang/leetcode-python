"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp_sum = [[0 for i in xrange(n)] for j in xrange(m)]
        dp_sum[0][0] = grid[0][0]

        # must start with 1!!!!!!!
        for i in xrange(1, m):
            dp_sum[i][0] = dp_sum[i-1][0] + grid[i][0]
        for j in xrange(1, n):
            dp_sum[0][j] = dp_sum[0][j-1] + grid[0][j]

        # must start with 1!!!!!!!
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp_sum[i][j] = min(dp_sum[i-1][j], dp_sum[i][j-1]) + grid[i][j]

        return dp_sum[m-1][n-1]