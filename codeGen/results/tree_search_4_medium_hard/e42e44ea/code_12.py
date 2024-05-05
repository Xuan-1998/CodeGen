def minInitialPoints(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j] if grid[i-1][j] >= 0 else float('inf'), 
                               dp[i][j-1] if grid[i][j-1] >= 0 else float('inf')) + grid[i][j]
            elif i > 0:
                dp[i][j] = min(dp[i-1][j], 0) + grid[i][j]
            elif j > 0:
                dp[i][j] = min(dp[i][j-1], 0) + grid[i][j]
    
    return dp[-1][-1]

# Example usage
N, M = map(int, input().split())
grid = [[*map(int, input().split()) for _ in range(M)] for _ in range(N)]
print(minInitialPoints(grid))
