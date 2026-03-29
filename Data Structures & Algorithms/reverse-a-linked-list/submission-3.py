class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        nextNode = head.next.next
        curr.next = prev
        head.next = None
        while nextNode:
            prev = curr
            curr = nextNode
            nextNode = nextNode.next
            curr.next = prev
        return curr