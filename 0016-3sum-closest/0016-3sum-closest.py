class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest_num = float('inf')
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1

            while(l < r):
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(closest_num - target):
                    closest_num = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s

        return closest_num

        