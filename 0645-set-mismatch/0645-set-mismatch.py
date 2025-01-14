class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)
        idx = -1

        for i,val in enumerate(nums):
            if val in seen:
                idx = i
            else:
                seen.add(val)

        actual_sum = int(n * (n + 1) / 2)
        present_sum = int(sum(seen))
        missing_num = actual_sum - present_sum

        return [nums[idx],missing_num]