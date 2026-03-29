def steady_table_count(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: only one way to fill an empty table
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(M + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j]
            elif j <= M:
                # Calculate the number of ways to fill the current cell
                # considering all possible sums up to i
                for k in range(j, -1, -1):
                    dp[i][j] += dp[i - 1].count(k)
    
    return dp[N][M]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_table_count(N, M) % (10**9 + 7))
