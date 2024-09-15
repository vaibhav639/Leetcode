class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        res = []

        for i in range(len(nums)-3):
            for j in range(i + 1, len(nums)-2):
                l = j + 1
                r = len(nums)-1
    
                while (l < r):
                    s = nums[i] + nums[j] + nums[l] + nums[r]
        
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while (l < r) and (nums[l] == nums[l + 1]):
                            l += 1
                        while (l < r) and (nums[r] == nums[r - 1]):
                            r -= 1
                        l += 1
                        r -= 1

                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        set_res = set(tuple(quadruplets) for quadruplets in res)
        unique_quadruplets = [list(quadruplets) for quadruplets in set_res] 
        return unique_quadruplets

        