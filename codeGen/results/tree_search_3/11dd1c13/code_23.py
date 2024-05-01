import sys

def min_falling_path_sum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[sys.maxsize] * (n+1) for _ in range(m+1)]

    # Base cases: handle edge cases where there are no rows or columns left to consider
    for i in range(m+1):
        if i > 0:
            dp[i][0] = -10**9
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    return min(dp[m])
