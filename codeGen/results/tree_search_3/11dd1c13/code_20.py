import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Base case: all elements in the first row
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], grid[i][j])
            elif j == n-1:
                dp[i][j] = max(dp[i-1][j-1], grid[i][j])
            else:
                dp[i][j] = grid[i][j] + min(dp[i-1][j-1], dp[i-1][j])

    return min(dp[-1])

# Read input
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path_sum(grid))
