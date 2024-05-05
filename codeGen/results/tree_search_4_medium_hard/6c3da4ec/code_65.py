import sys

n = int(input())
s = input()

dp = [0] * (n + 1)
max_or = 0

for i in range(1, n + 1):
    if s[i - 1] == '1':
        dp[i] = max(dp[i - 1], dp[i - 2] + 1 if i >= 2 else 1) if i > 1 else 1
        max_or = max(max_or, dp[i])
    else:
        dp[i] = dp[i - 1]

print(bin(max_or)[2:].zfill(n).lstrip('0'))
