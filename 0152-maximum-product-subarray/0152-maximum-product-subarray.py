import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minimum = nums[0]
        maximum = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            el = nums[i]
            c1 = el
            c2 = nums[i] * minimum
            c3 = nums[i] * maximum
    
            maximum = max(c1,c2,c3)
            ans = max(ans,maximum)
            minimum = min(c1,c2,c3)
    
        return ans
        