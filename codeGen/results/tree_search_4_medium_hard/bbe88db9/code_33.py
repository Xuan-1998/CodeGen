import sys

n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = min(dp[i-1], 1 + dp[p[i-1]])
    else:
        dp[i] = min(dp[i-1], 1 + dp[2*p[i-1]+p[i-1]])

print((dp[n]) % (10**9 + 7))
