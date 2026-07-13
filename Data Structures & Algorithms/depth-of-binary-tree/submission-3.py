# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        res = 0
        while stack:
            c, d = stack.pop()
            res = max(res, d)
            
            if c.left:
                stack.append([c.left, d + 1])
            if c.right:
                stack.append([c.right, d + 1])
        return res

