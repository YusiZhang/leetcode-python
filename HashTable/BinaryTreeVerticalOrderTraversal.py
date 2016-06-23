# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return None
        result = []

        m = {}
        q = deque()
        cols= deque()

        q.append(root)
        cols.append(0)

        minCol = 0
        maxCol = 0
        while len(q) != 0:
        	node = q.popleft()
        	col = cols.popleft()
        	if col not in m:
        		m[col] = []
        	m[col].append(node.val)
        	# why this is not working?
        	# m[col] = m.get(col, []).append(node.val)

        	if node.left:
        		q.append(node.left)
        		cols.add(col - 1)
        		if col <= minCol:
        			minCol = col - 1

        	if node.right:
        		q.append(node.right)
        		cols.append(col + 1)
        		if col >= maxCol:
        			maxCol = col + 1

        for i in range(minCol, maxCol+1):
        	result.append(m[i])

        return result

