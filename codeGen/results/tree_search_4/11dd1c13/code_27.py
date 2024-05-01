def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        if i == 0:
            for j in range(n):
                dp[i][j] = grid[i][j]
        else:
            for j in range(n):
                if j == 0:
                    dp[i][j] = dp[i-1][n-1] + grid[i][j]
                elif j == n-1:
                    dp[i][j] = dp[i-1][0] + grid[i][j]
                else:
                    min_sum = float('inf')
                    for k in range(n):
                        if k != j:
                            min_sum = min(min_sum, dp[i-1][k]) + grid[i][j]
                    dp[i][j] = min_sum

    return min(dp[-1])

# Receive input from stdin
grid = [list(map(int, input().split())) for _ in range(int(input()))]

# Print the answer to stdout
print(minFallingPathSum(grid))
