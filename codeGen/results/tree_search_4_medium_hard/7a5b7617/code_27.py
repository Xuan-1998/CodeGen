def count_stable_tables(N, M):
    MOD = 10**9 + 7

    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 1

    for j in range(1, M+1):
        for i in range(1, N+1):
            dp[i][j] = (sum(dp[k][M-k-1] for k in range(i)) % MOD) + dp[i-1][j]

    return dp[N][M]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_stable_tables(N, M))
