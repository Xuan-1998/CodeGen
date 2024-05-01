def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0]*n for _ in range(n)]
    
    for i in range(n-2, -1, -1):
        for j in range(n):
            if i == n-1:
                dp[i][j] = grid[i][j]
            else:
                min_sum = float('inf')
                for k in range(n):
                    if k != j:
                        min_sum = min(min_sum, dp[i+1][k])
                dp[i][j] = grid[i][j] + min_sum
    
    return min(dp[0])
