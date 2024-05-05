import sys

t, l, r = map(int, input().split())
dp = [0] * (r + 1)
dp[1] = 1

for i in range(2, r + 1):
    dp[i] = 1 + min((j - 1) + dp[j - 1] for j in range(2, i + 1))

print(((t0 * dp[l]) + (t1 * dp[l + 1]) + ... + (tr * dp[r])) % (10**9 + 7))
