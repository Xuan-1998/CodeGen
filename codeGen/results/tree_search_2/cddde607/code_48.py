def num_paths_to_collect_k_coins(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0:
                if arr[i-1][j] <= K:
                    dp[i][j][K-arr[i-1][j]] += 1
            elif j > 0:
                if arr[i][j-1] <= K:
                    dp[i][j][K-arr[i][j-1]] += 1
    
    return sum(sum(row) for row in dp[-1])
