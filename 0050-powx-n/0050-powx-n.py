class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(x,n):
            if n == 0:
                return 1
            if n < 0:
                x = 1/ x
                n = -n
            if n % 2 == 0:
                half =  solve(x,n // 2)
                return half * half
            else:
                half = solve(x, n // 2)
                return half * half * x

        return solve(x,n)
        