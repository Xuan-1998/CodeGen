import sys

t, l, r = map(int, input().split())
mod = 10**9 + 7

dp = [0] * (r - l + 1)
for i in range(2, r - l + 1):
    dp[i] = min(dp[i-1] + 1, dp[i//2] + 1 if i % 2 == 0 else dp[(i+1)//2] + 1)

result = t * (dp[r] - dp[l-1]) % mod
print(result)
