# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        dummy = ListNode(0)
        current = dummy
        while stack:
            element_pop = stack.pop()
            new_node = ListNode(element_pop)
            current.next = new_node
            current = current.next
        return dummy.next
            

        