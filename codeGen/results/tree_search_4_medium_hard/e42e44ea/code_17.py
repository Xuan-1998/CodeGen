def minInitialPoints(N, M, grid):
    # Initialize DP table with infinity values
    dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
    
    # Base case: Top-left cell has no initial points required
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        if grid[i - 1][0] > 0:
            dp[i][0] = dp[i - 1][0]
    
    for j in range(1, M + 1):
        if grid[0][j - 1] > 0:
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Update DP states considering only rightward or downward movements
            if grid[i - 1][j - 1] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
    
    return dp[N][M]

# Example usage:
N, M = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(N)]

result = minInitialPoints(N, M, grid)
print(result)
