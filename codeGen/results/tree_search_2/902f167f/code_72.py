import sys

def min_squares(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                top_part = dp[i-1][j]
                left_part = dp[i][j-1]
                min_squares_here = min(top_part, left_part) + (min(i, j) != 0)
                dp[i][j] = min(min_squares_here, top_part + left_part)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
