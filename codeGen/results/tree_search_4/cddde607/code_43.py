def numPaths(arr, K):
    N = len(arr)
    
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    
    # Base case: If there are no more coins to collect (k == 0), then there's only one path if the current cell is the bottom-right corner, and no paths otherwise.
    dp[0][0][0] = 1
    
    for k in range(K+1):
        for i in range(N):
            for j in range(N):
                if k > arr[i][j]:
                    dp[i][j][k] = dp[i][j][max(k-arr[i][j], 0)]
                elif i == N - 1 and j == N - 1:
                    dp[i][j][k] = 1
                else:
                    # Consider two possibilities: Move down or move right.
                    if i < N - 1:
                        dp[i][j][k] += dp[i+1][j][max(k-arr[i][j], 0)]
                    if j < N - 1:
                        dp[i][j][k] += dp[i][j+1][max(k-arr[i][j], 0)]
    
    return dp[0][0][K]
