def dp_tables(N, M):
    MOD = 10**9 + 7

    # Create a 2D array to store the memoized states
    dp = [[0] * (M+1) for _ in range(N+1)]

    # Base case: The number of different steady tables of size (1, j) where j is the current column is simply 1.
    for j in range(M+1):
        dp[1][j] = 1

    # Fill up the table using dynamic programming
    for i in range(2, N+1):
        for j in range(M+1):
            for k in range(j+1):
                if k <= M and (k == 0 or k + 1 > dp[i-1][j-k]):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD
    return dp[N][M]

# Read input from stdin
T = int(input())

# Solve each test case and print the result to stdout
for _ in range(T):
    N, M = map(int, input().split())
    print(dp_tables(N, M))
