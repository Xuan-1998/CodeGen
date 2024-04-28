def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0] = grid[0]
    
    for i in range(1, n):
        new_dp = [float('inf')] * n
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if abs(j-k) != 1: # non-zero shift
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            new_dp[j] = min_sum
        dp = new_dp
    
    return min(dp[-1])

grid = [[2,-1,1],[3,5,5],[1,5,1]]
print(minFallingPathSum(grid))  # Output: 7
