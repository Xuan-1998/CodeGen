import sys
input = lambda: [int(x) for x in input().split()]

def solve():
    T = int(input())
    MOD = 10**9 + 7

    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(M+1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][0]
            elif i == 0 and j > 0:
                dp[i][j] = dp[0][j-1]
            else:
                dp[i][j] = (dp[i-1][0] + dp[0][j-1]) % MOD

    for _ in range(T):
        N, M, C = input()
        for i in range(C+1):
            print(dp[N][M])
