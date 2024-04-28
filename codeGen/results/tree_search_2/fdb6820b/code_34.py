import sys

def solve(A, N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for a in A:
        for i in range(N, a - 1, -1):
            dp[i] += dp[i - a]
            if dp[i] >= MOD:
                dp[i] %= MOD
    return dp[N]

m, N = map(int, input().split())
A = list(map(int, input().split()))
print(solve(A, N))
