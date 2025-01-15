class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        for item in nums:
            freq[item] = freq.get(item,0) + 1
        max_freq = max(freq.values())

        element = [key for key,val in freq.items() if val == max_freq]

        min_length = float('inf')

        for e in element:
            first_index  = nums.index(e)
            last_index = len(nums)-1 - nums[::-1].index(e)
            min_length = min(min_length, last_index - first_index + 1)
        return min_length
                

        