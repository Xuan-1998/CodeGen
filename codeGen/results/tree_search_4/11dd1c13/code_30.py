import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Base case: Initialize the first row
    dp[0] = grid[0]

    for i in range(1, n):
        for j in range(n):
            min_val = float('inf')
            for k in range(n):
                if k != j:
                    min_val = min(min_val, grid[i-1][k] + dp[i-1][k])
            dp[i][j] = min_val

    return dp[-1][-1]

# Read input from stdin
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Print the minimum sum to stdout
print(min_falling_path_sum(grid))
