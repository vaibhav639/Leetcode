class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        dp = [[-1 for j in range(n)] for i in range(m)]

        def solve(x,y,m,n,dp):
            if x == m-1 and y == n-1:
                return grid[x][y]

            elif x>=m or y>=n:
                return float("inf")

            elif dp[x][y] != -1:
                return dp[x][y]

            right = solve(x,y+1,m,n,dp)
            down = solve(x+1,y,m,n,dp)
        
            dp[x][y] = grid[x][y] + min(right,down)
            return dp[x][y]

        return solve(0,0,m,n,dp)