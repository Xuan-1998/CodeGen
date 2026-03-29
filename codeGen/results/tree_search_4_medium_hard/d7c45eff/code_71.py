import sys

k = int(input())
s = input().strip()

dp = ['' for _ in range(k + 1)]

for i in range(1, k + 1):
    if s[i - 1] == s[-1]:
        dp[i] = min(dp[i - 1], dp[i - 1] + s[-1])
    else:
        dp[i] = dp[i - 1]

print(min(dp[k], dp[k - 1] + s[-1]))
