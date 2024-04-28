def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row of dp
    for i in range(n):
        dp[0][i] = grid[0][i]

    for i in range(1, n):
        for j in range(n):
            # Calculate the minimum sum for this cell
            min_sum = float('inf')
            for k in range(n):
                if (k == 0 or k == n - 1) and j != 0 and j != n - 1:
                    continue
                min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

    # Find the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])

# Read input from stdin
grid = [list(map(int, input().split())) for _ in range(int(input()))]

print(minFallingPathSum(grid))
