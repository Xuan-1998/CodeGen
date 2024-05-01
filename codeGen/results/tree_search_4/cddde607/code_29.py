def numPaths(K, N, coins):
    dp = [[0] * (N) for _ in range(N)]
    
    # Base case: If i or j is zero, return 0 because there's no way to reach the destination
    for i in range(N):
        for j in range(N):
            if i == 0:
                dp[i][j] = 1 if coins[j] <= K and j < N else 0
            elif j == 0:
                dp[i][j] = 1 if coins[i] <= K and i < N else 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Fill up dp[][] table in top-down manner
    for i in range(1, N):
        for j in range(1, N):
            if coins[i+j-2] <= K:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
    
    # Return the result as the number of possible paths that collect exactly K coins
    return dp[N-1][N-1]

# Receive inputs from stdin and print the answer to stdout
K, N = map(int, input().split())
coins = list(map(int, input().split()))
print(numPaths(K, N, coins))
