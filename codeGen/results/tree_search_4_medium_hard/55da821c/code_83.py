import sys

def min_replants():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(m + 1)]

    for k in range(1, m + 1):
        dp[0][k] = k

    for s in range(1, m + 1):
        prev_s = s - 1
        for k in range(s, n + 1):
            if k < 2:
                continue
            dp[s][k] = min(dp[prev_s][k - 1] + (s != k), 
                           dp[s][k - 1] + 1)

    return dp[m][n]

print(min_replants())
