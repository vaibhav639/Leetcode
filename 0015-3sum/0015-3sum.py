class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []

        for i in range(len(nums)-2):
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue

            left = i + 1
            right = len(nums)-1

            while (left < right):
                s = nums[i] + nums[left] + nums[right]

                if s > 0:
                    right -= 1

                if s < 0:
                    left += 1
                
                if s == 0:
                    res.append((nums[i] , nums[left] , nums[right]))
                    while left < right and  (nums[left] == nums[left + 1]):
                        left += 1
                    while left < right and (nums[right] == nums[right - 1]):
                        right -=1
                    left+=1
                    right-=1

        set_of_res = set(tuple(triplet) for triplet in res)
        unique_res = [list(triplet) for triplet in set_of_res]

        return unique_res


        