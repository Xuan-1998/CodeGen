import sys

n = int(input())
s = input()

dp = [0] * (n + 1)
for i in range(1, n + 1):
    if s[i - 1] == '+':
        dp[i] = min(dp[i - 1], 1) + dp[i - 1]
    else:
        dp[i] = max(0, dp[i - 1] - 1)

print(dp[-1])
