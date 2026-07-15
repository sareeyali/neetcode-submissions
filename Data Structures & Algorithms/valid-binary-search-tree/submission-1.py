# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            if root.left and root.val < root.left.val:
                return False
            if root.right and root.val > root.right.val:
                return False
            dfs(root.left)
            dfs(root.right)
            return True
        return dfs(root)