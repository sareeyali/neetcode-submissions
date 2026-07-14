# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        while q:
            lvl = len(q)
            vals = []
            for i in range(lvl):
                cur = q.popleft()
                if cur:
                    vals.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if vals:
                res.append(vals)
        return res
                