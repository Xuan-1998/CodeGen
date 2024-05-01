import sys

def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[-sys.maxsize] * n for _ in range(m)]
    
    # Initialize the base case
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Fill up the dynamic programming table
    for i in range(1, m):
        for j in range(n):
            min_sum = -sys.maxsize
            for k in range(j-1, -1, -1):
                if dp[i-1][k] != -sys.maxsize:
                    min_sum = max(min_sum, dp[i-1][k]) + grid[i][j]
            dp[i][j] = min_sum
    
    # Return the minimum sum of falling paths with non-zero shifts
    return min(dp[-1])

# Read input from stdin
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path_sum(grid))
