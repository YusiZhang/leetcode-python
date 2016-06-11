# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            top = stack.pop()
            ans.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return ans[::-1]

    def postorderTraversal2(self, root):
    	if root is None:
    		return None
    	stack = []
    	lastNodeVisited = None
    	cur = root
    	while stack or cur:
    		if cur:
    			stack.append(cur) #root 最后被访问，所以最前压栈
    			cur = cur.left
    		else:
    			top = stack[-1]
    			# if right child exists and traversing node from left child
    			# then move right
    			if top.right and lastNodeVisited is not top.right:
    				cur = top.right
    			else:
    				ans.append(top.val)
    				lastNodeVisited = stack.pop()
    	return ans