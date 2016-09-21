"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
"""

import collections
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        m = len(grid)
        n = len(grid[0])
        dist = [[0 for _ in xrange(n)] for _ in xrange(m)]
        totalB = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    totalB += 1

        ## do BFS from each building, and decrement all empty place for every building visit
        ## when grid[i][j] == -totalB, it means that grid[i][j] are already visited from all buildings
        ## and use dist to record distances from buildings
        def bfs(i, j, visitedBuildingCount):
            queue = collections.deque([(i, j, 0)])
            while queue:
                i, j, d = queue.popleft()
                for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == visitedBuildingCount:
                        dist[x][y] += d + 1
                        grid[x][y] -= 1
                        queue.append((x, y, d+1))
        visitedBuildingCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j, visitedBuildingCount)
                    visitedBuildingCount -= 1
        res = [dist[i][j] for i in range(m) for j in range(n) if grid[i][j] + totalB == 0]
        return min(res) if res else -1
