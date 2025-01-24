class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(nums,s,e):
            if s == e and nums[:] not in result:
                result.append(nums[:])

            for i in range(s,e+1):
                nums[i], nums[s] = nums[s], nums[i]
                solve(nums,s+1,e)
                nums[i], nums[s] = nums[s], nums[i]

        solve(nums, 0 , len(nums)-1)
        return result

        