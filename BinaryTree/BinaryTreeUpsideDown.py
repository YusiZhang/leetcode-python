# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.postOrderList = []

    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root


        self.getPostOrderArray(root)
        preOrderList = self.postOrderList

        return self.buildFromPreOrder(preOrderList)


    def getPostOrderArray(self, root):
        if not root:
            return
        self.getPostOrderArray(root.left)
        self.getPostOrderArray(root.right)
        self.postOrderList.append(root.val)

    def buildFromPreOrder(self, preOrderList):
        dummyNode = TreeNode(None)
        root = TreeNode(preOrderList[0])
        dummyNode = root

        for i in range(1, len(preOrderList)):
            if i % 2 == 0:
                root.val = preOrderList[i]
            else:
                root.left = TreeNode(preOrderList[i])
                root.right = TreeNode(None)
                root = root.right



        return dummyNode



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    solution.getPostOrderArray(root)
    print solution.postOrderList

    print solution.buildFromPreOrder(solution.postOrderList).right.left.val
