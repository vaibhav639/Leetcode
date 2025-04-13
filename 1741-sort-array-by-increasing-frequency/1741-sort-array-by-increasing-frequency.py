class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        sorted_v = [k for k,v in sorted(freq.items(),key=lambda x:(x[1],-x[0]))]
        ans = []
        for num in sorted_v:
            ans.extend([num]*freq[num])
        return ans

        

        