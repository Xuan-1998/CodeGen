import sys

def min_falling_path_sum(grid):
    n = len(grid)
    
    # Initialize dp table
    dp = [[0] * len(grid[0]) for _ in range(n)]
    
    # Fill up the dp table
    for i in range(n):
        for j in range(len(grid[0])):
            if i == 0:
                dp[i][j] = grid[i][j]
            else:
                min_sum = float('inf')
                for k in range(len(grid[0])):
                    if k != j and k >= j - (n - i):
                        min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
                dp[i][j] = grid[i][j] + min_sum
                
    # Return the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])

grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path_sum(grid))
