# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 1. recursive DFS
    def isSymmetric(self, root):
        return self.isMirror(root, root)
    def isMirror(self, t1, t2):
        if t1 is None and t2 is None: return True
        if t1 is None or t2 is None: return False
        
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
     
    
    # 2.Iterative DFS solution - stack
    def isSymmetric(self, root):
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            t1 = stack.pop()
            t2 = stack.pop()
            if t1 is None and t2 is None: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)
        
        return True
    
    # 3.BFS solution - queue
    def isSymmetric(self, root):
        if not root:
            return True
        q = collections.deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            if t1 is None and t2 is None: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        
        return True
        
"""
public boolean isSymmetric(TreeNode root) {
    return isMirror(root, root);
}

public boolean isMirror(TreeNode t1, TreeNode t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    return (t1.val == t2.val)
        && isMirror(t1.right, t2.left)
        && isMirror(t1.left, t2.right);
}
"""

"""BFS
public boolean isSymmetric(TreeNode root) {
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    q.add(root);
    while (!q.isEmpty()) {
        TreeNode t1 = q.poll();
        TreeNode t2 = q.poll();
        if (t1 == null && t2 == null) continue;
        if (t1 == null || t2 == null) return false;
        if (t1.val != t2.val) return false;
        q.add(t1.left);
        q.add(t2.right);
        q.add(t1.right);
        q.add(t2.left);
    }
    return true;
}
"""