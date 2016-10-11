# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic      = {node: nodeCopy}
        queue    = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy  = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
                    
                    