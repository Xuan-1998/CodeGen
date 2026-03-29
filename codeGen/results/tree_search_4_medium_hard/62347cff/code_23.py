from sys import stdin

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: top or left boundary
    for i in range(m):
        if i == 0:
            dp[i][0] = grid[i][0]
        else:
            dp[i][0] = dp[i-1][0] + grid[i][0]

    for j in range(n):
        if j == 0:
            dp[0][j] = grid[0][j]
        else:
            dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill up the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]


grid = [[int(x) for x in line.strip().split()] for line in stdin]
print(min_path_sum(grid))
