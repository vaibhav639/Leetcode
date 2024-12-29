# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # lst = []
        # while head:
        #     lst.append(head.val)
        #     head = head.next
        # lst[k-1] , lst[len(lst)-k] = lst[len(lst)-k] , lst[k-1]
        # dummy = ListNode(0)
        # current = dummy
        # for num in lst:
        #     current.next = ListNode(num)
        #     current = current.next
        # return dummy.next

        current = head
        for i in range(1,k):
            current = current.next
        a = current
        b = head

        while current is not None and current.next is not None:
            current = current.next
            b = b.next
        temp = a.val
        a.val = b.val
        b.val = temp
        return head
        