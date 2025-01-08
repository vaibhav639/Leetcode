class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        max_len = 0
        for key in freq:
            if key + 1 in freq:
                max_len = max(max_len, freq[key] + freq[key+1])

        return max_len