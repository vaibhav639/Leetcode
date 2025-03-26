import math
import functools
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sub_arr = nums[i:j+1]
                lcm = functools.reduce(math.lcm,sub_arr)
                hcf = functools.reduce(math.gcd,sub_arr)
                prod = math.prod(sub_arr)
        
                if lcm * hcf == prod:
                    curr_length = len(sub_arr)
                    max_length = max(max_length,curr_length)
            
        return max_length