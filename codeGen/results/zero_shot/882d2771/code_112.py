import sys

t, l, r = map(int, input().split())
mod = 10**9 + 7

def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[:i])
    return sum(range(l, r + 1))

print((t*sum(f(i) for i in range(l, r + 1)) - l*f(r)) % mod)
