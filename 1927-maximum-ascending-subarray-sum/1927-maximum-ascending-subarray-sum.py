class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ = curr_sum = nums[0]

        for i in range(len(nums)):
            curr_sum = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] > nums[j-1]:
                    curr_sum+=nums[j]
                else:
                    break
            summ = max(summ,curr_sum)

        return summ
        
