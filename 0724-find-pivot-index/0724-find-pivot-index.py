class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = []
        rsum = []
        totalsum = sum(nums[:])

        for i in range(len(nums)):
            if not lsum:
                lsum.append(0)
            else:
                lsum.append(sum(nums[:i]))
        
        
        for i in range(len(nums)):
            if not rsum:
                rsum.append(totalsum-nums[0])
            else:
                rsum.append(totalsum-sum(nums[:i+1]))

        i = 0
        flag = False
        while i < len(lsum):
            if lsum[i]==rsum[i]:
                flag = True
                break
            i+=1
        if flag:
            return i
        else:
            return -1
