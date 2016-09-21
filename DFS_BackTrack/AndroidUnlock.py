class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def dfs(visited, skip, cur, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            visited[cur] = True
            res = 0
            for i in range(1,10):
                if not visited[i] and (skip[cur][i] == 0 or visited[skip[cur][i]]):
                    res += dfs(visited, skip, i, remain - 1)

            visited[cur] = False
            return res

        skip = [[0 for _ in range(10)] for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5

        visited = [False for _ in range(10)]
        res = 0
        for i in range(m, n+1):
            res += dfs(visited, skip, 1, i-1) * 4 # start from 1; 1,3,7,9 are symmetric
            res += dfs(visited, skip, 2, i-1) * 4
            res += dfs(visited, skip, 5, i-1)

        return res