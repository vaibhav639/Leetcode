# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            a = current
            b = current.next
            temp = a.val
            a.val = b.val
            b.val = temp
            current = current.next.next

        return head

        