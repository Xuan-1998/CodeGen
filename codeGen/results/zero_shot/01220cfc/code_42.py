def can_reach_last_index(arr):
    n = len(arr)
    dp = [False] * (n + 1)  # Initialize a dynamic programming array

    dp[0] = True  # We can reach the first index
    for i in range(1, n):  # Iterate through the array
        if arr[i - 1] >= i:  # If we can jump to this position
            dp[i] = dp[i - 1] or True  # Update our dynamic programming array
        else:
            dp[i] = dp[i - 1]

    return dp[-1]
