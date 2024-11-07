# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #  if val < root:
        #         root.left = TreeNode(val)
        #     elif val > root:
        #         root.right = TreeNode(val)

        # root is first value in preorder

        # root = preorder[0]
        # minNode = inorder[0] 
        # maxNode = preorder[-1]

        root = TreeNode(preorder[0])
        cur = root
        for index, val in enumerate(inorder):
            if val == preorder[0]:
                inorder_root_index = index
                break


        # any value to the right of inorder root index goes on right and any to the left goes on left.
        left_values = inorder[: inorder_root_index]
        right_values = inorder[inorder_root_index + 1:]
        
        for i in left_values:
            cur.left = TreeNode(i)
            cur = cur.left

        for i in right_values:
            root.right = TreeNode(i)

        return root


           
            
            

        # for val in inorder:
        #     newNode = TreeNode(val)
            




