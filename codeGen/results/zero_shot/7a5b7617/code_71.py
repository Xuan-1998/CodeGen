def count_steady_tables(N, M):
    MOD = 1000000000
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(min(i, M) + 1):
            for k in range(j + 1):
                if (i == 1 and j == k) or (k <= j - 1):
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD

    return sum(dp[-1]) % MOD

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_steady_tables(N, M))
