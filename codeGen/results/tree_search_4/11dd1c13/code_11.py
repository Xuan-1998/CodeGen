import sys

grid_size = int(input())
grid = [list(map(int, input().split())) for _ in range(grid_size)]

dp = [[0] * grid_size for _ in range(grid_size)]

for i in range(1, grid_size):
    for j in range(grid_size):
        min_sum = sys.maxsize
        for k in range(j):  # Consider all columns that are not in the same column as the previous row
            if (i-1) % grid_size != k % grid_size:  # Ensure no two elements chosen in adjacent rows are in the same column
                min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
        dp[i][j] = min_sum

print(dp[grid_size-1][0])
