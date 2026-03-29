import sys

# Define the modulo value
MOD = 1e9 + 7

def solve(t, l, r):
    f = [0] * (r - l + 1)
    for i in range(r - l):
        f[i + 1] = min(f[i + 1], f[i] + t)

    dp = [0] * (l + 1)
    for i in range(l, r + 1):
        dp[i - l] = min(dp[j - l] + t * (f[i - l]) for j in range(i))
    return dp[r - l]

t, l, r = map(int, input().split())
print(solve(t, l, r) % MOD)
