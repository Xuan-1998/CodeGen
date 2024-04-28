def numPaths(arr, K, N):
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    # Base case: number of ways to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    dp[N-1][N-1] = int(arr[0][0] == K)

    # Fill up the DP table
    for i in range(N):
        for j in range(N):
            if i > 0 and j > 0:
                # Count number of ways to reach cell (i, j) with exactly K coins
                dp[i][j] = sum((dp[i-1][j], dp[i][j-1])) * int(arr[i][j] <= K)
            elif i == N-1 and j > 0:
                # Count number of ways to reach cell (N-1, j) with exactly K coins
                dp[i][j] = sum((dp[i][j-1],)) * int(arr[N-1][j] <= K)
            elif j == N-1 and i > 0:
                # Count number of ways to reach cell (i, N-1) with exactly K coins
                dp[i][j] = sum((dp[i-1][N-1],)) * int(arr[i][N-1] <= K)
            else:
                dp[i][j] = 0

    # Return the number of ways to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    return sum((dp[0][N-1],))

# Example usage
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(numPaths(arr, K, N))
