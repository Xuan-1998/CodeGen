def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: Initialize the minimum sum for the first row
    dp[0] = grid[0]

    # Fill up the dynamic programming table
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(n))
            elif j == n-1:
                dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(n-1, -1, -1))
            else:
                dp[i][j] = min(min(dp[i-1][k] + grid[i][j] for k in range(j)) +
                                 min(dp[i-1][k] + grid[i][j] for k in range(j+1, n)))

    # Return the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])

# Read input from stdin and print the output to stdout
grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_falling_path_sum(grid))
