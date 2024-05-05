def steady_tables(n, m):
    MOD = 1000000000

    dp = [[[0] * (M+1) for _ in range(M+1)] for _ in range(N+1)]

    # Base case: when n is 0, there's only one way to fill the table
    for j in range(M+1):
        dp[0][j][0] = 1

    # Fill up the dp array using dynamic programming and memoization
    for i in range(1, N+1):
        for k in range(i+1):
            if k == 0:
                dp[i][k][M-k] = dp[i-1][M-k][M-k]
            else:
                for j in range(k, M+1):
                    dp[i][j][k] = (dp[i-1][j-1][k-1] + dp[i-1][M-j][k]) % MOD

    # Calculate the number of different steady tables
    return sum(dp[-1][-1]) % MOD


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_tables(N, M))
