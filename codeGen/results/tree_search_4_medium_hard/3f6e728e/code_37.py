def solve():
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    MOD = 10**9 + 7

    dp = [[0] * (M + 1) for _ in range(C + 1)]

    dp[0][0] = 1
    for i in range(1, C + 1):
        for j in range(min(i, M) + 1):
            for k in range(1, min(i, C) + 1):
                if k <= U[j]:
                    dp[i][j] += dp[max(0, i - k)][min(j, len(U) - 1)]
                    dp[i][j] %= MOD
                if k <= L[j]:
                    dp[i][j] += dp[max(0, i - k)][min(j, len(L) - 1)]
                    dp[i][j] %= MOD

    print(*dp[C], sep=' ')
