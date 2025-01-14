class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        result = []

        while j < len(nums):
            if nums[j-1] < nums[j]:
                if j + 1 == len(nums):
                    result.append(nums[i:j+1])
                    j+=1
                j += 1
            else:
                result.append(nums[i:j])
                i+=1
                j = i + 1
        return max(len(sublist) for sublist in result)