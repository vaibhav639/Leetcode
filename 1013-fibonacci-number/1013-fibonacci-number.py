class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def fibo(n,dp):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] =  fibo(n-1,dp) + fibo(n-2,dp)
            return dp[n]
        return fibo(n,dp)