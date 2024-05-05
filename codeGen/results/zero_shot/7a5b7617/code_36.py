def count_steady_tables():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if i == 1:
                    dp[i][j] = min(j, M)
                else:
                    dp[i][j] = sum(dp[i-1][:j+1]) % (10**9 + 7)
        print(dp[N][M])

count_steady_tables()
