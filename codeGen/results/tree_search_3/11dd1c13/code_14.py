def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Base case: first row
    dp[0] = grid[0]

    for i in range(1, n):
        for j in range(n):
            if i > 0 and j > 0:
                min_val = float('inf')
                for k in range(n):
                    if k != dp[i-1][j-1]:
                        min_val = min(min_val, dp[i-1][k])
                dp[i][j] = grid[i][j] + min_val
            else:
                dp[i][j] = grid[i][j]

    return min(dp[-1])

# Read input from stdin
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path(grid))
