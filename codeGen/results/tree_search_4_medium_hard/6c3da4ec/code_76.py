import sys

# Read input from stdin
n = int(input())
s = input()

dp = [0] * (n + 1)
max_or = 0

for i in range(n):
    if s[i] == '1':
        dp[i + 1] = max(dp[i], dp[i // 2] + 1) if i % 2 else max(dp[i], dp[(i - 1) // 2] + 1)
    else:
        dp[i + 1] = max(dp[i], dp[i // 2])
    max_or = max(max_or, dp[i + 1])

print(bin(max_or)[2:].zfill(n).lstrip('0'))
