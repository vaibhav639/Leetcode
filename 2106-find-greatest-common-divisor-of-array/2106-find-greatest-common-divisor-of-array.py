class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)

        if mx % mn == 0:
            return mn
        else:
            gcd = 1

            for i in range(2,(mn//2)+1):
                if (mn % i == 0) and (mx % i == 0):
                    gcd = max(gcd,i)
            return gcd
        