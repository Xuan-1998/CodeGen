def numPaths(arr, N, K):
    dp = [[0 for _ in range(K+1)] for _ in range(N)]

    # Base case: there is only one way to collect 0 coins from any cell.
    for i in range(N):
        dp[i][0] = 1

    for i in range(1, N):
        for j in range(1, min(i+1, K)+1):
            if arr[i-1][j-1] > 0:
                # If there are coins at the current cell, add the number of ways to collect
                # the remaining coins from the top or left cell.
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                # If there are no coins at the current cell, we can only move from above.
                dp[i][j] = dp[i-1][j]

    return dp[N-1][K]

# Example usage
N = int(input())
K = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(numPaths(arr, N, K))
