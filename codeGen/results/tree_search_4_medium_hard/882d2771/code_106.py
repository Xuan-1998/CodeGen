import sys

MOD = 10**9 + 7

dp = {}

def f(n):
    if n in dp:
        return dp[n]
    if n == 1:
        return n - 1
    res = float('inf')
    for k in range(2, n+1):
        res = min(res, f(k) + (n-k))
    dp[n] = res
    return res

t, l, r = map(int, input().split())
ans = 0
for i in range(t):
    ans += pow(2, i, MOD) * (f(l+i) - l)
print(ans % MOD)
