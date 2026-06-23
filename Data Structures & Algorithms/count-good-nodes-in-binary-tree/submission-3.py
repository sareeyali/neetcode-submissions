# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxR):
            if not root:
                return 0

            if root.val >= maxR:
                good = 1
            else:
                good = 0
            maxR = max(maxR, root.val)

            good += dfs(root.right, maxR) 
            good += dfs(root.left, maxR)
            return good
        return dfs(root, root.val)
