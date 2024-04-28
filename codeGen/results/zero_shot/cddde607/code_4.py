def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[0][0] <= K:
                    dp[i][j][arr[0][0]] = 1
                else:
                    dp[i][j][K] = 0
            elif i == 0:
                if j > 0 and arr[i][j-1] + arr[i][j] <= K:
                    dp[i][j][arr[i][j]] += dp[i][j-1][K - arr[i][j]]
            elif j == 0:
                if i > 0 and arr[i-1][j] + arr[i][j] <= K:
                    dp[i][j][arr[i][j]] += dp[i-1][j][K - arr[i][j]]
            else:
                if i > 0 and j > 0 and arr[i-1][j] + arr[i][j] <= K:
                    dp[i][j][arr[i][j]] += dp[i-1][j][K - arr[i][j]]
                elif i > 0 and j > 0 and arr[i][j-1] + arr[i][j] <= K:
                    dp[i][j][arr[i][j]] += dp[i][j-1][K - arr[i][j]]
    return sum(sum(row[K]) for row in dp[-1])
