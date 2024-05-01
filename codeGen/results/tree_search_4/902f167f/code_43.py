import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                min_squares = sys.maxsize
                for k in range(min(i, j) ** 0.5 + 1):
                    area = k * k
                    if (i - k * k) >= 0 and (j - k * k) >= 0:
                        min_squares = min(min_squares, 1 + dp[i - k * k][j - k * k])
                dp[i][j] = min_squares

    return dp[n][m]

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())

print(min_squares(n, m))
