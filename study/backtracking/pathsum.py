# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return
        
        targetSum -= root.val
        
        if targetSum == 0 and not root.left and not root.right:
            return True

        root.left = self.hasPathSum(root.left, targetSum)
        if root.left: return root.left
        root.right = self.hasPathSum(root.right, targetSum)
        if root.right: return root.right

        
        return False
        

