# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # recursive solution
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return p == q
        
        # DFS using Stack
        # stack = [(p, q)]
        # while stack:
        #     n1, n2 = stack.pop()
        #     if n1 and n2 and n1.val == n2.val:
        #         stack.append((n1.right, n2.right))
        #         stack.append((n1.left, n2.left))
        #     elif not n1 and not n2:
        #         continue
        #     else:
        #         return False
        # return True
        
        # BFS using Queue
        queue = [(p, q)]
        while queue:
            n1, n2 = queue.pop(0)
            if n1 and n2 and n1.val == n2.val:
                queue.append((n1.right, n2.right))
                queue.append((n1.left, n2.left))
            elif not n1 and not n2:
                continue
            else:
                return False
        return True
        
        