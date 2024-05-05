import sys

def min_initial_points(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the first row and column
    dp[0][0] = 1 if grid[0][0] > 0 else float('inf')
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], grid[i][0]) if grid[i][0] > 0 else float('inf')
    for j in range(1, m):
        dp[0][j] = min(dp[0][j-1], grid[0][j]) if grid[0][j] > 0 else float('inf')

    # Fill in the rest of the dp array
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                dp[i][j] = float('inf')

    # Return the minimum initial points required to reach the bottom-right cell
    return min(dp[-1][-1], 0) if dp[-1][-1] > 0 else 0

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Call the function and print the output to stdout
print(min_initial_points(n, m, grid))
