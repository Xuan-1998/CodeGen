def numPathsWithExactlyKCoins(arr):
    N = len(arr)
    K = int(input())
    
    # Create a 2D DP table to store the results of subproblems
    dp = [[0] * (N) for _ in range(N)]
    
    # Base case: only one path from cell (0, 0) with exactly K coins
    dp[0][0] = int(arr[0][0] == K)
    
    # Fill up the DP table using tabulation
    for i in range(1, N):
        for j in range(N):
            if j > 0:
                dp[i][j] += dp[i-1][j]
            if i > 0:
                dp[i][j] += dp[i][j-1]
            if i > 0 and j > 0:
                dp[i][j] += dp[i-1][j-1]
            
            # Update the DP table with the number of coins in the current cell
            dp[i][j] *= (arr[i][j] <= K)
    
    return dp[N-1][N-1]
