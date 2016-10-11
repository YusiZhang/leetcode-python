class Solution(object):
    def minCost(self, costs):
            """
            :type costs: List[List[int]]
            :rtype: int
            """
            if not costs:
                return 0
            # state
            # f[i][color] represents until i-th house, min cost of painting the color
            # init
            f = [[sys.maxint for _ in range(3)] for _ in range(len(costs)+1)]
            f[0][0] = 0
            f[0][1] = 0
            f[0][2] = 0
            # func
            n = len(costs)
            for i in range(1, len(costs)+1):
                f[i][0] = min(f[i-1][1], f[i-1][2]) + costs[i-1][0]
                f[i][1] = min(f[i-1][0], f[i-1][2]) + costs[i-1][1]
                f[i][2] = min(f[i-1][0], f[i-1][1]) + costs[i-1][2]
            
            # ans
            return min(f[n][0], f[n][1], f[n][2])