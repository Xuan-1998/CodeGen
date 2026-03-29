def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Initialize the dp table with base cases
    for i in range(m):
        dp[i][0] = dp[i][j] = grid[i][0]
    for j in range(n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill up the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Example usage:
if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    print(min_path_sum(grid))
