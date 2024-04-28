import sys

def calculate_max_distance():
    v, w = map(int, input().split())
    t, k = map(int, input().split())

    dp = [[0] * (w+1) for _ in range(t+1)]

    for i in range(1, t+1):
        for j in range(v, w+1):
            if j >= v and abs(j-v) <= k:
                dp[i][j] = max(dp[i-1][v] + (j - v), dp[i-1][j] + (w - j))
            else:
                dp[i][j] = dp[i-1][j]

    return dp[t][w]

print(calculate_max_distance())
