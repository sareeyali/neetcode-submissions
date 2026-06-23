# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        if p.val < lca.val and q.val < lca.val:
            lca = self.lowestCommonAncestor(root.left, p, q)
        if p.val > lca.val and q.val > lca.val:
            lca = self.lowestCommonAncestor(root.right, p, q)
        return lca