def findPaths(arr):
    N = len(arr)
    K = int(input())
    
    # Initialize DP table with zeros
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]
    
    # Base case: the last cell is reached when we collect exactly K coins
    dp[N-1][N-1][K] = 1 if arr[N-1][N-1] >= K else 0
    
    # Fill the DP table from bottom to top and right to left
    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            # If we have enough coins in this cell
            if arr[i][j] >= K:
                dp[i][j][K] = 0
                if i < N-1 and dp[i+1][j][K-arr[i][j]] > 0:
                    dp[i][j][K] += dp[i+1][j][K-arr[i][j]]
                if j < N-1 and dp[i][j+1][K-arr[i][j]] > 0:
                    dp[i][j][K] += dp[i][j+1][K-arr[i][j]]
            # If we don't have enough coins in this cell
            else:
                dp[i][j][K] = 0
    
    return sum(sum(row[K]) for row in dp[0])

print(findPaths([[5,3], [2,8]]))
