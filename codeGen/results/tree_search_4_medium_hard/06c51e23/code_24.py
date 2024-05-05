import sys

n, t = map(int, input().split())
dp = [[-1] * (t + 1) for _ in range(n + 1)]

def solve():
    dp[0][t] = 0
    for i in range(1, n + 1):
        for j in range(t, -1, -1):
            if j >= 9:  # Round up to the nearest integer if the last digit is 8 or more
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + 1)
            else:
                dp[i][j] = dp[i-1][j-1]
    return dp[n][t]

print(solve())
