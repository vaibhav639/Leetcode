class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            summ = 0
            for j in range(i+1,len(nums)):
                if target - nums[j] == nums[i]:
                    return [i,j]


        