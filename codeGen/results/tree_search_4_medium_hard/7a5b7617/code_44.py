def count_stable_tables(N, M):
    MOD = 10**9 + 7
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for j in range(M + 1):
        dp[0][j] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            total_sum = sum(range(i)) * (M - j + 1)
            if total_sum <= M:
                for k in range(j + 1):
                    dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD

    return sum(dp[N]) % MOD

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_stable_tables(N, M))
