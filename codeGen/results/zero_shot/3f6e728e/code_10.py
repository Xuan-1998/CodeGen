import sys

def solve(N, M, C, U, L):
    MOD = 10**9 + 7
    dp = [0] * (C + 1)
    dp[0] = 1

    for r in U:
        for i in range(r, C + 1):
            dp[i] += dp[i - 1]
            if i >= r:
                dp[i] -= dp[i - r]
            dp[i] %= MOD

    for r in L:
        for i in range(C, r - 1, -1):
            dp[i] += dp[i - 1]
            if i >= r:
                dp[i] -= dp[i - r]
            dp[i] %= MOD

    return [str(dp[i]) for i in range(C + 1)]

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    print(*solve(N, M, C, U, L), sep=' ')
