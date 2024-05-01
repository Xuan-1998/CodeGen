def numPaths(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    
    # Base case: only one way to reach top-left corner
    dp[0][0] = 1
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0]
        
    for j in range(1, n):
        dp[0][j] = dp[0][j-1]
        
    for i in range(1, n):
        for j in range(1, n):
            # If K coins have been collected, then there are no more ways to collect
            if arr[i][j] > k:
                dp[i][j] = 0
            else:
                # Consider two cases: coming from top or left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[n-1][n-1]

k, n, arr = map(int, input().split())
print(numPaths(arr))
