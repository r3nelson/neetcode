# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        
        # go left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # at key
        else:
            # no children
            if not root.left and not root.right:
                root = None
            # two children
            if root.left and root.right:
                cur = root.left
                temp = root.right
                root = cur
                root.right = temp
            # one child 
            if not root.left:
                root.val = root.right
            if not root.right:
                root.val = root.left
            
        return root