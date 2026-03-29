def minInitialPoints(grid):
    N, M = len(grid), len(grid[0])
    
    # Initialize DP table with zeros
    dp = [[0] * N for _ in range(M)]
    
    # Fill in the DP table
    for i in range(1, M):
        for j in range(N):
            if grid[i-1][j] > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j]
    
    # Return the minimum initial points required
    return dp[-1][-1]

# Example usage
N, M = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(N)]
print(minInitialPoints(grid))
