def num Paths(arr):
    N = len(arr)
    K = int(input())
    
    # Create a 2D DP table where each cell dp[i][j] represents the number of ways to reach cell (i, j) with exactly K coins.
    dp = [[0]*N for _ in range(N)]
    
    # Base case: when i == N-1 and j == N-1
    if arr[N-1][N-1] == K:
        dp[N-1][N-1] = 1
    else:
        dp[N-1][N-1] = 0
    
    # Fill up the DP table from cell (N-1, N-1) to cell (0, 0)
    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            if arr[i][j] <= K:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
            else:
                dp[i][j] = 0
    
    # Return the number of ways to reach cell (0, 0) with exactly K coins
    return dp[0][0]

# Example usage:
arr = [[3, 2, 1], [4, 3, 2], [5, 6, 7]]
print(numPaths(arr))
