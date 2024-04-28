def min_falling_path(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]

    # Initialize the first row of dp table
    dp[0][j] = grid[0][j] for j in range(n)

    for i in range(1, m):
        for j in range(n):
            min_sum = float('inf')
            for k in range(max(0, j-1), min(n, j+2)):
                min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

    return min(dp[m-1])

# Read input from stdin
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path(grid))
