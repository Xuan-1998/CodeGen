from sys import stdin

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Initialize the dp array with all values as infinity
    dp = [[float('inf')] * n for _ in range(m)]
    
    # The initial state is initialized with all values as 0 except for the first cell which is grid[0][0]
    dp[0][0] = grid[0][0]
    
    # Fill in the dp array from top left to bottom right
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # Return the minimum path sum
    return dp[m-1][n-1]

grid = [[int(x) for x in stdin.read().split()] for _ in range(int(stdin.readline()))]
print(min_path_sum(grid))
