import sys

def steady_tables(N, M):
    # Initialize dp array with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Base case: only one way to create a table of size 1 x 1
    dp[1][1] = 1

    # Fill up the dp array using dynamic programming
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            if j <= M:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][M]

    # Return the answer
    return dp[N][M]
