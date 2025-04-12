class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    if (nums[i],nums[j]) not in result and (nums[j],nums[i]) not in result:
                        result.append((nums[i],nums[j]))

        return len(result)
        