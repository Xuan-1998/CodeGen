def steady_tables(N, M):
    MOD = 1000000000

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            if j < M // 2:
                for k in range(j + 1):
                    dp[i][j] += dp[k][M - 1 - k]
            else:
                for k in range(N - i + 1):
                    dp[i][j] += dp[k][M - 1 - k]

    return dp[N][M] % MOD

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_tables(N, M))
