def count_ways(arr, N, K):
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(N+1):
            if i == 0 and j == 0:  # base case
                if arr[0][0] <= K:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            elif i > 0 and j > 0:  # recurrence relation
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if arr[i][j] <= K:
                    dp[i][j] += (dp[i-1][j] if i > 0 else 0) * (K - arr[i][j])
            elif i > 0:  # only move down
                dp[i][j] = dp[i-1][j]
            elif j > 0:  # only move right
                dp[i][j] = dp[i][j-1]

    return dp[N][N]
