def steady_tables(N, M):
    MOD = 10**9 + 7

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(M + 1):
            if i == 1:
                dp[i][j] = 1
            else:
                total_sum = min(j, M)
                for k in range(total_sum, -1, -1):
                    dp[i][j] += dp[i-1][k]
                    if j < k: break
                dp[i][j] %= MOD

    return dp[N][M]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_tables(N, M))
