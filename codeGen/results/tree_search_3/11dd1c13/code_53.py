import sys

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    dp[0][j] = grid[0][j]  # base case: first row

    for i in range(1, n):
        for j in range(n):
            min_sum = sys.maxsize
            for k in range(j):  # iterate over previous rows
                min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

    return min(dp[-1])  # minimum sum of a falling path ending at the last row

# read input from stdin
grid = []
for _ in range(int(input())):
    grid.append(list(map(int, input().split())))

print(min_falling_path(grid))
