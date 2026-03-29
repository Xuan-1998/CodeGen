# Define the function to find the minimum sum of all numbers along the path
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a 2D array to store the minimum sum at each position
    dp = [[0] * n for _ in range(m)]
    
    # Base case: The minimum sum for the first row is equal to the values in the first row
    for i in range(n):
        dp[0][i] = grid[0][i]
    
    # For each row, calculate the minimum sum based on the previous row
    for i in range(1, m):
        for j in range(n):
            if j == 0:  # Left boundary, only move down
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif j == n-1:  # Right boundary, only move up
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The minimum sum of all numbers along the path from top left to bottom right is stored in the last cell
    return dp[m-1][n-1]

# Read input from stdin and print the output to stdout
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
print(min_path_sum(grid))
