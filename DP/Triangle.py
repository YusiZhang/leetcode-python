"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return -1
        
        self.n = len(triangle)
        self.triangle = triangle
        self.minSum = [[sys.maxint for _ in range(self.n)] for _ in range(self.n)]
        
        return self.search(0,0)
        
    def search(self, x, y):
        if x >= self.n:
            return 0
        if self.minSum[x][y] != sys.maxint:
            return self.minSum[x][y]
        self.minSum[x][y] = min(self.search(x+1, y), self.search(x+1, y+1)) + self.triangle[x][y]
        
        return self.minSum[x][y]
        