# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        stack1 = []
        stack2 = []

        while current:
            stack1.append(current.val)
            current = current.next
        prev = 0
        while stack1:
            el = stack1.pop()
            if el >= prev:
                stack2.append(el)
                prev = el
        dummy = ListNode(0)
        current = dummy
        while stack2:
            el = stack2.pop()
            new_node = ListNode(el)
            current.next = new_node
            current = current.next

        return dummy.next

            