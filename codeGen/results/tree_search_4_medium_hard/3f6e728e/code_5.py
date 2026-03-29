import sys

dp = [0] * (C + 1)
dp[0] = 1  # base case: there is one way to build an empty sequence

for u in upper_hemispheres:
    for i in range(u, C + 1):
        dp[i] += dp[i - u]

for l in lower_hemispheres:
    for i in range(l, C + 1):
        dp[i] = (dp[i] + dp[i - l]) % mod

print(*dp[1:], sep=' ')
