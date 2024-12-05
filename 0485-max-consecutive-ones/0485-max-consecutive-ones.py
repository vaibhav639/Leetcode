class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stack = []
        count = 0

        for num in nums:
            if stack and num != 1:
                len_of_stack = len(stack)
                count = max(count,len_of_stack)
                while stack:
                    stack.pop()
                
            if not stack and num != 1:
                pass
            if num == 1:
                stack.append(num)

        if stack:
            len_of_stack = len(stack)
            count = max(count,len_of_stack)

        return count



        
    
            


        