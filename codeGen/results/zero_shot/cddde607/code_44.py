def count_paths(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0 and j > 0:
                dp[i][j][:] = [sum(dp[i-1][j][:k+1]) + sum(dp[i][j-1][:k+1]) for k in range(K+1)]
            elif i > 0:
                dp[i][:, 0] = dp[i-1][:, :K+1]
            else:
                dp[:, 0] = dp[:-1, :K+1]
    
    return sum(dp[-1][-1][k] for k in range(K+1) if k == K)
