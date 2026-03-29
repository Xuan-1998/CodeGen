import sys

mod = 1e9 + 7

def solve():
    T = int(input())
    dp = [[0] * (2**18+1) for _ in range(2003)]

    dp[0][0] = 1
    for N in range(1, 2003):
        for M in range(2**18 + 1):
            if M > 0:
                for k in range(M // 2 + 1):
                    dp[N][M] += dp[N-1][k]
                    if dp[N][M] >= mod: 
                        dp[N][M] %= mod
            else:
                dp[N][M] = dp[N-1][0]

    for _ in range(T):
        N, M = map(int, input().split())
        print(dp[N][M])

solve()
