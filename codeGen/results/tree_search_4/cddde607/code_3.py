code = \\
def numPaths(arr):
    K, N = map(int, input().split())
    dp = [[0]*N for _ in range(N)]
    
    # initialize
    dp[0][0] = 1
    
    for i in range(1, N):
        for j in range(1, N):
            if arr[i][j] > K:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return sum([dp[N-1][j] for j in range(N) if arr[N-1][j] == K])
