class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 1
        m = len(dungeon)
        n = len(dungeon[0])
        minInitHealth = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if i == m-1 and j == n-1: #右下角
                    minInitHealth[i][j] = max(1, 1-dungeon[i][j])
                elif i == m-1: #最后一行 取决于其右侧格子的值
                    minInitHealth[i][j] = max(1, minInitHealth[i][j+1] - dungeon[i][j])
                elif j == n-1: #最后一列 取决于其上方格子的值
                    minInitHealth[i][j] = max(1, minInitHealth[i+1][j] - dungeon[i][j])
                else:
                    minInitHealth[i][j] = max(1, min(minInitHealth[i+1][j], minInitHealth[i][j+1]) - dungeon[i][j])
        return minInitHealth[0][0]

