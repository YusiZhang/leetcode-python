class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.val)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret

class TreeNodeHelper(object):
    def getTreeNodes(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node8 = TreeNode(8)

        node1.left  = node2
        node1.right = node3
        node2.left  = node4
        node2.right = node5
        node4.left  = node8
        node3.left  = node6
        node3.right = node7

        root = node1
        return root

    def printTreeLevelOrder(self, root):
        # level order print
        thislevel = [root]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print n.val,
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print
            thislevel = nextlevel

