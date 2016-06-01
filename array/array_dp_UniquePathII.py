# coding=utf-8
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0 for i in xrange(n)] for j in xrange(m)]
        # i对应m
        for i in xrange(m):
            if obstacleGrid[i][0] == 0:
                result[i][0] = 1
            else:
                result[i][0] = 0
                break
        # j对应n
        for j in xrange(n):
            if obstacleGrid[0][j] == 0:
                result[0][j] = 1
            else:
                result[0][j] = 0
                break
        # !!从1开始循环
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                else:
                    result[i][j] = result[i - 1][j] + result[i][j - 1]
        # 不要写成i-1, j-1
        return result[m - 1][n - 1]
