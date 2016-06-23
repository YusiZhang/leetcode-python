# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
        
"""java solution iterative 
// iteration method
public int maxDepth(TreeNode root) {
    int max = 0;
    if (root == null) {return 0;}
    Stack<TreeNode> path = new Stack<>();
    Stack<Integer> sub = new Stack<>();
    path.push(root);
    sub.push(1);
    while (!path.isEmpty()) {
        TreeNode temp = path.pop();
        int tempVal = sub.pop();
        if (temp.left == null && temp.right == null) {max = Math.max(max, tempVal);}
        else {
            if (temp.left != null) {
                path.push(temp.left);
                sub.push(tempVal + 1);
            }
            if (temp.right != null) {
                path.push(temp.right);
                sub.push(tempVal + 1);
            }
        }
    }
    return max;
}
"""