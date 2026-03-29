import sys

n = int(input())
t = float(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], round(t, i) - dp[i - 1])

print(int(round(t, 0) + dp[n]))
