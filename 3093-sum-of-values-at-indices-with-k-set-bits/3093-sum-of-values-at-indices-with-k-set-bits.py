class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        summ = 0

        for i in range(len(nums)):
            if bin(i).count("1") == k:
                summ += nums[i]

        return summ