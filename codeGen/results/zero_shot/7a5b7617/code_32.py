def count_steady_tables():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        total_sum = N * (N + 1) // 2
        for i in range(1, N + 1):
            dp[i][1] = min(total_sum, M)
            for j in range(2, M + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        print(dp[N][M] % (10**9 + 7))

count_steady_tables()
