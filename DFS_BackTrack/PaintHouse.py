import sys
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
        print "current depth {0}".format(depth)
        if depth == len(costs)-1:
            self.result = min(self.result, cursum)
            return
        print (set([0,1,2]) - set([color]))
        for c in (set([0,1,2]) - set([color])):
            self.dfs(depth+1, c, cursum+costs[depth+1][c], costs)

if __name__ == '__main__':
    input = [[7,6,2],[1,2,3]]
    solution = Solution()
    print solution.minCost(input)