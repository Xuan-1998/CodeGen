def count_paths(arr, K, N):
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[0][0] <= K:
                    dp[i][j][arr[0][0]] = 1
            elif i == 0:
                if arr[i][j] + dp[i][j-1][K-arr[i][j]].sum() > 0:
                    dp[i][j][:].fill(0)
                    for k in range(K+1):
                        if k <= K-arr[i][j]:
                            dp[i][j][k] = dp[i][j-1][k-arr[i][j]].sum()
            elif j == 0:
                if arr[i][j] + dp[i-1][j][K-arr[i][j]].sum() > 0:
                    dp[i][:].fill(0)
                    for k in range(K+1):
                        if k <= K-arr[i][j]:
                            dp[i][k] = dp[i-1][k-arr[i][j]].sum()
            else:
                if arr[i][j] + dp[i-1][j][K-arr[i][j]].sum() > 0 and arr[i][j] + dp[i][j-1][K-arr[i][j]].sum() > 0:
                    for k in range(K+1):
                        if k <= K-arr[i][j]:
                            dp[i][j][k] = dp[i-1][j][k-arr[i][j]].sum() + dp[i][j-1][k-arr[i][j]].sum()
    return sum(sum(row) for row in dp[-1])
