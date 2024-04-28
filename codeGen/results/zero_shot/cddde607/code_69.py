def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[0][0]
            elif i > 0:
                dp[i][j][0] += dp[i-1][j][0]
            elif j > 0:
                dp[i][j][0] += dp[i][j-1][0]
            else:
                continue
            if i > 0 and j > 0:
                for k in range(1, min(i+1, j+1)+1):
                    dp[i][j][k] = max(dp[i-k][j][k-1], dp[i][j-k][k-1])
            else:
                dp[i][j][K] = 1
    return sum([sum(row) for row in dp[-1][-1]])
