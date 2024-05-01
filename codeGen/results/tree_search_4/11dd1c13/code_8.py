import sys

def min_falling_path(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: Initialize the first row
    dp[0] = grid[0]
    
    # Calculate the DP table
    for j in range(1, m):
        for i in range(n):
            min_sum = sys.maxsize
            for k in range(m):
                if k != j:
                    min_sum = min(min_sum, dp[k][i] + grid[j][i])
            dp[j][i] = min_sum
    
    # Find the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])

# Read input from stdin and print output to stdout
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path(grid))
