"""
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        if lh == rh:
            return (1 << lh) + self.countNodes(root.right)
        else:
            return (1 << rh) + self.countNodes(root.left)
        
    def getHeight(self, root):
        if not root:
            return 0
        return 1 + self.getHeight(root.left)
        
"""
 class Solution {
    public:
        int countNodes(TreeNode* root) {
            if(!root) return 0;
            int lh=fTreeHt(root->left);
            int rh=fTreeHt(root->right);     
            if(lh==rh) 
               return (1<<lh)+countNodes(root->right);  /*1(根节点) + (1<<lh)-1(完全左子树) + # of rightNode */               
            else 
               return (1<<rh)+countNodes(root->left);  /*1(根节点) + (1<<rh)-1(完全右子树) + # of leftNode*/
        }
    private:
        int fTreeHt(TreeNode *root){ //get the height of a complete binary tree.
            if(!root) return 0;
            return 1+fTreeHt(root->left);
        }
    };
"""