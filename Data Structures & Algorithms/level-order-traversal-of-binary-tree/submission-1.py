# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        
        while q:
            lvl = len(q)
            path = []
            for i in range(lvl):
                curr = q.popleft()
                if curr:
                    path.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if path:
                res.append(path)
        return res
