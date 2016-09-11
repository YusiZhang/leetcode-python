class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        row = 0
        col = [None] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    continue
                if j == 0 or grid[i][j-1] == 'W':
                    row = self.killedEnemiesRow(grid, i, j)
                if i == 0 or grid[i-1][j] == 'W':
                    col[j] = self.killedEnemiesCol(grid, i, j)
                if grid[i][j] == '0':
                    res = max(res, row + col[j])

        return res
    # calculate killed enemies for row i from column j
    def killedEnemiesRow(self, grid, i, j):
        num = 0
        while j < len(grid[0]) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                num += 1
            j += 1
        return num

    def killedEnemiesCol(self, grid, i, j):
        num = 0
        while i < len(grid) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                num += 1
            i += 1
        return num

if __name__ == '__main__':
    matrix = [
        ['0', 'E', '0','0'],
        ['E', '0', 'W', 'E'],
        ['0', 'E', '0', '0']
    ]
    solution = Solution()
    print solution.maxKilledEnemies(matrix)

"""
walk over the matrix in row-wise fashion.
So I'm always in at most one horizontal streak,
and I finish it before I get to the next.
Hence I need to remember only the hits in one horizontal streak.
But since I'm moving horizontally,
that's not true for the vertical streaks,
and thus I remember the hits of all vertical streaks
(one per column) I'm currently involved with.
"""