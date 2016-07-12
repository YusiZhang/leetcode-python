class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        q = collections.deque()
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        diff = [(-1,0,1,0),(0,1,0,-1)]
        while q:
            pop = q.popleft()
            for i in xrange(len(diff[0])):
                newR = pop[0] + diff[0][i]
                newC = pop[1] + diff[1][i]
                if newR < 0 or newR >= len(rooms) or newC < 0 or newC >= len(rooms[0]) or rooms[newR][newC] != 2147483647:
                    continue
                rooms[newR][newC] = rooms[pop[0]][pop[1]] + 1
                q.append((newR,newC))