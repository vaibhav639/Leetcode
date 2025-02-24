class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        value = list(sorted(freq.values(),reverse = True))

        key = None

        for key,val in freq.items():
            if val == value[0]:
                return key

        