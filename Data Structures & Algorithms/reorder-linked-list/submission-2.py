# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # cut list in half
        l2 = slow.next
        slow.next = None

        prev = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l1 = head
        l2 = prev
        while l2:
            n1 = l1.next
            n2 = l2.next

            l1.next = l2     
            l2.next = n1     

            l1 = n1
            l2 = n2
