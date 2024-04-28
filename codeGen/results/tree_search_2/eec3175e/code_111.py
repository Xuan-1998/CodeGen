def find_subset_sum(arr, m):
    n = len(arr)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base case: There is a subset summing up to 0 for any set of numbers.
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # Check if there's a subset summing up to m
    return dp[n][m]
