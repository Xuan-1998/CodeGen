import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]
    prev = [[None] * n for _ in range(m)]

    # base case: bottom right corner
    dp[m-1][n-1] = grid[m-1][n-1]

    # fill up the dp table
    for i in range(m):
        for j in range(n):
            if i > 0 and dp[i-1][j] + grid[i][j] < dp[i][j]:
                dp[i][j] = dp[i-1][j] + grid[i][j]
                prev[i][j] = 'up'
            if j > 0 and dp[i][j-1] + grid[i][j] < dp[i][j]:
                dp[i][j] = dp[i][j-1] + grid[i][j]
                prev[i][j] = 'left'

    # backtracking to find the path
    i, j = m-1, n-1
    path_sum = 0
    while i > 0 or j > 0:
        if prev[i][j] == 'up':
            path_sum += grid[i][j]
            i -= 1
        else:
            path_sum += grid[i][j]
            j -= 1

    return path_sum

# read input from stdin
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

print(min_path_sum(grid))
