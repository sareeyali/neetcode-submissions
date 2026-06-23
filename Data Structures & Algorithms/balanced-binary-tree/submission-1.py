# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (True, 0)    

            LB, left = dfs(root.left)
            RB, right = dfs(root.right)
            height = 1 + max(left, right)
            diff = abs(right - left)
            balance = True if diff <= 1 and LB and RB else False
            return (balance, height)
        ans = dfs(root)
        return ans[0]








