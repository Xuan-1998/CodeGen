import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    
    # Base case: The first row has no elements above it.
    for j in range(n):
        dp[0][j] = grid[0][j]
        
    for i in range(1, n):
        for j in range(n):
            min_sum = sys.maxsize
            for k in range(n):
                if k != j and i > 0:
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum
    
    return min(dp[-1])

# Read input from stdin
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path_sum(grid))
