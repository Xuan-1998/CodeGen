def numPaths(arr, K):
    N = len(arr)
    
    # Initialize dp table
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    # Fill up the dp table
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[0][0] <= K:
                    dp[i][j][K - arr[0][0]] = 1
                else:
                    dp[i][j][0] = 1
            elif i == 0:
                for k in range(arr[0][j], K + 1):
                    dp[i][j][k] = dp[i][j][k-arr[0][j]]
            elif j == 0:
                for k in range(arr[i][0], K + 1):
                    dp[i][j][k] = dp[i-1][j][k-arr[i][0]]
            else:
                for k in range(K, -1, -1):
                    if arr[i][j] <= k:
                        dp[i][j][k] = dp[i-1][j][k-arr[i][j]] + dp[i][j-1][k-arr[i][j]]
    
    return sum([dp[N-1][N-2][k] for k in range(K+1) if k <= K])

# Example usage
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(numPaths(arr, K))
