def findPaths(arr, N, K):
    dp = [[0]*N for _ in range(N)]
    
    # Initialize the first row
    for j in range(N):
        if arr[0][j] <= K:
            dp[0][j] = 1
    
    # Fill the rest of the table using dynamic programming
    for i in range(1, N):
        for j in range(N):
            if arr[i][j] <= K:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if i > 0 and j > 0 else (dp[i-1][j] if i > 0 else dp[i][j-1])
    
    # Count the number of paths that collect exactly K coins
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[N-1-i][N-1-j] <= K:
                count += dp[N-1-i][N-1-j]
    
    return count

# Example usage:
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(findPaths(arr, N, K))
