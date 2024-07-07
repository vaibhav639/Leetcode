# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        result = ListNode(0)
        carry = 0
        head = result
        
        while l1 or l2 or carry:
            sum1 = carry
            if l1:
                sum1+=l1.val
                l1 = l1.next
            if l2:
                sum1+=l2.val
                l2 = l2.next
            
            carry = sum1//10
            rem = sum1 % 10
            
            head.next = ListNode(rem)
            head = head.next
            
        return result.next
        
                
            
             
                
            
        