class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0

        r = len(obstacleGrid)
        c = len(obstacleGrid[0]) if r > 0 else 0

        dp = [[-1 for j in range(c)] for i in range(r)]

        def solve(x,y,obstacleGrid,r,c,dp):
            if x == r-1 and y == c-1:
                return 1
            elif x >= r or y >= c or obstacleGrid[x][y] == 1:
                return 0
    
            elif dp[x][y] != -1:
                return dp[x][y]
        
            dp[x][y] = solve(x+1,y,obstacleGrid,r,c,dp) + solve(x,y+1,obstacleGrid,r,c,dp)
            return dp[x][y]
    
        return solve(0,0,obstacleGrid,r,c,dp)