def numPathsWithExactlyKCoins(N, K, arr):
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = dp[i-1][j][K-arr[i][j]] + dp[i][j-1][K-arr[i][j]]
            elif j > 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = dp[i][j-1][K-arr[i][j]]

    return dp[0][0][K]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPathsWithExactlyKCoins(N, K, arr))
