def minFallingPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]

    # base case: initialize the first row
    dp[0] = grid[0]

    for i in range(1, m):
        for j in range(n):
            if i == 1:
                dp[i][j] = min(dp[i-1]) + grid[i][j]
            else:
                dp[i][j] = float('inf')
                for k in range(n):
                    if abs(j-k) > 0:  # non-zero shift
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])
                dp[i][j] += grid[i][j]

    return min(min(row) for row in dp)

import sys
m = int(input().strip())
grid = []
for _ in range(m):
    grid.append(list(map(int, input().strip().split())))

print(minFallingPathSum(grid))
