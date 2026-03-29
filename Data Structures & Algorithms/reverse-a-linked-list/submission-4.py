# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        return self._reverse(None, head)
    
    def _reverse(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
        if not curr:
            return prev
        next = curr.next
        curr.next = prev
        return self._reverse(curr, next)