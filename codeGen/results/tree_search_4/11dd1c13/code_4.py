def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Base case: Initialize the first row
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the DP table
    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if k != j:
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

    # Return the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])

# Receive input from stdin and print output to stdout
grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_falling_path_sum(grid))
