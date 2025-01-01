# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        lst = []
        while current:
            lst.append(current.val)
            current = current.next
        
        freq = Counter(lst)
        lst = [key for key,count in freq.items() if count == 1]
        dummy = ListNode(0)
        current = dummy

        for i in range(len(lst)):
            current.next = ListNode(lst[i])
            current = current.next
        return dummy.next
            



            
            


