class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(30):
            if pow(4,i) > n:
                return False
            if pow(4,i) == n:
                return True

        return False
            
        