from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for j in range(n)] for i in range(m)]
        def solve(x,y,m,n,dp):
            
            if x==m-1 or y== n-1:
                return 1
            if x >= m or y >= n:
                return 0

            if dp[x][y] != -1:
                return dp[x][y]

            dp[x][y] = solve(x+1,y,m,n,dp) + solve(x,y+1,m,n,dp)
            return dp[x][y]

        return solve(0,0,m,n,dp)