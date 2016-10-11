class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        islands = Union()
        for p in map(tuple, positions): #conver [1,2] to (1,2)
            islands.add(p)
            for dp in (0,1), (0,-1), (1,0), (-1,0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.id:
                    islands.unite(p, q)
            ans += [islands.count]
        return ans


class Union(object):
    def __init__(self):
        self.id    = {}
        self.sz    = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, i):
        while i != self.id[i]:
            # path compression, change current's parent to its parent's parent
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1

    def find(self, p, q):
        return self.root(p) == self.root(q)

if __name__ == '__main__':
    positions = [[0,0], [0,1], [1,2], [2,1]]
    for p in map(tuple, positions):
        print p