def findPaths(N, K, arr):
    # Initialize a 3D table dp[][][] to store intermediate results
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Base case: Top-left corner with k coins
    dp[0][0][0] = arr[0][0]

    # Fill up the dp table
    for i in range(N):
        for j in range(N):
            if i > 0:
                dp[i][j][0] += dp[i - 1][j][0]
            if j > 0:
                dp[i][j][0] += dp[i][j - 1][0]

    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                # Count the number of paths collecting exactly k coins
                if i > 0:
                    dp[i][j][k] += dp[i - 1][j][k]
                if j > 0:
                    dp[i][j][k] += dp[i][j - 1][k]

    return dp[0][0][K]
