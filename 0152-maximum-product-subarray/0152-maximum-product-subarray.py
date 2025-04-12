import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minimum = nums[0]
        maximum = nums[0]
        answer = nums[0]

        for i in range(1,len(nums)):
            c1 = nums[i]
            c2 = maximum * c1
            c3 = minimum * c1

            maximum = max(c1,c2,c3)
            minimum = min(c1,c2,c3)
            answer = max(maximum,answer)

        return answer

        