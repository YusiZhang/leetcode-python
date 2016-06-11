# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return 
        ans = []
        stack = []
        stack.append(root)
        while stack:
        	cur = stack.pop()
        	ans.append(cur.val)
        	# 关键点：要先压入右孩子，再压入左孩子，这样在出栈时会先打印左孩子再打印右孩子
        	if cur.right:
        		stack.append(cur.right)
        	if cur.left:
        		stack.append(cur.left)

        return ans