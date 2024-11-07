# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
 
    def inOrderTraversal(self,root):
        res = []
        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inOrderTraversal(root)
        return res[k -1] if len(res)>= k else None 
        

        

        
