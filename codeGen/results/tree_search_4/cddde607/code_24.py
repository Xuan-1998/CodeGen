def find_paths(arr, N, K):
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Initialize the first row and column
    for i in range(1, N+1):
        dp[0][i] = 0
        dp[i][0] = 0
    
    # Fill up the dp table using bottom-up approach
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i-1][j-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + (arr[i-1][j-1] == K)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[N][N]

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(find_paths(arr, N, K))
