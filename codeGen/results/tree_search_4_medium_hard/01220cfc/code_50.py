def canJump(arr):
    n = len(arr)
    dp = [False] * n  # Initialize a DP table of size n

    for i in range(n):
        if i > 0:  # Only consider reachable indices
            if i <= arr[i]:  # If the current index is within reach
                for j in range(min(i + 1, arr[i] + 1), -1, -1):  # Iterate over the possible jumps
                    if dp[j]:  # If we've reached this index before (i.e., it's reachable)
                        dp[i] = True  # Mark the current index as reachable
                        break  # No need to continue iterating

    return dp[-1]  # Return whether the last index is reachable
