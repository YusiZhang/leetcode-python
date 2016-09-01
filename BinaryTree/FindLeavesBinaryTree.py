# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node):
            if not node:
                return -1
            i = 1 + max(dfs(node.left), dfs(node.right))
            # 能跳过i的最初值是1 + （-1） = 0
            if i == len(out):
                out.append([])
            out[i].append(node.val)
            return i
        out = []
        dfs(root)
        return out

if __name__ == '__main__':
    solution = Solution()
    node = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node.left = node1
    node.right = node2
    node1.left = node3
    node1.right = node4

    outarray = solution.findLeaves(node)

    print outarray