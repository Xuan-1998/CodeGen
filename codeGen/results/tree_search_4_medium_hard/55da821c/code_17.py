from math import inf

def min_replants(n, m):
    # Create the 2D array dp[] of size (m+1) x (n+1)
    dp = [[inf] * (n + 1) for _ in range(m + 1)]

    for i in range(0, m + 1):
        dp[i][0] = i

    for j in range(1, n + 1):
        for i in range(1, min(j, m) + 1):
            # Check if the current species is different from the last one
            if i != (j // (m + 1)) + 1:
                dp[i][j] = min(dp[max(0, i - 1)][max(0, j - 1)] + 1, dp[m][j])
            else:
                # If the current species is the same as the last one, no replant needed
                dp[i][j] = dp[i-1][j]

    return dp[m][n]
