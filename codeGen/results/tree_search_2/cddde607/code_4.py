def numPathsWithExactlyKCoins(K, N, arr):
    dp = [[0] * (N) for _ in range(N)]

    # Base case: count the number of ways to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                dp[i][j] = 1 if arr[i][j] <= K else 0
            elif i < N - 1 and j < N - 1:
                # If the current cell has more coins than the target K, skip it
                if arr[i][j] > K:
                    continue
                dp[i][j] = (dp.get((i-1), [0])[0] if i > 0 else 0) + (dp.get((j-1), [0])[0] if j > 0 else 0)
            elif i < N - 1:
                # Move down
                dp[i][j] = dp.get((i-1), [0])[0]
            elif j < N - 1:
                # Move right
                dp[i][j] = dp.get((j-1), [0])[0]

    return dp[N-1][N-1]
