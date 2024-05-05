def steady_table_count(N, M):
    MOD = 10**9 + 7
    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, min(i, M)+1):
            if i == 1:
                dp[i][j] = j
            else:
                dp[i][j] = (dp[i-1][j-1] + j) % MOD
    total = 0
    for i in range(N+1):
        total += dp[i][M]
        total %= MOD
    return total

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_table_count(N, M))
