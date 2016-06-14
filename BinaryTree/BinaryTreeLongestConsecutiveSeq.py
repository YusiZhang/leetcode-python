# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
A top down approach is similar to an in-order traversal.
We use a variable length to store the current consecutive path length and pass it down the tree.
As we traverse, we compare the current node with its parent node to determine if it is consecutive.
If not, we reset the length.
"""
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, None, 0)

    def dfs(self, p, parent, length):
        if p is None:
            return length
        length = length + 1 if parent is not None and p.val == parent.val+1 else 1
        return max(length, max(self.dfs(p.left, p, length), self.dfs(p.right, p, length)))
