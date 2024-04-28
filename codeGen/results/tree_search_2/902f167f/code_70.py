import sys

def min_squares(n, m):
    if n == 0 and m == 0:
        return 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0 and j > 0:
                if i >= j:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j] + 1
            elif i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i

    return dp[n][m]

n, m = map(int, sys.stdin.readline().split())
print(min_squares(n, m))
