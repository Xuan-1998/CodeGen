def count_stable_tables():
    T = int(input())
    MOD = 10**9 + 7
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        
        # Base case: number of ways to fill a row of sum 0 is 1 if the sum is less than or equal to M
        for j in range(M + 1):
            dp[0][j] = 1 if j <= M else 0
        
        # Fill up the dynamic programming table
        for i in range(1, N + 1):
            for j in range(M + 1):
                if j <= M:
                    dp[i][j] += dp[i-1][M - j]
                else:
                    for k in range(j+1):
                        dp[i][j] += dp[i-1][k] * (M-k) // (i+1)
        
        # Calculate the final answer
        ans = sum(dp[N][j] for j in range(M + 1)) % MOD
        print(ans)

count_stable_tables()
