import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize base case
    dp[m-1][n-1] = grid[m-1][n-1]

    # Fill up the DP table from bottom right to top left
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]

    # Return the minimum sum at the top left corner
    return dp[0][0]

if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    print(min_path_sum(grid))
