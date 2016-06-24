# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if not root:
        #     return None
        # right = self.invertTree(root.right)
        # left = self.invertTree(root.left)
        # root.left = right
        # root.right = left
        # return root
        
        #BFS solution
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        while len(q) != 0:
            current = q.popleft()
            current.left, current.right = current.right, current.left
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
                
        return root
        
"""
public TreeNode invertTree(TreeNode root) {
    if (root == null) {
        return null;
    }
    TreeNode right = invertTree(root.right);
    TreeNode left = invertTree(root.left);
    root.left = right;
    root.right = left;
    return root;
}
"""

"""BFS
public TreeNode invertTree(TreeNode root) {
    if (root == null) return null;
    Queue<TreeNode> queue = new LinkedList<TreeNode>();
    queue.add(root);
    while (!queue.isEmpty()) {
        TreeNode current = queue.poll();
        TreeNode temp = current.left;
        current.left = current.right;
        current.right = temp;
        if (current.left != null) queue.add(current.left);
        if (current.right != null) queue.add(current.right);
    }
    return root;
}
"""

"""java dfs/iterative style
public class Solution {
    public TreeNode invertTree(TreeNode root) {

        if (root == null) {
            return null;
        }

        final Deque<TreeNode> stack = new LinkedList<>();
        stack.push(root);

        while(!stack.isEmpty()) {
            final TreeNode node = stack.pop();
            final TreeNode left = node.left;
            node.left = node.right;
            node.right = left;

            if(node.left != null) {
                stack.push(node.left);
            }
            if(node.right != null) {
                stack.push(node.right);
            }
        }
        return root;
    }
}
"""
        