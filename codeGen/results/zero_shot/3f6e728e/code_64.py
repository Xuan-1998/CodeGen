import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = 1

        for i in range(N + 1):
            for j in range(M + 1):
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
                if i > 0 and j > 0:
                    for k in range(min(i, j)):
                        if U[k] >= L[j - 1]:
                            dp[i][j] += dp[i - 1][k]

        print(*[str(dp[i][M]) % (10 ** 9 + 7) for i in range(N + 1)], sep=' ')

solve()
