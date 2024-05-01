def findPathsToCollectKCoins(K, N, arr):
    # Create a 2D table to store the intermediate results
    dp = [[0] * (N+1) for _ in range(N+1)]

    # Fill the dp[][] table from top-down manner with memoization
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = arr[0][0]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j]
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j-1]
            else:
                # Calculate the number of ways to reach this cell
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[N-1][N-1]

# Read input from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# Calculate the result and print it to stdout
print(findPathsToCollectKCoins(K, N, arr))
