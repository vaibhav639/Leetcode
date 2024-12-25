class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def solve(n,op):
            if op == n:
                return True
            elif op > n:
                return False
            return solve(n,op*3)

        return solve(n,1)        