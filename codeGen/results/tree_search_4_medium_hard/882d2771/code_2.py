import sys

t, l, r = map(int, input().split())
mod = 10**9 + 7
dp = [0] * (r + 1)

for n in range(2, r + 1):
    if n % 2 == 1:
        dp[n] = min(dp[i] + dp[n - i - 1] for i in range(min(n // 2, l), max(n // 2, l) + 1))

print(sum(t * (dp[i] + i) for i in range(l, r + 1)) % mod)
