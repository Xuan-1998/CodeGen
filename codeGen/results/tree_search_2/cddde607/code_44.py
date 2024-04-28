def numPathsWithKCoins(K, N, arr):
    # Create a 2D DP table with (N+1) x (N+1) size
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Base case: when i == N-1 and j == N-1
    if arr[N - 1][N - 1] <= K:
        dp[N - 1][N - 1] = 1

    # Fill up the DP table in a top-down manner
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if i == N - 1 and j == N - 1:
                continue
            elif i < N - 1:
                dp[i][j] += dp[i + 1][j]
            elif j < N - 1:
                dp[i][j] += dp[i][j + 1]

            # If the current cell has coins, add its value to the DP table
            if i < N - 1 and arr[i][j] <= K:
                if i == N - 2:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j])
                elif j > 0:
                    dp[i][j] += dp[i][j - 1]

    # Return the value at the top-left corner (i.e., the number of paths with exactly K coins)
    return dp[0][0]
