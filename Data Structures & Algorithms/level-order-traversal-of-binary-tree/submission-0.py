# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])

        while queue:
            level = len(queue)
            vals = []
            for i in range(level):
                curr = queue.popleft()
                if curr:
                    vals.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if vals:
                res.append(vals)
            
        return res