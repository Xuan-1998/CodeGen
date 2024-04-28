def numPaths(arr):
    N = len(arr)
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    # Base case: the bottom right corner
    dp[N-1][N-1][K] = 1 if arr[N-1][N-1] == K else 0

    # Fill up the DP table
    for i in range(N):
        for j in range(N):
            for k in range(K+1):
                # If we are at the bottom row, only move right
                if i == N-1:
                    if arr[i][j] <= k and (k - arr[i][j]) >= 0:
                        dp[i][j][k] = sum(dp[i][j-1][k-coin] for coin in range(min(k+1, K)+1))
                # If we are at the rightmost column, only move down
                elif j == N-1:
                    if arr[i][j] <= k and (k - arr[i][j]) >= 0:
                        dp[i][j][k] = sum(dp[i-1][j][k-coin] for coin in range(min(k+1, K)+1))
                # If we are not at the border, move both down and right
                else:
                    if arr[i][j] <= k and (k - arr[i][j]) >= 0:
                        dp[i][j][k] = sum(dp[i-1][j][k-coin] for coin in range(min(k+1, K)+1)) + sum(dp[i][j-1][k-coin] for coin in range(min(k+1, K)+1))

    # Return the number of valid paths
    return sum(dp[0][0][K])
