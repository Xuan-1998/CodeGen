def steady_tables(N, M):
    MOD = 1_000_000_000
    dp = [[[0] * (M + 1) for _ in range(M + 1)] for _ in range(N + 1)]
    
    # Initialize base case: filling an empty table has one way
    for j in range(M + 1):
        dp[0][j][0] = 1
    
    # Fill dp array using dynamic programming
    for n_rows in range(1, N + 1):
        for max_sum in range(M + 1):
            for j in range(min(n_rows, M) + 1):
                if j > 0:
                    for k in range(min(max_sum, j)):
                        dp[n_rows][j][max_sum] += (dp[n_rows - 1][j - 1][k] % MOD)
                    dp[n_rows][j][max_sum] %= MOD
    
    return sum(dp[N][M]) % MOD

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_tables(N, M))
