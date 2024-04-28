def numPathsToCollectExactlyKCoins(K, N, arr):
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == 1 and j == 1:
                if arr[0][0] <= K:
                    dp[i][j] = 1
            elif i > 1 or j > 1:
                if arr[i-1][j-1] <= K:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[N][N]

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(numPathsToCollectExactlyKCoins(K, N, arr))
