# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root:Optional[TreeNode])-> int:
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal res
            res = max(res, left + right)

            return 1 + max(left,right)

        dfs(root)

        return res
    
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     self.res = 0

    #     def dfs(root:Optional[TreeNode])-> int:
    #         if not root:
    #             return 0
            
    #         left = dfs(root.left)
    #         right = dfs(root.right)

    #         self.res = max(self.res, left + right)

    #         return 1 + max(left,right)

    #     dfs(root)

    #     return self.res
            

