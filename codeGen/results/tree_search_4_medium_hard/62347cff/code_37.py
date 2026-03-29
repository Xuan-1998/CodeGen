from sys import stdin

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize first row and column
    for j in range(n):
        dp[0][j] = grid[0][j]
    for i in range(m):
        dp[i][0] = grid[i][0]

    # Fill up the dp table using memoization
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

grid = [list(map(int, input().split())) for _ in range(int(stdin.readline()))]
print(min_path_sum(grid))
