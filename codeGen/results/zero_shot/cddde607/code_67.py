def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
                else:
                    dp[i][j][K] = 0
            elif i > 0:
                if dp[i-1][j][K-arr[i][j]]:
                    dp[i][j][K] += 1
            elif j > 0:
                if dp[i][j-1][K-arr[i][j]]:
                    dp[i][j][K] += 1

    return dp[-1][-1][K]
