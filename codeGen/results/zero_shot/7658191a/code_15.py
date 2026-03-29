def max_score(n, k, z, arr):
    # Initialize dp array with initial values
    dp = [0] * (k + 1)
    for i in range(k + 1):
        dp[i] = float('-inf')

    # Fill up the dp array using dynamic programming
    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if j < z:
                # Try moving to the left (if allowed)
                dp[j] = max(dp[j], arr[i - 1])
            else:
                # Try moving to the right
                dp[j] = max(dp[j], arr[i])

    # Return the maximum score achieved
    return dp[k]
