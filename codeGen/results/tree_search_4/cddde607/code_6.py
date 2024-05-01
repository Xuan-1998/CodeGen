def numPaths(k, n, arr):
    # Initialize the dp table
    dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]

    # Base case: there is only one way to reach 0 coins from any cell
    for i in range(n):
        for j in range(n):
            dp[i][j][0] = 1

    # Fill up the table from top to bottom and left to right
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k:
                continue
            if i < n-1:
                dp[i][j][arr[i][j]+1] += dp[i+1][j][arr[i][j]]
            if j < n-1:
                dp[i][j][arr[i][j]+1] += dp[i][j+1][arr[i][j]]

    # Return the total number of paths collecting exactly k coins
    return dp[0][0][k]
