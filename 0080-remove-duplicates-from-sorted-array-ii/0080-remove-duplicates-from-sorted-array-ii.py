class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []
        freq = {}
        for num in nums:
            if num in freq and freq[num] >= 2:
                pass
            elif num in freq:
                freq[num] += 1
                new_nums.append(num)
            else:
                freq[num] = 1
                new_nums.append(num)
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

        nums = nums[:len(new_nums)]
        return len(nums)