"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = {None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            copied[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = copied[cur]
            copy.next = copied[cur.next]
            copy.random = copied[cur.random]
            cur = cur.next
            
        return copied[head]
