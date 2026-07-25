class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # If the starting or ending cell is blocked, no path exists
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize a 1D DP array representing the current row
        dp = [0] * n
        dp[0] = 1  # Base case: 1 way to start at the top-left cell
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0  # Obstacle blocks all paths through this cell
                elif c > 0:
                    dp[c] += dp[c - 1]  # Paths from top (dp[c]) + paths from left (dp[c-1])
                    
        return dp[-1]
     