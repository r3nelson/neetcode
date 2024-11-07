# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # check node exists
        if not root:
            return TreeNode(val)
        
        # go left
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        # go right
        elif val > root.val:
            root.right = self.insertIntoBST(root.right,val)

        return root
        