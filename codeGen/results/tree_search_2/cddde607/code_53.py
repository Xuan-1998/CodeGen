def findPaths(N, K, arr):
    # Create a 2D DP table
    dp = [[0] * (K + 1) for _ in range(N)]

    # Initialize the base case: if we're at the last cell and have collected exactly K coins, there's one way to get here
    dp[N-1][K] = 1

    # Fill up the DP table iteratively
    for i in range(N-2, -1, -1):
        for j in range(K+1):
            if arr[i][j] > 0:  # If there are coins in this cell
                if i < N-1:
                    dp[i][j] += dp[i+1][j]
                if j < K:
                    dp[i][j] += dp[i][j+1]
            else:
                if i < N-1:
                    dp[i][j] = dp[i+1][j]
                if j < K:
                    dp[i][j] = dp[i][j+1]

    # The number of paths that collect exactly K coins is stored in the top-left cell
    return dp[0][K]

# Example usage:
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(findPaths(N, K, arr))
