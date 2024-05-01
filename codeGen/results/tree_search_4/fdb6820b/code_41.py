import sys

def solve(m, N):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(i, N + 1):
            dp[j] += dp[j - i]
    return dp[N]

m, N = map(int, input().split())
print(solve(m, N) % (10**9 + 7))
