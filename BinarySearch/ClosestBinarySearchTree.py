"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:

Consider implement these two helper functions:
getPredecessor(N), which returns the next smaller node to N.
getSuccessor(N), which returns the next larger node to N.
Try to assume that each node has a parent pointer, it makes the problem much easier.
Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
You would need two stacks to track the path in finding predecessor and successor node separately.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = []
        s1 = []
        s2 = []

        self.inorder(root, target, False, s1)
        self.inorder(root, target, True, s2)

        while k > 0:
            if not s1:
                res.append(s2.pop())
            elif not s2:
                res.append(s1.pop())
            elif abs(s1[-1] - target) < abs(s2[-1] - target):
                res.append(s1.pop())
            else:
                res.append((s2.pop()))
            k -= 1

        return res

    def inorder(self, root, target, is_reverse, stack):
        if not root:
            return

        self.inorder(root.right if is_reverse else root.left, target, is_reverse, stack)

        if (is_reverse and root.val <= target) or (not is_reverse and root.val > target):
            return

        stack.append(root.val)

        self.inorder(root.left if is_reverse else root.right, target, is_reverse, stack)

