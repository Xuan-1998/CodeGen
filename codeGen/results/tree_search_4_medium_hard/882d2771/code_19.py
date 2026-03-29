=Begin Code=
import sys

t, l, r = map(int, input().split())

mod = 10**9 + 7

dp = [0] * (r + 1)
for i in range(2, r + 1):
    dp[i] = min(dp[j] + 1 for j in range(i))

ans = 0
for i in range(r, l - 1, -1):
    ans += t * (dp[i] - dp[i-1])
    ans %= mod

print(ans)
=End Code=
