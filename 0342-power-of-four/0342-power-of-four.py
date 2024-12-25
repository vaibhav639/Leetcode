class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def solve(n,op):
            if op > n:
                return False
            if op == n:
                return True

            return solve(n,op*4)
            
        return solve(n,1)