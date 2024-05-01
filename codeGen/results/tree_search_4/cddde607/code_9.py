def numPathsWithExactlyKCoins(K, N, arr):
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    # Base case: If we're at the top-left corner, 
    # there's only one way to reach it if K is equal to arr[0][0], otherwise there are no ways
    dp[0][0] = 1 if arr[0][0] == K else 0
    
    for i in range(1, N):
        for j in range(N):
            # If we're not at the top-left corner and 
            # we have coins left to collect (K >= arr[i][j]), 
            # then we can move down or right
            if K >= arr[i][j]:
                dp[i][j] = sum(dp[i-1][k]) + sum(dp[k][j-1]) for k in range(N)
            else:
                dp[i][j] = 0
    
    return dp[N-1][N-1]
