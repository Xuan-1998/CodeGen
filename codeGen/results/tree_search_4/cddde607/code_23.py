def numPathsWithKCoins(N, arr, K):
    dp = [[0]*N for _ in range(N)]
    
    # base case: only one way to collect 0 coins from the top-left corner
    dp[0][0] = 1
    
    for i in range(1, N):
        if arr[i-1][0] <= K:
            dp[i][0] += dp[i-1][0]
    
    for j in range(1, N):
        if arr[0][j-1] <= K:
            dp[0][j] += dp[0][j-1]
    
    for i in range(1, N):
        for j in range(1, N):
            # calculate the number of ways to reach cell (i, j) collecting exactly K coins
            if arr[i-1][j-1] <= K:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
    
    return dp[N-1][N-1]

# Example usage
K = int(input())  # number of coins to collect
N = int(input())  # size of the matrix
arr = [[int(x) for x in input().split()] for _ in range(N)]
print(numPathsWithKCoins(N, arr, K))
