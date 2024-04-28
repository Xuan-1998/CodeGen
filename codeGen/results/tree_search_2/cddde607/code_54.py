def numPaths(arr, K):
    n = len(arr)
    
    # Initialize dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: only one way to reach bottom-right corner with exactly K coins
    dp[n-1][n-1] = arr[n-1][n-1] == K
    
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if (i, j) != (0, 0):
                # Transition relation: sum of ways to reach cells above and to the left
                dp[i][j] = arr[i][j] == K or (dp[i-1][j] + dp[i][j-1]) % 2
            else:
                dp[i][j] = arr[i][j] == K
    
    return dp[0][0]
