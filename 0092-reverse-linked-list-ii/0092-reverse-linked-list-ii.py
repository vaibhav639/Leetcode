# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        nums = []

        while current:
            nums.append(current.val)
            current = current.next

        l_index = left - 1
        r_index = right - 1

        final = []
        final = final + nums[:l_index] + nums[l_index:r_index+1][::-1] + nums[r_index + 1:]

        node = ListNode(0)
        current = node

        for num in final:
            new_node = ListNode(num)
            current.next = new_node
            current = current.next

        return node.next

        