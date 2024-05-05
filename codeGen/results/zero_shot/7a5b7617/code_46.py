def steady_table_count():
    T = int(input())
    MOD = 1000000000

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(i, M + 1):
            dp[i][j] = (dp[i - 1][j - 1] + MOD) % MOD

    total_count = 0
    for i in range(N + 1):
        total_count += dp[i][M]
    print(total_count % MOD)

steady_table_count()
