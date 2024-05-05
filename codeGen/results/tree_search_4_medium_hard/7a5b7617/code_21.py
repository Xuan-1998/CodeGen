def num_steady_tables(N, M):
    MOD = 10**9 + 7

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if j > 0:
                dp[i][j] = (dp[i-1][j-1] * (i * j) % MOD + 1) % MOD
            else:
                dp[i][j] = 1

    return sum(dp[-1]) % MOD

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(num_steady_tables(N, M))
