class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            sub_arr = nums[i:i+3]
            if sub_arr[0]+sub_arr[-1] == sub_arr[1]/2:
                count+=1

        return count