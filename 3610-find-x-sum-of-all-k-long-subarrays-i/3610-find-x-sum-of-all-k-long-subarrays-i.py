class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i = 0
        sum_array = [0] * (len(nums)-k+1)

        while i <= len(nums)-k:
            freq = {}
            for num in nums[i:i+k]:
                freq[num] = freq.get(num,0) + 1

            sort_freq = sorted(freq.items(), key = lambda item: (item[1],item[0]), reverse = True)

            summ = sum([key*val for key,val in sort_freq[:x]])
            sum_array[i] = summ
            i+=1
        return sum_array 