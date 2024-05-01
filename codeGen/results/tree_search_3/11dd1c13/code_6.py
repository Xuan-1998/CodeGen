def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    dp[0] = grid[0]
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(min(j+1, n)))
            elif j == n-1:
                dp[i][j] = grid[i][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i-1][k] + grid[i][j]) for k in range(min(j-1, n-1))]

    return min(dp[-1])

# Read input from stdin
grid = []
n = int(input())
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
