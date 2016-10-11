# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)

        if self.prev and self.prev.val >= root.val:
            if not self.first:
                self.first = self.prev
            self.second = root

        self.prev = root

        self.inOrder(root.right)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)

    solution.recoverTree(root)

