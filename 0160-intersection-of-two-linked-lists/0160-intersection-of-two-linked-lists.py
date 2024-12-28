# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = headA
        second = headB
        headB_set = set()

        # while first is not None:
        #     while second is not None:
        #         if first is None or second is None:
        #             return None
        #         elif first == second:
        #             return first
        #         second = second.next
        #     first = first.next
        #     second = headB
        # return None

        while headB is not None:
            headB_set.add(headB)
            headB = headB.next

        while headA is not None:
            if headA in headB_set:
                return headA
            headA = headA.next
        return None


        

        




        