# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        stack = []
        while current:
            stack.append(current.val)
            current = current.next

        stack2 = stack[::-1]

        if stack == stack2:
            return True
        else:
            return False


        