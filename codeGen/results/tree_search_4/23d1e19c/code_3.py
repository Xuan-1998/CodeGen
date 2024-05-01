def solve(s, t, p):
    n, m = len(p), len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize base case
    dp[0][k] = 0

    # Iterate through each vertex and choice
    for i in range(s-1, t+1):
        for j in range(k+1):
            if p[i] == i:
                dp[i][j] = min(dp[i][j], dp[s-1][j-1])
            else:
                dp[i][j] = min(dp[i][j-1], 1 + dp[t][k-j-1])

    # Return the minimum and maximum number of recomputations
    return dp[t][k-1]
