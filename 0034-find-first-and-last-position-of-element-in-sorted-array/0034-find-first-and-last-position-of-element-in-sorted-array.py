class Solution:
    def searchRange(self, nums, target):
        l = len(nums)
        position = [-1, -1]
        flag = False

        for x in range(l):
            if nums[x] == target:
                if not flag:
                    position[0] = x
                    flag = True
                position[1] = x

        return position

        