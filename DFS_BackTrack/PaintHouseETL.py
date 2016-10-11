class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
            
        self.result = sys.maxint
        self.dfs(0, 0, costs[0][0], costs)
        self.dfs(0, 1, costs[0][1], costs)
        self.dfs(0, 2, costs[0][2], costs)
        return self.result
        
    def dfs(self, depth, color, cursum, costs):
        if depth == len(costs)-1:
            self.result = min(self.result, cursum)
            return
        for c in (set([0,1,2]) - set([color])):
            self.dfs(depth+1, c, cursum+costs[depth+1][c], costs)

"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
"""