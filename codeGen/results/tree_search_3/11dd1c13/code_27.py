def minFallingPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row as the input grid
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the rest of the table
    for i in range(1, m):
        for j in range(n):
            min_val = float('inf')
            for k in range(n):
                if abs(j - k) != 1:  # Ensure non-zero shifts
                    min_val = min(min_val, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_val

    return min(dp[-1])

# Read input from stdin and print the result to stdout
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
