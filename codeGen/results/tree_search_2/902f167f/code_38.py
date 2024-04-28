import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i == 1 or j == 1:
                dp[i][j] = min(i, j)
            else:
                for s in range(1, min(i, j) + 1):
                    if (i - s) % s != 0 and (j - s) % s != 0:
                        dp[i][j] = min(dp[i][j], dp[s-1][j-s] + dp[i-s][s-1] + 1)
    return dp[n][m]

# Read input from stdin
n, m = map(int, sys.stdin.readline().strip().split())

# Calculate and print the minimum number of integer-sided squares required to tile the rectangle
print(min_squares(n, m))
