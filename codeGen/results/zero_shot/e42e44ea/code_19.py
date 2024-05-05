import sys

def min_points_to_reach_destination(N, M, grid):
    # Create a 2D DP table filled with infinity values
    dp = [[sys.maxsize for _ in range(M)] for _ in range(N)]
    
    # Initialize the top-left cell as having 0 points required to reach
    dp[0][0] = 0
    
    # Fill up the DP table using dynamic programming
    for i in range(N):
        for j in range(M):
            if i > 0 and grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # Find the minimum points required to reach the destination cell
    return dp[-1][-1]

# Read input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
result = min_points_to_reach_destination(N, M, grid)
print(result)
