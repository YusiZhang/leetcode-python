import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        print sorted(tickets)
        for a, b in sorted(tickets)[::-1]:
            # += b, allows to add b as a string, otherwise, it will add each char in the string b.
            targets[a] += b,
        print targets
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

if __name__ == '__main__':
    # solution = Solution()
    # print solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    # print solution.findItinerary([["JFK","ATL"],["JFK","SFO"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    # print solution.findItinerary([["JFK","ATL"],["JFK","SFO"],["SFO","ATL"],["ATL","SFO"],["ATL","JFK"]])

    print sorted([["JFK","ATL"],["JFK","SFO"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    print sorted([["JFK","ATL"],["JFK","SFO"],["SFO","ATL"],["ATL","SFO"],["ATL","JFK"]])