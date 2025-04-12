class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        nums = sorted(arr)
        rank = {}
        for num in nums:
            rank[num] = None

        curr = 1
        rank[nums[0]] = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                rank[nums[i]] = curr
            else:
                curr += 1
                rank[nums[i]] = curr
    
        result = []

        for num in arr:
            result.append(rank[num])
        
        return result  

        