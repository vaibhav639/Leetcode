# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        before = []
        after = []

        while current:
            if current.val < x:
                before.append(current.val)
            else:
                after.append(current.val)
            current = current.next

        current = head

        while current:
            if before:
                current.val = before[0]
                before = before[1:]
                current = current.next
            else:
                current.val = after[0]
                after = after[1:]
                current = current.next

        return head




        