class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i,jump in enumerate(nums):
            if i > max_jump:
                return False

            max_jump = max(max_jump, i + jump)

            if max_jump >= len(nums) -1:
                return True
        return False
        
        