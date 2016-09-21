class Solution(object):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        """
        Do DFS from every cell
        Compare every 4 direction and skip cells that are out of boundary or smaller
        Get matrix max from every cell's max
        Use matrix[x][y] <= matrix[i][j] so we don't need a visited[m][n] array
        The key is to cache the distance because it's highly possible to revisit a cell
        """
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        res = 1
        for i in range(m):
            for j in range(n):
                length = self.dfs(matrix, i, j, m, n, cache)
                res = max(res, length)
        return res

    def dfs(self, matrix, i, j, m, n, cache):
        if cache[i][j] != 0:
            return cache[i][j]
        res = 1
        for d in self.dirs:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(matrix, x, y, m, n, cache)
            res = max(res, length)
        cache[i][j] = res
        return res

if __name__ == '__main__':
    nums = [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]
    solution = Solution()
    print solution.longestIncreasingPath(nums)



