===BEGIN CODE===
import sys
t, l, r = map(int, input().split())

dp = [0] * (r - l + 1)
for i in range(2, l):
    dp[i-1] += dp[i-2] + 1

ans = t
for i in range(l - 1, r):
    ans -= i
    if i >= l:
        ans += dp[i-l]
ans %= (10**9 + 7)

print(ans)
