class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                subarr = arr[i:j]
                if len(subarr) % 2 != 0:
                    summ+= sum(subarr)
            
        return summ