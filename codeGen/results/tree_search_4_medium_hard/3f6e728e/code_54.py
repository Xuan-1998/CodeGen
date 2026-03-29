from math import comb
MOD = 10**9 + 7

def solve(N, M, C):
    dp = [0] * (C+1)
    dp[0] = 1
    for i in range(1, C+1):
        for j in range(max(1, i-M+1), i):
            dp[i] += dp[j-1] * comb(N-j, M-i) % MOD
        dp[i] %= MOD
    return [str(int(x)) for x in dp[1:]]

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    print(' '.join(solve(N, M, C)))
