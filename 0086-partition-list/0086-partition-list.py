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

        for num in before + after:
            current.val = num
            current = current.next

        return head




        